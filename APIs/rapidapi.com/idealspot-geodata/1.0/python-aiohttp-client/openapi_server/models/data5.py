# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.metadata1 import Metadata1
from openapi_server.models.roadsegment import Roadsegment
from openapi_server.models.stats import Stats
from openapi_server import util


class Data5(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[List[int]]=None, metadata: Metadata1=None, roadsegment: Roadsegment=None, stats: Stats=None):
        """Data5 - a model defined in OpenAPI

        :param data: The data of this Data5.
        :param metadata: The metadata of this Data5.
        :param roadsegment: The roadsegment of this Data5.
        :param stats: The stats of this Data5.
        """
        self.openapi_types = {
            'data': List[List[int]],
            'metadata': Metadata1,
            'roadsegment': Roadsegment,
            'stats': Stats
        }

        self.attribute_map = {
            'data': 'data',
            'metadata': 'metadata',
            'roadsegment': 'roadsegment',
            'stats': 'stats'
        }

        self._data = data
        self._metadata = metadata
        self._roadsegment = roadsegment
        self._stats = stats

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Data5':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Data5 of this Data5.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this Data5.


        :return: The data of this Data5.
        :rtype: List[List[int]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Data5.


        :param data: The data of this Data5.
        :type data: List[List[int]]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def metadata(self):
        """Gets the metadata of this Data5.


        :return: The metadata of this Data5.
        :rtype: Metadata1
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Data5.


        :param metadata: The metadata of this Data5.
        :type metadata: Metadata1
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata

    @property
    def roadsegment(self):
        """Gets the roadsegment of this Data5.


        :return: The roadsegment of this Data5.
        :rtype: Roadsegment
        """
        return self._roadsegment

    @roadsegment.setter
    def roadsegment(self, roadsegment):
        """Sets the roadsegment of this Data5.


        :param roadsegment: The roadsegment of this Data5.
        :type roadsegment: Roadsegment
        """
        if roadsegment is None:
            raise ValueError("Invalid value for `roadsegment`, must not be `None`")

        self._roadsegment = roadsegment

    @property
    def stats(self):
        """Gets the stats of this Data5.


        :return: The stats of this Data5.
        :rtype: Stats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Data5.


        :param stats: The stats of this Data5.
        :type stats: Stats
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")

        self._stats = stats
