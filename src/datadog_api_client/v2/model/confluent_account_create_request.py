# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ConfluentAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_create_request_data import ConfluentAccountCreateRequestData

        return {
            "data": (ConfluentAccountCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        Payload schema when adding a Confluent account.

        :param data: The data body for adding a Confluent account.
        :type data: ConfluentAccountCreateRequestData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data