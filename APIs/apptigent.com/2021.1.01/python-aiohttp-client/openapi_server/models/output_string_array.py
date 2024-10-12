# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OutputStringArray(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[str]=None):
        """OutputStringArray - a model defined in OpenAPI

        :param data: The data of this OutputStringArray.
        """
        self.openapi_types = {
            'data': List[str]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputStringArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The outputStringArray of this OutputStringArray.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this OutputStringArray.

        data

        :return: The data of this OutputStringArray.
        :rtype: List[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this OutputStringArray.

        data

        :param data: The data of this OutputStringArray.
        :type data: List[str]
        """

        self._data = data
