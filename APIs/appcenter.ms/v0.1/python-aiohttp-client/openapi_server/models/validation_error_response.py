# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ValidationErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, id: str=None, message: str=None):
        """ValidationErrorResponse - a model defined in OpenAPI

        :param code: The code of this ValidationErrorResponse.
        :param id: The id of this ValidationErrorResponse.
        :param message: The message of this ValidationErrorResponse.
        """
        self.openapi_types = {
            'code': str,
            'id': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'id': 'id',
            'message': 'message'
        }

        self._code = code
        self._id = id
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ValidationErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ValidationErrorResponse of this ValidationErrorResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this ValidationErrorResponse.


        :return: The code of this ValidationErrorResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidationErrorResponse.


        :param code: The code of this ValidationErrorResponse.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def id(self):
        """Gets the id of this ValidationErrorResponse.


        :return: The id of this ValidationErrorResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ValidationErrorResponse.


        :param id: The id of this ValidationErrorResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def message(self):
        """Gets the message of this ValidationErrorResponse.


        :return: The message of this ValidationErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationErrorResponse.


        :param message: The message of this ValidationErrorResponse.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
