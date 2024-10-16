# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response_vpn_traffic_uplink_preferences_inner_performance_class import GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response_vpn_traffic_uplink_preferences_inner_traffic_filters_inner import GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner
from openapi_server import util


class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fail_over_criterion: str=None, performance_class: GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass=None, preferred_uplink: str=None, traffic_filters: List[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]=None):
        """GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner - a model defined in OpenAPI

        :param fail_over_criterion: The fail_over_criterion of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :param performance_class: The performance_class of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :param preferred_uplink: The preferred_uplink of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :param traffic_filters: The traffic_filters of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        """
        self.openapi_types = {
            'fail_over_criterion': str,
            'performance_class': GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass,
            'preferred_uplink': str,
            'traffic_filters': List[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]
        }

        self.attribute_map = {
            'fail_over_criterion': 'failOverCriterion',
            'performance_class': 'performanceClass',
            'preferred_uplink': 'preferredUplink',
            'traffic_filters': 'trafficFilters'
        }

        self._fail_over_criterion = fail_over_criterion
        self._performance_class = performance_class
        self._preferred_uplink = preferred_uplink
        self._traffic_filters = traffic_filters

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkApplianceTrafficShapingUplinkSelection_200_response_vpnTrafficUplinkPreferences_inner of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fail_over_criterion(self):
        """Gets the fail_over_criterion of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Fail over criterion for uplink preference rule. Must be one of: 'poorPerformance' or 'uplinkDown'

        :return: The fail_over_criterion of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :rtype: str
        """
        return self._fail_over_criterion

    @fail_over_criterion.setter
    def fail_over_criterion(self, fail_over_criterion):
        """Sets the fail_over_criterion of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Fail over criterion for uplink preference rule. Must be one of: 'poorPerformance' or 'uplinkDown'

        :param fail_over_criterion: The fail_over_criterion of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :type fail_over_criterion: str
        """
        allowed_values = ["poorPerformance", "uplinkDown"]  # noqa: E501
        if fail_over_criterion not in allowed_values:
            raise ValueError(
                "Invalid value for `fail_over_criterion` ({0}), must be one of {1}"
                .format(fail_over_criterion, allowed_values)
            )

        self._fail_over_criterion = fail_over_criterion

    @property
    def performance_class(self):
        """Gets the performance_class of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.


        :return: The performance_class of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :rtype: GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass
        """
        return self._performance_class

    @performance_class.setter
    def performance_class(self, performance_class):
        """Sets the performance_class of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.


        :param performance_class: The performance_class of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :type performance_class: GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass
        """

        self._performance_class = performance_class

    @property
    def preferred_uplink(self):
        """Gets the preferred_uplink of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Preferred uplink for uplink preference rule. Must be one of: 'wan1', 'wan2', 'bestForVoIP', 'loadBalancing' or 'defaultUplink'

        :return: The preferred_uplink of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :rtype: str
        """
        return self._preferred_uplink

    @preferred_uplink.setter
    def preferred_uplink(self, preferred_uplink):
        """Sets the preferred_uplink of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Preferred uplink for uplink preference rule. Must be one of: 'wan1', 'wan2', 'bestForVoIP', 'loadBalancing' or 'defaultUplink'

        :param preferred_uplink: The preferred_uplink of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :type preferred_uplink: str
        """
        allowed_values = ["bestForVoIP", "defaultUplink", "loadBalancing", "wan1", "wan2"]  # noqa: E501
        if preferred_uplink not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_uplink` ({0}), must be one of {1}"
                .format(preferred_uplink, allowed_values)
            )

        self._preferred_uplink = preferred_uplink

    @property
    def traffic_filters(self):
        """Gets the traffic_filters of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Traffic filters

        :return: The traffic_filters of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :rtype: List[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]
        """
        return self._traffic_filters

    @traffic_filters.setter
    def traffic_filters(self, traffic_filters):
        """Sets the traffic_filters of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.

        Traffic filters

        :param traffic_filters: The traffic_filters of this GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.
        :type traffic_filters: List[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]
        """
        if traffic_filters is None:
            raise ValueError("Invalid value for `traffic_filters`, must not be `None`")

        self._traffic_filters = traffic_filters
