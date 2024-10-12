# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FrontendSettingsLanguageSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, name: str=None):
        """FrontendSettingsLanguageSource - a model defined in OpenAPI

        :param code: The code of this FrontendSettingsLanguageSource.
        :param name: The name of this FrontendSettingsLanguageSource.
        """
        self.openapi_types = {
            'code': str,
            'name': str
        }

        self.attribute_map = {
            'code': 'code',
            'name': 'name'
        }

        self._code = code
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FrontendSettingsLanguageSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The frontend_settings_language_source of this FrontendSettingsLanguageSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this FrontendSettingsLanguageSource.

        Language code

        :return: The code of this FrontendSettingsLanguageSource.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FrontendSettingsLanguageSource.

        Language code

        :param code: The code of this FrontendSettingsLanguageSource.
        :type code: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this FrontendSettingsLanguageSource.

        Human-readable language name (in English)

        :return: The name of this FrontendSettingsLanguageSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FrontendSettingsLanguageSource.

        Human-readable language name (in English)

        :param name: The name of this FrontendSettingsLanguageSource.
        :type name: str
        """

        self._name = name
