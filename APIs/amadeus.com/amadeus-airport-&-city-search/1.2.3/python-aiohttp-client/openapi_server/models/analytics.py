# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.travelers import Travelers
from openapi_server import util


class Analytics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, travelers: Travelers=None):
        """Analytics - a model defined in OpenAPI

        :param travelers: The travelers of this Analytics.
        """
        self.openapi_types = {
            'travelers': Travelers
        }

        self.attribute_map = {
            'travelers': 'travelers'
        }

        self._travelers = travelers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Analytics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Analytics of this Analytics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def travelers(self):
        """Gets the travelers of this Analytics.


        :return: The travelers of this Analytics.
        :rtype: Travelers
        """
        return self._travelers

    @travelers.setter
    def travelers(self, travelers):
        """Sets the travelers of this Analytics.


        :param travelers: The travelers of this Analytics.
        :type travelers: Travelers
        """

        self._travelers = travelers
