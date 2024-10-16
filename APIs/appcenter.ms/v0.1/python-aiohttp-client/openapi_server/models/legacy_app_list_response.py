# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.legacy_app_list_response_apps_inner import LegacyAppListResponseAppsInner
from openapi_server import util


class LegacyAppListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, apps: List[LegacyAppListResponseAppsInner]=None):
        """LegacyAppListResponse - a model defined in OpenAPI

        :param apps: The apps of this LegacyAppListResponse.
        """
        self.openapi_types = {
            'apps': List[LegacyAppListResponseAppsInner]
        }

        self.attribute_map = {
            'apps': 'apps'
        }

        self._apps = apps

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegacyAppListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LegacyAppListResponse of this LegacyAppListResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def apps(self):
        """Gets the apps of this LegacyAppListResponse.


        :return: The apps of this LegacyAppListResponse.
        :rtype: List[LegacyAppListResponseAppsInner]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this LegacyAppListResponse.


        :param apps: The apps of this LegacyAppListResponse.
        :type apps: List[LegacyAppListResponseAppsInner]
        """

        self._apps = apps
