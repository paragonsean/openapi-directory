# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_meta import CollectionMeta
from openapi_server.models.issue import Issue
from openapi_server.models.safety_rated_location import SafetyRatedLocation
from openapi_server import util


class Success1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: SafetyRatedLocation=None, meta: CollectionMeta=None, warnings: List[Issue]=None):
        """Success1 - a model defined in OpenAPI

        :param data: The data of this Success1.
        :param meta: The meta of this Success1.
        :param warnings: The warnings of this Success1.
        """
        self.openapi_types = {
            'data': SafetyRatedLocation,
            'meta': CollectionMeta,
            'warnings': List[Issue]
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta',
            'warnings': 'warnings'
        }

        self._data = data
        self._meta = meta
        self._warnings = warnings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Success1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Success_1 of this Success1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this Success1.


        :return: The data of this Success1.
        :rtype: SafetyRatedLocation
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Success1.


        :param data: The data of this Success1.
        :type data: SafetyRatedLocation
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this Success1.


        :return: The meta of this Success1.
        :rtype: CollectionMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Success1.


        :param meta: The meta of this Success1.
        :type meta: CollectionMeta
        """

        self._meta = meta

    @property
    def warnings(self):
        """Gets the warnings of this Success1.


        :return: The warnings of this Success1.
        :rtype: List[Issue]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this Success1.


        :param warnings: The warnings of this Success1.
        :type warnings: List[Issue]
        """

        self._warnings = warnings
