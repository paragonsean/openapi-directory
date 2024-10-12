# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.reward_earning_resource import RewardEarningResource
from openapi_server import util


class FetchRewardEarningsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[RewardEarningResource]=None, meta: FetchMetaResponse=None):
        """FetchRewardEarningsResponse - a model defined in OpenAPI

        :param data: The data of this FetchRewardEarningsResponse.
        :param meta: The meta of this FetchRewardEarningsResponse.
        """
        self.openapi_types = {
            'data': List[RewardEarningResource],
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchRewardEarningsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchRewardEarningsResponse of this FetchRewardEarningsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchRewardEarningsResponse.


        :return: The data of this FetchRewardEarningsResponse.
        :rtype: List[RewardEarningResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchRewardEarningsResponse.


        :param data: The data of this FetchRewardEarningsResponse.
        :type data: List[RewardEarningResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this FetchRewardEarningsResponse.


        :return: The meta of this FetchRewardEarningsResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchRewardEarningsResponse.


        :param meta: The meta of this FetchRewardEarningsResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
