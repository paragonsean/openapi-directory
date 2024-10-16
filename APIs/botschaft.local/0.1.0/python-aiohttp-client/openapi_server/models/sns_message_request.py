# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SnsMessageRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base64_message: str=None, message: str=None):
        """SnsMessageRequest - a model defined in OpenAPI

        :param base64_message: The base64_message of this SnsMessageRequest.
        :param message: The message of this SnsMessageRequest.
        """
        self.openapi_types = {
            'base64_message': str,
            'message': str
        }

        self.attribute_map = {
            'base64_message': 'base64_message',
            'message': 'message'
        }

        self._base64_message = base64_message
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SnsMessageRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SnsMessageRequest of this SnsMessageRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base64_message(self):
        """Gets the base64_message of this SnsMessageRequest.


        :return: The base64_message of this SnsMessageRequest.
        :rtype: str
        """
        return self._base64_message

    @base64_message.setter
    def base64_message(self, base64_message):
        """Sets the base64_message of this SnsMessageRequest.


        :param base64_message: The base64_message of this SnsMessageRequest.
        :type base64_message: str
        """

        self._base64_message = base64_message

    @property
    def message(self):
        """Gets the message of this SnsMessageRequest.


        :return: The message of this SnsMessageRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SnsMessageRequest.


        :param message: The message of this SnsMessageRequest.
        :type message: str
        """

        self._message = message
