# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PointPointDailyMorningPrecipitationData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total: float=None, type: file=None):
        """PointPointDailyMorningPrecipitationData - a model defined in OpenAPI

        :param total: The total of this PointPointDailyMorningPrecipitationData.
        :param type: The type of this PointPointDailyMorningPrecipitationData.
        """
        self.openapi_types = {
            'total': float,
            'type': file
        }

        self.attribute_map = {
            'total': 'total',
            'type': 'type'
        }

        self._total = total
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PointPointDailyMorningPrecipitationData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Point_PointDailyMorningPrecipitationData of this PointPointDailyMorningPrecipitationData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self):
        """Gets the total of this PointPointDailyMorningPrecipitationData.

        Total precipitation amount accumulated since last hour. (morning sum) Units: metric = mm/h, us = inches per hour, uk = mm/h, ca = mm/h

        :return: The total of this PointPointDailyMorningPrecipitationData.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PointPointDailyMorningPrecipitationData.

        Total precipitation amount accumulated since last hour. (morning sum) Units: metric = mm/h, us = inches per hour, uk = mm/h, ca = mm/h

        :param total: The total of this PointPointDailyMorningPrecipitationData.
        :type total: float
        """

        self._total = total

    @property
    def type(self):
        """Gets the type of this PointPointDailyMorningPrecipitationData.

        Precipitation type, may be one of:  * `none`, it there is no precipitation * `rain` * `snow` * `rain_snow` * `ice pellets` * `frozen rain`  Unit: precipitation type

        :return: The type of this PointPointDailyMorningPrecipitationData.
        :rtype: file
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PointPointDailyMorningPrecipitationData.

        Precipitation type, may be one of:  * `none`, it there is no precipitation * `rain` * `snow` * `rain_snow` * `ice pellets` * `frozen rain`  Unit: precipitation type

        :param type: The type of this PointPointDailyMorningPrecipitationData.
        :type type: file
        """

        self._type = type
