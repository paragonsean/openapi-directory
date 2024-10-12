# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.reward_program_resource import RewardProgramResource
from openapi_server import util


class FetchRewardProgramResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: RewardProgramResource=None, meta: FetchMetaResponse=None):
        """FetchRewardProgramResponse - a model defined in OpenAPI

        :param data: The data of this FetchRewardProgramResponse.
        :param meta: The meta of this FetchRewardProgramResponse.
        """
        self.openapi_types = {
            'data': RewardProgramResource,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchRewardProgramResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchRewardProgramResponse of this FetchRewardProgramResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchRewardProgramResponse.


        :return: The data of this FetchRewardProgramResponse.
        :rtype: RewardProgramResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchRewardProgramResponse.


        :param data: The data of this FetchRewardProgramResponse.
        :type data: RewardProgramResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this FetchRewardProgramResponse.


        :return: The meta of this FetchRewardProgramResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchRewardProgramResponse.


        :param meta: The meta of this FetchRewardProgramResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
