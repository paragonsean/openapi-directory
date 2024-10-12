# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImageIdCreateEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, tag_ids: List[str]=None):
        """ImageIdCreateEntry - a model defined in OpenAPI

        :param id: The id of this ImageIdCreateEntry.
        :param tag_ids: The tag_ids of this ImageIdCreateEntry.
        """
        self.openapi_types = {
            'id': str,
            'tag_ids': List[str]
        }

        self.attribute_map = {
            'id': 'Id',
            'tag_ids': 'TagIds'
        }

        self._id = id
        self._tag_ids = tag_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImageIdCreateEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImageIdCreateEntry of this ImageIdCreateEntry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ImageIdCreateEntry.


        :return: The id of this ImageIdCreateEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageIdCreateEntry.


        :param id: The id of this ImageIdCreateEntry.
        :type id: str
        """

        self._id = id

    @property
    def tag_ids(self):
        """Gets the tag_ids of this ImageIdCreateEntry.


        :return: The tag_ids of this ImageIdCreateEntry.
        :rtype: List[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this ImageIdCreateEntry.


        :param tag_ids: The tag_ids of this ImageIdCreateEntry.
        :type tag_ids: List[str]
        """

        self._tag_ids = tag_ids
