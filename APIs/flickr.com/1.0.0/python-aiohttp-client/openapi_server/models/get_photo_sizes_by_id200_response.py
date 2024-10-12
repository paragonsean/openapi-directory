# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_photo_sizes_by_id200_response_sizes import GetPhotoSizesByID200ResponseSizes
from openapi_server import util


class GetPhotoSizesByID200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sizes: GetPhotoSizesByID200ResponseSizes=None, stat: str=None):
        """GetPhotoSizesByID200Response - a model defined in OpenAPI

        :param sizes: The sizes of this GetPhotoSizesByID200Response.
        :param stat: The stat of this GetPhotoSizesByID200Response.
        """
        self.openapi_types = {
            'sizes': GetPhotoSizesByID200ResponseSizes,
            'stat': str
        }

        self.attribute_map = {
            'sizes': 'sizes',
            'stat': 'stat'
        }

        self._sizes = sizes
        self._stat = stat

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetPhotoSizesByID200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getPhotoSizesByID_200_response of this GetPhotoSizesByID200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sizes(self):
        """Gets the sizes of this GetPhotoSizesByID200Response.


        :return: The sizes of this GetPhotoSizesByID200Response.
        :rtype: GetPhotoSizesByID200ResponseSizes
        """
        return self._sizes

    @sizes.setter
    def sizes(self, sizes):
        """Sets the sizes of this GetPhotoSizesByID200Response.


        :param sizes: The sizes of this GetPhotoSizesByID200Response.
        :type sizes: GetPhotoSizesByID200ResponseSizes
        """

        self._sizes = sizes

    @property
    def stat(self):
        """Gets the stat of this GetPhotoSizesByID200Response.


        :return: The stat of this GetPhotoSizesByID200Response.
        :rtype: str
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this GetPhotoSizesByID200Response.


        :param stat: The stat of this GetPhotoSizesByID200Response.
        :type stat: str
        """

        self._stat = stat
