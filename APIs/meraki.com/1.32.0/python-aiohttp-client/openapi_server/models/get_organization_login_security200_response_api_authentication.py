# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organization_login_security200_response_api_authentication_ip_restrictions_for_keys import GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys
from openapi_server import util


class GetOrganizationLoginSecurity200ResponseApiAuthentication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ip_restrictions_for_keys: GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys=None):
        """GetOrganizationLoginSecurity200ResponseApiAuthentication - a model defined in OpenAPI

        :param ip_restrictions_for_keys: The ip_restrictions_for_keys of this GetOrganizationLoginSecurity200ResponseApiAuthentication.
        """
        self.openapi_types = {
            'ip_restrictions_for_keys': GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys
        }

        self.attribute_map = {
            'ip_restrictions_for_keys': 'ipRestrictionsForKeys'
        }

        self._ip_restrictions_for_keys = ip_restrictions_for_keys

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationLoginSecurity200ResponseApiAuthentication':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationLoginSecurity_200_response_apiAuthentication of this GetOrganizationLoginSecurity200ResponseApiAuthentication.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_restrictions_for_keys(self):
        """Gets the ip_restrictions_for_keys of this GetOrganizationLoginSecurity200ResponseApiAuthentication.


        :return: The ip_restrictions_for_keys of this GetOrganizationLoginSecurity200ResponseApiAuthentication.
        :rtype: GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys
        """
        return self._ip_restrictions_for_keys

    @ip_restrictions_for_keys.setter
    def ip_restrictions_for_keys(self, ip_restrictions_for_keys):
        """Sets the ip_restrictions_for_keys of this GetOrganizationLoginSecurity200ResponseApiAuthentication.


        :param ip_restrictions_for_keys: The ip_restrictions_for_keys of this GetOrganizationLoginSecurity200ResponseApiAuthentication.
        :type ip_restrictions_for_keys: GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys
        """

        self._ip_restrictions_for_keys = ip_restrictions_for_keys
