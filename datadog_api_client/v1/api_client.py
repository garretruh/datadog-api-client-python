# coding: utf-8
# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from __future__ import absolute_import

import json
import atexit
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from datadog_api_client.v1 import rest
from datadog_api_client.v1.configuration import Configuration
from datadog_api_client.v1.exceptions import ApiValueError, ApiException
from datadog_api_client.v1.model_utils import (
    ModelNormal,
    ModelSimple,
    ModelComposed,
    date,
    datetime,
    deserialize_file,
    file_type,
    model_to_dict,
    str,
    validate_and_convert_types
)


class ApiClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    # six.binary_type python2=str, python3=bytes
    # six.text_type python2=unicode, python3=str
    PRIMITIVE_TYPES = (
        (float, bool, six.binary_type, six.text_type) + six.integer_types
    )
    _pool = None

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1):
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = user_agent()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
            self, resource_path, method, path_params=None,
            query_params=None, header_params=None, body=None, post_params=None,
            files=None, response_type=None, auth_settings=None,
            _return_http_data_only=None, collection_formats=None,
            _preload_content=True, _request_timeout=None, _host=None,
            _check_type=None):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            post_params.extend(self.files_parameters(files))

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # auth setting
        self.update_params_for_auth(header_params, query_params,
                                    auth_settings, resource_path, method, body)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        try:
            # perform request and return response
            response_data = self.request(
                method, url, query_params=query_params, headers=header_params,
                post_params=post_params, body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout)
        except ApiException as e:
            e.body = e.body.decode('utf-8') if six.PY3 else e.body
            raise e

        content_type = response_data.getheader('content-type')

        self.last_response = response_data

        return_data = response_data

        if not _preload_content:
            return (return_data)
            return return_data

        if six.PY3 and response_type not in ["file", "bytes"]:
            match = None
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_data.data = response_data.data.decode(encoding)

        # deserialize response data
        if response_type:
            return_data = self.deserialize(
                response_data,
                response_type,
                _check_type
            )
        else:
            return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        elif isinstance(obj, ModelNormal) or isinstance(obj, ModelComposed):
            # Convert model obj to dict
            # Convert attribute name to json key in
            # model definition for request
            obj_dict = model_to_dict(obj, serialize=True)
        elif isinstance(obj, ModelSimple):
            return self.sanitize_for_serialization(obj.value)

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def deserialize(self, response, response_type, _check_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param _check_type: boolean, whether to check the types of the data
            received from the server
        :type _check_type: bool

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == (file_type,):
            content_disposition = response.getheader("Content-Disposition")
            return deserialize_file(response.data, self.configuration,
                                    content_disposition=content_disposition)

        # fetch data from response object
        try:
            received_data = json.loads(response.data)
        except ValueError:
            received_data = response.data

        # store our data under the key of 'received_data' so users have some
        # context if they are deserializing a string and the data type is wrong
        deserialized_data = validate_and_convert_types(
            received_data,
            response_type,
            ['received_data'],
            True,
            _check_type,
            configuration=self.configuration
        )
        return deserialized_data

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, async_req=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True, _request_timeout=None, _host=None,
                 _check_type=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param files: key -> field name, value -> a list of open file
            objects for `multipart/form-data`.
        :type files: dict
        :param async_req bool: execute request asynchronously
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :type collection_formats: dict, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _check_type: boolean describing if the data back from the server
            should have its type checked.
        :type _check_type: bool, optional
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout, _host,
                                   _check_type)

        return self.pool.apply_async(self.__call_api, (resource_path,
                                                       method, path_params,
                                                       query_params,
                                                       header_params, body,
                                                       post_params, files,
                                                       response_type,
                                                       auth_settings,
                                                       _return_http_data_only,
                                                       collection_formats,
                                                       _preload_content,
                                                       _request_timeout,
                                                       _host, _check_type))

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def files_parameters(self, files=None):
        """Builds form parameters.

        :param files: None or a dict with key=param_name and
            value is a list of open file objects
        :return: List of tuples of form parameters with file data
        """
        if files is None:
            return []

        params = []
        for param_name, file_instances in six.iteritems(files):
            if file_instances is None:
                # if the file field is nullable, skip None values
                continue
            for file_instance in file_instances:
                if file_instance is None:
                    # if the file field is nullable, skip None values
                    continue
                if file_instance.closed is True:
                    raise ApiValueError(
                        "Cannot read a closed file. The passed in file_type "
                        "for %s must be open." % param_name
                    )
                filename = os.path.basename(file_instance.name)
                filedata = file_instance.read()
                mimetype = (mimetypes.guess_type(filename)[0] or
                            'application/octet-stream')
                params.append(
                    tuple([param_name, tuple([filename, filedata, mimetype])]))
                file_instance.close()

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings,
                               resource_path, method, body):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :param resource_path: A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method.
        :param body: A object representing the body of the HTTP request.
            The object type is the return value of sanitize_for_serialization().
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if auth_setting['in'] == 'cookie':
                    headers['Cookie'] = auth_setting['value']
                elif auth_setting['in'] == 'header':
                    if auth_setting['type'] != 'http-signature':
                        headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ApiValueError(
                        'Authentication token must be in `query` or `header`'
                    )


def user_agent():
    """Generate default User-Agent header."""
    import platform
    from datadog_api_client.version import __version__
    return "datadog-api-client-python/{version} (python {py}; os {os}; arch {arch})".format(
        version=__version__,
        py=platform.python_version(),
        os=platform.system(),
        arch=platform.machine(),
    )
