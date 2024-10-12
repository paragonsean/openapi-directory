# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateConfigRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, name: str=None):
        """UpdateConfigRequest - a model defined in OpenAPI

        :param description: The description of this UpdateConfigRequest.
        :param name: The name of this UpdateConfigRequest.
        """
        self.openapi_types = {
            'description': str,
            'name': str
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name'
        }

        self._description = description
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateConfigRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateConfigRequest of this UpdateConfigRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this UpdateConfigRequest.


        :return: The description of this UpdateConfigRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateConfigRequest.


        :param description: The description of this UpdateConfigRequest.
        :type description: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateConfigRequest.


        :return: The name of this UpdateConfigRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateConfigRequest.


        :param name: The name of this UpdateConfigRequest.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name
