# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.field_selector import FieldSelector
from openapi_server import util


class TemplateItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, first_value: FieldSelector=None, predefined_item: str=None, second_value: FieldSelector=None):
        """TemplateItem - a model defined in OpenAPI

        :param first_value: The first_value of this TemplateItem.
        :param predefined_item: The predefined_item of this TemplateItem.
        :param second_value: The second_value of this TemplateItem.
        """
        self.openapi_types = {
            'first_value': FieldSelector,
            'predefined_item': str,
            'second_value': FieldSelector
        }

        self.attribute_map = {
            'first_value': 'firstValue',
            'predefined_item': 'predefinedItem',
            'second_value': 'secondValue'
        }

        self._first_value = first_value
        self._predefined_item = predefined_item
        self._second_value = second_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TemplateItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TemplateItem of this TemplateItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_value(self):
        """Gets the first_value of this TemplateItem.


        :return: The first_value of this TemplateItem.
        :rtype: FieldSelector
        """
        return self._first_value

    @first_value.setter
    def first_value(self, first_value):
        """Sets the first_value of this TemplateItem.


        :param first_value: The first_value of this TemplateItem.
        :type first_value: FieldSelector
        """

        self._first_value = first_value

    @property
    def predefined_item(self):
        """Gets the predefined_item of this TemplateItem.

        A predefined item to display. Only one of `firstValue` or `predefinedItem` may be set.

        :return: The predefined_item of this TemplateItem.
        :rtype: str
        """
        return self._predefined_item

    @predefined_item.setter
    def predefined_item(self, predefined_item):
        """Sets the predefined_item of this TemplateItem.

        A predefined item to display. Only one of `firstValue` or `predefinedItem` may be set.

        :param predefined_item: The predefined_item of this TemplateItem.
        :type predefined_item: str
        """
        allowed_values = ["PREDEFINED_ITEM_UNSPECIFIED", "FREQUENT_FLYER_PROGRAM_NAME_AND_NUMBER", "frequentFlyerProgramNameAndNumber", "FLIGHT_NUMBER_AND_OPERATING_FLIGHT_NUMBER", "flightNumberAndOperatingFlightNumber"]  # noqa: E501
        if predefined_item not in allowed_values:
            raise ValueError(
                "Invalid value for `predefined_item` ({0}), must be one of {1}"
                .format(predefined_item, allowed_values)
            )

        self._predefined_item = predefined_item

    @property
    def second_value(self):
        """Gets the second_value of this TemplateItem.


        :return: The second_value of this TemplateItem.
        :rtype: FieldSelector
        """
        return self._second_value

    @second_value.setter
    def second_value(self, second_value):
        """Sets the second_value of this TemplateItem.


        :param second_value: The second_value of this TemplateItem.
        :type second_value: FieldSelector
        """

        self._second_value = second_value
