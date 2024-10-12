# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EnvironmentModelHaljsonLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _self: str=None):
        """EnvironmentModelHaljsonLinks - a model defined in OpenAPI

        :param _self: The _self of this EnvironmentModelHaljsonLinks.
        """
        self.openapi_types = {
            '_self': str
        }

        self.attribute_map = {
            '_self': 'self'
        }

        self.__self = _self

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EnvironmentModelHaljsonLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EnvironmentModel_haljson__links of this EnvironmentModelHaljsonLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self):
        """Gets the _self of this EnvironmentModelHaljsonLinks.


        :return: The _self of this EnvironmentModelHaljsonLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this EnvironmentModelHaljsonLinks.


        :param _self: The _self of this EnvironmentModelHaljsonLinks.
        :type _self: str
        """

        self.__self = _self
