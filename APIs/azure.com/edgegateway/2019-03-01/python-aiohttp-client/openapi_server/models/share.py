# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.share_properties import ShareProperties
from openapi_server import util


class Share(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: ShareProperties=None, id: str=None, name: str=None, type: str=None):
        """Share - a model defined in OpenAPI

        :param properties: The properties of this Share.
        :param id: The id of this Share.
        :param name: The name of this Share.
        :param type: The type of this Share.
        """
        self.openapi_types = {
            'properties': ShareProperties,
            'id': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._properties = properties
        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Share':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Share of this Share.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this Share.


        :return: The properties of this Share.
        :rtype: ShareProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Share.


        :param properties: The properties of this Share.
        :type properties: ShareProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this Share.

        The path ID that uniquely identifies the object.

        :return: The id of this Share.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Share.

        The path ID that uniquely identifies the object.

        :param id: The id of this Share.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Share.

        The object name.

        :return: The name of this Share.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Share.

        The object name.

        :param name: The name of this Share.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Share.

        The hierarchical type of the object.

        :return: The type of this Share.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Share.

        The hierarchical type of the object.

        :param type: The type of this Share.
        :type type: str
        """

        self._type = type
