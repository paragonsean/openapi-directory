# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildTaskFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alias: str=None):
        """BuildTaskFilter - a model defined in OpenAPI

        :param alias: The alias of this BuildTaskFilter.
        """
        self.openapi_types = {
            'alias': str
        }

        self.attribute_map = {
            'alias': 'alias'
        }

        self._alias = alias

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildTaskFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildTaskFilter of this BuildTaskFilter.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alias(self):
        """Gets the alias of this BuildTaskFilter.

        The alternative name for build task.

        :return: The alias of this BuildTaskFilter.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this BuildTaskFilter.

        The alternative name for build task.

        :param alias: The alias of this BuildTaskFilter.
        :type alias: str
        """

        self._alias = alias
