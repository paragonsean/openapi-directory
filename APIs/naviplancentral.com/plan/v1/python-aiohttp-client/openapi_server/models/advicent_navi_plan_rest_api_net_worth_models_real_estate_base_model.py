# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.advicent_navi_plan_rest_api_net_worth_models_real_estate_model import AdvicentNaviPlanRestApiNetWorthModelsRealEstateModel
from openapi_server import util


class AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, real_estate_assets: List[AdvicentNaviPlanRestApiNetWorthModelsRealEstateModel]=None):
        """AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel - a model defined in OpenAPI

        :param real_estate_assets: The real_estate_assets of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.
        """
        self.openapi_types = {
            'real_estate_assets': List[AdvicentNaviPlanRestApiNetWorthModelsRealEstateModel]
        }

        self.attribute_map = {
            'real_estate_assets': 'realEstateAssets'
        }

        self._real_estate_assets = real_estate_assets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def real_estate_assets(self):
        """Gets the real_estate_assets of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.


        :return: The real_estate_assets of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.
        :rtype: List[AdvicentNaviPlanRestApiNetWorthModelsRealEstateModel]
        """
        return self._real_estate_assets

    @real_estate_assets.setter
    def real_estate_assets(self, real_estate_assets):
        """Sets the real_estate_assets of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.


        :param real_estate_assets: The real_estate_assets of this AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.
        :type real_estate_assets: List[AdvicentNaviPlanRestApiNetWorthModelsRealEstateModel]
        """

        self._real_estate_assets = real_estate_assets
