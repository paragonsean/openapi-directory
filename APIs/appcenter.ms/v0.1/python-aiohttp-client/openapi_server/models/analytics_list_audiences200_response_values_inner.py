# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AnalyticsListAudiences200ResponseValuesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, definition: str=None, description: str=None, estimated_count: int=None, name: str=None, state: str=None):
        """AnalyticsListAudiences200ResponseValuesInner - a model defined in OpenAPI

        :param definition: The definition of this AnalyticsListAudiences200ResponseValuesInner.
        :param description: The description of this AnalyticsListAudiences200ResponseValuesInner.
        :param estimated_count: The estimated_count of this AnalyticsListAudiences200ResponseValuesInner.
        :param name: The name of this AnalyticsListAudiences200ResponseValuesInner.
        :param state: The state of this AnalyticsListAudiences200ResponseValuesInner.
        """
        self.openapi_types = {
            'definition': str,
            'description': str,
            'estimated_count': int,
            'name': str,
            'state': str
        }

        self.attribute_map = {
            'definition': 'definition',
            'description': 'description',
            'estimated_count': 'estimated_count',
            'name': 'name',
            'state': 'state'
        }

        self._definition = definition
        self._description = description
        self._estimated_count = estimated_count
        self._name = name
        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AnalyticsListAudiences200ResponseValuesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Analytics_ListAudiences_200_response_values_inner of this AnalyticsListAudiences200ResponseValuesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def definition(self):
        """Gets the definition of this AnalyticsListAudiences200ResponseValuesInner.

        Audience definition in OData format.

        :return: The definition of this AnalyticsListAudiences200ResponseValuesInner.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this AnalyticsListAudiences200ResponseValuesInner.

        Audience definition in OData format.

        :param definition: The definition of this AnalyticsListAudiences200ResponseValuesInner.
        :type definition: str
        """

        self._definition = definition

    @property
    def description(self):
        """Gets the description of this AnalyticsListAudiences200ResponseValuesInner.

        Audience description.

        :return: The description of this AnalyticsListAudiences200ResponseValuesInner.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalyticsListAudiences200ResponseValuesInner.

        Audience description.

        :param description: The description of this AnalyticsListAudiences200ResponseValuesInner.
        :type description: str
        """

        self._description = description

    @property
    def estimated_count(self):
        """Gets the estimated_count of this AnalyticsListAudiences200ResponseValuesInner.

        Estimated audience size.

        :return: The estimated_count of this AnalyticsListAudiences200ResponseValuesInner.
        :rtype: int
        """
        return self._estimated_count

    @estimated_count.setter
    def estimated_count(self, estimated_count):
        """Sets the estimated_count of this AnalyticsListAudiences200ResponseValuesInner.

        Estimated audience size.

        :param estimated_count: The estimated_count of this AnalyticsListAudiences200ResponseValuesInner.
        :type estimated_count: int
        """

        self._estimated_count = estimated_count

    @property
    def name(self):
        """Gets the name of this AnalyticsListAudiences200ResponseValuesInner.

        Audience name.

        :return: The name of this AnalyticsListAudiences200ResponseValuesInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsListAudiences200ResponseValuesInner.

        Audience name.

        :param name: The name of this AnalyticsListAudiences200ResponseValuesInner.
        :type name: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this AnalyticsListAudiences200ResponseValuesInner.

        Audience state.

        :return: The state of this AnalyticsListAudiences200ResponseValuesInner.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AnalyticsListAudiences200ResponseValuesInner.

        Audience state.

        :param state: The state of this AnalyticsListAudiences200ResponseValuesInner.
        :type state: str
        """
        allowed_values = ["Calculating", "Ready", "Disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
