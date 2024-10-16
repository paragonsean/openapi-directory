# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, builtin_performance_class_name: str=None, custom_performance_class_id: str=None, type: str=None):
        """UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass - a model defined in OpenAPI

        :param builtin_performance_class_name: The builtin_performance_class_name of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :param custom_performance_class_id: The custom_performance_class_id of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :param type: The type of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        """
        self.openapi_types = {
            'builtin_performance_class_name': str,
            'custom_performance_class_id': str,
            'type': str
        }

        self.attribute_map = {
            'builtin_performance_class_name': 'builtinPerformanceClassName',
            'custom_performance_class_id': 'customPerformanceClassId',
            'type': 'type'
        }

        self._builtin_performance_class_name = builtin_performance_class_name
        self._custom_performance_class_id = custom_performance_class_id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_performanceClass of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def builtin_performance_class_name(self):
        """Gets the builtin_performance_class_name of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        Name of builtin performance class, must be present when performanceClass type is 'builtin', and value must be one of: 'VoIP'

        :return: The builtin_performance_class_name of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :rtype: str
        """
        return self._builtin_performance_class_name

    @builtin_performance_class_name.setter
    def builtin_performance_class_name(self, builtin_performance_class_name):
        """Sets the builtin_performance_class_name of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        Name of builtin performance class, must be present when performanceClass type is 'builtin', and value must be one of: 'VoIP'

        :param builtin_performance_class_name: The builtin_performance_class_name of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :type builtin_performance_class_name: str
        """
        allowed_values = ["VoIP"]  # noqa: E501
        if builtin_performance_class_name not in allowed_values:
            raise ValueError(
                "Invalid value for `builtin_performance_class_name` ({0}), must be one of {1}"
                .format(builtin_performance_class_name, allowed_values)
            )

        self._builtin_performance_class_name = builtin_performance_class_name

    @property
    def custom_performance_class_id(self):
        """Gets the custom_performance_class_id of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        ID of created custom performance class, must be present when performanceClass type is 'custom'

        :return: The custom_performance_class_id of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :rtype: str
        """
        return self._custom_performance_class_id

    @custom_performance_class_id.setter
    def custom_performance_class_id(self, custom_performance_class_id):
        """Sets the custom_performance_class_id of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        ID of created custom performance class, must be present when performanceClass type is 'custom'

        :param custom_performance_class_id: The custom_performance_class_id of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :type custom_performance_class_id: str
        """

        self._custom_performance_class_id = custom_performance_class_id

    @property
    def type(self):
        """Gets the type of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        Type of this performance class. Must be one of: 'builtin' or 'custom'

        :return: The type of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.

        Type of this performance class. Must be one of: 'builtin' or 'custom'

        :param type: The type of this UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerPerformanceClass.
        :type type: str
        """
        allowed_values = ["builtin", "custom"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
