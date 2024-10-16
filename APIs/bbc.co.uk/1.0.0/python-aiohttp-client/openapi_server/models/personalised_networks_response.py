# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.personalised_networks import PersonalisedNetworks
from openapi_server import util


class PersonalisedNetworksResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _schema: str=None, limit: int=None, offset: int=None, results: List[PersonalisedNetworks]=None, total: int=None):
        """PersonalisedNetworksResponse - a model defined in OpenAPI

        :param _schema: The _schema of this PersonalisedNetworksResponse.
        :param limit: The limit of this PersonalisedNetworksResponse.
        :param offset: The offset of this PersonalisedNetworksResponse.
        :param results: The results of this PersonalisedNetworksResponse.
        :param total: The total of this PersonalisedNetworksResponse.
        """
        self.openapi_types = {
            '_schema': str,
            'limit': int,
            'offset': int,
            'results': List[PersonalisedNetworks],
            'total': int
        }

        self.attribute_map = {
            '_schema': '$schema',
            'limit': 'limit',
            'offset': 'offset',
            'results': 'results',
            'total': 'total'
        }

        self.__schema = _schema
        self._limit = limit
        self._offset = offset
        self._results = results
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PersonalisedNetworksResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PersonalisedNetworksResponse of this PersonalisedNetworksResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _schema(self):
        """Gets the _schema of this PersonalisedNetworksResponse.


        :return: The _schema of this PersonalisedNetworksResponse.
        :rtype: str
        """
        return self.__schema

    @_schema.setter
    def _schema(self, _schema):
        """Sets the _schema of this PersonalisedNetworksResponse.


        :param _schema: The _schema of this PersonalisedNetworksResponse.
        :type _schema: str
        """
        if _schema is None:
            raise ValueError("Invalid value for `_schema`, must not be `None`")

        self.__schema = _schema

    @property
    def limit(self):
        """Gets the limit of this PersonalisedNetworksResponse.


        :return: The limit of this PersonalisedNetworksResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PersonalisedNetworksResponse.


        :param limit: The limit of this PersonalisedNetworksResponse.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this PersonalisedNetworksResponse.


        :return: The offset of this PersonalisedNetworksResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PersonalisedNetworksResponse.


        :param offset: The offset of this PersonalisedNetworksResponse.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")

        self._offset = offset

    @property
    def results(self):
        """Gets the results of this PersonalisedNetworksResponse.


        :return: The results of this PersonalisedNetworksResponse.
        :rtype: List[PersonalisedNetworks]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PersonalisedNetworksResponse.


        :param results: The results of this PersonalisedNetworksResponse.
        :type results: List[PersonalisedNetworks]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results

    @property
    def total(self):
        """Gets the total of this PersonalisedNetworksResponse.


        :return: The total of this PersonalisedNetworksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PersonalisedNetworksResponse.


        :param total: The total of this PersonalisedNetworksResponse.
        :type total: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")

        self._total = total
