# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.image_object import ImageObject
from openapi_server.models.query import Query
from openapi_server import util


class TrendingImagesTile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image: ImageObject=None, query: Query=None):
        """TrendingImagesTile - a model defined in OpenAPI

        :param image: The image of this TrendingImagesTile.
        :param query: The query of this TrendingImagesTile.
        """
        self.openapi_types = {
            'image': ImageObject,
            'query': Query
        }

        self.attribute_map = {
            'image': 'image',
            'query': 'query'
        }

        self._image = image
        self._query = query

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TrendingImagesTile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TrendingImagesTile of this TrendingImagesTile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self):
        """Gets the image of this TrendingImagesTile.


        :return: The image of this TrendingImagesTile.
        :rtype: ImageObject
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TrendingImagesTile.


        :param image: The image of this TrendingImagesTile.
        :type image: ImageObject
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def query(self):
        """Gets the query of this TrendingImagesTile.


        :return: The query of this TrendingImagesTile.
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this TrendingImagesTile.


        :param query: The query of this TrendingImagesTile.
        :type query: Query
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")

        self._query = query
