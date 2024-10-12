# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geocoding_point import GeocodingPoint
from openapi_server import util


class GeocodingLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, country: str=None, housenumber: str=None, name: str=None, osm_id: str=None, osm_key: str=None, osm_type: str=None, point: GeocodingPoint=None, postcode: str=None, state: str=None, street: str=None):
        """GeocodingLocation - a model defined in OpenAPI

        :param city: The city of this GeocodingLocation.
        :param country: The country of this GeocodingLocation.
        :param housenumber: The housenumber of this GeocodingLocation.
        :param name: The name of this GeocodingLocation.
        :param osm_id: The osm_id of this GeocodingLocation.
        :param osm_key: The osm_key of this GeocodingLocation.
        :param osm_type: The osm_type of this GeocodingLocation.
        :param point: The point of this GeocodingLocation.
        :param postcode: The postcode of this GeocodingLocation.
        :param state: The state of this GeocodingLocation.
        :param street: The street of this GeocodingLocation.
        """
        self.openapi_types = {
            'city': str,
            'country': str,
            'housenumber': str,
            'name': str,
            'osm_id': str,
            'osm_key': str,
            'osm_type': str,
            'point': GeocodingPoint,
            'postcode': str,
            'state': str,
            'street': str
        }

        self.attribute_map = {
            'city': 'city',
            'country': 'country',
            'housenumber': 'housenumber',
            'name': 'name',
            'osm_id': 'osm_id',
            'osm_key': 'osm_key',
            'osm_type': 'osm_type',
            'point': 'point',
            'postcode': 'postcode',
            'state': 'state',
            'street': 'street'
        }

        self._city = city
        self._country = country
        self._housenumber = housenumber
        self._name = name
        self._osm_id = osm_id
        self._osm_key = osm_key
        self._osm_type = osm_type
        self._point = point
        self._postcode = postcode
        self._state = state
        self._street = street

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GeocodingLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GeocodingLocation of this GeocodingLocation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this GeocodingLocation.

        The city of the address

        :return: The city of this GeocodingLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this GeocodingLocation.

        The city of the address

        :param city: The city of this GeocodingLocation.
        :type city: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this GeocodingLocation.

        The country of the address

        :return: The country of this GeocodingLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this GeocodingLocation.

        The country of the address

        :param country: The country of this GeocodingLocation.
        :type country: str
        """

        self._country = country

    @property
    def housenumber(self):
        """Gets the housenumber of this GeocodingLocation.

        The housenumber of the address

        :return: The housenumber of this GeocodingLocation.
        :rtype: str
        """
        return self._housenumber

    @housenumber.setter
    def housenumber(self, housenumber):
        """Sets the housenumber of this GeocodingLocation.

        The housenumber of the address

        :param housenumber: The housenumber of this GeocodingLocation.
        :type housenumber: str
        """

        self._housenumber = housenumber

    @property
    def name(self):
        """Gets the name of this GeocodingLocation.

        The name of the entity. Can be a boundary, POI, address, etc

        :return: The name of this GeocodingLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeocodingLocation.

        The name of the entity. Can be a boundary, POI, address, etc

        :param name: The name of this GeocodingLocation.
        :type name: str
        """

        self._name = name

    @property
    def osm_id(self):
        """Gets the osm_id of this GeocodingLocation.

        The OSM ID of the entity

        :return: The osm_id of this GeocodingLocation.
        :rtype: str
        """
        return self._osm_id

    @osm_id.setter
    def osm_id(self, osm_id):
        """Sets the osm_id of this GeocodingLocation.

        The OSM ID of the entity

        :param osm_id: The osm_id of this GeocodingLocation.
        :type osm_id: str
        """

        self._osm_id = osm_id

    @property
    def osm_key(self):
        """Gets the osm_key of this GeocodingLocation.

        The OSM key of the entity

        :return: The osm_key of this GeocodingLocation.
        :rtype: str
        """
        return self._osm_key

    @osm_key.setter
    def osm_key(self, osm_key):
        """Sets the osm_key of this GeocodingLocation.

        The OSM key of the entity

        :param osm_key: The osm_key of this GeocodingLocation.
        :type osm_key: str
        """

        self._osm_key = osm_key

    @property
    def osm_type(self):
        """Gets the osm_type of this GeocodingLocation.

        N = node, R = relation, W = way

        :return: The osm_type of this GeocodingLocation.
        :rtype: str
        """
        return self._osm_type

    @osm_type.setter
    def osm_type(self, osm_type):
        """Sets the osm_type of this GeocodingLocation.

        N = node, R = relation, W = way

        :param osm_type: The osm_type of this GeocodingLocation.
        :type osm_type: str
        """

        self._osm_type = osm_type

    @property
    def point(self):
        """Gets the point of this GeocodingLocation.


        :return: The point of this GeocodingLocation.
        :rtype: GeocodingPoint
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this GeocodingLocation.


        :param point: The point of this GeocodingLocation.
        :type point: GeocodingPoint
        """

        self._point = point

    @property
    def postcode(self):
        """Gets the postcode of this GeocodingLocation.

        The postcode of the address

        :return: The postcode of this GeocodingLocation.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this GeocodingLocation.

        The postcode of the address

        :param postcode: The postcode of this GeocodingLocation.
        :type postcode: str
        """

        self._postcode = postcode

    @property
    def state(self):
        """Gets the state of this GeocodingLocation.

        The state of the address

        :return: The state of this GeocodingLocation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GeocodingLocation.

        The state of the address

        :param state: The state of this GeocodingLocation.
        :type state: str
        """

        self._state = state

    @property
    def street(self):
        """Gets the street of this GeocodingLocation.

        The street of the address

        :return: The street of this GeocodingLocation.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this GeocodingLocation.

        The street of the address

        :param street: The street of this GeocodingLocation.
        :type street: str
        """

        self._street = street
