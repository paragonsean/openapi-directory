# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Settings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, closed_caption: object=None, control_notifications: int=None, country_code: str=None, locale: str=None, network_standby: int=None, system_sound_effects: bool=None, time_format: int=None, timezone: str=None, wake_on_cast: int=None):
        """Settings - a model defined in OpenAPI

        :param closed_caption: The closed_caption of this Settings.
        :param control_notifications: The control_notifications of this Settings.
        :param country_code: The country_code of this Settings.
        :param locale: The locale of this Settings.
        :param network_standby: The network_standby of this Settings.
        :param system_sound_effects: The system_sound_effects of this Settings.
        :param time_format: The time_format of this Settings.
        :param timezone: The timezone of this Settings.
        :param wake_on_cast: The wake_on_cast of this Settings.
        """
        self.openapi_types = {
            'closed_caption': object,
            'control_notifications': int,
            'country_code': str,
            'locale': str,
            'network_standby': int,
            'system_sound_effects': bool,
            'time_format': int,
            'timezone': str,
            'wake_on_cast': int
        }

        self.attribute_map = {
            'closed_caption': 'closed_caption',
            'control_notifications': 'control_notifications',
            'country_code': 'country_code',
            'locale': 'locale',
            'network_standby': 'network_standby',
            'system_sound_effects': 'system_sound_effects',
            'time_format': 'time_format',
            'timezone': 'timezone',
            'wake_on_cast': 'wake_on_cast'
        }

        self._closed_caption = closed_caption
        self._control_notifications = control_notifications
        self._country_code = country_code
        self._locale = locale
        self._network_standby = network_standby
        self._system_sound_effects = system_sound_effects
        self._time_format = time_format
        self._timezone = timezone
        self._wake_on_cast = wake_on_cast

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Settings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Settings of this Settings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def closed_caption(self):
        """Gets the closed_caption of this Settings.


        :return: The closed_caption of this Settings.
        :rtype: object
        """
        return self._closed_caption

    @closed_caption.setter
    def closed_caption(self, closed_caption):
        """Sets the closed_caption of this Settings.


        :param closed_caption: The closed_caption of this Settings.
        :type closed_caption: object
        """
        if closed_caption is None:
            raise ValueError("Invalid value for `closed_caption`, must not be `None`")

        self._closed_caption = closed_caption

    @property
    def control_notifications(self):
        """Gets the control_notifications of this Settings.


        :return: The control_notifications of this Settings.
        :rtype: int
        """
        return self._control_notifications

    @control_notifications.setter
    def control_notifications(self, control_notifications):
        """Sets the control_notifications of this Settings.


        :param control_notifications: The control_notifications of this Settings.
        :type control_notifications: int
        """
        if control_notifications is None:
            raise ValueError("Invalid value for `control_notifications`, must not be `None`")

        self._control_notifications = control_notifications

    @property
    def country_code(self):
        """Gets the country_code of this Settings.


        :return: The country_code of this Settings.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Settings.


        :param country_code: The country_code of this Settings.
        :type country_code: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")

        self._country_code = country_code

    @property
    def locale(self):
        """Gets the locale of this Settings.


        :return: The locale of this Settings.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Settings.


        :param locale: The locale of this Settings.
        :type locale: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")

        self._locale = locale

    @property
    def network_standby(self):
        """Gets the network_standby of this Settings.


        :return: The network_standby of this Settings.
        :rtype: int
        """
        return self._network_standby

    @network_standby.setter
    def network_standby(self, network_standby):
        """Sets the network_standby of this Settings.


        :param network_standby: The network_standby of this Settings.
        :type network_standby: int
        """
        if network_standby is None:
            raise ValueError("Invalid value for `network_standby`, must not be `None`")

        self._network_standby = network_standby

    @property
    def system_sound_effects(self):
        """Gets the system_sound_effects of this Settings.


        :return: The system_sound_effects of this Settings.
        :rtype: bool
        """
        return self._system_sound_effects

    @system_sound_effects.setter
    def system_sound_effects(self, system_sound_effects):
        """Sets the system_sound_effects of this Settings.


        :param system_sound_effects: The system_sound_effects of this Settings.
        :type system_sound_effects: bool
        """
        if system_sound_effects is None:
            raise ValueError("Invalid value for `system_sound_effects`, must not be `None`")

        self._system_sound_effects = system_sound_effects

    @property
    def time_format(self):
        """Gets the time_format of this Settings.


        :return: The time_format of this Settings.
        :rtype: int
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this Settings.


        :param time_format: The time_format of this Settings.
        :type time_format: int
        """
        if time_format is None:
            raise ValueError("Invalid value for `time_format`, must not be `None`")

        self._time_format = time_format

    @property
    def timezone(self):
        """Gets the timezone of this Settings.


        :return: The timezone of this Settings.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Settings.


        :param timezone: The timezone of this Settings.
        :type timezone: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")

        self._timezone = timezone

    @property
    def wake_on_cast(self):
        """Gets the wake_on_cast of this Settings.


        :return: The wake_on_cast of this Settings.
        :rtype: int
        """
        return self._wake_on_cast

    @wake_on_cast.setter
    def wake_on_cast(self, wake_on_cast):
        """Sets the wake_on_cast of this Settings.


        :param wake_on_cast: The wake_on_cast of this Settings.
        :type wake_on_cast: int
        """
        if wake_on_cast is None:
            raise ValueError("Invalid value for `wake_on_cast`, must not be `None`")

        self._wake_on_cast = wake_on_cast
