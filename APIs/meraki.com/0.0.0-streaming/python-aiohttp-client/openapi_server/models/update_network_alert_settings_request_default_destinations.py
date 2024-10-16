# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkAlertSettingsRequestDefaultDestinations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, all_admins: bool=None, emails: List[str]=None, http_server_ids: List[str]=None, snmp: bool=None):
        """UpdateNetworkAlertSettingsRequestDefaultDestinations - a model defined in OpenAPI

        :param all_admins: The all_admins of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :param emails: The emails of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :param http_server_ids: The http_server_ids of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :param snmp: The snmp of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        """
        self.openapi_types = {
            'all_admins': bool,
            'emails': List[str],
            'http_server_ids': List[str],
            'snmp': bool
        }

        self.attribute_map = {
            'all_admins': 'allAdmins',
            'emails': 'emails',
            'http_server_ids': 'httpServerIds',
            'snmp': 'snmp'
        }

        self._all_admins = all_admins
        self._emails = emails
        self._http_server_ids = http_server_ids
        self._snmp = snmp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkAlertSettingsRequestDefaultDestinations':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkAlertSettings_request_defaultDestinations of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def all_admins(self):
        """Gets the all_admins of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        If true, then all network admins will receive emails.

        :return: The all_admins of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :rtype: bool
        """
        return self._all_admins

    @all_admins.setter
    def all_admins(self, all_admins):
        """Sets the all_admins of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        If true, then all network admins will receive emails.

        :param all_admins: The all_admins of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :type all_admins: bool
        """

        self._all_admins = all_admins

    @property
    def emails(self):
        """Gets the emails of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        A list of emails that will recieve the alert(s).

        :return: The emails of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :rtype: List[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        A list of emails that will recieve the alert(s).

        :param emails: The emails of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :type emails: List[str]
        """

        self._emails = emails

    @property
    def http_server_ids(self):
        """Gets the http_server_ids of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        A list of HTTP server IDs to send a Webhook to

        :return: The http_server_ids of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :rtype: List[str]
        """
        return self._http_server_ids

    @http_server_ids.setter
    def http_server_ids(self, http_server_ids):
        """Sets the http_server_ids of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        A list of HTTP server IDs to send a Webhook to

        :param http_server_ids: The http_server_ids of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :type http_server_ids: List[str]
        """

        self._http_server_ids = http_server_ids

    @property
    def snmp(self):
        """Gets the snmp of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.

        :return: The snmp of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :rtype: bool
        """
        return self._snmp

    @snmp.setter
    def snmp(self, snmp):
        """Sets the snmp of this UpdateNetworkAlertSettingsRequestDefaultDestinations.

        If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.

        :param snmp: The snmp of this UpdateNetworkAlertSettingsRequestDefaultDestinations.
        :type snmp: bool
        """

        self._snmp = snmp
