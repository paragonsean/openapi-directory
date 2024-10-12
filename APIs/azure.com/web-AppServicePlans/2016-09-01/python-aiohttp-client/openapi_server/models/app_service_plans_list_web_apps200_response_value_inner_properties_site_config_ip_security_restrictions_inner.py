# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ip_address: str=None, subnet_mask: str=None):
        """AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner - a model defined in OpenAPI

        :param ip_address: The ip_address of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        :param subnet_mask: The subnet_mask of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        """
        self.openapi_types = {
            'ip_address': str,
            'subnet_mask': str
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'subnet_mask': 'subnetMask'
        }

        self._ip_address = ip_address
        self._subnet_mask = subnet_mask

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_ipSecurityRestrictions_inner of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_address(self):
        """Gets the ip_address of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.

        IP address the security restriction is valid for.

        :return: The ip_address of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.

        IP address the security restriction is valid for.

        :param ip_address: The ip_address of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        :type ip_address: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")

        self._ip_address = ip_address

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.

        Subnet mask for the range of IP addresses the restriction is valid for.

        :return: The subnet_mask of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.

        Subnet mask for the range of IP addresses the restriction is valid for.

        :param subnet_mask: The subnet_mask of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.
        :type subnet_mask: str
        """

        self._subnet_mask = subnet_mask
