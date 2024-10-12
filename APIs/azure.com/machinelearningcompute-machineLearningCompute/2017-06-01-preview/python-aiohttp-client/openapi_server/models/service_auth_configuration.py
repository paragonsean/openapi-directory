# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ServiceAuthConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, primary_auth_key_hash: str=None, secondary_auth_key_hash: str=None):
        """ServiceAuthConfiguration - a model defined in OpenAPI

        :param primary_auth_key_hash: The primary_auth_key_hash of this ServiceAuthConfiguration.
        :param secondary_auth_key_hash: The secondary_auth_key_hash of this ServiceAuthConfiguration.
        """
        self.openapi_types = {
            'primary_auth_key_hash': str,
            'secondary_auth_key_hash': str
        }

        self.attribute_map = {
            'primary_auth_key_hash': 'primaryAuthKeyHash',
            'secondary_auth_key_hash': 'secondaryAuthKeyHash'
        }

        self._primary_auth_key_hash = primary_auth_key_hash
        self._secondary_auth_key_hash = secondary_auth_key_hash

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServiceAuthConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceAuthConfiguration of this ServiceAuthConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def primary_auth_key_hash(self):
        """Gets the primary_auth_key_hash of this ServiceAuthConfiguration.

        The primary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.

        :return: The primary_auth_key_hash of this ServiceAuthConfiguration.
        :rtype: str
        """
        return self._primary_auth_key_hash

    @primary_auth_key_hash.setter
    def primary_auth_key_hash(self, primary_auth_key_hash):
        """Sets the primary_auth_key_hash of this ServiceAuthConfiguration.

        The primary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.

        :param primary_auth_key_hash: The primary_auth_key_hash of this ServiceAuthConfiguration.
        :type primary_auth_key_hash: str
        """
        if primary_auth_key_hash is None:
            raise ValueError("Invalid value for `primary_auth_key_hash`, must not be `None`")

        self._primary_auth_key_hash = primary_auth_key_hash

    @property
    def secondary_auth_key_hash(self):
        """Gets the secondary_auth_key_hash of this ServiceAuthConfiguration.

        The secondary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.

        :return: The secondary_auth_key_hash of this ServiceAuthConfiguration.
        :rtype: str
        """
        return self._secondary_auth_key_hash

    @secondary_auth_key_hash.setter
    def secondary_auth_key_hash(self, secondary_auth_key_hash):
        """Sets the secondary_auth_key_hash of this ServiceAuthConfiguration.

        The secondary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.

        :param secondary_auth_key_hash: The secondary_auth_key_hash of this ServiceAuthConfiguration.
        :type secondary_auth_key_hash: str
        """
        if secondary_auth_key_hash is None:
            raise ValueError("Invalid value for `secondary_auth_key_hash`, must not be `None`")

        self._secondary_auth_key_hash = secondary_auth_key_hash
