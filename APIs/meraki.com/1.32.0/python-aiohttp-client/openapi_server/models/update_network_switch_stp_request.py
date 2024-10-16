# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_switch_stp_request_stp_bridge_priority_inner import UpdateNetworkSwitchStpRequestStpBridgePriorityInner
from openapi_server import util


class UpdateNetworkSwitchStpRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rstp_enabled: bool=None, stp_bridge_priority: List[UpdateNetworkSwitchStpRequestStpBridgePriorityInner]=None):
        """UpdateNetworkSwitchStpRequest - a model defined in OpenAPI

        :param rstp_enabled: The rstp_enabled of this UpdateNetworkSwitchStpRequest.
        :param stp_bridge_priority: The stp_bridge_priority of this UpdateNetworkSwitchStpRequest.
        """
        self.openapi_types = {
            'rstp_enabled': bool,
            'stp_bridge_priority': List[UpdateNetworkSwitchStpRequestStpBridgePriorityInner]
        }

        self.attribute_map = {
            'rstp_enabled': 'rstpEnabled',
            'stp_bridge_priority': 'stpBridgePriority'
        }

        self._rstp_enabled = rstp_enabled
        self._stp_bridge_priority = stp_bridge_priority

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkSwitchStpRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkSwitchStp_request of this UpdateNetworkSwitchStpRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rstp_enabled(self):
        """Gets the rstp_enabled of this UpdateNetworkSwitchStpRequest.

        The spanning tree protocol status in network

        :return: The rstp_enabled of this UpdateNetworkSwitchStpRequest.
        :rtype: bool
        """
        return self._rstp_enabled

    @rstp_enabled.setter
    def rstp_enabled(self, rstp_enabled):
        """Sets the rstp_enabled of this UpdateNetworkSwitchStpRequest.

        The spanning tree protocol status in network

        :param rstp_enabled: The rstp_enabled of this UpdateNetworkSwitchStpRequest.
        :type rstp_enabled: bool
        """

        self._rstp_enabled = rstp_enabled

    @property
    def stp_bridge_priority(self):
        """Gets the stp_bridge_priority of this UpdateNetworkSwitchStpRequest.

        STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.

        :return: The stp_bridge_priority of this UpdateNetworkSwitchStpRequest.
        :rtype: List[UpdateNetworkSwitchStpRequestStpBridgePriorityInner]
        """
        return self._stp_bridge_priority

    @stp_bridge_priority.setter
    def stp_bridge_priority(self, stp_bridge_priority):
        """Sets the stp_bridge_priority of this UpdateNetworkSwitchStpRequest.

        STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.

        :param stp_bridge_priority: The stp_bridge_priority of this UpdateNetworkSwitchStpRequest.
        :type stp_bridge_priority: List[UpdateNetworkSwitchStpRequestStpBridgePriorityInner]
        """

        self._stp_bridge_priority = stp_bridge_priority
