# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CrashDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_start_timestamp: datetime=None, carrier_country: str=None, carrier_name: str=None, locale: str=None, os_build: str=None, rooted: bool=None, screen_size: str=None):
        """CrashDetails - a model defined in OpenAPI

        :param app_start_timestamp: The app_start_timestamp of this CrashDetails.
        :param carrier_country: The carrier_country of this CrashDetails.
        :param carrier_name: The carrier_name of this CrashDetails.
        :param locale: The locale of this CrashDetails.
        :param os_build: The os_build of this CrashDetails.
        :param rooted: The rooted of this CrashDetails.
        :param screen_size: The screen_size of this CrashDetails.
        """
        self.openapi_types = {
            'app_start_timestamp': datetime,
            'carrier_country': str,
            'carrier_name': str,
            'locale': str,
            'os_build': str,
            'rooted': bool,
            'screen_size': str
        }

        self.attribute_map = {
            'app_start_timestamp': 'app_start_timestamp',
            'carrier_country': 'carrier_country',
            'carrier_name': 'carrier_name',
            'locale': 'locale',
            'os_build': 'os_build',
            'rooted': 'rooted',
            'screen_size': 'screen_size'
        }

        self._app_start_timestamp = app_start_timestamp
        self._carrier_country = carrier_country
        self._carrier_name = carrier_name
        self._locale = locale
        self._os_build = os_build
        self._rooted = rooted
        self._screen_size = screen_size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Crash_details of this CrashDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_start_timestamp(self):
        """Gets the app_start_timestamp of this CrashDetails.

        Application launch timestamp (example: 1985-04-12T23:20:50.52Z). 

        :return: The app_start_timestamp of this CrashDetails.
        :rtype: datetime
        """
        return self._app_start_timestamp

    @app_start_timestamp.setter
    def app_start_timestamp(self, app_start_timestamp):
        """Sets the app_start_timestamp of this CrashDetails.

        Application launch timestamp (example: 1985-04-12T23:20:50.52Z). 

        :param app_start_timestamp: The app_start_timestamp of this CrashDetails.
        :type app_start_timestamp: datetime
        """

        self._app_start_timestamp = app_start_timestamp

    @property
    def carrier_country(self):
        """Gets the carrier_country of this CrashDetails.

        Carrier country code (for mobile devices). 

        :return: The carrier_country of this CrashDetails.
        :rtype: str
        """
        return self._carrier_country

    @carrier_country.setter
    def carrier_country(self, carrier_country):
        """Sets the carrier_country of this CrashDetails.

        Carrier country code (for mobile devices). 

        :param carrier_country: The carrier_country of this CrashDetails.
        :type carrier_country: str
        """

        self._carrier_country = carrier_country

    @property
    def carrier_name(self):
        """Gets the carrier_name of this CrashDetails.

        Carrier name (for mobile devices). 

        :return: The carrier_name of this CrashDetails.
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this CrashDetails.

        Carrier name (for mobile devices). 

        :param carrier_name: The carrier_name of this CrashDetails.
        :type carrier_name: str
        """

        self._carrier_name = carrier_name

    @property
    def locale(self):
        """Gets the locale of this CrashDetails.

        Language code (example: en_US). 

        :return: The locale of this CrashDetails.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CrashDetails.

        Language code (example: en_US). 

        :param locale: The locale of this CrashDetails.
        :type locale: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")

        self._locale = locale

    @property
    def os_build(self):
        """Gets the os_build of this CrashDetails.

        OS build code (example: LMY47X). 

        :return: The os_build of this CrashDetails.
        :rtype: str
        """
        return self._os_build

    @os_build.setter
    def os_build(self, os_build):
        """Sets the os_build of this CrashDetails.

        OS build code (example: LMY47X). 

        :param os_build: The os_build of this CrashDetails.
        :type os_build: str
        """

        self._os_build = os_build

    @property
    def rooted(self):
        """Gets the rooted of this CrashDetails.

        Whether the device where the crash occurred is rooted or jailbroken 

        :return: The rooted of this CrashDetails.
        :rtype: bool
        """
        return self._rooted

    @rooted.setter
    def rooted(self, rooted):
        """Sets the rooted of this CrashDetails.

        Whether the device where the crash occurred is rooted or jailbroken 

        :param rooted: The rooted of this CrashDetails.
        :type rooted: bool
        """
        if rooted is None:
            raise ValueError("Invalid value for `rooted`, must not be `None`")

        self._rooted = rooted

    @property
    def screen_size(self):
        """Gets the screen_size of this CrashDetails.

        Screen size of the device in pixels (example: 640x480). 

        :return: The screen_size of this CrashDetails.
        :rtype: str
        """
        return self._screen_size

    @screen_size.setter
    def screen_size(self, screen_size):
        """Sets the screen_size of this CrashDetails.

        Screen size of the device in pixels (example: 640x480). 

        :param screen_size: The screen_size of this CrashDetails.
        :type screen_size: str
        """
        if screen_size is None:
            raise ValueError("Invalid value for `screen_size`, must not be `None`")

        self._screen_size = screen_size
