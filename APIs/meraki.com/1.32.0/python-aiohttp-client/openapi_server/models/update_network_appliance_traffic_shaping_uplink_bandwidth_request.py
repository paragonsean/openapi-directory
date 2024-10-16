# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_bandwidth_request_bandwidth_limits import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequestBandwidthLimits
from openapi_server import util


class UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bandwidth_limits: UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequestBandwidthLimits=None):
        """UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest - a model defined in OpenAPI

        :param bandwidth_limits: The bandwidth_limits of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.
        """
        self.openapi_types = {
            'bandwidth_limits': UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequestBandwidthLimits
        }

        self.attribute_map = {
            'bandwidth_limits': 'bandwidthLimits'
        }

        self._bandwidth_limits = bandwidth_limits

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceTrafficShapingUplinkBandwidth_request of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bandwidth_limits(self):
        """Gets the bandwidth_limits of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.


        :return: The bandwidth_limits of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.
        :rtype: UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequestBandwidthLimits
        """
        return self._bandwidth_limits

    @bandwidth_limits.setter
    def bandwidth_limits(self, bandwidth_limits):
        """Sets the bandwidth_limits of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.


        :param bandwidth_limits: The bandwidth_limits of this UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.
        :type bandwidth_limits: UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequestBandwidthLimits
        """

        self._bandwidth_limits = bandwidth_limits
