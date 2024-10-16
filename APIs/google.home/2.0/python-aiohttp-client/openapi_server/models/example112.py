# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Example112(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_class: int=None, device_type: int=None, expected_profiles: int=None, mac_address: str=None, name: str=None, rssi: int=None):
        """Example112 - a model defined in OpenAPI

        :param device_class: The device_class of this Example112.
        :param device_type: The device_type of this Example112.
        :param expected_profiles: The expected_profiles of this Example112.
        :param mac_address: The mac_address of this Example112.
        :param name: The name of this Example112.
        :param rssi: The rssi of this Example112.
        """
        self.openapi_types = {
            'device_class': int,
            'device_type': int,
            'expected_profiles': int,
            'mac_address': str,
            'name': str,
            'rssi': int
        }

        self.attribute_map = {
            'device_class': 'device_class',
            'device_type': 'device_type',
            'expected_profiles': 'expected_profiles',
            'mac_address': 'mac_address',
            'name': 'name',
            'rssi': 'rssi'
        }

        self._device_class = device_class
        self._device_type = device_type
        self._expected_profiles = expected_profiles
        self._mac_address = mac_address
        self._name = name
        self._rssi = rssi

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Example112':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Example112 of this Example112.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_class(self):
        """Gets the device_class of this Example112.


        :return: The device_class of this Example112.
        :rtype: int
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """Sets the device_class of this Example112.


        :param device_class: The device_class of this Example112.
        :type device_class: int
        """
        if device_class is None:
            raise ValueError("Invalid value for `device_class`, must not be `None`")

        self._device_class = device_class

    @property
    def device_type(self):
        """Gets the device_type of this Example112.


        :return: The device_type of this Example112.
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Example112.


        :param device_type: The device_type of this Example112.
        :type device_type: int
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")

        self._device_type = device_type

    @property
    def expected_profiles(self):
        """Gets the expected_profiles of this Example112.


        :return: The expected_profiles of this Example112.
        :rtype: int
        """
        return self._expected_profiles

    @expected_profiles.setter
    def expected_profiles(self, expected_profiles):
        """Sets the expected_profiles of this Example112.


        :param expected_profiles: The expected_profiles of this Example112.
        :type expected_profiles: int
        """
        if expected_profiles is None:
            raise ValueError("Invalid value for `expected_profiles`, must not be `None`")

        self._expected_profiles = expected_profiles

    @property
    def mac_address(self):
        """Gets the mac_address of this Example112.


        :return: The mac_address of this Example112.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Example112.


        :param mac_address: The mac_address of this Example112.
        :type mac_address: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this Example112.


        :return: The name of this Example112.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Example112.


        :param name: The name of this Example112.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rssi(self):
        """Gets the rssi of this Example112.


        :return: The rssi of this Example112.
        :rtype: int
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """Sets the rssi of this Example112.


        :param rssi: The rssi of this Example112.
        :type rssi: int
        """
        if rssi is None:
            raise ValueError("Invalid value for `rssi`, must not be `None`")

        self._rssi = rssi
