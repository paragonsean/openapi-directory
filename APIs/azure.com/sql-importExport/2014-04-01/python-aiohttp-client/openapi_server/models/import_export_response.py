# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.import_export_response_properties import ImportExportResponseProperties
from openapi_server import util


class ImportExportResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: ImportExportResponseProperties=None, id: str=None, name: str=None, type: str=None):
        """ImportExportResponse - a model defined in OpenAPI

        :param properties: The properties of this ImportExportResponse.
        :param id: The id of this ImportExportResponse.
        :param name: The name of this ImportExportResponse.
        :param type: The type of this ImportExportResponse.
        """
        self.openapi_types = {
            'properties': ImportExportResponseProperties,
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
    def from_dict(cls, dikt: dict) -> 'ImportExportResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportExportResponse of this ImportExportResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this ImportExportResponse.


        :return: The properties of this ImportExportResponse.
        :rtype: ImportExportResponseProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ImportExportResponse.


        :param properties: The properties of this ImportExportResponse.
        :type properties: ImportExportResponseProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this ImportExportResponse.

        Resource ID.

        :return: The id of this ImportExportResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportExportResponse.

        Resource ID.

        :param id: The id of this ImportExportResponse.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportExportResponse.

        Resource name.

        :return: The name of this ImportExportResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportExportResponse.

        Resource name.

        :param name: The name of this ImportExportResponse.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ImportExportResponse.

        Resource type.

        :return: The type of this ImportExportResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportExportResponse.

        Resource type.

        :param type: The type of this ImportExportResponse.
        :type type: str
        """

        self._type = type
