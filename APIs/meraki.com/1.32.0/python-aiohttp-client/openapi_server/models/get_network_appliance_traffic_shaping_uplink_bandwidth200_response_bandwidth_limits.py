# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response_bandwidth_limits_cellular import GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsCellular
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response_bandwidth_limits_wan1 import GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response_bandwidth_limits_wan2 import GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan2
from openapi_server import util


class GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cellular: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsCellular=None, wan1: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1=None, wan2: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan2=None):
        """GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits - a model defined in OpenAPI

        :param cellular: The cellular of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :param wan1: The wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :param wan2: The wan2 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        """
        self.openapi_types = {
            'cellular': GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsCellular,
            'wan1': GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1,
            'wan2': GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan2
        }

        self.attribute_map = {
            'cellular': 'cellular',
            'wan1': 'wan1',
            'wan2': 'wan2'
        }

        self._cellular = cellular
        self._wan1 = wan1
        self._wan2 = wan2

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cellular(self):
        """Gets the cellular of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :return: The cellular of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :rtype: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsCellular
        """
        return self._cellular

    @cellular.setter
    def cellular(self, cellular):
        """Sets the cellular of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :param cellular: The cellular of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :type cellular: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsCellular
        """

        self._cellular = cellular

    @property
    def wan1(self):
        """Gets the wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :return: The wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :rtype: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1
        """
        return self._wan1

    @wan1.setter
    def wan1(self, wan1):
        """Sets the wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :param wan1: The wan1 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :type wan1: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan1
        """

        self._wan1 = wan1

    @property
    def wan2(self):
        """Gets the wan2 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :return: The wan2 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :rtype: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan2
        """
        return self._wan2

    @wan2.setter
    def wan2(self, wan2):
        """Sets the wan2 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.


        :param wan2: The wan2 of this GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimits.
        :type wan2: GetNetworkApplianceTrafficShapingUplinkBandwidth200ResponseBandwidthLimitsWan2
        """

        self._wan2 = wan2
