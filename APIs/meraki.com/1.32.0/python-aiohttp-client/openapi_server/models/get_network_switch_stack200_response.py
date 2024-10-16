# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSwitchStack200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, serials: List[str]=None):
        """GetNetworkSwitchStack200Response - a model defined in OpenAPI

        :param id: The id of this GetNetworkSwitchStack200Response.
        :param name: The name of this GetNetworkSwitchStack200Response.
        :param serials: The serials of this GetNetworkSwitchStack200Response.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'serials': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'serials': 'serials'
        }

        self._id = id
        self._name = name
        self._serials = serials

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchStack200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchStack_200_response of this GetNetworkSwitchStack200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetNetworkSwitchStack200Response.

        Switch stacks id

        :return: The id of this GetNetworkSwitchStack200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkSwitchStack200Response.

        Switch stacks id

        :param id: The id of this GetNetworkSwitchStack200Response.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetNetworkSwitchStack200Response.

        Switch stacks name

        :return: The name of this GetNetworkSwitchStack200Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetNetworkSwitchStack200Response.

        Switch stacks name

        :param name: The name of this GetNetworkSwitchStack200Response.
        :type name: str
        """

        self._name = name

    @property
    def serials(self):
        """Gets the serials of this GetNetworkSwitchStack200Response.

        Serials of the switches in the switch stack

        :return: The serials of this GetNetworkSwitchStack200Response.
        :rtype: List[str]
        """
        return self._serials

    @serials.setter
    def serials(self, serials):
        """Sets the serials of this GetNetworkSwitchStack200Response.

        Serials of the switches in the switch stack

        :param serials: The serials of this GetNetworkSwitchStack200Response.
        :type serials: List[str]
        """

        self._serials = serials
