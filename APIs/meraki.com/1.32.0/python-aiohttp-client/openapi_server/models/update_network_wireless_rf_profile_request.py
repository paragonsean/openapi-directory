# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_wireless_rf_profile_request_per_ssid_settings import CreateNetworkWirelessRfProfileRequestPerSsidSettings
from openapi_server.models.create_network_wireless_rf_profile_request_transmission import CreateNetworkWirelessRfProfileRequestTransmission
from openapi_server.models.update_network_wireless_rf_profile_request_ap_band_settings import UpdateNetworkWirelessRfProfileRequestApBandSettings
from openapi_server.models.update_network_wireless_rf_profile_request_five_ghz_settings import UpdateNetworkWirelessRfProfileRequestFiveGhzSettings
from openapi_server.models.update_network_wireless_rf_profile_request_two_four_ghz_settings import UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings
from openapi_server import util


class UpdateNetworkWirelessRfProfileRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ap_band_settings: UpdateNetworkWirelessRfProfileRequestApBandSettings=None, band_selection_type: str=None, client_balancing_enabled: bool=None, five_ghz_settings: UpdateNetworkWirelessRfProfileRequestFiveGhzSettings=None, min_bitrate_type: str=None, name: str=None, per_ssid_settings: CreateNetworkWirelessRfProfileRequestPerSsidSettings=None, transmission: CreateNetworkWirelessRfProfileRequestTransmission=None, two_four_ghz_settings: UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings=None):
        """UpdateNetworkWirelessRfProfileRequest - a model defined in OpenAPI

        :param ap_band_settings: The ap_band_settings of this UpdateNetworkWirelessRfProfileRequest.
        :param band_selection_type: The band_selection_type of this UpdateNetworkWirelessRfProfileRequest.
        :param client_balancing_enabled: The client_balancing_enabled of this UpdateNetworkWirelessRfProfileRequest.
        :param five_ghz_settings: The five_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        :param min_bitrate_type: The min_bitrate_type of this UpdateNetworkWirelessRfProfileRequest.
        :param name: The name of this UpdateNetworkWirelessRfProfileRequest.
        :param per_ssid_settings: The per_ssid_settings of this UpdateNetworkWirelessRfProfileRequest.
        :param transmission: The transmission of this UpdateNetworkWirelessRfProfileRequest.
        :param two_four_ghz_settings: The two_four_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        """
        self.openapi_types = {
            'ap_band_settings': UpdateNetworkWirelessRfProfileRequestApBandSettings,
            'band_selection_type': str,
            'client_balancing_enabled': bool,
            'five_ghz_settings': UpdateNetworkWirelessRfProfileRequestFiveGhzSettings,
            'min_bitrate_type': str,
            'name': str,
            'per_ssid_settings': CreateNetworkWirelessRfProfileRequestPerSsidSettings,
            'transmission': CreateNetworkWirelessRfProfileRequestTransmission,
            'two_four_ghz_settings': UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings
        }

        self.attribute_map = {
            'ap_band_settings': 'apBandSettings',
            'band_selection_type': 'bandSelectionType',
            'client_balancing_enabled': 'clientBalancingEnabled',
            'five_ghz_settings': 'fiveGhzSettings',
            'min_bitrate_type': 'minBitrateType',
            'name': 'name',
            'per_ssid_settings': 'perSsidSettings',
            'transmission': 'transmission',
            'two_four_ghz_settings': 'twoFourGhzSettings'
        }

        self._ap_band_settings = ap_band_settings
        self._band_selection_type = band_selection_type
        self._client_balancing_enabled = client_balancing_enabled
        self._five_ghz_settings = five_ghz_settings
        self._min_bitrate_type = min_bitrate_type
        self._name = name
        self._per_ssid_settings = per_ssid_settings
        self._transmission = transmission
        self._two_four_ghz_settings = two_four_ghz_settings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessRfProfileRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessRfProfile_request of this UpdateNetworkWirelessRfProfileRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ap_band_settings(self):
        """Gets the ap_band_settings of this UpdateNetworkWirelessRfProfileRequest.


        :return: The ap_band_settings of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: UpdateNetworkWirelessRfProfileRequestApBandSettings
        """
        return self._ap_band_settings

    @ap_band_settings.setter
    def ap_band_settings(self, ap_band_settings):
        """Sets the ap_band_settings of this UpdateNetworkWirelessRfProfileRequest.


        :param ap_band_settings: The ap_band_settings of this UpdateNetworkWirelessRfProfileRequest.
        :type ap_band_settings: UpdateNetworkWirelessRfProfileRequestApBandSettings
        """

        self._ap_band_settings = ap_band_settings

    @property
    def band_selection_type(self):
        """Gets the band_selection_type of this UpdateNetworkWirelessRfProfileRequest.

        Band selection can be set to either 'ssid' or 'ap'.

        :return: The band_selection_type of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: str
        """
        return self._band_selection_type

    @band_selection_type.setter
    def band_selection_type(self, band_selection_type):
        """Sets the band_selection_type of this UpdateNetworkWirelessRfProfileRequest.

        Band selection can be set to either 'ssid' or 'ap'.

        :param band_selection_type: The band_selection_type of this UpdateNetworkWirelessRfProfileRequest.
        :type band_selection_type: str
        """
        allowed_values = ["ap", "ssid"]  # noqa: E501
        if band_selection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `band_selection_type` ({0}), must be one of {1}"
                .format(band_selection_type, allowed_values)
            )

        self._band_selection_type = band_selection_type

    @property
    def client_balancing_enabled(self):
        """Gets the client_balancing_enabled of this UpdateNetworkWirelessRfProfileRequest.

        Steers client to best available access point. Can be either true or false.

        :return: The client_balancing_enabled of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: bool
        """
        return self._client_balancing_enabled

    @client_balancing_enabled.setter
    def client_balancing_enabled(self, client_balancing_enabled):
        """Sets the client_balancing_enabled of this UpdateNetworkWirelessRfProfileRequest.

        Steers client to best available access point. Can be either true or false.

        :param client_balancing_enabled: The client_balancing_enabled of this UpdateNetworkWirelessRfProfileRequest.
        :type client_balancing_enabled: bool
        """

        self._client_balancing_enabled = client_balancing_enabled

    @property
    def five_ghz_settings(self):
        """Gets the five_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.


        :return: The five_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: UpdateNetworkWirelessRfProfileRequestFiveGhzSettings
        """
        return self._five_ghz_settings

    @five_ghz_settings.setter
    def five_ghz_settings(self, five_ghz_settings):
        """Sets the five_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.


        :param five_ghz_settings: The five_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        :type five_ghz_settings: UpdateNetworkWirelessRfProfileRequestFiveGhzSettings
        """

        self._five_ghz_settings = five_ghz_settings

    @property
    def min_bitrate_type(self):
        """Gets the min_bitrate_type of this UpdateNetworkWirelessRfProfileRequest.

        Minimum bitrate can be set to either 'band' or 'ssid'.

        :return: The min_bitrate_type of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: str
        """
        return self._min_bitrate_type

    @min_bitrate_type.setter
    def min_bitrate_type(self, min_bitrate_type):
        """Sets the min_bitrate_type of this UpdateNetworkWirelessRfProfileRequest.

        Minimum bitrate can be set to either 'band' or 'ssid'.

        :param min_bitrate_type: The min_bitrate_type of this UpdateNetworkWirelessRfProfileRequest.
        :type min_bitrate_type: str
        """
        allowed_values = ["band", "ssid"]  # noqa: E501
        if min_bitrate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `min_bitrate_type` ({0}), must be one of {1}"
                .format(min_bitrate_type, allowed_values)
            )

        self._min_bitrate_type = min_bitrate_type

    @property
    def name(self):
        """Gets the name of this UpdateNetworkWirelessRfProfileRequest.

        The name of the new profile. Must be unique.

        :return: The name of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkWirelessRfProfileRequest.

        The name of the new profile. Must be unique.

        :param name: The name of this UpdateNetworkWirelessRfProfileRequest.
        :type name: str
        """

        self._name = name

    @property
    def per_ssid_settings(self):
        """Gets the per_ssid_settings of this UpdateNetworkWirelessRfProfileRequest.


        :return: The per_ssid_settings of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: CreateNetworkWirelessRfProfileRequestPerSsidSettings
        """
        return self._per_ssid_settings

    @per_ssid_settings.setter
    def per_ssid_settings(self, per_ssid_settings):
        """Sets the per_ssid_settings of this UpdateNetworkWirelessRfProfileRequest.


        :param per_ssid_settings: The per_ssid_settings of this UpdateNetworkWirelessRfProfileRequest.
        :type per_ssid_settings: CreateNetworkWirelessRfProfileRequestPerSsidSettings
        """

        self._per_ssid_settings = per_ssid_settings

    @property
    def transmission(self):
        """Gets the transmission of this UpdateNetworkWirelessRfProfileRequest.


        :return: The transmission of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: CreateNetworkWirelessRfProfileRequestTransmission
        """
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        """Sets the transmission of this UpdateNetworkWirelessRfProfileRequest.


        :param transmission: The transmission of this UpdateNetworkWirelessRfProfileRequest.
        :type transmission: CreateNetworkWirelessRfProfileRequestTransmission
        """

        self._transmission = transmission

    @property
    def two_four_ghz_settings(self):
        """Gets the two_four_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.


        :return: The two_four_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        :rtype: UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings
        """
        return self._two_four_ghz_settings

    @two_four_ghz_settings.setter
    def two_four_ghz_settings(self, two_four_ghz_settings):
        """Sets the two_four_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.


        :param two_four_ghz_settings: The two_four_ghz_settings of this UpdateNetworkWirelessRfProfileRequest.
        :type two_four_ghz_settings: UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings
        """

        self._two_four_ghz_settings = two_four_ghz_settings
