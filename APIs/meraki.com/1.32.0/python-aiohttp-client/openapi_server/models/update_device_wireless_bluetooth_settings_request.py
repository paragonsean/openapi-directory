# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateDeviceWirelessBluetoothSettingsRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, major: int=None, minor: int=None, uuid: str=None):
        """UpdateDeviceWirelessBluetoothSettingsRequest - a model defined in OpenAPI

        :param major: The major of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :param minor: The minor of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :param uuid: The uuid of this UpdateDeviceWirelessBluetoothSettingsRequest.
        """
        self.openapi_types = {
            'major': int,
            'minor': int,
            'uuid': str
        }

        self.attribute_map = {
            'major': 'major',
            'minor': 'minor',
            'uuid': 'uuid'
        }

        self._major = major
        self._minor = minor
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateDeviceWirelessBluetoothSettingsRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateDeviceWirelessBluetoothSettings_request of this UpdateDeviceWirelessBluetoothSettingsRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def major(self):
        """Gets the major of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :return: The major of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :param major: The major of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :type major: int
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :return: The minor of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :param minor: The minor of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :type minor: int
        """

        self._minor = minor

    @property
    def uuid(self):
        """Gets the uuid of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :return: The uuid of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this UpdateDeviceWirelessBluetoothSettingsRequest.

        Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.

        :param uuid: The uuid of this UpdateDeviceWirelessBluetoothSettingsRequest.
        :type uuid: str
        """

        self._uuid = uuid
