# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.database_operation_properties import DatabaseOperationProperties
from openapi_server import util


class DatabaseOperation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: DatabaseOperationProperties=None, id: str=None, name: str=None, type: str=None):
        """DatabaseOperation - a model defined in OpenAPI

        :param properties: The properties of this DatabaseOperation.
        :param id: The id of this DatabaseOperation.
        :param name: The name of this DatabaseOperation.
        :param type: The type of this DatabaseOperation.
        """
        self.openapi_types = {
            'properties': DatabaseOperationProperties,
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
    def from_dict(cls, dikt: dict) -> 'DatabaseOperation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DatabaseOperation of this DatabaseOperation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this DatabaseOperation.


        :return: The properties of this DatabaseOperation.
        :rtype: DatabaseOperationProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DatabaseOperation.


        :param properties: The properties of this DatabaseOperation.
        :type properties: DatabaseOperationProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this DatabaseOperation.

        Resource ID.

        :return: The id of this DatabaseOperation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseOperation.

        Resource ID.

        :param id: The id of this DatabaseOperation.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatabaseOperation.

        Resource name.

        :return: The name of this DatabaseOperation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseOperation.

        Resource name.

        :param name: The name of this DatabaseOperation.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DatabaseOperation.

        Resource type.

        :return: The type of this DatabaseOperation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatabaseOperation.

        Resource type.

        :param type: The type of this DatabaseOperation.
        :type type: str
        """

        self._type = type
