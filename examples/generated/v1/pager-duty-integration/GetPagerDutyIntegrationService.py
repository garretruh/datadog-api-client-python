import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import pager_duty_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pager_duty_integration_api.PagerDutyIntegrationApi(api_client)
    service_name = "service_name_example"  # str | The service name.

    # example passing only required values which don't have defaults set
    try:
        # Get a single service object
        api_response = api_instance.get_pager_duty_integration_service(service_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PagerDutyIntegrationApi->get_pager_duty_integration_service: %s\n" % e)