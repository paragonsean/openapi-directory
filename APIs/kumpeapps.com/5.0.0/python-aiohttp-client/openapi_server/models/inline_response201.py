# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InlineResponse201(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_key: str=None, success: bool=None):
        """InlineResponse201 - a model defined in OpenAPI

        :param app_key: The app_key of this InlineResponse201.
        :param success: The success of this InlineResponse201.
        """
        self.openapi_types = {
            'app_key': str,
            'success': bool
        }

        self.attribute_map = {
            'app_key': 'app_key',
            'success': 'success'
        }

        self._app_key = app_key
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponse201':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_201 of this InlineResponse201.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_key(self):
        """Gets the app_key of this InlineResponse201.


        :return: The app_key of this InlineResponse201.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this InlineResponse201.


        :param app_key: The app_key of this InlineResponse201.
        :type app_key: str
        """
        if app_key is None:
            raise ValueError("Invalid value for `app_key`, must not be `None`")

        self._app_key = app_key

    @property
    def success(self):
        """Gets the success of this InlineResponse201.


        :return: The success of this InlineResponse201.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse201.


        :param success: The success of this InlineResponse201.
        :type success: bool
        """

        self._success = success
