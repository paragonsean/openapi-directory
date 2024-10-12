# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class HealthProfileResourceLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _self: str=None):
        """HealthProfileResourceLinks - a model defined in OpenAPI

        :param _self: The _self of this HealthProfileResourceLinks.
        """
        self.openapi_types = {
            '_self': str
        }

        self.attribute_map = {
            '_self': 'self'
        }

        self.__self = _self

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HealthProfileResourceLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthProfileResource_links of this HealthProfileResourceLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self):
        """Gets the _self of this HealthProfileResourceLinks.


        :return: The _self of this HealthProfileResourceLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this HealthProfileResourceLinks.


        :param _self: The _self of this HealthProfileResourceLinks.
        :type _self: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")
        if _self is not None and not re.search(r'health_profile', _self):
            raise ValueError("Invalid value for `_self`, must be a follow pattern or equal to `/health_profile/[0-9a-z]+`")

        self.__self = _self
