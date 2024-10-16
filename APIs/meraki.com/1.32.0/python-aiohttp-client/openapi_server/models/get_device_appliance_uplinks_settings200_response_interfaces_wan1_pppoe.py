# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_device_appliance_uplinks_settings200_response_interfaces_wan1_pppoe_authentication import GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication
from openapi_server import util


class GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authentication: GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication=None, enabled: bool=None):
        """GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe - a model defined in OpenAPI

        :param authentication: The authentication of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        :param enabled: The enabled of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        """
        self.openapi_types = {
            'authentication': GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication,
            'enabled': bool
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'enabled': 'enabled'
        }

        self._authentication = authentication
        self._enabled = enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getDeviceApplianceUplinksSettings_200_response_interfaces_wan1_pppoe of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authentication(self):
        """Gets the authentication of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.


        :return: The authentication of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        :rtype: GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.


        :param authentication: The authentication of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        :type authentication: GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication
        """

        self._authentication = authentication

    @property
    def enabled(self):
        """Gets the enabled of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.

        Whether PPPoE is enabled.

        :return: The enabled of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.

        Whether PPPoE is enabled.

        :param enabled: The enabled of this GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1Pppoe.
        :type enabled: bool
        """

        self._enabled = enabled
