# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_or_update_meta_response import CreateOrUpdateMetaResponse
from openapi_server.models.reward_earning_resource import RewardEarningResource
from openapi_server import util


class CreateRewardEarningResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: RewardEarningResource=None, meta: CreateOrUpdateMetaResponse=None):
        """CreateRewardEarningResponse - a model defined in OpenAPI

        :param data: The data of this CreateRewardEarningResponse.
        :param meta: The meta of this CreateRewardEarningResponse.
        """
        self.openapi_types = {
            'data': RewardEarningResource,
            'meta': CreateOrUpdateMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateRewardEarningResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateRewardEarningResponse of this CreateRewardEarningResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CreateRewardEarningResponse.


        :return: The data of this CreateRewardEarningResponse.
        :rtype: RewardEarningResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateRewardEarningResponse.


        :param data: The data of this CreateRewardEarningResponse.
        :type data: RewardEarningResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this CreateRewardEarningResponse.


        :return: The meta of this CreateRewardEarningResponse.
        :rtype: CreateOrUpdateMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CreateRewardEarningResponse.


        :param meta: The meta of this CreateRewardEarningResponse.
        :type meta: CreateOrUpdateMetaResponse
        """

        self._meta = meta
