# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.analytics_model_counts200_response_models_inner import AnalyticsModelCounts200ResponseModelsInner
from openapi_server import util


class AnalyticsModels(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, models: List[AnalyticsModelCounts200ResponseModelsInner]=None, total: int=None):
        """AnalyticsModels - a model defined in OpenAPI

        :param models: The models of this AnalyticsModels.
        :param total: The total of this AnalyticsModels.
        """
        self.openapi_types = {
            'models': List[AnalyticsModelCounts200ResponseModelsInner],
            'total': int
        }

        self.attribute_map = {
            'models': 'models',
            'total': 'total'
        }

        self._models = models
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AnalyticsModels':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AnalyticsModels of this AnalyticsModels.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def models(self):
        """Gets the models of this AnalyticsModels.


        :return: The models of this AnalyticsModels.
        :rtype: List[AnalyticsModelCounts200ResponseModelsInner]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this AnalyticsModels.


        :param models: The models of this AnalyticsModels.
        :type models: List[AnalyticsModelCounts200ResponseModelsInner]
        """

        self._models = models

    @property
    def total(self):
        """Gets the total of this AnalyticsModels.


        :return: The total of this AnalyticsModels.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AnalyticsModels.


        :param total: The total of this AnalyticsModels.
        :type total: int
        """

        self._total = total
