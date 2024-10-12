# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Execute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, script: str=None):
        """Execute - a model defined in OpenAPI

        :param script: The script of this Execute.
        """
        self.openapi_types = {
            'script': str
        }

        self.attribute_map = {
            'script': 'script'
        }

        self._script = script

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Execute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The execute of this Execute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def script(self):
        """Gets the script of this Execute.

        The JavaScript snippet to run

        :return: The script of this Execute.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Execute.

        The JavaScript snippet to run

        :param script: The script of this Execute.
        :type script: str
        """

        self._script = script
