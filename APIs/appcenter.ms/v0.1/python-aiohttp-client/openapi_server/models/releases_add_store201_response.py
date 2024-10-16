# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ReleasesAddStore201Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None):
        """ReleasesAddStore201Response - a model defined in OpenAPI

        :param id: The id of this ReleasesAddStore201Response.
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleasesAddStore201Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The releases_addStore_201_response of this ReleasesAddStore201Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ReleasesAddStore201Response.

        Unique id for the release destination

        :return: The id of this ReleasesAddStore201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleasesAddStore201Response.

        Unique id for the release destination

        :param id: The id of this ReleasesAddStore201Response.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
