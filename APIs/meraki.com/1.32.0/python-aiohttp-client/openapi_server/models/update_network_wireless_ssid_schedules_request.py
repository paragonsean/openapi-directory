# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_wireless_ssid_schedules_request_ranges_in_seconds_inner import UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner
from openapi_server.models.update_network_wireless_ssid_schedules_request_ranges_inner import UpdateNetworkWirelessSsidSchedulesRequestRangesInner
from openapi_server import util


class UpdateNetworkWirelessSsidSchedulesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, ranges: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInner]=None, ranges_in_seconds: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner]=None):
        """UpdateNetworkWirelessSsidSchedulesRequest - a model defined in OpenAPI

        :param enabled: The enabled of this UpdateNetworkWirelessSsidSchedulesRequest.
        :param ranges: The ranges of this UpdateNetworkWirelessSsidSchedulesRequest.
        :param ranges_in_seconds: The ranges_in_seconds of this UpdateNetworkWirelessSsidSchedulesRequest.
        """
        self.openapi_types = {
            'enabled': bool,
            'ranges': List[UpdateNetworkWirelessSsidSchedulesRequestRangesInner],
            'ranges_in_seconds': List[UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner]
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'ranges': 'ranges',
            'ranges_in_seconds': 'rangesInSeconds'
        }

        self._enabled = enabled
        self._ranges = ranges
        self._ranges_in_seconds = ranges_in_seconds

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidSchedulesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsidSchedules_request of this UpdateNetworkWirelessSsidSchedulesRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this UpdateNetworkWirelessSsidSchedulesRequest.

        If true, the SSID outage schedule is enabled.

        :return: The enabled of this UpdateNetworkWirelessSsidSchedulesRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateNetworkWirelessSsidSchedulesRequest.

        If true, the SSID outage schedule is enabled.

        :param enabled: The enabled of this UpdateNetworkWirelessSsidSchedulesRequest.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def ranges(self):
        """Gets the ranges of this UpdateNetworkWirelessSsidSchedulesRequest.

        List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.

        :return: The ranges of this UpdateNetworkWirelessSsidSchedulesRequest.
        :rtype: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInner]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this UpdateNetworkWirelessSsidSchedulesRequest.

        List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.

        :param ranges: The ranges of this UpdateNetworkWirelessSsidSchedulesRequest.
        :type ranges: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInner]
        """

        self._ranges = ranges

    @property
    def ranges_in_seconds(self):
        """Gets the ranges_in_seconds of this UpdateNetworkWirelessSsidSchedulesRequest.

        List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.

        :return: The ranges_in_seconds of this UpdateNetworkWirelessSsidSchedulesRequest.
        :rtype: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner]
        """
        return self._ranges_in_seconds

    @ranges_in_seconds.setter
    def ranges_in_seconds(self, ranges_in_seconds):
        """Sets the ranges_in_seconds of this UpdateNetworkWirelessSsidSchedulesRequest.

        List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.

        :param ranges_in_seconds: The ranges_in_seconds of this UpdateNetworkWirelessSsidSchedulesRequest.
        :type ranges_in_seconds: List[UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner]
        """

        self._ranges_in_seconds = ranges_in_seconds
