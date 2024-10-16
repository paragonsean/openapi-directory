# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class V2FailureResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):
        """V2FailureResponse - a model defined in OpenAPI

        :param code: The code of this V2FailureResponse.
        :param message: The message of this V2FailureResponse.
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
    def from_dict(cls, dikt: dict) -> 'V2FailureResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The v2FailureResponse of this V2FailureResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this V2FailureResponse.


        :return: The code of this V2FailureResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this V2FailureResponse.


        :param code: The code of this V2FailureResponse.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """Gets the message of this V2FailureResponse.


        :return: The message of this V2FailureResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V2FailureResponse.


        :param message: The message of this V2FailureResponse.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
