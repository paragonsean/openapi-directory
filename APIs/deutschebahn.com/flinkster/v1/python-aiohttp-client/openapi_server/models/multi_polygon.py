# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.crs import Crs
from openapi_server.models.geo_json_object import GeoJsonObject
from openapi_server.models.lng_lat_alt import LngLatAlt
from openapi_server import util


class MultiPolygon(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bbox: List[float]=None, crs: Crs=None, coordinates: List[List[List[LngLatAlt]]]=None):
        """MultiPolygon - a model defined in OpenAPI

        :param bbox: The bbox of this MultiPolygon.
        :param crs: The crs of this MultiPolygon.
        :param coordinates: The coordinates of this MultiPolygon.
        """
        self.openapi_types = {
            'bbox': List[float],
            'crs': Crs,
            'coordinates': List[List[List[LngLatAlt]]]
        }

        self.attribute_map = {
            'bbox': 'bbox',
            'crs': 'crs',
            'coordinates': 'coordinates'
        }

        self._bbox = bbox
        self._crs = crs
        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MultiPolygon':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MultiPolygon of this MultiPolygon.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bbox(self):
        """Gets the bbox of this MultiPolygon.


        :return: The bbox of this MultiPolygon.
        :rtype: List[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this MultiPolygon.


        :param bbox: The bbox of this MultiPolygon.
        :type bbox: List[float]
        """

        self._bbox = bbox

    @property
    def crs(self):
        """Gets the crs of this MultiPolygon.


        :return: The crs of this MultiPolygon.
        :rtype: Crs
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """Sets the crs of this MultiPolygon.


        :param crs: The crs of this MultiPolygon.
        :type crs: Crs
        """

        self._crs = crs

    @property
    def coordinates(self):
        """Gets the coordinates of this MultiPolygon.


        :return: The coordinates of this MultiPolygon.
        :rtype: List[List[List[LngLatAlt]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this MultiPolygon.


        :param coordinates: The coordinates of this MultiPolygon.
        :type coordinates: List[List[List[LngLatAlt]]]
        """

        self._coordinates = coordinates
