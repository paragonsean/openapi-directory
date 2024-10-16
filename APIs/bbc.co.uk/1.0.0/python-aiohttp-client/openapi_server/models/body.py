# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Body(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category_id: str=None, platform: str=None):
        """Body - a model defined in OpenAPI

        :param category_id: The category_id of this Body.
        :param platform: The platform of this Body.
        """
        self.openapi_types = {
            'category_id': str,
            'platform': str
        }

        self.attribute_map = {
            'category_id': 'category_id',
            'platform': 'platform'
        }

        self._category_id = category_id
        self._platform = platform

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Body of this Body.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category_id(self):
        """Gets the category_id of this Body.


        :return: The category_id of this Body.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Body.


        :param category_id: The category_id of this Body.
        :type category_id: str
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")

        self._category_id = category_id

    @property
    def platform(self):
        """Gets the platform of this Body.


        :return: The platform of this Body.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Body.


        :param platform: The platform of this Body.
        :type platform: str
        """
        allowed_values = ["responsiveweb", "app"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"
                .format(platform, allowed_values)
            )

        self._platform = platform
