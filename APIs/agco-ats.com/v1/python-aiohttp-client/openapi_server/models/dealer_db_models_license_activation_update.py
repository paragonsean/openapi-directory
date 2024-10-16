# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DealerDBModelsLicenseActivationUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, license_version: str=None, system_info: str=None):
        """DealerDBModelsLicenseActivationUpdate - a model defined in OpenAPI

        :param license_version: The license_version of this DealerDBModelsLicenseActivationUpdate.
        :param system_info: The system_info of this DealerDBModelsLicenseActivationUpdate.
        """
        self.openapi_types = {
            'license_version': str,
            'system_info': str
        }

        self.attribute_map = {
            'license_version': 'LicenseVersion',
            'system_info': 'SystemInfo'
        }

        self._license_version = license_version
        self._system_info = system_info

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DealerDBModelsLicenseActivationUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DealerDB.Models.LicenseActivationUpdate of this DealerDBModelsLicenseActivationUpdate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def license_version(self):
        """Gets the license_version of this DealerDBModelsLicenseActivationUpdate.

        The license version to update

        :return: The license_version of this DealerDBModelsLicenseActivationUpdate.
        :rtype: str
        """
        return self._license_version

    @license_version.setter
    def license_version(self, license_version):
        """Sets the license_version of this DealerDBModelsLicenseActivationUpdate.

        The license version to update

        :param license_version: The license_version of this DealerDBModelsLicenseActivationUpdate.
        :type license_version: str
        """
        if license_version is None:
            raise ValueError("Invalid value for `license_version`, must not be `None`")

        self._license_version = license_version

    @property
    def system_info(self):
        """Gets the system_info of this DealerDBModelsLicenseActivationUpdate.

        Information about  the system being activated

        :return: The system_info of this DealerDBModelsLicenseActivationUpdate.
        :rtype: str
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this DealerDBModelsLicenseActivationUpdate.

        Information about  the system being activated

        :param system_info: The system_info of this DealerDBModelsLicenseActivationUpdate.
        :type system_info: str
        """

        self._system_info = system_info
