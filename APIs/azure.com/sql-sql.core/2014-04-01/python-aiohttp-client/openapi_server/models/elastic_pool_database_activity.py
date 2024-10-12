# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.elastic_pool_database_activity_properties import ElasticPoolDatabaseActivityProperties
from openapi_server import util


class ElasticPoolDatabaseActivity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location: str=None, properties: ElasticPoolDatabaseActivityProperties=None, id: str=None, name: str=None, type: str=None):
        """ElasticPoolDatabaseActivity - a model defined in OpenAPI

        :param location: The location of this ElasticPoolDatabaseActivity.
        :param properties: The properties of this ElasticPoolDatabaseActivity.
        :param id: The id of this ElasticPoolDatabaseActivity.
        :param name: The name of this ElasticPoolDatabaseActivity.
        :param type: The type of this ElasticPoolDatabaseActivity.
        """
        self.openapi_types = {
            'location': str,
            'properties': ElasticPoolDatabaseActivityProperties,
            'id': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'location': 'location',
            'properties': 'properties',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._location = location
        self._properties = properties
        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ElasticPoolDatabaseActivity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ElasticPoolDatabaseActivity of this ElasticPoolDatabaseActivity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this ElasticPoolDatabaseActivity.

        The geo-location where the resource lives

        :return: The location of this ElasticPoolDatabaseActivity.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ElasticPoolDatabaseActivity.

        The geo-location where the resource lives

        :param location: The location of this ElasticPoolDatabaseActivity.
        :type location: str
        """

        self._location = location

    @property
    def properties(self):
        """Gets the properties of this ElasticPoolDatabaseActivity.


        :return: The properties of this ElasticPoolDatabaseActivity.
        :rtype: ElasticPoolDatabaseActivityProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ElasticPoolDatabaseActivity.


        :param properties: The properties of this ElasticPoolDatabaseActivity.
        :type properties: ElasticPoolDatabaseActivityProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this ElasticPoolDatabaseActivity.

        Resource ID.

        :return: The id of this ElasticPoolDatabaseActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElasticPoolDatabaseActivity.

        Resource ID.

        :param id: The id of this ElasticPoolDatabaseActivity.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ElasticPoolDatabaseActivity.

        Resource name.

        :return: The name of this ElasticPoolDatabaseActivity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElasticPoolDatabaseActivity.

        Resource name.

        :param name: The name of this ElasticPoolDatabaseActivity.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ElasticPoolDatabaseActivity.

        Resource type.

        :return: The type of this ElasticPoolDatabaseActivity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElasticPoolDatabaseActivity.

        Resource type.

        :param type: The type of this ElasticPoolDatabaseActivity.
        :type type: str
        """

        self._type = type
