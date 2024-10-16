# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.active_crashing_app_details_apps_with_crashes_inner import ActiveCrashingAppDetailsAppsWithCrashesInner
from openapi_server import util


class ActiveCrashingAppDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, apps_with_crashes: List[ActiveCrashingAppDetailsAppsWithCrashesInner]=None, next_link: str=None):
        """ActiveCrashingAppDetails - a model defined in OpenAPI

        :param apps_with_crashes: The apps_with_crashes of this ActiveCrashingAppDetails.
        :param next_link: The next_link of this ActiveCrashingAppDetails.
        """
        self.openapi_types = {
            'apps_with_crashes': List[ActiveCrashingAppDetailsAppsWithCrashesInner],
            'next_link': str
        }

        self.attribute_map = {
            'apps_with_crashes': 'appsWithCrashes',
            'next_link': 'nextLink'
        }

        self._apps_with_crashes = apps_with_crashes
        self._next_link = next_link

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ActiveCrashingAppDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ActiveCrashingAppDetails of this ActiveCrashingAppDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def apps_with_crashes(self):
        """Gets the apps_with_crashes of this ActiveCrashingAppDetails.

        details of the apps with crashes

        :return: The apps_with_crashes of this ActiveCrashingAppDetails.
        :rtype: List[ActiveCrashingAppDetailsAppsWithCrashesInner]
        """
        return self._apps_with_crashes

    @apps_with_crashes.setter
    def apps_with_crashes(self, apps_with_crashes):
        """Sets the apps_with_crashes of this ActiveCrashingAppDetails.

        details of the apps with crashes

        :param apps_with_crashes: The apps_with_crashes of this ActiveCrashingAppDetails.
        :type apps_with_crashes: List[ActiveCrashingAppDetailsAppsWithCrashesInner]
        """

        self._apps_with_crashes = apps_with_crashes

    @property
    def next_link(self):
        """Gets the next_link of this ActiveCrashingAppDetails.


        :return: The next_link of this ActiveCrashingAppDetails.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ActiveCrashingAppDetails.


        :param next_link: The next_link of this ActiveCrashingAppDetails.
        :type next_link: str
        """

        self._next_link = next_link
