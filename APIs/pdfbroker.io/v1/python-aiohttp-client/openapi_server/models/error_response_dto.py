# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ErrorResponseDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, error_message: str=None, status_code: int=None):
        """ErrorResponseDto - a model defined in OpenAPI

        :param description: The description of this ErrorResponseDto.
        :param error_message: The error_message of this ErrorResponseDto.
        :param status_code: The status_code of this ErrorResponseDto.
        """
        self.openapi_types = {
            'description': str,
            'error_message': str,
            'status_code': int
        }

        self.attribute_map = {
            'description': 'description',
            'error_message': 'errorMessage',
            'status_code': 'statusCode'
        }

        self._description = description
        self._error_message = error_message
        self._status_code = status_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorResponseDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorResponseDto of this ErrorResponseDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this ErrorResponseDto.


        :return: The description of this ErrorResponseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ErrorResponseDto.


        :param description: The description of this ErrorResponseDto.
        :type description: str
        """

        self._description = description

    @property
    def error_message(self):
        """Gets the error_message of this ErrorResponseDto.

        If any error occurs the message will be displayed in here

        :return: The error_message of this ErrorResponseDto.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ErrorResponseDto.

        If any error occurs the message will be displayed in here

        :param error_message: The error_message of this ErrorResponseDto.
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def status_code(self):
        """Gets the status_code of this ErrorResponseDto.


        :return: The status_code of this ErrorResponseDto.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ErrorResponseDto.


        :param status_code: The status_code of this ErrorResponseDto.
        :type status_code: int
        """

        self._status_code = status_code
