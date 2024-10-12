# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TimeSettingsProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, primary_time_server: str=None, secondary_time_server: List[str]=None, time_zone: str=None):
        """TimeSettingsProperties - a model defined in OpenAPI

        :param primary_time_server: The primary_time_server of this TimeSettingsProperties.
        :param secondary_time_server: The secondary_time_server of this TimeSettingsProperties.
        :param time_zone: The time_zone of this TimeSettingsProperties.
        """
        self.openapi_types = {
            'primary_time_server': str,
            'secondary_time_server': List[str],
            'time_zone': str
        }

        self.attribute_map = {
            'primary_time_server': 'primaryTimeServer',
            'secondary_time_server': 'secondaryTimeServer',
            'time_zone': 'timeZone'
        }

        self._primary_time_server = primary_time_server
        self._secondary_time_server = secondary_time_server
        self._time_zone = time_zone

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TimeSettingsProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TimeSettingsProperties of this TimeSettingsProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def primary_time_server(self):
        """Gets the primary_time_server of this TimeSettingsProperties.

        The primary Network Time Protocol (NTP) server name, like 'time.windows.com'.

        :return: The primary_time_server of this TimeSettingsProperties.
        :rtype: str
        """
        return self._primary_time_server

    @primary_time_server.setter
    def primary_time_server(self, primary_time_server):
        """Sets the primary_time_server of this TimeSettingsProperties.

        The primary Network Time Protocol (NTP) server name, like 'time.windows.com'.

        :param primary_time_server: The primary_time_server of this TimeSettingsProperties.
        :type primary_time_server: str
        """

        self._primary_time_server = primary_time_server

    @property
    def secondary_time_server(self):
        """Gets the secondary_time_server of this TimeSettingsProperties.

        The secondary Network Time Protocol (NTP) server name, like 'time.contoso.com'. It's optional.

        :return: The secondary_time_server of this TimeSettingsProperties.
        :rtype: List[str]
        """
        return self._secondary_time_server

    @secondary_time_server.setter
    def secondary_time_server(self, secondary_time_server):
        """Sets the secondary_time_server of this TimeSettingsProperties.

        The secondary Network Time Protocol (NTP) server name, like 'time.contoso.com'. It's optional.

        :param secondary_time_server: The secondary_time_server of this TimeSettingsProperties.
        :type secondary_time_server: List[str]
        """

        self._secondary_time_server = secondary_time_server

    @property
    def time_zone(self):
        """Gets the time_zone of this TimeSettingsProperties.

        The timezone of device, like '(UTC -06:00) Central America'

        :return: The time_zone of this TimeSettingsProperties.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this TimeSettingsProperties.

        The timezone of device, like '(UTC -06:00) Central America'

        :param time_zone: The time_zone of this TimeSettingsProperties.
        :type time_zone: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")

        self._time_zone = time_zone
