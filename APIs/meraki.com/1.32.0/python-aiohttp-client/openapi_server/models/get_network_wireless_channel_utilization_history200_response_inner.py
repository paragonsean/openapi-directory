# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkWirelessChannelUtilizationHistory200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_ts: datetime=None, start_ts: datetime=None, utilization80211: float=None, utilization_non80211: float=None, utilization_total: float=None):
        """GetNetworkWirelessChannelUtilizationHistory200ResponseInner - a model defined in OpenAPI

        :param end_ts: The end_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :param start_ts: The start_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :param utilization80211: The utilization80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :param utilization_non80211: The utilization_non80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :param utilization_total: The utilization_total of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        """
        self.openapi_types = {
            'end_ts': datetime,
            'start_ts': datetime,
            'utilization80211': float,
            'utilization_non80211': float,
            'utilization_total': float
        }

        self.attribute_map = {
            'end_ts': 'endTs',
            'start_ts': 'startTs',
            'utilization80211': 'utilization80211',
            'utilization_non80211': 'utilizationNon80211',
            'utilization_total': 'utilizationTotal'
        }

        self._end_ts = end_ts
        self._start_ts = start_ts
        self._utilization80211 = utilization80211
        self._utilization_non80211 = utilization_non80211
        self._utilization_total = utilization_total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkWirelessChannelUtilizationHistory200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkWirelessChannelUtilizationHistory_200_response_inner of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_ts(self):
        """Gets the end_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        The end time of the query range

        :return: The end_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :rtype: datetime
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        The end time of the query range

        :param end_ts: The end_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :type end_ts: datetime
        """

        self._end_ts = end_ts

    @property
    def start_ts(self):
        """Gets the start_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        The start time of the query range

        :return: The start_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :rtype: datetime
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        The start time of the query range

        :param start_ts: The start_ts of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :type start_ts: datetime
        """

        self._start_ts = start_ts

    @property
    def utilization80211(self):
        """Gets the utilization80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Average wifi utilization

        :return: The utilization80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :rtype: float
        """
        return self._utilization80211

    @utilization80211.setter
    def utilization80211(self, utilization80211):
        """Sets the utilization80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Average wifi utilization

        :param utilization80211: The utilization80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :type utilization80211: float
        """

        self._utilization80211 = utilization80211

    @property
    def utilization_non80211(self):
        """Gets the utilization_non80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Average signal interference

        :return: The utilization_non80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :rtype: float
        """
        return self._utilization_non80211

    @utilization_non80211.setter
    def utilization_non80211(self, utilization_non80211):
        """Sets the utilization_non80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Average signal interference

        :param utilization_non80211: The utilization_non80211 of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :type utilization_non80211: float
        """

        self._utilization_non80211 = utilization_non80211

    @property
    def utilization_total(self):
        """Gets the utilization_total of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Total channel utilization

        :return: The utilization_total of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :rtype: float
        """
        return self._utilization_total

    @utilization_total.setter
    def utilization_total(self, utilization_total):
        """Sets the utilization_total of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.

        Total channel utilization

        :param utilization_total: The utilization_total of this GetNetworkWirelessChannelUtilizationHistory200ResponseInner.
        :type utilization_total: float
        """

        self._utilization_total = utilization_total
