# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, developer_message: str=None, help_link: str=None, http_status_code: int=None, internal_code: str=None, message: str=None):
        """ErrorResponse - a model defined in OpenAPI

        :param developer_message: The developer_message of this ErrorResponse.
        :param help_link: The help_link of this ErrorResponse.
        :param http_status_code: The http_status_code of this ErrorResponse.
        :param internal_code: The internal_code of this ErrorResponse.
        :param message: The message of this ErrorResponse.
        """
        self.openapi_types = {
            'developer_message': str,
            'help_link': str,
            'http_status_code': int,
            'internal_code': str,
            'message': str
        }

        self.attribute_map = {
            'developer_message': 'developerMessage',
            'help_link': 'helpLink',
            'http_status_code': 'httpStatusCode',
            'internal_code': 'internalCode',
            'message': 'message'
        }

        self._developer_message = developer_message
        self._help_link = help_link
        self._http_status_code = http_status_code
        self._internal_code = internal_code
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorResponse of this ErrorResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def developer_message(self):
        """Gets the developer_message of this ErrorResponse.

        ~

        :return: The developer_message of this ErrorResponse.
        :rtype: str
        """
        return self._developer_message

    @developer_message.setter
    def developer_message(self, developer_message):
        """Sets the developer_message of this ErrorResponse.

        ~

        :param developer_message: The developer_message of this ErrorResponse.
        :type developer_message: str
        """

        self._developer_message = developer_message

    @property
    def help_link(self):
        """Gets the help_link of this ErrorResponse.

        ~

        :return: The help_link of this ErrorResponse.
        :rtype: str
        """
        return self._help_link

    @help_link.setter
    def help_link(self, help_link):
        """Sets the help_link of this ErrorResponse.

        ~

        :param help_link: The help_link of this ErrorResponse.
        :type help_link: str
        """

        self._help_link = help_link

    @property
    def http_status_code(self):
        """Gets the http_status_code of this ErrorResponse.

        ~

        :return: The http_status_code of this ErrorResponse.
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this ErrorResponse.

        ~

        :param http_status_code: The http_status_code of this ErrorResponse.
        :type http_status_code: int
        """

        self._http_status_code = http_status_code

    @property
    def internal_code(self):
        """Gets the internal_code of this ErrorResponse.

        ~

        :return: The internal_code of this ErrorResponse.
        :rtype: str
        """
        return self._internal_code

    @internal_code.setter
    def internal_code(self, internal_code):
        """Sets the internal_code of this ErrorResponse.

        ~

        :param internal_code: The internal_code of this ErrorResponse.
        :type internal_code: str
        """

        self._internal_code = internal_code

    @property
    def message(self):
        """Gets the message of this ErrorResponse.

        ~

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorResponse.

        ~

        :param message: The message of this ErrorResponse.
        :type message: str
        """

        self._message = message
