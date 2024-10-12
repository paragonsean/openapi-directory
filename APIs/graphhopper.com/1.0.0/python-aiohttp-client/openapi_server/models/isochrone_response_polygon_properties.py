# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IsochroneResponsePolygonProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bucket: int=None):
        """IsochroneResponsePolygonProperties - a model defined in OpenAPI

        :param bucket: The bucket of this IsochroneResponsePolygonProperties.
        """
        self.openapi_types = {
            'bucket': int
        }

        self.attribute_map = {
            'bucket': 'bucket'
        }

        self._bucket = bucket

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IsochroneResponsePolygonProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IsochroneResponsePolygon_properties of this IsochroneResponsePolygonProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bucket(self):
        """Gets the bucket of this IsochroneResponsePolygonProperties.


        :return: The bucket of this IsochroneResponsePolygonProperties.
        :rtype: int
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this IsochroneResponsePolygonProperties.


        :param bucket: The bucket of this IsochroneResponsePolygonProperties.
        :type bucket: int
        """

        self._bucket = bucket
