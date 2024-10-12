# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResponseBase(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None):
        """ResponseBase - a model defined in OpenAPI

        :param type: The type of this ResponseBase.
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': '_type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResponseBase':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResponseBase of this ResponseBase.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ResponseBase.


        :return: The type of this ResponseBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseBase.


        :param type: The type of this ResponseBase.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
