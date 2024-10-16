# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, limit_down: int=None, limit_up: int=None):
        """GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1 - a model defined in OpenAPI

        :param limit_down: The limit_down of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        :param limit_up: The limit_up of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        """
        self.openapi_types = {
            'limit_down': int,
            'limit_up': int
        }

        self.attribute_map = {
            'limit_down': 'limitDown',
            'limit_up': 'limitUp'
        }

        self._limit_down = limit_down
        self._limit_up = limit_up

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def limit_down(self):
        """Gets the limit_down of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.

        configured DOWN limit for the uplink (in Kbps).  Null indicated unlimited

        :return: The limit_down of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        :rtype: int
        """
        return self._limit_down

    @limit_down.setter
    def limit_down(self, limit_down):
        """Sets the limit_down of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.

        configured DOWN limit for the uplink (in Kbps).  Null indicated unlimited

        :param limit_down: The limit_down of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        :type limit_down: int
        """

        self._limit_down = limit_down

    @property
    def limit_up(self):
        """Gets the limit_up of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.

        configured UP limit for the uplink (in Kbps).  Null indicated unlimited

        :return: The limit_up of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        :rtype: int
        """
        return self._limit_up

    @limit_up.setter
    def limit_up(self, limit_up):
        """Sets the limit_up of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.

        configured UP limit for the uplink (in Kbps).  Null indicated unlimited

        :param limit_up: The limit_up of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1.
        :type limit_up: int
        """

        self._limit_up = limit_up
