# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties_routes_inner import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner
import re
from openapi_server import util


class AppServicePlansListVnets200ResponseInnerProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cert_blob: str=None, cert_thumbprint: str=None, dns_servers: str=None, resync_required: bool=None, routes: List[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]=None, vnet_resource_id: str=None):
        """AppServicePlansListVnets200ResponseInnerProperties - a model defined in OpenAPI

        :param cert_blob: The cert_blob of this AppServicePlansListVnets200ResponseInnerProperties.
        :param cert_thumbprint: The cert_thumbprint of this AppServicePlansListVnets200ResponseInnerProperties.
        :param dns_servers: The dns_servers of this AppServicePlansListVnets200ResponseInnerProperties.
        :param resync_required: The resync_required of this AppServicePlansListVnets200ResponseInnerProperties.
        :param routes: The routes of this AppServicePlansListVnets200ResponseInnerProperties.
        :param vnet_resource_id: The vnet_resource_id of this AppServicePlansListVnets200ResponseInnerProperties.
        """
        self.openapi_types = {
            'cert_blob': str,
            'cert_thumbprint': str,
            'dns_servers': str,
            'resync_required': bool,
            'routes': List[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner],
            'vnet_resource_id': str
        }

        self.attribute_map = {
            'cert_blob': 'certBlob',
            'cert_thumbprint': 'certThumbprint',
            'dns_servers': 'dnsServers',
            'resync_required': 'resyncRequired',
            'routes': 'routes',
            'vnet_resource_id': 'vnetResourceId'
        }

        self._cert_blob = cert_blob
        self._cert_thumbprint = cert_thumbprint
        self._dns_servers = dns_servers
        self._resync_required = resync_required
        self._routes = routes
        self._vnet_resource_id = vnet_resource_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListVnets200ResponseInnerProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListVnets_200_response_inner_properties of this AppServicePlansListVnets200ResponseInnerProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cert_blob(self):
        """Gets the cert_blob of this AppServicePlansListVnets200ResponseInnerProperties.

        A certificate file (.cer) blob containing the public key of the private key used to authenticate a  Point-To-Site VPN connection.

        :return: The cert_blob of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: str
        """
        return self._cert_blob

    @cert_blob.setter
    def cert_blob(self, cert_blob):
        """Sets the cert_blob of this AppServicePlansListVnets200ResponseInnerProperties.

        A certificate file (.cer) blob containing the public key of the private key used to authenticate a  Point-To-Site VPN connection.

        :param cert_blob: The cert_blob of this AppServicePlansListVnets200ResponseInnerProperties.
        :type cert_blob: str
        """
        if cert_blob is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', cert_blob):
            raise ValueError("Invalid value for `cert_blob`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._cert_blob = cert_blob

    @property
    def cert_thumbprint(self):
        """Gets the cert_thumbprint of this AppServicePlansListVnets200ResponseInnerProperties.

        The client certificate thumbprint.

        :return: The cert_thumbprint of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: str
        """
        return self._cert_thumbprint

    @cert_thumbprint.setter
    def cert_thumbprint(self, cert_thumbprint):
        """Sets the cert_thumbprint of this AppServicePlansListVnets200ResponseInnerProperties.

        The client certificate thumbprint.

        :param cert_thumbprint: The cert_thumbprint of this AppServicePlansListVnets200ResponseInnerProperties.
        :type cert_thumbprint: str
        """

        self._cert_thumbprint = cert_thumbprint

    @property
    def dns_servers(self):
        """Gets the dns_servers of this AppServicePlansListVnets200ResponseInnerProperties.

        DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.

        :return: The dns_servers of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: str
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this AppServicePlansListVnets200ResponseInnerProperties.

        DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.

        :param dns_servers: The dns_servers of this AppServicePlansListVnets200ResponseInnerProperties.
        :type dns_servers: str
        """

        self._dns_servers = dns_servers

    @property
    def resync_required(self):
        """Gets the resync_required of this AppServicePlansListVnets200ResponseInnerProperties.

        <code>true</code> if a resync is required; otherwise, <code>false</code>.

        :return: The resync_required of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: bool
        """
        return self._resync_required

    @resync_required.setter
    def resync_required(self, resync_required):
        """Sets the resync_required of this AppServicePlansListVnets200ResponseInnerProperties.

        <code>true</code> if a resync is required; otherwise, <code>false</code>.

        :param resync_required: The resync_required of this AppServicePlansListVnets200ResponseInnerProperties.
        :type resync_required: bool
        """

        self._resync_required = resync_required

    @property
    def routes(self):
        """Gets the routes of this AppServicePlansListVnets200ResponseInnerProperties.

        The routes that this Virtual Network connection uses.

        :return: The routes of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: List[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this AppServicePlansListVnets200ResponseInnerProperties.

        The routes that this Virtual Network connection uses.

        :param routes: The routes of this AppServicePlansListVnets200ResponseInnerProperties.
        :type routes: List[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]
        """

        self._routes = routes

    @property
    def vnet_resource_id(self):
        """Gets the vnet_resource_id of this AppServicePlansListVnets200ResponseInnerProperties.

        The Virtual Network's resource ID.

        :return: The vnet_resource_id of this AppServicePlansListVnets200ResponseInnerProperties.
        :rtype: str
        """
        return self._vnet_resource_id

    @vnet_resource_id.setter
    def vnet_resource_id(self, vnet_resource_id):
        """Sets the vnet_resource_id of this AppServicePlansListVnets200ResponseInnerProperties.

        The Virtual Network's resource ID.

        :param vnet_resource_id: The vnet_resource_id of this AppServicePlansListVnets200ResponseInnerProperties.
        :type vnet_resource_id: str
        """

        self._vnet_resource_id = vnet_resource_id
