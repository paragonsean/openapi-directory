# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.rollout_rule_comparator import RolloutRuleComparator
from openapi_server import util


class UpdateSegmentModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comparator: RolloutRuleComparator=None, comparison_attribute: str=None, comparison_value: str=None, description: str=None, name: str=None):
        """UpdateSegmentModel - a model defined in OpenAPI

        :param comparator: The comparator of this UpdateSegmentModel.
        :param comparison_attribute: The comparison_attribute of this UpdateSegmentModel.
        :param comparison_value: The comparison_value of this UpdateSegmentModel.
        :param description: The description of this UpdateSegmentModel.
        :param name: The name of this UpdateSegmentModel.
        """
        self.openapi_types = {
            'comparator': RolloutRuleComparator,
            'comparison_attribute': str,
            'comparison_value': str,
            'description': str,
            'name': str
        }

        self.attribute_map = {
            'comparator': 'comparator',
            'comparison_attribute': 'comparisonAttribute',
            'comparison_value': 'comparisonValue',
            'description': 'description',
            'name': 'name'
        }

        self._comparator = comparator
        self._comparison_attribute = comparison_attribute
        self._comparison_value = comparison_value
        self._description = description
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSegmentModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSegmentModel of this UpdateSegmentModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comparator(self):
        """Gets the comparator of this UpdateSegmentModel.


        :return: The comparator of this UpdateSegmentModel.
        :rtype: RolloutRuleComparator
        """
        return self._comparator

    @comparator.setter
    def comparator(self, comparator):
        """Sets the comparator of this UpdateSegmentModel.


        :param comparator: The comparator of this UpdateSegmentModel.
        :type comparator: RolloutRuleComparator
        """

        self._comparator = comparator

    @property
    def comparison_attribute(self):
        """Gets the comparison_attribute of this UpdateSegmentModel.


        :return: The comparison_attribute of this UpdateSegmentModel.
        :rtype: str
        """
        return self._comparison_attribute

    @comparison_attribute.setter
    def comparison_attribute(self, comparison_attribute):
        """Sets the comparison_attribute of this UpdateSegmentModel.


        :param comparison_attribute: The comparison_attribute of this UpdateSegmentModel.
        :type comparison_attribute: str
        """
        if comparison_attribute is not None and len(comparison_attribute) > 1000:
            raise ValueError("Invalid value for `comparison_attribute`, length must be less than or equal to `1000`")
        if comparison_attribute is not None and len(comparison_attribute) < 0:
            raise ValueError("Invalid value for `comparison_attribute`, length must be greater than or equal to `0`")

        self._comparison_attribute = comparison_attribute

    @property
    def comparison_value(self):
        """Gets the comparison_value of this UpdateSegmentModel.


        :return: The comparison_value of this UpdateSegmentModel.
        :rtype: str
        """
        return self._comparison_value

    @comparison_value.setter
    def comparison_value(self, comparison_value):
        """Sets the comparison_value of this UpdateSegmentModel.


        :param comparison_value: The comparison_value of this UpdateSegmentModel.
        :type comparison_value: str
        """
        if comparison_value is not None and len(comparison_value) > 65535:
            raise ValueError("Invalid value for `comparison_value`, length must be less than or equal to `65535`")
        if comparison_value is not None and len(comparison_value) < 0:
            raise ValueError("Invalid value for `comparison_value`, length must be greater than or equal to `0`")

        self._comparison_value = comparison_value

    @property
    def description(self):
        """Gets the description of this UpdateSegmentModel.


        :return: The description of this UpdateSegmentModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSegmentModel.


        :param description: The description of this UpdateSegmentModel.
        :type description: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateSegmentModel.


        :return: The name of this UpdateSegmentModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSegmentModel.


        :param name: The name of this UpdateSegmentModel.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name
