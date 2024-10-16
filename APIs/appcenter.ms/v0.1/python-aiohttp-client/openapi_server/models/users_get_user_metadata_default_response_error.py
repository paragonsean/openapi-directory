# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UsersGetUserMetadataDefaultResponseError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):
        """UsersGetUserMetadataDefaultResponseError - a model defined in OpenAPI

        :param code: The code of this UsersGetUserMetadataDefaultResponseError.
        :param message: The message of this UsersGetUserMetadataDefaultResponseError.
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
    def from_dict(cls, dikt: dict) -> 'UsersGetUserMetadataDefaultResponseError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Users_getUserMetadata_default_response_error of this UsersGetUserMetadataDefaultResponseError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this UsersGetUserMetadataDefaultResponseError.


        :return: The code of this UsersGetUserMetadataDefaultResponseError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UsersGetUserMetadataDefaultResponseError.


        :param code: The code of this UsersGetUserMetadataDefaultResponseError.
        :type code: str
        """
        allowed_values = ["BadRequest", "Conflict", "NotAcceptable", "NotFound", "InternalServerError", "Unauthorized"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self):
        """Gets the message of this UsersGetUserMetadataDefaultResponseError.


        :return: The message of this UsersGetUserMetadataDefaultResponseError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UsersGetUserMetadataDefaultResponseError.


        :param message: The message of this UsersGetUserMetadataDefaultResponseError.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
