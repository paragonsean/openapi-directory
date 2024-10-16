# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AlertUserAppEmailSettingsResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, request_id: str=None, e_tag: str=None, enabled: bool=None, settings: List[object]=None, user_id: str=None, app_id: str=None, user_enabled: bool=None):
        """AlertUserAppEmailSettingsResult - a model defined in OpenAPI

        :param request_id: The request_id of this AlertUserAppEmailSettingsResult.
        :param e_tag: The e_tag of this AlertUserAppEmailSettingsResult.
        :param enabled: The enabled of this AlertUserAppEmailSettingsResult.
        :param settings: The settings of this AlertUserAppEmailSettingsResult.
        :param user_id: The user_id of this AlertUserAppEmailSettingsResult.
        :param app_id: The app_id of this AlertUserAppEmailSettingsResult.
        :param user_enabled: The user_enabled of this AlertUserAppEmailSettingsResult.
        """
        self.openapi_types = {
            'request_id': str,
            'e_tag': str,
            'enabled': bool,
            'settings': List[object],
            'user_id': str,
            'app_id': str,
            'user_enabled': bool
        }

        self.attribute_map = {
            'request_id': 'request_id',
            'e_tag': 'eTag',
            'enabled': 'enabled',
            'settings': 'settings',
            'user_id': 'userId',
            'app_id': 'appId',
            'user_enabled': 'user_enabled'
        }

        self._request_id = request_id
        self._e_tag = e_tag
        self._enabled = enabled
        self._settings = settings
        self._user_id = user_id
        self._app_id = app_id
        self._user_enabled = user_enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlertUserAppEmailSettingsResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlertUserAppEmailSettingsResult of this AlertUserAppEmailSettingsResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_id(self):
        """Gets the request_id of this AlertUserAppEmailSettingsResult.

        Unique request

        :return: The request_id of this AlertUserAppEmailSettingsResult.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AlertUserAppEmailSettingsResult.

        Unique request

        :param request_id: The request_id of this AlertUserAppEmailSettingsResult.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def e_tag(self):
        """Gets the e_tag of this AlertUserAppEmailSettingsResult.

        The ETag of the entity

        :return: The e_tag of this AlertUserAppEmailSettingsResult.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        """Sets the e_tag of this AlertUserAppEmailSettingsResult.

        The ETag of the entity

        :param e_tag: The e_tag of this AlertUserAppEmailSettingsResult.
        :type e_tag: str
        """

        self._e_tag = e_tag

    @property
    def enabled(self):
        """Gets the enabled of this AlertUserAppEmailSettingsResult.

        Allows to forcefully disable emails on app or user level

        :return: The enabled of this AlertUserAppEmailSettingsResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AlertUserAppEmailSettingsResult.

        Allows to forcefully disable emails on app or user level

        :param enabled: The enabled of this AlertUserAppEmailSettingsResult.
        :type enabled: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def settings(self):
        """Gets the settings of this AlertUserAppEmailSettingsResult.

        The settings the user has for the app

        :return: The settings of this AlertUserAppEmailSettingsResult.
        :rtype: List[object]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AlertUserAppEmailSettingsResult.

        The settings the user has for the app

        :param settings: The settings of this AlertUserAppEmailSettingsResult.
        :type settings: List[object]
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")

        self._settings = settings

    @property
    def user_id(self):
        """Gets the user_id of this AlertUserAppEmailSettingsResult.

        The unique id (UUID) of the user

        :return: The user_id of this AlertUserAppEmailSettingsResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AlertUserAppEmailSettingsResult.

        The unique id (UUID) of the user

        :param user_id: The user_id of this AlertUserAppEmailSettingsResult.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def app_id(self):
        """Gets the app_id of this AlertUserAppEmailSettingsResult.

        Application ID

        :return: The app_id of this AlertUserAppEmailSettingsResult.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AlertUserAppEmailSettingsResult.

        Application ID

        :param app_id: The app_id of this AlertUserAppEmailSettingsResult.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def user_enabled(self):
        """Gets the user_enabled of this AlertUserAppEmailSettingsResult.

        A flag indicating if settings are enabled at user/global level

        :return: The user_enabled of this AlertUserAppEmailSettingsResult.
        :rtype: bool
        """
        return self._user_enabled

    @user_enabled.setter
    def user_enabled(self, user_enabled):
        """Sets the user_enabled of this AlertUserAppEmailSettingsResult.

        A flag indicating if settings are enabled at user/global level

        :param user_enabled: The user_enabled of this AlertUserAppEmailSettingsResult.
        :type user_enabled: bool
        """
        if user_enabled is None:
            raise ValueError("Invalid value for `user_enabled`, must not be `None`")

        self._user_enabled = user_enabled
