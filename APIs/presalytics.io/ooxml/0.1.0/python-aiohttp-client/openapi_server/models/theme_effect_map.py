# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ThemeEffectMap(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, intensity_id: int=None, theme_id: str=None):
        """ThemeEffectMap - a model defined in OpenAPI

        :param id: The id of this ThemeEffectMap.
        :param intensity_id: The intensity_id of this ThemeEffectMap.
        :param theme_id: The theme_id of this ThemeEffectMap.
        """
        self.openapi_types = {
            'id': str,
            'intensity_id': int,
            'theme_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'intensity_id': 'intensityId',
            'theme_id': 'themeId'
        }

        self._id = id
        self._intensity_id = intensity_id
        self._theme_id = theme_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ThemeEffectMap':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Theme.EffectMap of this ThemeEffectMap.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ThemeEffectMap.


        :return: The id of this ThemeEffectMap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeEffectMap.


        :param id: The id of this ThemeEffectMap.
        :type id: str
        """

        self._id = id

    @property
    def intensity_id(self):
        """Gets the intensity_id of this ThemeEffectMap.


        :return: The intensity_id of this ThemeEffectMap.
        :rtype: int
        """
        return self._intensity_id

    @intensity_id.setter
    def intensity_id(self, intensity_id):
        """Sets the intensity_id of this ThemeEffectMap.


        :param intensity_id: The intensity_id of this ThemeEffectMap.
        :type intensity_id: int
        """

        self._intensity_id = intensity_id

    @property
    def theme_id(self):
        """Gets the theme_id of this ThemeEffectMap.


        :return: The theme_id of this ThemeEffectMap.
        :rtype: str
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this ThemeEffectMap.


        :param theme_id: The theme_id of this ThemeEffectMap.
        :type theme_id: str
        """

        self._theme_id = theme_id
