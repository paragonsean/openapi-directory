# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, band_operation_mode: str=None, band_steering_enabled: bool=None, min_bitrate: int=None, name: str=None):
        """CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14 - a model defined in OpenAPI

        :param band_operation_mode: The band_operation_mode of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :param band_steering_enabled: The band_steering_enabled of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :param min_bitrate: The min_bitrate of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :param name: The name of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        """
        self.openapi_types = {
            'band_operation_mode': str,
            'band_steering_enabled': bool,
            'min_bitrate': int,
            'name': str
        }

        self.attribute_map = {
            'band_operation_mode': 'bandOperationMode',
            'band_steering_enabled': 'bandSteeringEnabled',
            'min_bitrate': 'minBitrate',
            'name': 'name'
        }

        self._band_operation_mode = band_operation_mode
        self._band_steering_enabled = band_steering_enabled
        self._min_bitrate = min_bitrate
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkWirelessRfProfile_201_response_perSsidSettings_14 of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def band_operation_mode(self):
        """Gets the band_operation_mode of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Choice between 'dual', '2.4ghz' or '5ghz'.

        :return: The band_operation_mode of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :rtype: str
        """
        return self._band_operation_mode

    @band_operation_mode.setter
    def band_operation_mode(self, band_operation_mode):
        """Sets the band_operation_mode of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Choice between 'dual', '2.4ghz' or '5ghz'.

        :param band_operation_mode: The band_operation_mode of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :type band_operation_mode: str
        """
        allowed_values = ["2.4ghz", "5ghz", "dual"]  # noqa: E501
        if band_operation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `band_operation_mode` ({0}), must be one of {1}"
                .format(band_operation_mode, allowed_values)
            )

        self._band_operation_mode = band_operation_mode

    @property
    def band_steering_enabled(self):
        """Gets the band_steering_enabled of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.

        :return: The band_steering_enabled of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :rtype: bool
        """
        return self._band_steering_enabled

    @band_steering_enabled.setter
    def band_steering_enabled(self, band_steering_enabled):
        """Sets the band_steering_enabled of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.

        :param band_steering_enabled: The band_steering_enabled of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :type band_steering_enabled: bool
        """

        self._band_steering_enabled = band_steering_enabled

    @property
    def min_bitrate(self):
        """Gets the min_bitrate of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Sets min bitrate (Mbps) of this SSID. Can be one of '1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54'.

        :return: The min_bitrate of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        """Sets the min_bitrate of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Sets min bitrate (Mbps) of this SSID. Can be one of '1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54'.

        :param min_bitrate: The min_bitrate of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :type min_bitrate: int
        """

        self._min_bitrate = min_bitrate

    @property
    def name(self):
        """Gets the name of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Name of SSID

        :return: The name of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.

        Name of SSID

        :param name: The name of this CreateNetworkWirelessRfProfile201ResponsePerSsidSettings14.
        :type name: str
        """

        self._name = name
