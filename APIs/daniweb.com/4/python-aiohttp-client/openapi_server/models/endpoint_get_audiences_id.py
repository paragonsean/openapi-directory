# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bubble import Bubble
from openapi_server import util


class EndpointGetAudiencesID(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[Bubble]=None):
        """EndpointGetAudiencesID - a model defined in OpenAPI

        :param data: The data of this EndpointGetAudiencesID.
        """
        self.openapi_types = {
            'data': List[Bubble]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointGetAudiencesID':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-get-audiences-ID of this EndpointGetAudiencesID.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EndpointGetAudiencesID.


        :return: The data of this EndpointGetAudiencesID.
        :rtype: List[Bubble]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EndpointGetAudiencesID.


        :param data: The data of this EndpointGetAudiencesID.
        :type data: List[Bubble]
        """

        self._data = data
