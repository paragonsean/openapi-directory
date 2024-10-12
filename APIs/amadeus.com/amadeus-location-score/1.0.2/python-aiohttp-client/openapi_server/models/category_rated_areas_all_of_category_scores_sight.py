# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CategoryRatedAreasAllOfCategoryScoresSight(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, beach_and_park: int=None, historical: int=None, overall: int=None):
        """CategoryRatedAreasAllOfCategoryScoresSight - a model defined in OpenAPI

        :param beach_and_park: The beach_and_park of this CategoryRatedAreasAllOfCategoryScoresSight.
        :param historical: The historical of this CategoryRatedAreasAllOfCategoryScoresSight.
        :param overall: The overall of this CategoryRatedAreasAllOfCategoryScoresSight.
        """
        self.openapi_types = {
            'beach_and_park': int,
            'historical': int,
            'overall': int
        }

        self.attribute_map = {
            'beach_and_park': 'beachAndPark',
            'historical': 'historical',
            'overall': 'overall'
        }

        self._beach_and_park = beach_and_park
        self._historical = historical
        self._overall = overall

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CategoryRatedAreasAllOfCategoryScoresSight':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The category_rated_areas_allOf_categoryScores_sight of this CategoryRatedAreasAllOfCategoryScoresSight.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def beach_and_park(self):
        """Gets the beach_and_park of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of outdoor activity possibility from 0 (no outdoor spaces) to 100 (many parks or beaches to enjoy)

        :return: The beach_and_park of this CategoryRatedAreasAllOfCategoryScoresSight.
        :rtype: int
        """
        return self._beach_and_park

    @beach_and_park.setter
    def beach_and_park(self, beach_and_park):
        """Sets the beach_and_park of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of outdoor activity possibility from 0 (no outdoor spaces) to 100 (many parks or beaches to enjoy)

        :param beach_and_park: The beach_and_park of this CategoryRatedAreasAllOfCategoryScoresSight.
        :type beach_and_park: int
        """

        self._beach_and_park = beach_and_park

    @property
    def historical(self):
        """Gets the historical of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of historical discovery possibility from 0 (no historical site) to 100 (many historical site to enjoy)

        :return: The historical of this CategoryRatedAreasAllOfCategoryScoresSight.
        :rtype: int
        """
        return self._historical

    @historical.setter
    def historical(self, historical):
        """Sets the historical of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of historical discovery possibility from 0 (no historical site) to 100 (many historical site to enjoy)

        :param historical: The historical of this CategoryRatedAreasAllOfCategoryScoresSight.
        :type historical: int
        """

        self._historical = historical

    @property
    def overall(self):
        """Gets the overall of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of sight seeing possibility from 0 (nothing to see) to 100 (many sceneries to enjoy)

        :return: The overall of this CategoryRatedAreasAllOfCategoryScoresSight.
        :rtype: int
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this CategoryRatedAreasAllOfCategoryScoresSight.

        score of sight seeing possibility from 0 (nothing to see) to 100 (many sceneries to enjoy)

        :param overall: The overall of this CategoryRatedAreasAllOfCategoryScoresSight.
        :type overall: int
        """

        self._overall = overall
