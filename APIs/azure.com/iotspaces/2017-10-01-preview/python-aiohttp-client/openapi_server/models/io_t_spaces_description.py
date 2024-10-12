# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.io_t_spaces_properties import IoTSpacesProperties
from openapi_server.models.io_t_spaces_sku_info import IoTSpacesSkuInfo
import re
from openapi_server import util


class IoTSpacesDescription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: IoTSpacesProperties=None, sku: IoTSpacesSkuInfo=None, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """IoTSpacesDescription - a model defined in OpenAPI

        :param properties: The properties of this IoTSpacesDescription.
        :param sku: The sku of this IoTSpacesDescription.
        :param id: The id of this IoTSpacesDescription.
        :param location: The location of this IoTSpacesDescription.
        :param name: The name of this IoTSpacesDescription.
        :param tags: The tags of this IoTSpacesDescription.
        :param type: The type of this IoTSpacesDescription.
        """
        self.openapi_types = {
            'properties': IoTSpacesProperties,
            'sku': IoTSpacesSkuInfo,
            'id': str,
            'location': str,
            'name': str,
            'tags': Dict[str, str],
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'sku': 'sku',
            'id': 'id',
            'location': 'location',
            'name': 'name',
            'tags': 'tags',
            'type': 'type'
        }

        self._properties = properties
        self._sku = sku
        self._id = id
        self._location = location
        self._name = name
        self._tags = tags
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IoTSpacesDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IoTSpacesDescription of this IoTSpacesDescription.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this IoTSpacesDescription.


        :return: The properties of this IoTSpacesDescription.
        :rtype: IoTSpacesProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this IoTSpacesDescription.


        :param properties: The properties of this IoTSpacesDescription.
        :type properties: IoTSpacesProperties
        """

        self._properties = properties

    @property
    def sku(self):
        """Gets the sku of this IoTSpacesDescription.


        :return: The sku of this IoTSpacesDescription.
        :rtype: IoTSpacesSkuInfo
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this IoTSpacesDescription.


        :param sku: The sku of this IoTSpacesDescription.
        :type sku: IoTSpacesSkuInfo
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def id(self):
        """Gets the id of this IoTSpacesDescription.

        The resource identifier.

        :return: The id of this IoTSpacesDescription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IoTSpacesDescription.

        The resource identifier.

        :param id: The id of this IoTSpacesDescription.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this IoTSpacesDescription.

        The resource location.

        :return: The location of this IoTSpacesDescription.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this IoTSpacesDescription.

        The resource location.

        :param location: The location of this IoTSpacesDescription.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location

    @property
    def name(self):
        """Gets the name of this IoTSpacesDescription.

        The resource name.

        :return: The name of this IoTSpacesDescription.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoTSpacesDescription.

        The resource name.

        :param name: The name of this IoTSpacesDescription.
        :type name: str
        """
        if name is not None and not re.search(r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,49}[a-zA-Z0-9]$/`")

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this IoTSpacesDescription.

        The resource tags.

        :return: The tags of this IoTSpacesDescription.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IoTSpacesDescription.

        The resource tags.

        :param tags: The tags of this IoTSpacesDescription.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this IoTSpacesDescription.

        The resource type.

        :return: The type of this IoTSpacesDescription.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoTSpacesDescription.

        The resource type.

        :param type: The type of this IoTSpacesDescription.
        :type type: str
        """

        self._type = type
