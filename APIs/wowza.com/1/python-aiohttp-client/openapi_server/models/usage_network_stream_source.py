# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UsageNetworkStreamSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bytes_billed: int=None, bytes_used: int=None, deleted: bool=None, id: str=None, name: str=None):
        """UsageNetworkStreamSource - a model defined in OpenAPI

        :param bytes_billed: The bytes_billed of this UsageNetworkStreamSource.
        :param bytes_used: The bytes_used of this UsageNetworkStreamSource.
        :param deleted: The deleted of this UsageNetworkStreamSource.
        :param id: The id of this UsageNetworkStreamSource.
        :param name: The name of this UsageNetworkStreamSource.
        """
        self.openapi_types = {
            'bytes_billed': int,
            'bytes_used': int,
            'deleted': bool,
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'bytes_billed': 'bytes_billed',
            'bytes_used': 'bytes_used',
            'deleted': 'deleted',
            'id': 'id',
            'name': 'name'
        }

        self._bytes_billed = bytes_billed
        self._bytes_used = bytes_used
        self._deleted = deleted
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UsageNetworkStreamSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The usage_network_stream_source of this UsageNetworkStreamSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bytes_billed(self):
        """Gets the bytes_billed of this UsageNetworkStreamSource.

        The amount of usage, in bytes, that was billed for the stream source during the selected time frame.

        :return: The bytes_billed of this UsageNetworkStreamSource.
        :rtype: int
        """
        return self._bytes_billed

    @bytes_billed.setter
    def bytes_billed(self, bytes_billed):
        """Sets the bytes_billed of this UsageNetworkStreamSource.

        The amount of usage, in bytes, that was billed for the stream source during the selected time frame.

        :param bytes_billed: The bytes_billed of this UsageNetworkStreamSource.
        :type bytes_billed: int
        """

        self._bytes_billed = bytes_billed

    @property
    def bytes_used(self):
        """Gets the bytes_used of this UsageNetworkStreamSource.

        The amount of content, in bytes, that went through the stream source during the selected time frame.

        :return: The bytes_used of this UsageNetworkStreamSource.
        :rtype: int
        """
        return self._bytes_used

    @bytes_used.setter
    def bytes_used(self, bytes_used):
        """Sets the bytes_used of this UsageNetworkStreamSource.

        The amount of content, in bytes, that went through the stream source during the selected time frame.

        :param bytes_used: The bytes_used of this UsageNetworkStreamSource.
        :type bytes_used: int
        """

        self._bytes_used = bytes_used

    @property
    def deleted(self):
        """Gets the deleted of this UsageNetworkStreamSource.

        A value of <strong>true</strong> indicates that the stream source has been removed from Wowza Streaming Cloud.

        :return: The deleted of this UsageNetworkStreamSource.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this UsageNetworkStreamSource.

        A value of <strong>true</strong> indicates that the stream source has been removed from Wowza Streaming Cloud.

        :param deleted: The deleted of this UsageNetworkStreamSource.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this UsageNetworkStreamSource.

        The unique alphanumeric string that identifies the stream source.

        :return: The id of this UsageNetworkStreamSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UsageNetworkStreamSource.

        The unique alphanumeric string that identifies the stream source.

        :param id: The id of this UsageNetworkStreamSource.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UsageNetworkStreamSource.

        A descriptive name for the stream source.

        :return: The name of this UsageNetworkStreamSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UsageNetworkStreamSource.

        A descriptive name for the stream source.

        :param name: The name of this UsageNetworkStreamSource.
        :type name: str
        """

        self._name = name
