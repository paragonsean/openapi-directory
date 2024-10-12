# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.web_service_send_sms_request import WebServiceSendSmsRequest
from openapi_server import util


class WebServiceSendSmsRequests(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_date_to_send: datetime=None, messages_per_minute: int=None, send_sms_requests: List[WebServiceSendSmsRequest]=None):
        """WebServiceSendSmsRequests - a model defined in OpenAPI

        :param default_date_to_send: The default_date_to_send of this WebServiceSendSmsRequests.
        :param messages_per_minute: The messages_per_minute of this WebServiceSendSmsRequests.
        :param send_sms_requests: The send_sms_requests of this WebServiceSendSmsRequests.
        """
        self.openapi_types = {
            'default_date_to_send': datetime,
            'messages_per_minute': int,
            'send_sms_requests': List[WebServiceSendSmsRequest]
        }

        self.attribute_map = {
            'default_date_to_send': 'defaultDateToSend',
            'messages_per_minute': 'messagesPerMinute',
            'send_sms_requests': 'sendSmsRequests'
        }

        self._default_date_to_send = default_date_to_send
        self._messages_per_minute = messages_per_minute
        self._send_sms_requests = send_sms_requests

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebServiceSendSmsRequests':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebServiceSendSmsRequests of this WebServiceSendSmsRequests.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_date_to_send(self):
        """Gets the default_date_to_send of this WebServiceSendSmsRequests.


        :return: The default_date_to_send of this WebServiceSendSmsRequests.
        :rtype: datetime
        """
        return self._default_date_to_send

    @default_date_to_send.setter
    def default_date_to_send(self, default_date_to_send):
        """Sets the default_date_to_send of this WebServiceSendSmsRequests.


        :param default_date_to_send: The default_date_to_send of this WebServiceSendSmsRequests.
        :type default_date_to_send: datetime
        """

        self._default_date_to_send = default_date_to_send

    @property
    def messages_per_minute(self):
        """Gets the messages_per_minute of this WebServiceSendSmsRequests.


        :return: The messages_per_minute of this WebServiceSendSmsRequests.
        :rtype: int
        """
        return self._messages_per_minute

    @messages_per_minute.setter
    def messages_per_minute(self, messages_per_minute):
        """Sets the messages_per_minute of this WebServiceSendSmsRequests.


        :param messages_per_minute: The messages_per_minute of this WebServiceSendSmsRequests.
        :type messages_per_minute: int
        """

        self._messages_per_minute = messages_per_minute

    @property
    def send_sms_requests(self):
        """Gets the send_sms_requests of this WebServiceSendSmsRequests.


        :return: The send_sms_requests of this WebServiceSendSmsRequests.
        :rtype: List[WebServiceSendSmsRequest]
        """
        return self._send_sms_requests

    @send_sms_requests.setter
    def send_sms_requests(self, send_sms_requests):
        """Sets the send_sms_requests of this WebServiceSendSmsRequests.


        :param send_sms_requests: The send_sms_requests of this WebServiceSendSmsRequests.
        :type send_sms_requests: List[WebServiceSendSmsRequest]
        """

        self._send_sms_requests = send_sms_requests
