# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_x_path_operator import SyntheticsAssertionXPathOperator
    from datadog_api_client.v1.model.synthetics_assertion_x_path_target_target import (
        SyntheticsAssertionXPathTargetTarget,
    )
    from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType


class SyntheticsAssertionXPathTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_x_path_operator import SyntheticsAssertionXPathOperator
        from datadog_api_client.v1.model.synthetics_assertion_x_path_target_target import (
            SyntheticsAssertionXPathTargetTarget,
        )
        from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

        return {
            "operator": (SyntheticsAssertionXPathOperator,),
            "_property": (str,),
            "target": (SyntheticsAssertionXPathTargetTarget,),
            "type": (SyntheticsAssertionType,),
        }

    attribute_map = {
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsAssertionXPathOperator,
        type: SyntheticsAssertionType,
        _property: Union[str, UnsetType] = unset,
        target: Union[SyntheticsAssertionXPathTargetTarget, UnsetType] = unset,
        **kwargs,
    ):
        """
        An assertion for the ``validatesXPath`` operator.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionXPathOperator

        :param _property: The associated assertion property.
        :type _property: str, optional

        :param target: Composed target for ``validatesXPath`` operator.
        :type target: SyntheticsAssertionXPathTargetTarget, optional

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionType
        """
        if _property is not unset:
            kwargs["_property"] = _property
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.operator = operator
        self_.type = type
