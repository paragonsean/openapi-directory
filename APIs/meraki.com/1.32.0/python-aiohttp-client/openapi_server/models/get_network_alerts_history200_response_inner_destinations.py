# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_alerts_history200_response_inner_destinations_email import GetNetworkAlertsHistory200ResponseInnerDestinationsEmail
from openapi_server.models.get_network_alerts_history200_response_inner_destinations_push import GetNetworkAlertsHistory200ResponseInnerDestinationsPush
from openapi_server.models.get_network_alerts_history200_response_inner_destinations_sms import GetNetworkAlertsHistory200ResponseInnerDestinationsSms
from openapi_server.models.get_network_alerts_history200_response_inner_destinations_webhook import GetNetworkAlertsHistory200ResponseInnerDestinationsWebhook
from openapi_server import util


class GetNetworkAlertsHistory200ResponseInnerDestinations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email: GetNetworkAlertsHistory200ResponseInnerDestinationsEmail=None, push: GetNetworkAlertsHistory200ResponseInnerDestinationsPush=None, sms: GetNetworkAlertsHistory200ResponseInnerDestinationsSms=None, webhook: GetNetworkAlertsHistory200ResponseInnerDestinationsWebhook=None):
        """GetNetworkAlertsHistory200ResponseInnerDestinations - a model defined in OpenAPI

        :param email: The email of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :param push: The push of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :param sms: The sms of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :param webhook: The webhook of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        """
        self.openapi_types = {
            'email': GetNetworkAlertsHistory200ResponseInnerDestinationsEmail,
            'push': GetNetworkAlertsHistory200ResponseInnerDestinationsPush,
            'sms': GetNetworkAlertsHistory200ResponseInnerDestinationsSms,
            'webhook': GetNetworkAlertsHistory200ResponseInnerDestinationsWebhook
        }

        self.attribute_map = {
            'email': 'email',
            'push': 'push',
            'sms': 'sms',
            'webhook': 'webhook'
        }

        self._email = email
        self._push = push
        self._sms = sms
        self._webhook = webhook

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkAlertsHistory200ResponseInnerDestinations':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkAlertsHistory_200_response_inner_destinations of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :return: The email of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :rtype: GetNetworkAlertsHistory200ResponseInnerDestinationsEmail
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :param email: The email of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :type email: GetNetworkAlertsHistory200ResponseInnerDestinationsEmail
        """

        self._email = email

    @property
    def push(self):
        """Gets the push of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :return: The push of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :rtype: GetNetworkAlertsHistory200ResponseInnerDestinationsPush
        """
        return self._push

    @push.setter
    def push(self, push):
        """Sets the push of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :param push: The push of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :type push: GetNetworkAlertsHistory200ResponseInnerDestinationsPush
        """

        self._push = push

    @property
    def sms(self):
        """Gets the sms of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :return: The sms of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :rtype: GetNetworkAlertsHistory200ResponseInnerDestinationsSms
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :param sms: The sms of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :type sms: GetNetworkAlertsHistory200ResponseInnerDestinationsSms
        """

        self._sms = sms

    @property
    def webhook(self):
        """Gets the webhook of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :return: The webhook of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :rtype: GetNetworkAlertsHistory200ResponseInnerDestinationsWebhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this GetNetworkAlertsHistory200ResponseInnerDestinations.


        :param webhook: The webhook of this GetNetworkAlertsHistory200ResponseInnerDestinations.
        :type webhook: GetNetworkAlertsHistory200ResponseInnerDestinationsWebhook
        """

        self._webhook = webhook
