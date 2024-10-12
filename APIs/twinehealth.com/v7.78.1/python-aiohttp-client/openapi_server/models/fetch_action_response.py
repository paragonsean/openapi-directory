# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.action_resource import ActionResource
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server import util


class FetchActionResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: ActionResource=None, meta: FetchMetaResponse=None):
        """FetchActionResponse - a model defined in OpenAPI

        :param data: The data of this FetchActionResponse.
        :param meta: The meta of this FetchActionResponse.
        """
        self.openapi_types = {
            'data': ActionResource,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchActionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchActionResponse of this FetchActionResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchActionResponse.


        :return: The data of this FetchActionResponse.
        :rtype: ActionResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchActionResponse.


        :param data: The data of this FetchActionResponse.
        :type data: ActionResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this FetchActionResponse.


        :return: The meta of this FetchActionResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchActionResponse.


        :param meta: The meta of this FetchActionResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
