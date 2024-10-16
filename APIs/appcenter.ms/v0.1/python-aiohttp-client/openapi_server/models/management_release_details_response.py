# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ManagementReleaseDetailsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, build_version: str=None, created_at: str=None, deleted_at: str=None, distinct_id: int=None, enabled: bool=None, origin: str=None, sort_version: str=None, version: str=None):
        """ManagementReleaseDetailsResponse - a model defined in OpenAPI

        :param build_version: The build_version of this ManagementReleaseDetailsResponse.
        :param created_at: The created_at of this ManagementReleaseDetailsResponse.
        :param deleted_at: The deleted_at of this ManagementReleaseDetailsResponse.
        :param distinct_id: The distinct_id of this ManagementReleaseDetailsResponse.
        :param enabled: The enabled of this ManagementReleaseDetailsResponse.
        :param origin: The origin of this ManagementReleaseDetailsResponse.
        :param sort_version: The sort_version of this ManagementReleaseDetailsResponse.
        :param version: The version of this ManagementReleaseDetailsResponse.
        """
        self.openapi_types = {
            'build_version': str,
            'created_at': str,
            'deleted_at': str,
            'distinct_id': int,
            'enabled': bool,
            'origin': str,
            'sort_version': str,
            'version': str
        }

        self.attribute_map = {
            'build_version': 'buildVersion',
            'created_at': 'createdAt',
            'deleted_at': 'deletedAt',
            'distinct_id': 'distinctId',
            'enabled': 'enabled',
            'origin': 'origin',
            'sort_version': 'sortVersion',
            'version': 'version'
        }

        self._build_version = build_version
        self._created_at = created_at
        self._deleted_at = deleted_at
        self._distinct_id = distinct_id
        self._enabled = enabled
        self._origin = origin
        self._sort_version = sort_version
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ManagementReleaseDetailsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ManagementReleaseDetailsResponse of this ManagementReleaseDetailsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def build_version(self):
        """Gets the build_version of this ManagementReleaseDetailsResponse.

        The release's buildVersion.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 

        :return: The build_version of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this ManagementReleaseDetailsResponse.

        The release's buildVersion.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml. 

        :param build_version: The build_version of this ManagementReleaseDetailsResponse.
        :type build_version: str
        """

        self._build_version = build_version

    @property
    def created_at(self):
        """Gets the created_at of this ManagementReleaseDetailsResponse.

        UTC time the release was created in ISO 8601 format.

        :return: The created_at of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ManagementReleaseDetailsResponse.

        UTC time the release was created in ISO 8601 format.

        :param created_at: The created_at of this ManagementReleaseDetailsResponse.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ManagementReleaseDetailsResponse.

        UTC time the release was created in ISO 8601 format.

        :return: The deleted_at of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ManagementReleaseDetailsResponse.

        UTC time the release was created in ISO 8601 format.

        :param deleted_at: The deleted_at of this ManagementReleaseDetailsResponse.
        :type deleted_at: str
        """

        self._deleted_at = deleted_at

    @property
    def distinct_id(self):
        """Gets the distinct_id of this ManagementReleaseDetailsResponse.

        ID identifying this unique release.

        :return: The distinct_id of this ManagementReleaseDetailsResponse.
        :rtype: int
        """
        return self._distinct_id

    @distinct_id.setter
    def distinct_id(self, distinct_id):
        """Sets the distinct_id of this ManagementReleaseDetailsResponse.

        ID identifying this unique release.

        :param distinct_id: The distinct_id of this ManagementReleaseDetailsResponse.
        :type distinct_id: int
        """

        self._distinct_id = distinct_id

    @property
    def enabled(self):
        """Gets the enabled of this ManagementReleaseDetailsResponse.

        This value determines the whether a release currently is enabled or disabled.

        :return: The enabled of this ManagementReleaseDetailsResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ManagementReleaseDetailsResponse.

        This value determines the whether a release currently is enabled or disabled.

        :param enabled: The enabled of this ManagementReleaseDetailsResponse.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def origin(self):
        """Gets the origin of this ManagementReleaseDetailsResponse.

        The release's origin

        :return: The origin of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ManagementReleaseDetailsResponse.

        The release's origin

        :param origin: The origin of this ManagementReleaseDetailsResponse.
        :type origin: str
        """
        allowed_values = ["hockeyapp", "appcenter"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def sort_version(self):
        """Gets the sort_version of this ManagementReleaseDetailsResponse.

        The release's sortVersion.

        :return: The sort_version of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._sort_version

    @sort_version.setter
    def sort_version(self, sort_version):
        """Sets the sort_version of this ManagementReleaseDetailsResponse.

        The release's sortVersion.

        :param sort_version: The sort_version of this ManagementReleaseDetailsResponse.
        :type sort_version: str
        """

        self._sort_version = sort_version

    @property
    def version(self):
        """Gets the version of this ManagementReleaseDetailsResponse.

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 

        :return: The version of this ManagementReleaseDetailsResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ManagementReleaseDetailsResponse.

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml. 

        :param version: The version of this ManagementReleaseDetailsResponse.
        :type version: str
        """

        self._version = version
