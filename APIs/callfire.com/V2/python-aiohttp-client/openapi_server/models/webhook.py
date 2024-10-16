# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Webhook(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, callback: str=None, created_at: int=None, enabled: bool=None, events: list[str]=None, expires_at: int=None, fields: str=None, id: int=None, name: str=None, non_strict_ssl: bool=None, resource: str=None, secret: str=None, single_use: bool=None, updated_at: int=None):
        """Webhook - a model defined in OpenAPI

        :param callback: The callback of this Webhook.
        :param created_at: The created_at of this Webhook.
        :param enabled: The enabled of this Webhook.
        :param events: The events of this Webhook.
        :param expires_at: The expires_at of this Webhook.
        :param fields: The fields of this Webhook.
        :param id: The id of this Webhook.
        :param name: The name of this Webhook.
        :param non_strict_ssl: The non_strict_ssl of this Webhook.
        :param resource: The resource of this Webhook.
        :param secret: The secret of this Webhook.
        :param single_use: The single_use of this Webhook.
        :param updated_at: The updated_at of this Webhook.
        """
        self.openapi_types = {
            'callback': str,
            'created_at': int,
            'enabled': bool,
            'events': list[str],
            'expires_at': int,
            'fields': str,
            'id': int,
            'name': str,
            'non_strict_ssl': bool,
            'resource': str,
            'secret': str,
            'single_use': bool,
            'updated_at': int
        }

        self.attribute_map = {
            'callback': 'callback',
            'created_at': 'createdAt',
            'enabled': 'enabled',
            'events': 'events',
            'expires_at': 'expiresAt',
            'fields': 'fields',
            'id': 'id',
            'name': 'name',
            'non_strict_ssl': 'nonStrictSsl',
            'resource': 'resource',
            'secret': 'secret',
            'single_use': 'singleUse',
            'updated_at': 'updatedAt'
        }

        self._callback = callback
        self._created_at = created_at
        self._enabled = enabled
        self._events = events
        self._expires_at = expires_at
        self._fields = fields
        self._id = id
        self._name = name
        self._non_strict_ssl = non_strict_ssl
        self._resource = resource
        self._secret = secret
        self._single_use = single_use
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Webhook':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Webhook of this Webhook.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def callback(self):
        """Gets the callback of this Webhook.

        URL that webhook will send POST to on resource event trigger

        :return: The callback of this Webhook.
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this Webhook.

        URL that webhook will send POST to on resource event trigger

        :param callback: The callback of this Webhook.
        :type callback: str
        """

        self._callback = callback

    @property
    def created_at(self):
        """Gets the created_at of this Webhook.

        A time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000

        :return: The created_at of this Webhook.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Webhook.

        A time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000

        :param created_at: The created_at of this Webhook.
        :type created_at: int
        """

        self._created_at = created_at

    @property
    def enabled(self):
        """Gets the enabled of this Webhook.

        A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)

        :return: The enabled of this Webhook.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Webhook.

        A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)

        :param enabled: The enabled of this Webhook.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def events(self):
        """Gets the events of this Webhook.

        Comma separated list of events on resource that will trigger callbacks (ex: STARTED, STOPPED, FINISHED, etc...). 

        :return: The events of this Webhook.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Webhook.

        Comma separated list of events on resource that will trigger callbacks (ex: STARTED, STOPPED, FINISHED, etc...). 

        :param events: The events of this Webhook.
        :type events: list[str]
        """

        self._events = events

    @property
    def expires_at(self):
        """Gets the expires_at of this Webhook.

        ~

        :return: The expires_at of this Webhook.
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Webhook.

        ~

        :param expires_at: The expires_at of this Webhook.
        :type expires_at: int
        """

        self._expires_at = expires_at

    @property
    def fields(self):
        """Gets the fields of this Webhook.

        A limit callback response to a particular fields

        :return: The fields of this Webhook.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Webhook.

        A limit callback response to a particular fields

        :param fields: The fields of this Webhook.
        :type fields: str
        """

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this Webhook.

        An id of a webhook

        :return: The id of this Webhook.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.

        An id of a webhook

        :param id: The id of this Webhook.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Webhook.

        A name of a webhook

        :return: The name of this Webhook.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Webhook.

        A name of a webhook

        :param name: The name of this Webhook.
        :type name: str
        """

        self._name = name

    @property
    def non_strict_ssl(self):
        """Gets the non_strict_ssl of this Webhook.

        A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)

        :return: The non_strict_ssl of this Webhook.
        :rtype: bool
        """
        return self._non_strict_ssl

    @non_strict_ssl.setter
    def non_strict_ssl(self, non_strict_ssl):
        """Sets the non_strict_ssl of this Webhook.

        A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)

        :param non_strict_ssl: The non_strict_ssl of this Webhook.
        :type non_strict_ssl: bool
        """

        self._non_strict_ssl = non_strict_ssl

    @property
    def resource(self):
        """Gets the resource of this Webhook.

        A resource name that webhook is watching events on. Use GET /webhooks/resources to determine resources and events available (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...)

        :return: The resource of this Webhook.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Webhook.

        A resource name that webhook is watching events on. Use GET /webhooks/resources to determine resources and events available (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...)

        :param resource: The resource of this Webhook.
        :type resource: str
        """

        self._resource = resource

    @property
    def secret(self):
        """Gets the secret of this Webhook.

        Webhook secret token which is used as a signing key to HmacSHA1 hash of json payload which is returned in 'X-CallFire-Signature' header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)

        :return: The secret of this Webhook.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this Webhook.

        Webhook secret token which is used as a signing key to HmacSHA1 hash of json payload which is returned in 'X-CallFire-Signature' header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)

        :param secret: The secret of this Webhook.
        :type secret: str
        """

        self._secret = secret

    @property
    def single_use(self):
        """Gets the single_use of this Webhook.

        If true is set then webhook triggers only once. Afterwards the webhook will be deleted

        :return: The single_use of this Webhook.
        :rtype: bool
        """
        return self._single_use

    @single_use.setter
    def single_use(self, single_use):
        """Sets the single_use of this Webhook.

        If true is set then webhook triggers only once. Afterwards the webhook will be deleted

        :param single_use: The single_use of this Webhook.
        :type single_use: bool
        """

        self._single_use = single_use

    @property
    def updated_at(self):
        """Gets the updated_at of this Webhook.

        A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000

        :return: The updated_at of this Webhook.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Webhook.

        A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000

        :param updated_at: The updated_at of this Webhook.
        :type updated_at: int
        """

        self._updated_at = updated_at
