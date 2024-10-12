# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_pagination import ApiPagination
from openapi_server.models.bubble import Bubble
from openapi_server import util


class EndpointGetAudiences(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[Bubble]=None, pagination: ApiPagination=None):
        """EndpointGetAudiences - a model defined in OpenAPI

        :param data: The data of this EndpointGetAudiences.
        :param pagination: The pagination of this EndpointGetAudiences.
        """
        self.openapi_types = {
            'data': List[Bubble],
            'pagination': ApiPagination
        }

        self.attribute_map = {
            'data': 'data',
            'pagination': 'pagination'
        }

        self._data = data
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointGetAudiences':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-get-audiences of this EndpointGetAudiences.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EndpointGetAudiences.


        :return: The data of this EndpointGetAudiences.
        :rtype: List[Bubble]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EndpointGetAudiences.


        :param data: The data of this EndpointGetAudiences.
        :type data: List[Bubble]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this EndpointGetAudiences.


        :return: The pagination of this EndpointGetAudiences.
        :rtype: ApiPagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EndpointGetAudiences.


        :param pagination: The pagination of this EndpointGetAudiences.
        :type pagination: ApiPagination
        """

        self._pagination = pagination
