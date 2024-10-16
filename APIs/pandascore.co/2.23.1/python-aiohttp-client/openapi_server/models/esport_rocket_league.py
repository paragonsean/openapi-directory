# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.betting_serie import BettingSerie
from openapi_server import util


class EsportRocketLeague(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_version: object=None, id: float=None, name: str=None, series: List[BettingSerie]=None, slug: str=None):
        """EsportRocketLeague - a model defined in OpenAPI

        :param current_version: The current_version of this EsportRocketLeague.
        :param id: The id of this EsportRocketLeague.
        :param name: The name of this EsportRocketLeague.
        :param series: The series of this EsportRocketLeague.
        :param slug: The slug of this EsportRocketLeague.
        """
        self.openapi_types = {
            'current_version': object,
            'id': float,
            'name': str,
            'series': List[BettingSerie],
            'slug': str
        }

        self.attribute_map = {
            'current_version': 'current_version',
            'id': 'id',
            'name': 'name',
            'series': 'series',
            'slug': 'slug'
        }

        self._current_version = current_version
        self._id = id
        self._name = name
        self._series = series
        self._slug = slug

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EsportRocketLeague':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Esport_RocketLeague of this EsportRocketLeague.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_version(self):
        """Gets the current_version of this EsportRocketLeague.


        :return: The current_version of this EsportRocketLeague.
        :rtype: object
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this EsportRocketLeague.


        :param current_version: The current_version of this EsportRocketLeague.
        :type current_version: object
        """
        if current_version is None:
            raise ValueError("Invalid value for `current_version`, must not be `None`")

        self._current_version = current_version

    @property
    def id(self):
        """Gets the id of this EsportRocketLeague.


        :return: The id of this EsportRocketLeague.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EsportRocketLeague.


        :param id: The id of this EsportRocketLeague.
        :type id: float
        """
        allowed_values = [22]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def name(self):
        """Gets the name of this EsportRocketLeague.


        :return: The name of this EsportRocketLeague.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EsportRocketLeague.


        :param name: The name of this EsportRocketLeague.
        :type name: str
        """
        allowed_values = ["Rocket League"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def series(self):
        """Gets the series of this EsportRocketLeague.


        :return: The series of this EsportRocketLeague.
        :rtype: List[BettingSerie]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this EsportRocketLeague.


        :param series: The series of this EsportRocketLeague.
        :type series: List[BettingSerie]
        """
        if series is None:
            raise ValueError("Invalid value for `series`, must not be `None`")

        self._series = series

    @property
    def slug(self):
        """Gets the slug of this EsportRocketLeague.


        :return: The slug of this EsportRocketLeague.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this EsportRocketLeague.


        :param slug: The slug of this EsportRocketLeague.
        :type slug: str
        """
        allowed_values = ["rl"]  # noqa: E501
        if slug not in allowed_values:
            raise ValueError(
                "Invalid value for `slug` ({0}), must be one of {1}"
                .format(slug, allowed_values)
            )

        self._slug = slug
