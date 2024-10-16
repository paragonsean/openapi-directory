# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, firmware: str=None, id: str=None, release_date: datetime=None, release_type: str=None, short_name: str=None):
        """GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner - a model defined in OpenAPI

        :param firmware: The firmware of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :param id: The id of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :param release_date: The release_date of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :param release_type: The release_type of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :param short_name: The short_name of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        """
        self.openapi_types = {
            'firmware': str,
            'id': str,
            'release_date': datetime,
            'release_type': str,
            'short_name': str
        }

        self.attribute_map = {
            'firmware': 'firmware',
            'id': 'id',
            'release_date': 'releaseDate',
            'release_type': 'releaseType',
            'short_name': 'shortName'
        }

        self._firmware = firmware
        self._id = id
        self._release_date = release_date
        self._release_type = release_type
        self._short_name = short_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkFirmwareUpgrades_200_response_products_appliance_availableVersions_inner of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def firmware(self):
        """Gets the firmware of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Name of the firmware version

        :return: The firmware of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Name of the firmware version

        :param firmware: The firmware of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :type firmware: str
        """

        self._firmware = firmware

    @property
    def id(self):
        """Gets the id of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Firmware version identifier

        :return: The id of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Firmware version identifier

        :param id: The id of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :type id: str
        """

        self._id = id

    @property
    def release_date(self):
        """Gets the release_date of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Release date of the firmware version

        :return: The release_date of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Release date of the firmware version

        :param release_date: The release_date of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :type release_date: datetime
        """

        self._release_date = release_date

    @property
    def release_type(self):
        """Gets the release_type of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Release type of the firmware version

        :return: The release_type of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """Sets the release_type of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Release type of the firmware version

        :param release_type: The release_type of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :type release_type: str
        """

        self._release_type = release_type

    @property
    def short_name(self):
        """Gets the short_name of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Firmware version short name

        :return: The short_name of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.

        Firmware version short name

        :param short_name: The short_name of this GetNetworkFirmwareUpgrades200ResponseProductsApplianceAvailableVersionsInner.
        :type short_name: str
        """

        self._short_name = short_name
