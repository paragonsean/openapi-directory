# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_id: str=None, network_id: str=None, udi: str=None):
        """CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner - a model defined in OpenAPI

        :param device_id: The device_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :param network_id: The network_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :param udi: The udi of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        """
        self.openapi_types = {
            'device_id': str,
            'network_id': str,
            'udi': str
        }

        self.attribute_map = {
            'device_id': 'deviceId',
            'network_id': 'networkId',
            'udi': 'udi'
        }

        self._device_id = device_id
        self._network_id = network_id
        self._udi = udi

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createOrganizationInventoryOnboardingCloudMonitoringImport_request_devices_inner of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self):
        """Gets the device_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Import ID from the Import operation

        :return: The device_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Import ID from the Import operation

        :param device_id: The device_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :type device_id: str
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        self._device_id = device_id

    @property
    def network_id(self):
        """Gets the network_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Network Id

        :return: The network_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Network Id

        :param network_id: The network_id of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :type network_id: str
        """
        if network_id is None:
            raise ValueError("Invalid value for `network_id`, must not be `None`")

        self._network_id = network_id

    @property
    def udi(self):
        """Gets the udi of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Device UDI certificate

        :return: The udi of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :rtype: str
        """
        return self._udi

    @udi.setter
    def udi(self, udi):
        """Sets the udi of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.

        Device UDI certificate

        :param udi: The udi of this CreateOrganizationInventoryOnboardingCloudMonitoringImportRequestDevicesInner.
        :type udi: str
        """
        if udi is None:
            raise ValueError("Invalid value for `udi`, must not be `None`")

        self._udi = udi
