# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.context_photo import ContextPhoto
from openapi_server import util


class ContextPhotos(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, photos: List[ContextPhoto]=None):
        """ContextPhotos - a model defined in OpenAPI

        :param photos: The photos of this ContextPhotos.
        """
        self.openapi_types = {
            'photos': List[ContextPhoto]
        }

        self.attribute_map = {
            'photos': 'photos'
        }

        self._photos = photos

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContextPhotos':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContextPhotos of this ContextPhotos.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def photos(self):
        """Gets the photos of this ContextPhotos.


        :return: The photos of this ContextPhotos.
        :rtype: List[ContextPhoto]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this ContextPhotos.


        :param photos: The photos of this ContextPhotos.
        :type photos: List[ContextPhoto]
        """

        self._photos = photos
