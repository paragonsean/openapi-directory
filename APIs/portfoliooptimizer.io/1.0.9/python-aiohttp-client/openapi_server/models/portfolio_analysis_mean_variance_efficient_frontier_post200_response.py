# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_mean_variance_efficient_frontier_post200_response_portfolios_inner import PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner
from openapi_server import util


class PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolios: List[PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner]=None):
        """PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response - a model defined in OpenAPI

        :param portfolios: The portfolios of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.
        """
        self.openapi_types = {
            'portfolios': List[PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner]
        }

        self.attribute_map = {
            'portfolios': 'portfolios'
        }

        self._portfolios = portfolios

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_analysis_mean_variance_efficient_frontier_post_200_response of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolios(self):
        """Gets the portfolios of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.


        :return: The portfolios of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.
        :rtype: List[PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios):
        """Sets the portfolios of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.


        :param portfolios: The portfolios of this PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response.
        :type portfolios: List[PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")
        if portfolios is not None and len(portfolios) < 1:
            raise ValueError("Invalid value for `portfolios`, number of items must be greater than or equal to `1`")

        self._portfolios = portfolios
