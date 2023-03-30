# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamLinkType(ModelSimple):
    """
    Team link type

    :param value: If omitted defaults to "team_links". Must be one of ["team_links"].
    :type value: str
    """

    allowed_values = {
        "team_links",
    }
    TEAM_LINKS: ClassVar["TeamLinkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamLinkType.TEAM_LINKS = TeamLinkType("team_links")
