# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSensorAlertsProfiles200ResponseInnerRecipients(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, emails: List[str]=None, http_server_ids: List[str]=None, sms_numbers: List[str]=None):
        """GetNetworkSensorAlertsProfiles200ResponseInnerRecipients - a model defined in OpenAPI

        :param emails: The emails of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :param http_server_ids: The http_server_ids of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :param sms_numbers: The sms_numbers of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        """
        self.openapi_types = {
            'emails': List[str],
            'http_server_ids': List[str],
            'sms_numbers': List[str]
        }

        self.attribute_map = {
            'emails': 'emails',
            'http_server_ids': 'httpServerIds',
            'sms_numbers': 'smsNumbers'
        }

        self._emails = emails
        self._http_server_ids = http_server_ids
        self._sms_numbers = sms_numbers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSensorAlertsProfiles200ResponseInnerRecipients':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSensorAlertsProfiles_200_response_inner_recipients of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def emails(self):
        """Gets the emails of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of emails that will receive information about the alert.

        :return: The emails of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :rtype: List[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of emails that will receive information about the alert.

        :param emails: The emails of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :type emails: List[str]
        """

        self._emails = emails

    @property
    def http_server_ids(self):
        """Gets the http_server_ids of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of webhook endpoint IDs that will receive information about the alert.

        :return: The http_server_ids of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :rtype: List[str]
        """
        return self._http_server_ids

    @http_server_ids.setter
    def http_server_ids(self, http_server_ids):
        """Sets the http_server_ids of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of webhook endpoint IDs that will receive information about the alert.

        :param http_server_ids: The http_server_ids of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :type http_server_ids: List[str]
        """

        self._http_server_ids = http_server_ids

    @property
    def sms_numbers(self):
        """Gets the sms_numbers of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of SMS numbers that will receive information about the alert.

        :return: The sms_numbers of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :rtype: List[str]
        """
        return self._sms_numbers

    @sms_numbers.setter
    def sms_numbers(self, sms_numbers):
        """Sets the sms_numbers of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.

        A list of SMS numbers that will receive information about the alert.

        :param sms_numbers: The sms_numbers of this GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.
        :type sms_numbers: List[str]
        """

        self._sms_numbers = sms_numbers
