# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputConvertAngle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input: float=None, source: str=None, target: str=None):
        """InputConvertAngle - a model defined in OpenAPI

        :param input: The input of this InputConvertAngle.
        :param source: The source of this InputConvertAngle.
        :param target: The target of this InputConvertAngle.
        """
        self.openapi_types = {
            'input': float,
            'source': str,
            'target': str
        }

        self.attribute_map = {
            'input': 'input',
            'source': 'source',
            'target': 'target'
        }

        self._input = input
        self._source = source
        self._target = target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputConvertAngle':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputConvertAngle of this InputConvertAngle.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InputConvertAngle.


        :return: The input of this InputConvertAngle.
        :rtype: float
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InputConvertAngle.


        :param input: The input of this InputConvertAngle.
        :type input: float
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")

        self._input = input

    @property
    def source(self):
        """Gets the source of this InputConvertAngle.


        :return: The source of this InputConvertAngle.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InputConvertAngle.


        :param source: The source of this InputConvertAngle.
        :type source: str
        """
        allowed_values = ["Arcminute", "Arcsecond", "Centiradian", "Deciradian", "Degree", "Gradian", "Microdegree", "Microradian", "Millidegree", "Milliradian", "Nanodegree", "Nanoradian", "Radian", "Revolution"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def target(self):
        """Gets the target of this InputConvertAngle.


        :return: The target of this InputConvertAngle.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this InputConvertAngle.


        :param target: The target of this InputConvertAngle.
        :type target: str
        """
        allowed_values = ["Arcminute", "Arcsecond", "Centiradian", "Deciradian", "Degree", "Gradian", "Microdegree", "Microradian", "Millidegree", "Milliradian", "Nanodegree", "Nanoradian", "Radian", "Revolution"]  # noqa: E501
        if target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}"
                .format(target, allowed_values)
            )

        self._target = target
