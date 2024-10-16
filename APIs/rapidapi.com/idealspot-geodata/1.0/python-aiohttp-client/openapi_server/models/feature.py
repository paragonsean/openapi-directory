# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geometry import Geometry
from openapi_server.models.properties2 import Properties2
from openapi_server import util


class Feature(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, geometry: Geometry=None, properties: Properties2=None, type: str=None):
        """Feature - a model defined in OpenAPI

        :param geometry: The geometry of this Feature.
        :param properties: The properties of this Feature.
        :param type: The type of this Feature.
        """
        self.openapi_types = {
            'geometry': Geometry,
            'properties': Properties2,
            'type': str
        }

        self.attribute_map = {
            'geometry': 'geometry',
            'properties': 'properties',
            'type': 'type'
        }

        self._geometry = geometry
        self._properties = properties
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Feature':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Feature of this Feature.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def geometry(self):
        """Gets the geometry of this Feature.


        :return: The geometry of this Feature.
        :rtype: Geometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Feature.


        :param geometry: The geometry of this Feature.
        :type geometry: Geometry
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")

        self._geometry = geometry

    @property
    def properties(self):
        """Gets the properties of this Feature.


        :return: The properties of this Feature.
        :rtype: Properties2
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Feature.


        :param properties: The properties of this Feature.
        :type properties: Properties2
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this Feature.


        :return: The type of this Feature.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Feature.


        :param type: The type of this Feature.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
