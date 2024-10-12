# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.key_view import KeyView
from openapi_server import util


class KeysApiFind200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, callback_on_modify: bool=None, callback_url: str=None, commenced: datetime=None, created: datetime=None, current: bool=None, custom: object=None, frequency: str=None, name: str=None, serial: str=None, updated: datetime=None):
        """KeysApiFind200Response - a model defined in OpenAPI

        :param action: The action of this KeysApiFind200Response.
        :param callback_on_modify: The callback_on_modify of this KeysApiFind200Response.
        :param callback_url: The callback_url of this KeysApiFind200Response.
        :param commenced: The commenced of this KeysApiFind200Response.
        :param created: The created of this KeysApiFind200Response.
        :param current: The current of this KeysApiFind200Response.
        :param custom: The custom of this KeysApiFind200Response.
        :param frequency: The frequency of this KeysApiFind200Response.
        :param name: The name of this KeysApiFind200Response.
        :param serial: The serial of this KeysApiFind200Response.
        :param updated: The updated of this KeysApiFind200Response.
        """
        self.openapi_types = {
            'action': str,
            'callback_on_modify': bool,
            'callback_url': str,
            'commenced': datetime,
            'created': datetime,
            'current': bool,
            'custom': object,
            'frequency': str,
            'name': str,
            'serial': str,
            'updated': datetime
        }

        self.attribute_map = {
            'action': 'action',
            'callback_on_modify': 'callbackOnModify',
            'callback_url': 'callbackUrl',
            'commenced': 'commenced',
            'created': 'created',
            'current': 'current',
            'custom': 'custom',
            'frequency': 'frequency',
            'name': 'name',
            'serial': 'serial',
            'updated': 'updated'
        }

        self._action = action
        self._callback_on_modify = callback_on_modify
        self._callback_url = callback_url
        self._commenced = commenced
        self._created = created
        self._current = current
        self._custom = custom
        self._frequency = frequency
        self._name = name
        self._serial = serial
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KeysApiFind200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KeysApi_Find_200_response of this KeysApiFind200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this KeysApiFind200Response.


        :return: The action of this KeysApiFind200Response.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this KeysApiFind200Response.


        :param action: The action of this KeysApiFind200Response.
        :type action: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")
        if action is not None and len(action) < 1:
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `1`")

        self._action = action

    @property
    def callback_on_modify(self):
        """Gets the callback_on_modify of this KeysApiFind200Response.


        :return: The callback_on_modify of this KeysApiFind200Response.
        :rtype: bool
        """
        return self._callback_on_modify

    @callback_on_modify.setter
    def callback_on_modify(self, callback_on_modify):
        """Sets the callback_on_modify of this KeysApiFind200Response.


        :param callback_on_modify: The callback_on_modify of this KeysApiFind200Response.
        :type callback_on_modify: bool
        """
        if callback_on_modify is None:
            raise ValueError("Invalid value for `callback_on_modify`, must not be `None`")

        self._callback_on_modify = callback_on_modify

    @property
    def callback_url(self):
        """Gets the callback_url of this KeysApiFind200Response.


        :return: The callback_url of this KeysApiFind200Response.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this KeysApiFind200Response.


        :param callback_url: The callback_url of this KeysApiFind200Response.
        :type callback_url: str
        """
        if callback_url is not None and len(callback_url) > 800:
            raise ValueError("Invalid value for `callback_url`, length must be less than or equal to `800`")
        if callback_url is not None and len(callback_url) < 0:
            raise ValueError("Invalid value for `callback_url`, length must be greater than or equal to `0`")

        self._callback_url = callback_url

    @property
    def commenced(self):
        """Gets the commenced of this KeysApiFind200Response.


        :return: The commenced of this KeysApiFind200Response.
        :rtype: datetime
        """
        return self._commenced

    @commenced.setter
    def commenced(self, commenced):
        """Sets the commenced of this KeysApiFind200Response.


        :param commenced: The commenced of this KeysApiFind200Response.
        :type commenced: datetime
        """
        if commenced is None:
            raise ValueError("Invalid value for `commenced`, must not be `None`")
        if commenced is not None and len(commenced) < 1:
            raise ValueError("Invalid value for `commenced`, length must be greater than or equal to `1`")

        self._commenced = commenced

    @property
    def created(self):
        """Gets the created of this KeysApiFind200Response.


        :return: The created of this KeysApiFind200Response.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this KeysApiFind200Response.


        :param created: The created of this KeysApiFind200Response.
        :type created: datetime
        """

        self._created = created

    @property
    def current(self):
        """Gets the current of this KeysApiFind200Response.


        :return: The current of this KeysApiFind200Response.
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this KeysApiFind200Response.


        :param current: The current of this KeysApiFind200Response.
        :type current: bool
        """

        self._current = current

    @property
    def custom(self):
        """Gets the custom of this KeysApiFind200Response.


        :return: The custom of this KeysApiFind200Response.
        :rtype: object
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this KeysApiFind200Response.


        :param custom: The custom of this KeysApiFind200Response.
        :type custom: object
        """

        self._custom = custom

    @property
    def frequency(self):
        """Gets the frequency of this KeysApiFind200Response.


        :return: The frequency of this KeysApiFind200Response.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this KeysApiFind200Response.


        :param frequency: The frequency of this KeysApiFind200Response.
        :type frequency: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")
        if frequency is not None and len(frequency) < 1:
            raise ValueError("Invalid value for `frequency`, length must be greater than or equal to `1`")

        self._frequency = frequency

    @property
    def name(self):
        """Gets the name of this KeysApiFind200Response.


        :return: The name of this KeysApiFind200Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeysApiFind200Response.


        :param name: The name of this KeysApiFind200Response.
        :type name: str
        """
        if name is not None and len(name) > 80:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this KeysApiFind200Response.


        :return: The serial of this KeysApiFind200Response.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this KeysApiFind200Response.


        :param serial: The serial of this KeysApiFind200Response.
        :type serial: str
        """

        self._serial = serial

    @property
    def updated(self):
        """Gets the updated of this KeysApiFind200Response.


        :return: The updated of this KeysApiFind200Response.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this KeysApiFind200Response.


        :param updated: The updated of this KeysApiFind200Response.
        :type updated: datetime
        """

        self._updated = updated
