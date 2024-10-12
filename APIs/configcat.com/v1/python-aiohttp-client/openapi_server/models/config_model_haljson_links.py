# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConfigModelHaljsonLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _self: str=None, settings: str=None):
        """ConfigModelHaljsonLinks - a model defined in OpenAPI

        :param _self: The _self of this ConfigModelHaljsonLinks.
        :param settings: The settings of this ConfigModelHaljsonLinks.
        """
        self.openapi_types = {
            '_self': str,
            'settings': str
        }

        self.attribute_map = {
            '_self': 'self',
            'settings': 'settings'
        }

        self.__self = _self
        self._settings = settings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigModelHaljsonLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConfigModel_haljson__links of this ConfigModelHaljsonLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self):
        """Gets the _self of this ConfigModelHaljsonLinks.


        :return: The _self of this ConfigModelHaljsonLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ConfigModelHaljsonLinks.


        :param _self: The _self of this ConfigModelHaljsonLinks.
        :type _self: str
        """

        self.__self = _self

    @property
    def settings(self):
        """Gets the settings of this ConfigModelHaljsonLinks.


        :return: The settings of this ConfigModelHaljsonLinks.
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ConfigModelHaljsonLinks.


        :param settings: The settings of this ConfigModelHaljsonLinks.
        :type settings: str
        """

        self._settings = settings
