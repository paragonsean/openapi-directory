# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.available_media_sets_media_sets_media_set_inner_media_sets_media_set_inner import AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner
from openapi_server import util


class AvailableMediaSetsMediaSetsMediaSetInnerMediaSets(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, media_set: List[AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner]=None):
        """AvailableMediaSetsMediaSetsMediaSetInnerMediaSets - a model defined in OpenAPI

        :param media_set: The media_set of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.
        """
        self.openapi_types = {
            'media_set': List[AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner]
        }

        self.attribute_map = {
            'media_set': 'media_set'
        }

        self._media_set = media_set

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AvailableMediaSetsMediaSetsMediaSetInnerMediaSets':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The available_media_sets_media_sets_media_set_inner_media_sets of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media_set(self):
        """Gets the media_set of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.


        :return: The media_set of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.
        :rtype: List[AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner]
        """
        return self._media_set

    @media_set.setter
    def media_set(self, media_set):
        """Sets the media_set of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.


        :param media_set: The media_set of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSets.
        :type media_set: List[AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner]
        """
        if media_set is None:
            raise ValueError("Invalid value for `media_set`, must not be `None`")
        if media_set is not None and len(media_set) < 1:
            raise ValueError("Invalid value for `media_set`, number of items must be greater than or equal to `1`")

        self._media_set = media_set
