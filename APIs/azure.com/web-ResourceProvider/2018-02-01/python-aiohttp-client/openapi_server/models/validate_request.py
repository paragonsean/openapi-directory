# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.validate_properties import ValidateProperties
from openapi_server import util


class ValidateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location: str=None, name: str=None, properties: ValidateProperties=None, type: str=None):
        """ValidateRequest - a model defined in OpenAPI

        :param location: The location of this ValidateRequest.
        :param name: The name of this ValidateRequest.
        :param properties: The properties of this ValidateRequest.
        :param type: The type of this ValidateRequest.
        """
        self.openapi_types = {
            'location': str,
            'name': str,
            'properties': ValidateProperties,
            'type': str
        }

        self.attribute_map = {
            'location': 'location',
            'name': 'name',
            'properties': 'properties',
            'type': 'type'
        }

        self._location = location
        self._name = name
        self._properties = properties
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ValidateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ValidateRequest of this ValidateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this ValidateRequest.

        Expected location of the resource.

        :return: The location of this ValidateRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ValidateRequest.

        Expected location of the resource.

        :param location: The location of this ValidateRequest.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location

    @property
    def name(self):
        """Gets the name of this ValidateRequest.

        Resource name to verify.

        :return: The name of this ValidateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateRequest.

        Resource name to verify.

        :param name: The name of this ValidateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this ValidateRequest.


        :return: The properties of this ValidateRequest.
        :rtype: ValidateProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ValidateRequest.


        :param properties: The properties of this ValidateRequest.
        :type properties: ValidateProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this ValidateRequest.

        Resource type used for verification.

        :return: The type of this ValidateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ValidateRequest.

        Resource type used for verification.

        :param type: The type of this ValidateRequest.
        :type type: str
        """
        allowed_values = ["ServerFarm", "Site"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
