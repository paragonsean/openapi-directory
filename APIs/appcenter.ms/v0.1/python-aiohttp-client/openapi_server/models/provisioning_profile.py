# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProvisioningProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application_identifier: str=None, expired_at: str=None, name: str=None, profile_type: str=None, team_identifier: str=None, udids: List[str]=None):
        """ProvisioningProfile - a model defined in OpenAPI

        :param application_identifier: The application_identifier of this ProvisioningProfile.
        :param expired_at: The expired_at of this ProvisioningProfile.
        :param name: The name of this ProvisioningProfile.
        :param profile_type: The profile_type of this ProvisioningProfile.
        :param team_identifier: The team_identifier of this ProvisioningProfile.
        :param udids: The udids of this ProvisioningProfile.
        """
        self.openapi_types = {
            'application_identifier': str,
            'expired_at': str,
            'name': str,
            'profile_type': str,
            'team_identifier': str,
            'udids': List[str]
        }

        self.attribute_map = {
            'application_identifier': 'application_identifier',
            'expired_at': 'expired_at',
            'name': 'name',
            'profile_type': 'profile_type',
            'team_identifier': 'team_identifier',
            'udids': 'udids'
        }

        self._application_identifier = application_identifier
        self._expired_at = expired_at
        self._name = name
        self._profile_type = profile_type
        self._team_identifier = team_identifier
        self._udids = udids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProvisioningProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProvisioningProfile of this ProvisioningProfile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application_identifier(self):
        """Gets the application_identifier of this ProvisioningProfile.

        The application identifier.

        :return: The application_identifier of this ProvisioningProfile.
        :rtype: str
        """
        return self._application_identifier

    @application_identifier.setter
    def application_identifier(self, application_identifier):
        """Sets the application_identifier of this ProvisioningProfile.

        The application identifier.

        :param application_identifier: The application_identifier of this ProvisioningProfile.
        :type application_identifier: str
        """
        if application_identifier is None:
            raise ValueError("Invalid value for `application_identifier`, must not be `None`")

        self._application_identifier = application_identifier

    @property
    def expired_at(self):
        """Gets the expired_at of this ProvisioningProfile.

        The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z

        :return: The expired_at of this ProvisioningProfile.
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this ProvisioningProfile.

        The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z

        :param expired_at: The expired_at of this ProvisioningProfile.
        :type expired_at: str
        """
        if expired_at is None:
            raise ValueError("Invalid value for `expired_at`, must not be `None`")

        self._expired_at = expired_at

    @property
    def name(self):
        """Gets the name of this ProvisioningProfile.

        The name of the provisioning profile.

        :return: The name of this ProvisioningProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvisioningProfile.

        The name of the provisioning profile.

        :param name: The name of this ProvisioningProfile.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def profile_type(self):
        """Gets the profile_type of this ProvisioningProfile.


        :return: The profile_type of this ProvisioningProfile.
        :rtype: str
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """Sets the profile_type of this ProvisioningProfile.


        :param profile_type: The profile_type of this ProvisioningProfile.
        :type profile_type: str
        """
        allowed_values = ["adhoc", "enterprise", "other"]  # noqa: E501
        if profile_type not in allowed_values:
            raise ValueError(
                "Invalid value for `profile_type` ({0}), must be one of {1}"
                .format(profile_type, allowed_values)
            )

        self._profile_type = profile_type

    @property
    def team_identifier(self):
        """Gets the team_identifier of this ProvisioningProfile.

        The team identifier.

        :return: The team_identifier of this ProvisioningProfile.
        :rtype: str
        """
        return self._team_identifier

    @team_identifier.setter
    def team_identifier(self, team_identifier):
        """Sets the team_identifier of this ProvisioningProfile.

        The team identifier.

        :param team_identifier: The team_identifier of this ProvisioningProfile.
        :type team_identifier: str
        """
        if team_identifier is None:
            raise ValueError("Invalid value for `team_identifier`, must not be `None`")

        self._team_identifier = team_identifier

    @property
    def udids(self):
        """Gets the udids of this ProvisioningProfile.


        :return: The udids of this ProvisioningProfile.
        :rtype: List[str]
        """
        return self._udids

    @udids.setter
    def udids(self, udids):
        """Sets the udids of this ProvisioningProfile.


        :param udids: The udids of this ProvisioningProfile.
        :type udids: List[str]
        """

        self._udids = udids
