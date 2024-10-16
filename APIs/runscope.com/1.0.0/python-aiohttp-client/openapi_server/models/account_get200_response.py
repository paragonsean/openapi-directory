# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account import Account
from openapi_server.models.meta import Meta
from openapi_server import util


class AccountGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: Account=None, meta: Meta=None):
        """AccountGet200Response - a model defined in OpenAPI

        :param data: The data of this AccountGet200Response.
        :param meta: The meta of this AccountGet200Response.
        """
        self.openapi_types = {
            'data': Account,
            'meta': Meta
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccountGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _account_get_200_response of this AccountGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this AccountGet200Response.


        :return: The data of this AccountGet200Response.
        :rtype: Account
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AccountGet200Response.


        :param data: The data of this AccountGet200Response.
        :type data: Account
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this AccountGet200Response.


        :return: The meta of this AccountGet200Response.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this AccountGet200Response.


        :param meta: The meta of this AccountGet200Response.
        :type meta: Meta
        """

        self._meta = meta
