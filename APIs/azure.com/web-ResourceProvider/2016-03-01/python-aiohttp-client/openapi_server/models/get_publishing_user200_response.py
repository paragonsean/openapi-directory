# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_publishing_user200_response_properties import GetPublishingUser200ResponseProperties
from openapi_server import util


class GetPublishingUser200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: GetPublishingUser200ResponseProperties=None, id: str=None, kind: str=None, name: str=None, type: str=None):
        """GetPublishingUser200Response - a model defined in OpenAPI

        :param properties: The properties of this GetPublishingUser200Response.
        :param id: The id of this GetPublishingUser200Response.
        :param kind: The kind of this GetPublishingUser200Response.
        :param name: The name of this GetPublishingUser200Response.
        :param type: The type of this GetPublishingUser200Response.
        """
        self.openapi_types = {
            'properties': GetPublishingUser200ResponseProperties,
            'id': str,
            'kind': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'id': 'id',
            'kind': 'kind',
            'name': 'name',
            'type': 'type'
        }

        self._properties = properties
        self._id = id
        self._kind = kind
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetPublishingUser200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetPublishingUser_200_response of this GetPublishingUser200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this GetPublishingUser200Response.


        :return: The properties of this GetPublishingUser200Response.
        :rtype: GetPublishingUser200ResponseProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GetPublishingUser200Response.


        :param properties: The properties of this GetPublishingUser200Response.
        :type properties: GetPublishingUser200ResponseProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this GetPublishingUser200Response.

        Resource Id.

        :return: The id of this GetPublishingUser200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetPublishingUser200Response.

        Resource Id.

        :param id: The id of this GetPublishingUser200Response.
        :type id: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this GetPublishingUser200Response.

        Kind of resource.

        :return: The kind of this GetPublishingUser200Response.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this GetPublishingUser200Response.

        Kind of resource.

        :param kind: The kind of this GetPublishingUser200Response.
        :type kind: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this GetPublishingUser200Response.

        Resource Name.

        :return: The name of this GetPublishingUser200Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetPublishingUser200Response.

        Resource Name.

        :param name: The name of this GetPublishingUser200Response.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GetPublishingUser200Response.

        Resource type.

        :return: The type of this GetPublishingUser200Response.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetPublishingUser200Response.

        Resource type.

        :param type: The type of this GetPublishingUser200Response.
        :type type: str
        """

        self._type = type
