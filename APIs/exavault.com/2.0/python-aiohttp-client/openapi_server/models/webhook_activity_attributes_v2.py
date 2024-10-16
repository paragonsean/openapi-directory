# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.webhook_v2_details import WebhookV2Details
from openapi_server import util


class WebhookActivityAttributesV2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_id: str=None, attempt_id: str=None, created: str=None, details: WebhookV2Details=None, endpoint_url: str=None, event: str=None, ip_address: str=None, resend: bool=None, _resource_path: str=None, response: str=None, status: int=None, username: str=None, webhook_format: str=None, webhook_id: int=None, webhook_path: str=None):
        """WebhookActivityAttributesV2 - a model defined in OpenAPI

        :param account_id: The account_id of this WebhookActivityAttributesV2.
        :param attempt_id: The attempt_id of this WebhookActivityAttributesV2.
        :param created: The created of this WebhookActivityAttributesV2.
        :param details: The details of this WebhookActivityAttributesV2.
        :param endpoint_url: The endpoint_url of this WebhookActivityAttributesV2.
        :param event: The event of this WebhookActivityAttributesV2.
        :param ip_address: The ip_address of this WebhookActivityAttributesV2.
        :param resend: The resend of this WebhookActivityAttributesV2.
        :param _resource_path: The _resource_path of this WebhookActivityAttributesV2.
        :param response: The response of this WebhookActivityAttributesV2.
        :param status: The status of this WebhookActivityAttributesV2.
        :param username: The username of this WebhookActivityAttributesV2.
        :param webhook_format: The webhook_format of this WebhookActivityAttributesV2.
        :param webhook_id: The webhook_id of this WebhookActivityAttributesV2.
        :param webhook_path: The webhook_path of this WebhookActivityAttributesV2.
        """
        self.openapi_types = {
            'account_id': str,
            'attempt_id': str,
            'created': str,
            'details': WebhookV2Details,
            'endpoint_url': str,
            'event': str,
            'ip_address': str,
            'resend': bool,
            '_resource_path': str,
            'response': str,
            'status': int,
            'username': str,
            'webhook_format': str,
            'webhook_id': int,
            'webhook_path': str
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'attempt_id': 'attemptId',
            'created': 'created',
            'details': 'details',
            'endpoint_url': 'endpointUrl',
            'event': 'event',
            'ip_address': 'ipAddress',
            'resend': 'resend',
            '_resource_path': 'resourcePath',
            'response': 'response',
            'status': 'status',
            'username': 'username',
            'webhook_format': 'webhookFormat',
            'webhook_id': 'webhookId',
            'webhook_path': 'webhookPath'
        }

        self._account_id = account_id
        self._attempt_id = attempt_id
        self._created = created
        self._details = details
        self._endpoint_url = endpoint_url
        self._event = event
        self._ip_address = ip_address
        self._resend = resend
        self.__resource_path = _resource_path
        self._response = response
        self._status = status
        self._username = username
        self._webhook_format = webhook_format
        self._webhook_id = webhook_id
        self._webhook_path = webhook_path

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebhookActivityAttributesV2':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebhookActivityAttributesV2 of this WebhookActivityAttributesV2.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self):
        """Gets the account_id of this WebhookActivityAttributesV2.

        Unique ID of account

        :return: The account_id of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this WebhookActivityAttributesV2.

        Unique ID of account

        :param account_id: The account_id of this WebhookActivityAttributesV2.
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def attempt_id(self):
        """Gets the attempt_id of this WebhookActivityAttributesV2.

        Event - retry identifier

        :return: The attempt_id of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._attempt_id

    @attempt_id.setter
    def attempt_id(self, attempt_id):
        """Sets the attempt_id of this WebhookActivityAttributesV2.

        Event - retry identifier

        :param attempt_id: The attempt_id of this WebhookActivityAttributesV2.
        :type attempt_id: str
        """

        self._attempt_id = attempt_id

    @property
    def created(self):
        """Gets the created of this WebhookActivityAttributesV2.

        Date and time of webhook message being generated by system

        :return: The created of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WebhookActivityAttributesV2.

        Date and time of webhook message being generated by system

        :param created: The created of this WebhookActivityAttributesV2.
        :type created: str
        """

        self._created = created

    @property
    def details(self):
        """Gets the details of this WebhookActivityAttributesV2.


        :return: The details of this WebhookActivityAttributesV2.
        :rtype: WebhookV2Details
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this WebhookActivityAttributesV2.


        :param details: The details of this WebhookActivityAttributesV2.
        :type details: WebhookV2Details
        """

        self._details = details

    @property
    def endpoint_url(self):
        """Gets the endpoint_url of this WebhookActivityAttributesV2.

        The URL the message was sent to

        :return: The endpoint_url of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """Sets the endpoint_url of this WebhookActivityAttributesV2.

        The URL the message was sent to

        :param endpoint_url: The endpoint_url of this WebhookActivityAttributesV2.
        :type endpoint_url: str
        """

        self._endpoint_url = endpoint_url

    @property
    def event(self):
        """Gets the event of this WebhookActivityAttributesV2.

        Event type

        :return: The event of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this WebhookActivityAttributesV2.

        Event type

        :param event: The event of this WebhookActivityAttributesV2.
        :type event: str
        """
        allowed_values = ["resources.upload", "resources.download", "resources.delete", "resources.rename", "resources.copy", "resources.move", "resources.compress", "resources.extract", "resources.createFolder", "shares.formSubmit"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def ip_address(self):
        """Gets the ip_address of this WebhookActivityAttributesV2.

        IP Address of related activity

        :return: The ip_address of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this WebhookActivityAttributesV2.

        IP Address of related activity

        :param ip_address: The ip_address of this WebhookActivityAttributesV2.
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def resend(self):
        """Gets the resend of this WebhookActivityAttributesV2.

        Whether this attempt was a re-send of a previous attempt

        :return: The resend of this WebhookActivityAttributesV2.
        :rtype: bool
        """
        return self._resend

    @resend.setter
    def resend(self, resend):
        """Sets the resend of this WebhookActivityAttributesV2.

        Whether this attempt was a re-send of a previous attempt

        :param resend: The resend of this WebhookActivityAttributesV2.
        :type resend: bool
        """

        self._resend = resend

    @property
    def _resource_path(self):
        """Gets the _resource_path of this WebhookActivityAttributesV2.

        Path of resource that matched webhook

        :return: The _resource_path of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self.__resource_path

    @_resource_path.setter
    def _resource_path(self, _resource_path):
        """Sets the _resource_path of this WebhookActivityAttributesV2.

        Path of resource that matched webhook

        :param _resource_path: The _resource_path of this WebhookActivityAttributesV2.
        :type _resource_path: str
        """

        self.__resource_path = _resource_path

    @property
    def response(self):
        """Gets the response of this WebhookActivityAttributesV2.

        Body of web response returned by webhook listener

        :return: The response of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this WebhookActivityAttributesV2.

        Body of web response returned by webhook listener

        :param response: The response of this WebhookActivityAttributesV2.
        :type response: str
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this WebhookActivityAttributesV2.

        HTTP Status Code returned by webhook listener

        :return: The status of this WebhookActivityAttributesV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookActivityAttributesV2.

        HTTP Status Code returned by webhook listener

        :param status: The status of this WebhookActivityAttributesV2.
        :type status: int
        """

        self._status = status

    @property
    def username(self):
        """Gets the username of this WebhookActivityAttributesV2.

        Username of related activity

        :return: The username of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this WebhookActivityAttributesV2.

        Username of related activity

        :param username: The username of this WebhookActivityAttributesV2.
        :type username: str
        """

        self._username = username

    @property
    def webhook_format(self):
        """Gets the webhook_format of this WebhookActivityAttributesV2.

        What version of webhook message is being sent `v2`

        :return: The webhook_format of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._webhook_format

    @webhook_format.setter
    def webhook_format(self, webhook_format):
        """Sets the webhook_format of this WebhookActivityAttributesV2.

        What version of webhook message is being sent `v2`

        :param webhook_format: The webhook_format of this WebhookActivityAttributesV2.
        :type webhook_format: str
        """

        self._webhook_format = webhook_format

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookActivityAttributesV2.

        Unique ID of webhook configuration

        :return: The webhook_id of this WebhookActivityAttributesV2.
        :rtype: int
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookActivityAttributesV2.

        Unique ID of webhook configuration

        :param webhook_id: The webhook_id of this WebhookActivityAttributesV2.
        :type webhook_id: int
        """

        self._webhook_id = webhook_id

    @property
    def webhook_path(self):
        """Gets the webhook_path of this WebhookActivityAttributesV2.

        Path that webhook is watching

        :return: The webhook_path of this WebhookActivityAttributesV2.
        :rtype: str
        """
        return self._webhook_path

    @webhook_path.setter
    def webhook_path(self, webhook_path):
        """Sets the webhook_path of this WebhookActivityAttributesV2.

        Path that webhook is watching

        :param webhook_path: The webhook_path of this WebhookActivityAttributesV2.
        :type webhook_path: str
        """

        self._webhook_path = webhook_path
