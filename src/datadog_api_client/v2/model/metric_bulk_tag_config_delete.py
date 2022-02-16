# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType
    from datadog_api_client.v2.model.metric_bulk_tag_config_delete_attributes import MetricBulkTagConfigDeleteAttributes

    globals()["MetricBulkConfigureTagsType"] = MetricBulkConfigureTagsType
    globals()["MetricBulkTagConfigDeleteAttributes"] = MetricBulkTagConfigDeleteAttributes


class MetricBulkTagConfigDelete(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (MetricBulkTagConfigDeleteAttributes,),
            "id": (str,),
            "type": (MetricBulkConfigureTagsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
        "attributes": "attributes",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """MetricBulkTagConfigDelete - a model defined in OpenAPI


        :param id: A text prefix to match against metric names.
        :type id: str

        :type type: MetricBulkConfigureTagsType

        :type attributes: MetricBulkTagConfigDeleteAttributes, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigDelete, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self