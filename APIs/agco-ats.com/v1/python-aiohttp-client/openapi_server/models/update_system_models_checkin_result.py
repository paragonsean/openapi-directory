# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_system_models_package import UpdateSystemModelsPackage
from openapi_server import util


class UpdateSystemModelsCheckinResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, packages: List[UpdateSystemModelsPackage]=None, remove_packages: List[str]=None):
        """UpdateSystemModelsCheckinResult - a model defined in OpenAPI

        :param packages: The packages of this UpdateSystemModelsCheckinResult.
        :param remove_packages: The remove_packages of this UpdateSystemModelsCheckinResult.
        """
        self.openapi_types = {
            'packages': List[UpdateSystemModelsPackage],
            'remove_packages': List[str]
        }

        self.attribute_map = {
            'packages': 'Packages',
            'remove_packages': 'RemovePackages'
        }

        self._packages = packages
        self._remove_packages = remove_packages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSystemModelsCheckinResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSystem.Models.CheckinResult of this UpdateSystemModelsCheckinResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def packages(self):
        """Gets the packages of this UpdateSystemModelsCheckinResult.

        The packages for the client to run.

        :return: The packages of this UpdateSystemModelsCheckinResult.
        :rtype: List[UpdateSystemModelsPackage]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this UpdateSystemModelsCheckinResult.

        The packages for the client to run.

        :param packages: The packages of this UpdateSystemModelsCheckinResult.
        :type packages: List[UpdateSystemModelsPackage]
        """

        self._packages = packages

    @property
    def remove_packages(self):
        """Gets the remove_packages of this UpdateSystemModelsCheckinResult.

        The package ids for the client to remove.

        :return: The remove_packages of this UpdateSystemModelsCheckinResult.
        :rtype: List[str]
        """
        return self._remove_packages

    @remove_packages.setter
    def remove_packages(self, remove_packages):
        """Sets the remove_packages of this UpdateSystemModelsCheckinResult.

        The package ids for the client to remove.

        :param remove_packages: The remove_packages of this UpdateSystemModelsCheckinResult.
        :type remove_packages: List[str]
        """

        self._remove_packages = remove_packages
