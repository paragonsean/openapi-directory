# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_resource import AccountResource
from openapi_server import util


class GetAccountResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: AccountResource=None):
        """GetAccountResponse - a model defined in OpenAPI

        :param data: The data of this GetAccountResponse.
        """
        self.openapi_types = {
            'data': AccountResource
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetAccountResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetAccountResponse of this GetAccountResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this GetAccountResponse.

        The account returned in this response. 

        :return: The data of this GetAccountResponse.
        :rtype: AccountResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetAccountResponse.

        The account returned in this response. 

        :param data: The data of this GetAccountResponse.
        :type data: AccountResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data
