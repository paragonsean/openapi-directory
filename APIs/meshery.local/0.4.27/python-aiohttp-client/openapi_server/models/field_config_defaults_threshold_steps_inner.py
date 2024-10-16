# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FieldConfigDefaultsThresholdStepsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color: str=None, value: str=None):
        """FieldConfigDefaultsThresholdStepsInner - a model defined in OpenAPI

        :param color: The color of this FieldConfigDefaultsThresholdStepsInner.
        :param value: The value of this FieldConfigDefaultsThresholdStepsInner.
        """
        self.openapi_types = {
            'color': str,
            'value': str
        }

        self.attribute_map = {
            'color': 'color',
            'value': 'value'
        }

        self._color = color
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FieldConfigDefaultsThresholdStepsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FieldConfig_defaults_threshold_steps_inner of this FieldConfigDefaultsThresholdStepsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color(self):
        """Gets the color of this FieldConfigDefaultsThresholdStepsInner.


        :return: The color of this FieldConfigDefaultsThresholdStepsInner.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this FieldConfigDefaultsThresholdStepsInner.


        :param color: The color of this FieldConfigDefaultsThresholdStepsInner.
        :type color: str
        """

        self._color = color

    @property
    def value(self):
        """Gets the value of this FieldConfigDefaultsThresholdStepsInner.


        :return: The value of this FieldConfigDefaultsThresholdStepsInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FieldConfigDefaultsThresholdStepsInner.


        :param value: The value of this FieldConfigDefaultsThresholdStepsInner.
        :type value: str
        """

        self._value = value
