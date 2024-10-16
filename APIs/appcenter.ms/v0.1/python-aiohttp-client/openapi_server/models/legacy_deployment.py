# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.legacy_code_push_release_response_package import LegacyCodePushReleaseResponsePackage
from openapi_server import util


class LegacyDeployment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_time: int=None, id: str=None, key: str=None, name: str=None, package: LegacyCodePushReleaseResponsePackage=None):
        """LegacyDeployment - a model defined in OpenAPI

        :param created_time: The created_time of this LegacyDeployment.
        :param id: The id of this LegacyDeployment.
        :param key: The key of this LegacyDeployment.
        :param name: The name of this LegacyDeployment.
        :param package: The package of this LegacyDeployment.
        """
        self.openapi_types = {
            'created_time': int,
            'id': str,
            'key': str,
            'name': str,
            'package': LegacyCodePushReleaseResponsePackage
        }

        self.attribute_map = {
            'created_time': 'createdTime',
            'id': 'id',
            'key': 'key',
            'name': 'name',
            'package': 'package'
        }

        self._created_time = created_time
        self._id = id
        self._key = key
        self._name = name
        self._package = package

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegacyDeployment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LegacyDeployment of this LegacyDeployment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_time(self):
        """Gets the created_time of this LegacyDeployment.

        Time at which the deployment was created as a Unix timestamp.

        :return: The created_time of this LegacyDeployment.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this LegacyDeployment.

        Time at which the deployment was created as a Unix timestamp.

        :param created_time: The created_time of this LegacyDeployment.
        :type created_time: int
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this LegacyDeployment.

        The ID of the deployment (internal use only).

        :return: The id of this LegacyDeployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LegacyDeployment.

        The ID of the deployment (internal use only).

        :param id: The id of this LegacyDeployment.
        :type id: str
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this LegacyDeployment.

        Deployment key (aka Deployment Id)

        :return: The key of this LegacyDeployment.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LegacyDeployment.

        Deployment key (aka Deployment Id)

        :param key: The key of this LegacyDeployment.
        :type key: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this LegacyDeployment.

        Updated deployment name

        :return: The name of this LegacyDeployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LegacyDeployment.

        Updated deployment name

        :param name: The name of this LegacyDeployment.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def package(self):
        """Gets the package of this LegacyDeployment.


        :return: The package of this LegacyDeployment.
        :rtype: LegacyCodePushReleaseResponsePackage
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this LegacyDeployment.


        :param package: The package of this LegacyDeployment.
        :type package: LegacyCodePushReleaseResponsePackage
        """

        self._package = package
