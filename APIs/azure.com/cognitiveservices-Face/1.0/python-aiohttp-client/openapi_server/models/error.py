# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Error(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):
        """Error - a model defined in OpenAPI

        :param code: The code of this Error.
        :param message: The message of this Error.
        """
        self.openapi_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error of this Error.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Error.


        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.


        :param code: The code of this Error.
        :type code: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this Error.


        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.


        :param message: The message of this Error.
        :type message: str
        """

        self._message = message
