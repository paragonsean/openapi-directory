# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.usage_network_transcoder import UsageNetworkTranscoder
from openapi_server import util


class UsageNetworkTranscoders(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transcoders: List[UsageNetworkTranscoder]=None):
        """UsageNetworkTranscoders - a model defined in OpenAPI

        :param transcoders: The transcoders of this UsageNetworkTranscoders.
        """
        self.openapi_types = {
            'transcoders': List[UsageNetworkTranscoder]
        }

        self.attribute_map = {
            'transcoders': 'transcoders'
        }

        self._transcoders = transcoders

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UsageNetworkTranscoders':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The usage_network_transcoders of this UsageNetworkTranscoders.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transcoders(self):
        """Gets the transcoders of this UsageNetworkTranscoders.


        :return: The transcoders of this UsageNetworkTranscoders.
        :rtype: List[UsageNetworkTranscoder]
        """
        return self._transcoders

    @transcoders.setter
    def transcoders(self, transcoders):
        """Sets the transcoders of this UsageNetworkTranscoders.


        :param transcoders: The transcoders of this UsageNetworkTranscoders.
        :type transcoders: List[UsageNetworkTranscoder]
        """

        self._transcoders = transcoders
