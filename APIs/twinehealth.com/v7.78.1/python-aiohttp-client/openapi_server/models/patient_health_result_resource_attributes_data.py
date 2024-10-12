# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PatientHealthResultResourceAttributesData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: object=None):
        """PatientHealthResultResourceAttributesData - a model defined in OpenAPI

        :param value: The value of this PatientHealthResultResourceAttributesData.
        """
        self.openapi_types = {
            'value': object
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientHealthResultResourceAttributesData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientHealthResultResource_attributes_data of this PatientHealthResultResourceAttributesData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this PatientHealthResultResourceAttributesData.

        Can be any value (number, boolean, string, object) depending on the metric type. Most values are of type number

        :return: The value of this PatientHealthResultResourceAttributesData.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PatientHealthResultResourceAttributesData.

        Can be any value (number, boolean, string, object) depending on the metric type. Most values are of type number

        :param value: The value of this PatientHealthResultResourceAttributesData.
        :type value: object
        """

        self._value = value
