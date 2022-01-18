# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class MonthlyUsageAttributionValues(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "api_percentage": (float,),
            "api_usage": (float,),
            "apm_host_percentage": (float,),
            "apm_host_usage": (float,),
            "browser_percentage": (float,),
            "browser_usage": (float,),
            "container_percentage": (float,),
            "container_usage": (float,),
            "custom_timeseries_percentage": (float,),
            "custom_timeseries_usage": (float,),
            "fargate_percentage": (float,),
            "fargate_usage": (float,),
            "functions_percentage": (float,),
            "functions_usage": (float,),
            "indexed_logs_percentage": (float,),
            "indexed_logs_usage": (float,),
            "infra_host_percentage": (float,),
            "infra_host_usage": (float,),
            "invocations_percentage": (float,),
            "invocations_usage": (float,),
            "npm_host_percentage": (float,),
            "npm_host_usage": (float,),
            "profiled_container_percentage": (float,),
            "profiled_container_usage": (float,),
            "profiled_host_percentage": (float,),
            "profiled_host_usage": (float,),
            "snmp_percentage": (float,),
            "snmp_usage": (float,),
        }

    attribute_map = {
        "api_percentage": "api_percentage",
        "api_usage": "api_usage",
        "apm_host_percentage": "apm_host_percentage",
        "apm_host_usage": "apm_host_usage",
        "browser_percentage": "browser_percentage",
        "browser_usage": "browser_usage",
        "container_percentage": "container_percentage",
        "container_usage": "container_usage",
        "custom_timeseries_percentage": "custom_timeseries_percentage",
        "custom_timeseries_usage": "custom_timeseries_usage",
        "fargate_percentage": "fargate_percentage",
        "fargate_usage": "fargate_usage",
        "functions_percentage": "functions_percentage",
        "functions_usage": "functions_usage",
        "indexed_logs_percentage": "indexed_logs_percentage",
        "indexed_logs_usage": "indexed_logs_usage",
        "infra_host_percentage": "infra_host_percentage",
        "infra_host_usage": "infra_host_usage",
        "invocations_percentage": "invocations_percentage",
        "invocations_usage": "invocations_usage",
        "npm_host_percentage": "npm_host_percentage",
        "npm_host_usage": "npm_host_usage",
        "profiled_container_percentage": "profiled_container_percentage",
        "profiled_container_usage": "profiled_container_usage",
        "profiled_host_percentage": "profiled_host_percentage",
        "profiled_host_usage": "profiled_host_usage",
        "snmp_percentage": "snmp_percentage",
        "snmp_usage": "snmp_usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """MonthlyUsageAttributionValues - a model defined in OpenAPI

        Keyword Args:
            api_percentage (float): [optional] The percentage of synthetic API test usage by tag(s).
            api_usage (float): [optional] The synthetic API test usage by tag(s).
            apm_host_percentage (float): [optional] The percentage of APM host usage by tag(s).
            apm_host_usage (float): [optional] The APM host usage by tag(s).
            browser_percentage (float): [optional] The percentage of synthetic browser test usage by tag(s).
            browser_usage (float): [optional] The synthetic browser test usage by tag(s).
            container_percentage (float): [optional] The percentage of container usage by tag(s).
            container_usage (float): [optional] The container usage by tag(s).
            custom_timeseries_percentage (float): [optional] The percentage of custom metrics usage by tag(s).
            custom_timeseries_usage (float): [optional] The custom metrics usage by tag(s).
            fargate_percentage (float): [optional] The percentage of Fargate usage by tags.
            fargate_usage (float): [optional] The Fargate usage by tags.
            functions_percentage (float): [optional] The percentage of Lambda function usage by tag(s).
            functions_usage (float): [optional] The Lambda function usage by tag(s).
            indexed_logs_percentage (float): [optional] The percentage of indexed logs usage by tags.
            indexed_logs_usage (float): [optional] The indexed logs usage by tags.
            infra_host_percentage (float): [optional] The percentage of infrastructure host usage by tag(s).
            infra_host_usage (float): [optional] The infrastructure host usage by tag(s).
            invocations_percentage (float): [optional] The percentage of Lambda invocation usage by tag(s).
            invocations_usage (float): [optional] The Lambda invocation usage by tag(s).
            npm_host_percentage (float): [optional] The percentage of network host usage by tag(s).
            npm_host_usage (float): [optional] The network host usage by tag(s).
            profiled_container_percentage (float): [optional] The percentage of profiled container usage by tag(s).
            profiled_container_usage (float): [optional] The profiled container usage by tag(s).
            profiled_host_percentage (float): [optional] The percentage of profiled hosts usage by tag(s).
            profiled_host_usage (float): [optional] The profiled hosts usage by tag(s).
            snmp_percentage (float): [optional] The percentage of network device usage by tag(s).
            snmp_usage (float): [optional] The network device usage by tag(s).
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonthlyUsageAttributionValues, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self