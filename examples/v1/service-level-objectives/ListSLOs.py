"""
Get all SLOs returns "OK" response
"""

from os import environ
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.list_sl_os(ids=SLO_DATA_0_ID)

    print(response)
