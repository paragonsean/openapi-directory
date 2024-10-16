# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AvailableVersionsDiagnostics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total_count: int=None, versions: List[str]=None):
        """AvailableVersionsDiagnostics - a model defined in OpenAPI

        :param total_count: The total_count of this AvailableVersionsDiagnostics.
        :param versions: The versions of this AvailableVersionsDiagnostics.
        """
        self.openapi_types = {
            'total_count': int,
            'versions': List[str]
        }

        self.attribute_map = {
            'total_count': 'total_count',
            'versions': 'versions'
        }

        self._total_count = total_count
        self._versions = versions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AvailableVersionsDiagnostics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AvailableVersions_Diagnostics of this AvailableVersionsDiagnostics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_count(self):
        """Gets the total_count of this AvailableVersionsDiagnostics.

        The full number of versions across all pages.

        :return: The total_count of this AvailableVersionsDiagnostics.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this AvailableVersionsDiagnostics.

        The full number of versions across all pages.

        :param total_count: The total_count of this AvailableVersionsDiagnostics.
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def versions(self):
        """Gets the versions of this AvailableVersionsDiagnostics.

        List of available versions.

        :return: The versions of this AvailableVersionsDiagnostics.
        :rtype: List[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this AvailableVersionsDiagnostics.

        List of available versions.

        :param versions: The versions of this AvailableVersionsDiagnostics.
        :type versions: List[str]
        """

        self._versions = versions
