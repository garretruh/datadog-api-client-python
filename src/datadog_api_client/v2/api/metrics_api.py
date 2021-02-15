# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_tag_configuration_response import MetricTagConfigurationResponse
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequest
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations_response import (
    MetricsAndMetricTagConfigurationsResponse,
)


class MetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_tag_configuration(self, metric_name, body, **kwargs):
            """Create a Tag Configuration  # noqa: E501

            Create and define a list of queryable tag keys for a count/gauge/rate/distribution metric. Optionally, include percentile aggregations on any distribution metric. Can only be used with application keys of users with the `Manage Tags for Metrics` permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_tag_configuration(metric_name, body, async_req=True)
            >>> result = thread.get()

            Args:
                metric_name (str): The name of the metric.
                body (MetricTagConfigurationCreateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MetricTagConfigurationResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["metric_name"] = metric_name
            kwargs["body"] = body
            return self.call_with_http_info(**kwargs)

        self.create_tag_configuration = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "create_tag_configuration",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                    "body",
                ],
                "required": [
                    "metric_name",
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                    "body": (MetricTagConfigurationCreateRequest,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__create_tag_configuration,
        )

        def __delete_tag_configuration(self, metric_name, **kwargs):
            """Delete a Tag Configuration  # noqa: E501

            Deletes a metric's tag configuration. Can only be used with application keys from users with the `Manage Tags for Metrics` permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_tag_configuration(metric_name, async_req=True)
            >>> result = thread.get()

            Args:
                metric_name (str): The name of the metric.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["metric_name"] = metric_name
            return self.call_with_http_info(**kwargs)

        self.delete_tag_configuration = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "delete_tag_configuration",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                ],
                "required": [
                    "metric_name",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__delete_tag_configuration,
        )

        def __list_tag_configuration_by_name(self, metric_name, **kwargs):
            """List Tag Configuration by Name  # noqa: E501

            Returns the tag configuration for the given metric name.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_tag_configuration_by_name(metric_name, async_req=True)
            >>> result = thread.get()

            Args:
                metric_name (str): The name of the metric.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MetricTagConfigurationResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["metric_name"] = metric_name
            return self.call_with_http_info(**kwargs)

        self.list_tag_configuration_by_name = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "list_tag_configuration_by_name",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                ],
                "required": [
                    "metric_name",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list_tag_configuration_by_name,
        )

        def __list_tag_configurations(self, **kwargs):
            """List Tag Configurations  # noqa: E501

            Returns all configured count/gauge/rate/distribution metric names (with additional filters if specified).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_tag_configurations(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                filter_configured (bool): Filter metrics that have configured tags.. [optional]
                filter_tags_configured (str): Filter tag configurations by configured tags.. [optional]
                filter_metric_type (MetricTagConfigurationMetricTypes): Filter tag configurations by metric type.. [optional]
                filter_include_percentiles (bool): Filter distributions with additional percentile aggregations enabled or disabled.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MetricsAndMetricTagConfigurationsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.list_tag_configurations = _Endpoint(
            settings={
                "response_type": (MetricsAndMetricTagConfigurationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics",
                "operation_id": "list_tag_configurations",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "filter_configured",
                    "filter_tags_configured",
                    "filter_metric_type",
                    "filter_include_percentiles",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "filter_configured": (bool,),
                    "filter_tags_configured": (str,),
                    "filter_metric_type": (MetricTagConfigurationMetricTypes,),
                    "filter_include_percentiles": (bool,),
                },
                "attribute_map": {
                    "filter_configured": "filter[configured]",
                    "filter_tags_configured": "filter[tags_configured]",
                    "filter_metric_type": "filter[metric_type]",
                    "filter_include_percentiles": "filter[include_percentiles]",
                },
                "location_map": {
                    "filter_configured": "query",
                    "filter_tags_configured": "query",
                    "filter_metric_type": "query",
                    "filter_include_percentiles": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list_tag_configurations,
        )

        def __update_tag_configuration(self, metric_name, body, **kwargs):
            """Update a Tag Configuration  # noqa: E501

            Update the tag configuration of a metric or percentile aggregations of a distribution metric. Can only be used with application keys from users with the `Manage Tags for Metrics` permission.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_tag_configuration(metric_name, body, async_req=True)
            >>> result = thread.get()

            Args:
                metric_name (str): The name of the metric.
                body (MetricTagConfigurationUpdateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MetricTagConfigurationResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["metric_name"] = metric_name
            kwargs["body"] = body
            return self.call_with_http_info(**kwargs)

        self.update_tag_configuration = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "update_tag_configuration",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                    "body",
                ],
                "required": [
                    "metric_name",
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                    "body": (MetricTagConfigurationUpdateRequest,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__update_tag_configuration,
        )
