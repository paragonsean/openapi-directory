# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LockNetworkSmDevicesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids: str=None, pin: int=None, scope: str=None, serials: str=None, wifi_macs: str=None):
        """LockNetworkSmDevicesRequest - a model defined in OpenAPI

        :param ids: The ids of this LockNetworkSmDevicesRequest.
        :param pin: The pin of this LockNetworkSmDevicesRequest.
        :param scope: The scope of this LockNetworkSmDevicesRequest.
        :param serials: The serials of this LockNetworkSmDevicesRequest.
        :param wifi_macs: The wifi_macs of this LockNetworkSmDevicesRequest.
        """
        self.openapi_types = {
            'ids': str,
            'pin': int,
            'scope': str,
            'serials': str,
            'wifi_macs': str
        }

        self.attribute_map = {
            'ids': 'ids',
            'pin': 'pin',
            'scope': 'scope',
            'serials': 'serials',
            'wifi_macs': 'wifiMacs'
        }

        self._ids = ids
        self._pin = pin
        self._scope = scope
        self._serials = serials
        self._wifi_macs = wifi_macs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LockNetworkSmDevicesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The lockNetworkSmDevices_request of this LockNetworkSmDevicesRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this LockNetworkSmDevicesRequest.

        The ids of the devices to be locked.

        :return: The ids of this LockNetworkSmDevicesRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this LockNetworkSmDevicesRequest.

        The ids of the devices to be locked.

        :param ids: The ids of this LockNetworkSmDevicesRequest.
        :type ids: str
        """

        self._ids = ids

    @property
    def pin(self):
        """Gets the pin of this LockNetworkSmDevicesRequest.

        The pin number for locking macOS devices (a six digit number). Required only for macOS devices.

        :return: The pin of this LockNetworkSmDevicesRequest.
        :rtype: int
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this LockNetworkSmDevicesRequest.

        The pin number for locking macOS devices (a six digit number). Required only for macOS devices.

        :param pin: The pin of this LockNetworkSmDevicesRequest.
        :type pin: int
        """

        self._pin = pin

    @property
    def scope(self):
        """Gets the scope of this LockNetworkSmDevicesRequest.

        The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.

        :return: The scope of this LockNetworkSmDevicesRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this LockNetworkSmDevicesRequest.

        The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.

        :param scope: The scope of this LockNetworkSmDevicesRequest.
        :type scope: str
        """

        self._scope = scope

    @property
    def serials(self):
        """Gets the serials of this LockNetworkSmDevicesRequest.

        The serials of the devices to be locked.

        :return: The serials of this LockNetworkSmDevicesRequest.
        :rtype: str
        """
        return self._serials

    @serials.setter
    def serials(self, serials):
        """Sets the serials of this LockNetworkSmDevicesRequest.

        The serials of the devices to be locked.

        :param serials: The serials of this LockNetworkSmDevicesRequest.
        :type serials: str
        """

        self._serials = serials

    @property
    def wifi_macs(self):
        """Gets the wifi_macs of this LockNetworkSmDevicesRequest.

        The wifiMacs of the devices to be locked.

        :return: The wifi_macs of this LockNetworkSmDevicesRequest.
        :rtype: str
        """
        return self._wifi_macs

    @wifi_macs.setter
    def wifi_macs(self, wifi_macs):
        """Sets the wifi_macs of this LockNetworkSmDevicesRequest.

        The wifiMacs of the devices to be locked.

        :param wifi_macs: The wifi_macs of this LockNetworkSmDevicesRequest.
        :type wifi_macs: str
        """

        self._wifi_macs = wifi_macs
