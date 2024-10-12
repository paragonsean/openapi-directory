# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateFavoritesBulkRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_favorite: bool=None, object_ids: List[int]=None):
        """UpdateFavoritesBulkRequest - a model defined in OpenAPI

        :param is_favorite: The is_favorite of this UpdateFavoritesBulkRequest.
        :param object_ids: The object_ids of this UpdateFavoritesBulkRequest.
        """
        self.openapi_types = {
            'is_favorite': bool,
            'object_ids': List[int]
        }

        self.attribute_map = {
            'is_favorite': 'isFavorite',
            'object_ids': 'objectIds'
        }

        self._is_favorite = is_favorite
        self._object_ids = object_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateFavoritesBulkRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateFavoritesBulkRequest of this UpdateFavoritesBulkRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_favorite(self):
        """Gets the is_favorite of this UpdateFavoritesBulkRequest.

        Sets the favorite attribute to true or false on each file in an array of nodes.

        :return: The is_favorite of this UpdateFavoritesBulkRequest.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this UpdateFavoritesBulkRequest.

        Sets the favorite attribute to true or false on each file in an array of nodes.

        :param is_favorite: The is_favorite of this UpdateFavoritesBulkRequest.
        :type is_favorite: bool
        """
        if is_favorite is None:
            raise ValueError("Invalid value for `is_favorite`, must not be `None`")

        self._is_favorite = is_favorite

    @property
    def object_ids(self):
        """Gets the object_ids of this UpdateFavoritesBulkRequest.

        List of ids

        :return: The object_ids of this UpdateFavoritesBulkRequest.
        :rtype: List[int]
        """
        return self._object_ids

    @object_ids.setter
    def object_ids(self, object_ids):
        """Sets the object_ids of this UpdateFavoritesBulkRequest.

        List of ids

        :param object_ids: The object_ids of this UpdateFavoritesBulkRequest.
        :type object_ids: List[int]
        """
        if object_ids is None:
            raise ValueError("Invalid value for `object_ids`, must not be `None`")

        self._object_ids = object_ids
