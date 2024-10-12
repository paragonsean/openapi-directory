# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.group_message import GroupMessage
from openapi_server import util


class EndpointDeleteGroupsMessagesID(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[GroupMessage]=None, status: bool=None):
        """EndpointDeleteGroupsMessagesID - a model defined in OpenAPI

        :param data: The data of this EndpointDeleteGroupsMessagesID.
        :param status: The status of this EndpointDeleteGroupsMessagesID.
        """
        self.openapi_types = {
            'data': List[GroupMessage],
            'status': bool
        }

        self.attribute_map = {
            'data': 'data',
            'status': 'status'
        }

        self._data = data
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointDeleteGroupsMessagesID':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-delete-groups-messages-ID of this EndpointDeleteGroupsMessagesID.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EndpointDeleteGroupsMessagesID.


        :return: The data of this EndpointDeleteGroupsMessagesID.
        :rtype: List[GroupMessage]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EndpointDeleteGroupsMessagesID.


        :param data: The data of this EndpointDeleteGroupsMessagesID.
        :type data: List[GroupMessage]
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this EndpointDeleteGroupsMessagesID.


        :return: The status of this EndpointDeleteGroupsMessagesID.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointDeleteGroupsMessagesID.


        :param status: The status of this EndpointDeleteGroupsMessagesID.
        :type status: bool
        """

        self._status = status
