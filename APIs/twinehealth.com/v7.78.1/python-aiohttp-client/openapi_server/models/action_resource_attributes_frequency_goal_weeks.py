# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ActionResourceAttributesFrequencyGoalWeeks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, days: List[int]=None):
        """ActionResourceAttributesFrequencyGoalWeeks - a model defined in OpenAPI

        :param days: The days of this ActionResourceAttributesFrequencyGoalWeeks.
        """
        self.openapi_types = {
            'days': List[int]
        }

        self.attribute_map = {
            'days': 'days'
        }

        self._days = days

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ActionResourceAttributesFrequencyGoalWeeks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ActionResource_attributes_frequency_goal_weeks of this ActionResourceAttributesFrequencyGoalWeeks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def days(self):
        """Gets the days of this ActionResourceAttributesFrequencyGoalWeeks.


        :return: The days of this ActionResourceAttributesFrequencyGoalWeeks.
        :rtype: List[int]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this ActionResourceAttributesFrequencyGoalWeeks.


        :param days: The days of this ActionResourceAttributesFrequencyGoalWeeks.
        :type days: List[int]
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if not set(days).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `days` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(days) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._days = days
