# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, certificate_name: str=None, local_interface: int=None, loopback_number: int=None, name: str=None):
        """CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel - a model defined in OpenAPI

        :param certificate_name: The certificate_name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :param local_interface: The local_interface of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :param loopback_number: The loopback_number of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :param name: The name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        """
        self.openapi_types = {
            'certificate_name': str,
            'local_interface': int,
            'loopback_number': int,
            'name': str
        }

        self.attribute_map = {
            'certificate_name': 'certificateName',
            'local_interface': 'localInterface',
            'loopback_number': 'loopbackNumber',
            'name': 'name'
        }

        self._certificate_name = certificate_name
        self._local_interface = local_interface
        self._loopback_number = loopback_number
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createOrganizationInventoryOnboardingCloudMonitoringPrepare_request_devices_inner_tunnel of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def certificate_name(self):
        """Gets the certificate_name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Name of the configured TLS certificate

        :return: The certificate_name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Name of the configured TLS certificate

        :param certificate_name: The certificate_name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :type certificate_name: str
        """

        self._certificate_name = certificate_name

    @property
    def local_interface(self):
        """Gets the local_interface of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Number of the vlan expected to be used to connect to the cloud

        :return: The local_interface of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :rtype: int
        """
        return self._local_interface

    @local_interface.setter
    def local_interface(self, local_interface):
        """Sets the local_interface of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Number of the vlan expected to be used to connect to the cloud

        :param local_interface: The local_interface of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :type local_interface: int
        """

        self._local_interface = local_interface

    @property
    def loopback_number(self):
        """Gets the loopback_number of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Number of the configured Loopback Interface used for TLS overlay

        :return: The loopback_number of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :rtype: int
        """
        return self._loopback_number

    @loopback_number.setter
    def loopback_number(self, loopback_number):
        """Sets the loopback_number of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Number of the configured Loopback Interface used for TLS overlay

        :param loopback_number: The loopback_number of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :type loopback_number: int
        """

        self._loopback_number = loopback_number

    @property
    def name(self):
        """Gets the name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Name of the configured TLS tunnel

        :return: The name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.

        Name of the configured TLS tunnel

        :param name: The name of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequestDevicesInnerTunnel.
        :type name: str
        """

        self._name = name
