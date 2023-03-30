# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_metric_response_data import SpansMetricResponseData


class SpansMetricsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_metric_response_data import SpansMetricResponseData

        return {
            "data": ([SpansMetricResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[SpansMetricResponseData], UnsetType] = unset, **kwargs):
        """
        All the available span-based metric objects.

        :param data: A list of span-based metric objects.
        :type data: [SpansMetricResponseData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
