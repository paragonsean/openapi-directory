# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AutoRedirectConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None):
        """AutoRedirectConfig - a model defined in OpenAPI

        :param enabled: The enabled of this AutoRedirectConfig.
        """
        self.openapi_types = {
            'enabled': bool
        }

        self.attribute_map = {
            'enabled': 'enabled'
        }

        self._enabled = enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AutoRedirectConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AutoRedirectConfig of this AutoRedirectConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this AutoRedirectConfig.

        Enabled

        :return: The enabled of this AutoRedirectConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AutoRedirectConfig.

        Enabled

        :param enabled: The enabled of this AutoRedirectConfig.
        :type enabled: bool
        """

        self._enabled = enabled
