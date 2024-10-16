# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Opencast(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pin_code: str=None):
        """Opencast - a model defined in OpenAPI

        :param pin_code: The pin_code of this Opencast.
        """
        self.openapi_types = {
            'pin_code': str
        }

        self.attribute_map = {
            'pin_code': 'pin_code'
        }

        self._pin_code = pin_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Opencast':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Opencast of this Opencast.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pin_code(self):
        """Gets the pin_code of this Opencast.


        :return: The pin_code of this Opencast.
        :rtype: str
        """
        return self._pin_code

    @pin_code.setter
    def pin_code(self, pin_code):
        """Sets the pin_code of this Opencast.


        :param pin_code: The pin_code of this Opencast.
        :type pin_code: str
        """
        if pin_code is None:
            raise ValueError("Invalid value for `pin_code`, must not be `None`")

        self._pin_code = pin_code
