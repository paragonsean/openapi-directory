# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Wifi(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bssid: str=None, has_changes: bool=None, noise_level: int=None, signal_level: int=None, ssid: str=None, wpa_configured: bool=None, wpa_id: int=None, wpa_state: int=None):
        """Wifi - a model defined in OpenAPI

        :param bssid: The bssid of this Wifi.
        :param has_changes: The has_changes of this Wifi.
        :param noise_level: The noise_level of this Wifi.
        :param signal_level: The signal_level of this Wifi.
        :param ssid: The ssid of this Wifi.
        :param wpa_configured: The wpa_configured of this Wifi.
        :param wpa_id: The wpa_id of this Wifi.
        :param wpa_state: The wpa_state of this Wifi.
        """
        self.openapi_types = {
            'bssid': str,
            'has_changes': bool,
            'noise_level': int,
            'signal_level': int,
            'ssid': str,
            'wpa_configured': bool,
            'wpa_id': int,
            'wpa_state': int
        }

        self.attribute_map = {
            'bssid': 'bssid',
            'has_changes': 'has_changes',
            'noise_level': 'noise_level',
            'signal_level': 'signal_level',
            'ssid': 'ssid',
            'wpa_configured': 'wpa_configured',
            'wpa_id': 'wpa_id',
            'wpa_state': 'wpa_state'
        }

        self._bssid = bssid
        self._has_changes = has_changes
        self._noise_level = noise_level
        self._signal_level = signal_level
        self._ssid = ssid
        self._wpa_configured = wpa_configured
        self._wpa_id = wpa_id
        self._wpa_state = wpa_state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Wifi':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Wifi of this Wifi.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bssid(self):
        """Gets the bssid of this Wifi.


        :return: The bssid of this Wifi.
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this Wifi.


        :param bssid: The bssid of this Wifi.
        :type bssid: str
        """
        if bssid is None:
            raise ValueError("Invalid value for `bssid`, must not be `None`")

        self._bssid = bssid

    @property
    def has_changes(self):
        """Gets the has_changes of this Wifi.


        :return: The has_changes of this Wifi.
        :rtype: bool
        """
        return self._has_changes

    @has_changes.setter
    def has_changes(self, has_changes):
        """Sets the has_changes of this Wifi.


        :param has_changes: The has_changes of this Wifi.
        :type has_changes: bool
        """
        if has_changes is None:
            raise ValueError("Invalid value for `has_changes`, must not be `None`")

        self._has_changes = has_changes

    @property
    def noise_level(self):
        """Gets the noise_level of this Wifi.


        :return: The noise_level of this Wifi.
        :rtype: int
        """
        return self._noise_level

    @noise_level.setter
    def noise_level(self, noise_level):
        """Sets the noise_level of this Wifi.


        :param noise_level: The noise_level of this Wifi.
        :type noise_level: int
        """
        if noise_level is None:
            raise ValueError("Invalid value for `noise_level`, must not be `None`")

        self._noise_level = noise_level

    @property
    def signal_level(self):
        """Gets the signal_level of this Wifi.


        :return: The signal_level of this Wifi.
        :rtype: int
        """
        return self._signal_level

    @signal_level.setter
    def signal_level(self, signal_level):
        """Sets the signal_level of this Wifi.


        :param signal_level: The signal_level of this Wifi.
        :type signal_level: int
        """
        if signal_level is None:
            raise ValueError("Invalid value for `signal_level`, must not be `None`")

        self._signal_level = signal_level

    @property
    def ssid(self):
        """Gets the ssid of this Wifi.


        :return: The ssid of this Wifi.
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this Wifi.


        :param ssid: The ssid of this Wifi.
        :type ssid: str
        """
        if ssid is None:
            raise ValueError("Invalid value for `ssid`, must not be `None`")

        self._ssid = ssid

    @property
    def wpa_configured(self):
        """Gets the wpa_configured of this Wifi.


        :return: The wpa_configured of this Wifi.
        :rtype: bool
        """
        return self._wpa_configured

    @wpa_configured.setter
    def wpa_configured(self, wpa_configured):
        """Sets the wpa_configured of this Wifi.


        :param wpa_configured: The wpa_configured of this Wifi.
        :type wpa_configured: bool
        """
        if wpa_configured is None:
            raise ValueError("Invalid value for `wpa_configured`, must not be `None`")

        self._wpa_configured = wpa_configured

    @property
    def wpa_id(self):
        """Gets the wpa_id of this Wifi.


        :return: The wpa_id of this Wifi.
        :rtype: int
        """
        return self._wpa_id

    @wpa_id.setter
    def wpa_id(self, wpa_id):
        """Sets the wpa_id of this Wifi.


        :param wpa_id: The wpa_id of this Wifi.
        :type wpa_id: int
        """
        if wpa_id is None:
            raise ValueError("Invalid value for `wpa_id`, must not be `None`")

        self._wpa_id = wpa_id

    @property
    def wpa_state(self):
        """Gets the wpa_state of this Wifi.


        :return: The wpa_state of this Wifi.
        :rtype: int
        """
        return self._wpa_state

    @wpa_state.setter
    def wpa_state(self, wpa_state):
        """Sets the wpa_state of this Wifi.


        :param wpa_state: The wpa_state of this Wifi.
        :type wpa_state: int
        """
        if wpa_state is None:
            raise ValueError("Invalid value for `wpa_state`, must not be `None`")

        self._wpa_state = wpa_state
