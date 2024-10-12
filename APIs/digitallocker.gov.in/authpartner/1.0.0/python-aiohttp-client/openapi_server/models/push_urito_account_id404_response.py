# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PushURIToAccountId404Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: str=None, error_description: str=None):
        """PushURIToAccountId404Response - a model defined in OpenAPI

        :param error: The error of this PushURIToAccountId404Response.
        :param error_description: The error_description of this PushURIToAccountId404Response.
        """
        self.openapi_types = {
            'error': str,
            'error_description': str
        }

        self.attribute_map = {
            'error': 'error',
            'error_description': 'error_description'
        }

        self._error = error
        self._error_description = error_description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PushURIToAccountId404Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Push_URI_to_Account_id_404_response of this PushURIToAccountId404Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this PushURIToAccountId404Response.

        invalid_digilocker_id

        :return: The error of this PushURIToAccountId404Response.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PushURIToAccountId404Response.

        invalid_digilocker_id

        :param error: The error of this PushURIToAccountId404Response.
        :type error: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this PushURIToAccountId404Response.

        The digilockerid parameter is invalid

        :return: The error_description of this PushURIToAccountId404Response.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this PushURIToAccountId404Response.

        The digilockerid parameter is invalid

        :param error_description: The error_description of this PushURIToAccountId404Response.
        :type error_description: str
        """

        self._error_description = error_description
