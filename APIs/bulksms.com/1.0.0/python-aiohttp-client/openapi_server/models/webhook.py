# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Webhook(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active: bool=None, contact_email_address: str=None, id: float=None, name: str=None, on_web_app: bool=None, trigger_scope: str=None, url: str=None):
        """Webhook - a model defined in OpenAPI

        :param active: The active of this Webhook.
        :param contact_email_address: The contact_email_address of this Webhook.
        :param id: The id of this Webhook.
        :param name: The name of this Webhook.
        :param on_web_app: The on_web_app of this Webhook.
        :param trigger_scope: The trigger_scope of this Webhook.
        :param url: The url of this Webhook.
        """
        self.openapi_types = {
            'active': bool,
            'contact_email_address': str,
            'id': float,
            'name': str,
            'on_web_app': bool,
            'trigger_scope': str,
            'url': str
        }

        self.attribute_map = {
            'active': 'active',
            'contact_email_address': 'contactEmailAddress',
            'id': 'id',
            'name': 'name',
            'on_web_app': 'onWebApp',
            'trigger_scope': 'triggerScope',
            'url': 'url'
        }

        self._active = active
        self._contact_email_address = contact_email_address
        self._id = id
        self._name = name
        self._on_web_app = on_web_app
        self._trigger_scope = trigger_scope
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Webhook':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Webhook of this Webhook.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self):
        """Gets the active of this Webhook.


        :return: The active of this Webhook.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Webhook.


        :param active: The active of this Webhook.
        :type active: bool
        """

        self._active = active

    @property
    def contact_email_address(self):
        """Gets the contact_email_address of this Webhook.


        :return: The contact_email_address of this Webhook.
        :rtype: str
        """
        return self._contact_email_address

    @contact_email_address.setter
    def contact_email_address(self, contact_email_address):
        """Sets the contact_email_address of this Webhook.


        :param contact_email_address: The contact_email_address of this Webhook.
        :type contact_email_address: str
        """

        self._contact_email_address = contact_email_address

    @property
    def id(self):
        """Gets the id of this Webhook.


        :return: The id of this Webhook.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.


        :param id: The id of this Webhook.
        :type id: float
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Webhook.


        :return: The name of this Webhook.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Webhook.


        :param name: The name of this Webhook.
        :type name: str
        """

        self._name = name

    @property
    def on_web_app(self):
        """Gets the on_web_app of this Webhook.


        :return: The on_web_app of this Webhook.
        :rtype: bool
        """
        return self._on_web_app

    @on_web_app.setter
    def on_web_app(self, on_web_app):
        """Sets the on_web_app of this Webhook.


        :param on_web_app: The on_web_app of this Webhook.
        :type on_web_app: bool
        """

        self._on_web_app = on_web_app

    @property
    def trigger_scope(self):
        """Gets the trigger_scope of this Webhook.


        :return: The trigger_scope of this Webhook.
        :rtype: str
        """
        return self._trigger_scope

    @trigger_scope.setter
    def trigger_scope(self, trigger_scope):
        """Sets the trigger_scope of this Webhook.


        :param trigger_scope: The trigger_scope of this Webhook.
        :type trigger_scope: str
        """

        self._trigger_scope = trigger_scope

    @property
    def url(self):
        """Gets the url of this Webhook.


        :return: The url of this Webhook.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.


        :param url: The url of this Webhook.
        :type url: str
        """

        self._url = url
