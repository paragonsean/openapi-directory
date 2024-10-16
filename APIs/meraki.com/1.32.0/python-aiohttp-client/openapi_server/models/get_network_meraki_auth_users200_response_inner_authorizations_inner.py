# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authorized_by_email: str=None, authorized_by_name: str=None, authorized_zone: str=None, expires_at: datetime=None, ssid_number: int=None):
        """GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner - a model defined in OpenAPI

        :param authorized_by_email: The authorized_by_email of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :param authorized_by_name: The authorized_by_name of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :param authorized_zone: The authorized_zone of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :param expires_at: The expires_at of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :param ssid_number: The ssid_number of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        """
        self.openapi_types = {
            'authorized_by_email': str,
            'authorized_by_name': str,
            'authorized_zone': str,
            'expires_at': datetime,
            'ssid_number': int
        }

        self.attribute_map = {
            'authorized_by_email': 'authorizedByEmail',
            'authorized_by_name': 'authorizedByName',
            'authorized_zone': 'authorizedZone',
            'expires_at': 'expiresAt',
            'ssid_number': 'ssidNumber'
        }

        self._authorized_by_email = authorized_by_email
        self._authorized_by_name = authorized_by_name
        self._authorized_zone = authorized_zone
        self._expires_at = expires_at
        self._ssid_number = ssid_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkMerakiAuthUsers_200_response_inner_authorizations_inner of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authorized_by_email(self):
        """Gets the authorized_by_email of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        User is authorized by the account email address

        :return: The authorized_by_email of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :rtype: str
        """
        return self._authorized_by_email

    @authorized_by_email.setter
    def authorized_by_email(self, authorized_by_email):
        """Sets the authorized_by_email of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        User is authorized by the account email address

        :param authorized_by_email: The authorized_by_email of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :type authorized_by_email: str
        """

        self._authorized_by_email = authorized_by_email

    @property
    def authorized_by_name(self):
        """Gets the authorized_by_name of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        User is authorized by the account name

        :return: The authorized_by_name of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :rtype: str
        """
        return self._authorized_by_name

    @authorized_by_name.setter
    def authorized_by_name(self, authorized_by_name):
        """Sets the authorized_by_name of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        User is authorized by the account name

        :param authorized_by_name: The authorized_by_name of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :type authorized_by_name: str
        """

        self._authorized_by_name = authorized_by_name

    @property
    def authorized_zone(self):
        """Gets the authorized_zone of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        Authorized zone of the user

        :return: The authorized_zone of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :rtype: str
        """
        return self._authorized_zone

    @authorized_zone.setter
    def authorized_zone(self, authorized_zone):
        """Sets the authorized_zone of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        Authorized zone of the user

        :param authorized_zone: The authorized_zone of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :type authorized_zone: str
        """

        self._authorized_zone = authorized_zone

    @property
    def expires_at(self):
        """Gets the expires_at of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        Authorization expiration time

        :return: The expires_at of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        Authorization expiration time

        :param expires_at: The expires_at of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :type expires_at: datetime
        """

        self._expires_at = expires_at

    @property
    def ssid_number(self):
        """Gets the ssid_number of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        SSID number

        :return: The ssid_number of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :rtype: int
        """
        return self._ssid_number

    @ssid_number.setter
    def ssid_number(self, ssid_number):
        """Sets the ssid_number of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.

        SSID number

        :param ssid_number: The ssid_number of this GetNetworkMerakiAuthUsers200ResponseInnerAuthorizationsInner.
        :type ssid_number: int
        """

        self._ssid_number = ssid_number
