# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text: str=None):
        """AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner - a model defined in OpenAPI

        :param text: The text of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.
        """
        self.openapi_types = {
            'text': str
        }

        self.attribute_map = {
            'text': '#text'
        }

        self._text = text

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The available_media_sets_media_sets_media_set_inner_media_sets_media_set_inner of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.


        :return: The text of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.


        :param text: The text of this AvailableMediaSetsMediaSetsMediaSetInnerMediaSetsMediaSetInner.
        :type text: str
        """

        self._text = text
