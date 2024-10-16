# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSmDeviceDeviceProfiles200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_id: str=None, id: str=None, is_encrypted: bool=None, is_managed: bool=None, name: str=None, profile_data: str=None, profile_identifier: str=None, version: str=None):
        """GetNetworkSmDeviceDeviceProfiles200ResponseInner - a model defined in OpenAPI

        :param device_id: The device_id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param id: The id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param is_encrypted: The is_encrypted of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param is_managed: The is_managed of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param name: The name of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param profile_data: The profile_data of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param profile_identifier: The profile_identifier of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :param version: The version of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        """
        self.openapi_types = {
            'device_id': str,
            'id': str,
            'is_encrypted': bool,
            'is_managed': bool,
            'name': str,
            'profile_data': str,
            'profile_identifier': str,
            'version': str
        }

        self.attribute_map = {
            'device_id': 'deviceId',
            'id': 'id',
            'is_encrypted': 'isEncrypted',
            'is_managed': 'isManaged',
            'name': 'name',
            'profile_data': 'profileData',
            'profile_identifier': 'profileIdentifier',
            'version': 'version'
        }

        self._device_id = device_id
        self._id = id
        self._is_encrypted = is_encrypted
        self._is_managed = is_managed
        self._name = name
        self._profile_data = profile_data
        self._profile_identifier = profile_identifier
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSmDeviceDeviceProfiles200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSmDeviceDeviceProfiles_200_response_inner of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self):
        """Gets the device_id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The Meraki managed device Id.

        :return: The device_id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The Meraki managed device Id.

        :param device_id: The device_id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type device_id: str
        """

        self._device_id = device_id

    @property
    def id(self):
        """Gets the id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The numerical Meraki Id of the profile.

        :return: The id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The numerical Meraki Id of the profile.

        :param id: The id of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        A boolean indicating if the profile is encrypted.

        :return: The is_encrypted of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        A boolean indicating if the profile is encrypted.

        :param is_encrypted: The is_encrypted of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type is_encrypted: bool
        """

        self._is_encrypted = is_encrypted

    @property
    def is_managed(self):
        """Gets the is_managed of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        Whether or not the profile is managed by Meraki.

        :return: The is_managed of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        Whether or not the profile is managed by Meraki.

        :param is_managed: The is_managed of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type is_managed: bool
        """

        self._is_managed = is_managed

    @property
    def name(self):
        """Gets the name of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The name of the profile.

        :return: The name of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The name of the profile.

        :param name: The name of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type name: str
        """

        self._name = name

    @property
    def profile_data(self):
        """Gets the profile_data of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        A string containing a JSON object with the profile data.

        :return: The profile_data of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._profile_data

    @profile_data.setter
    def profile_data(self, profile_data):
        """Sets the profile_data of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        A string containing a JSON object with the profile data.

        :param profile_data: The profile_data of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type profile_data: str
        """

        self._profile_data = profile_data

    @property
    def profile_identifier(self):
        """Gets the profile_identifier of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The identifier of the profile.

        :return: The profile_identifier of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._profile_identifier

    @profile_identifier.setter
    def profile_identifier(self, profile_identifier):
        """Sets the profile_identifier of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The identifier of the profile.

        :param profile_identifier: The profile_identifier of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type profile_identifier: str
        """

        self._profile_identifier = profile_identifier

    @property
    def version(self):
        """Gets the version of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The verison of the profile.

        :return: The version of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.

        The verison of the profile.

        :param version: The version of this GetNetworkSmDeviceDeviceProfiles200ResponseInner.
        :type version: str
        """

        self._version = version
