# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputXmlConversionJSON(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input: str=None):
        """InputXmlConversionJSON - a model defined in OpenAPI

        :param input: The input of this InputXmlConversionJSON.
        """
        self.openapi_types = {
            'input': str
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputXmlConversionJSON':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputXmlConversionJSON of this InputXmlConversionJSON.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InputXmlConversionJSON.

        XML string

        :return: The input of this InputXmlConversionJSON.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InputXmlConversionJSON.

        XML string

        :param input: The input of this InputXmlConversionJSON.
        :type input: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")

        self._input = input
