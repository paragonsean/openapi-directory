# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.point_info_lsoa_population import PointInfoLsoaPopulation
from openapi_server import util


class PointInfoLsoa(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, crimes: object=None, name: str=None, population: PointInfoLsoaPopulation=None):
        """PointInfoLsoa - a model defined in OpenAPI

        :param crimes: The crimes of this PointInfoLsoa.
        :param name: The name of this PointInfoLsoa.
        :param population: The population of this PointInfoLsoa.
        """
        self.openapi_types = {
            'crimes': object,
            'name': str,
            'population': PointInfoLsoaPopulation
        }

        self.attribute_map = {
            'crimes': 'crimes',
            'name': 'name',
            'population': 'population'
        }

        self._crimes = crimes
        self._name = name
        self._population = population

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PointInfoLsoa':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PointInfo_lsoa of this PointInfoLsoa.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def crimes(self):
        """Gets the crimes of this PointInfoLsoa.


        :return: The crimes of this PointInfoLsoa.
        :rtype: object
        """
        return self._crimes

    @crimes.setter
    def crimes(self, crimes):
        """Sets the crimes of this PointInfoLsoa.


        :param crimes: The crimes of this PointInfoLsoa.
        :type crimes: object
        """

        self._crimes = crimes

    @property
    def name(self):
        """Gets the name of this PointInfoLsoa.


        :return: The name of this PointInfoLsoa.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PointInfoLsoa.


        :param name: The name of this PointInfoLsoa.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def population(self):
        """Gets the population of this PointInfoLsoa.


        :return: The population of this PointInfoLsoa.
        :rtype: PointInfoLsoaPopulation
        """
        return self._population

    @population.setter
    def population(self, population):
        """Sets the population of this PointInfoLsoa.


        :param population: The population of this PointInfoLsoa.
        :type population: PointInfoLsoaPopulation
        """

        self._population = population
