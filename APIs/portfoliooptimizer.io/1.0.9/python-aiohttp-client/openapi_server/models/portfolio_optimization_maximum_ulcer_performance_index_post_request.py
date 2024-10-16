# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_post_request_assets_inner import AssetsReturnsPostRequestAssetsInner
from openapi_server.models.portfolio_analysis_mean_variance_efficient_frontier_post_request_constraints import PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints
from openapi_server import util


class PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: List[AssetsReturnsPostRequestAssetsInner]=None, constraints: PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints=None, risk_free_rate: float=None):
        """PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest - a model defined in OpenAPI

        :param assets: The assets of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :param constraints: The constraints of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :param risk_free_rate: The risk_free_rate of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        """
        self.openapi_types = {
            'assets': List[AssetsReturnsPostRequestAssetsInner],
            'constraints': PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints,
            'risk_free_rate': float
        }

        self.attribute_map = {
            'assets': 'assets',
            'constraints': 'constraints',
            'risk_free_rate': 'riskFreeRate'
        }

        self._assets = assets
        self._constraints = constraints
        self._risk_free_rate = risk_free_rate

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_optimization_maximum_ulcer_performance_index_post_request of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.


        :return: The assets of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :rtype: List[AssetsReturnsPostRequestAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.


        :param assets: The assets of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :type assets: List[AssetsReturnsPostRequestAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and len(assets) < 1:
            raise ValueError("Invalid value for `assets`, number of items must be greater than or equal to `1`")

        self._assets = assets

    @property
    def constraints(self):
        """Gets the constraints of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.


        :return: The constraints of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :rtype: PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.


        :param constraints: The constraints of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :type constraints: PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints
        """

        self._constraints = constraints

    @property
    def risk_free_rate(self):
        """Gets the risk_free_rate of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.

        The risk free rate

        :return: The risk_free_rate of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :rtype: float
        """
        return self._risk_free_rate

    @risk_free_rate.setter
    def risk_free_rate(self, risk_free_rate):
        """Sets the risk_free_rate of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.

        The risk free rate

        :param risk_free_rate: The risk_free_rate of this PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest.
        :type risk_free_rate: float
        """
        if risk_free_rate is None:
            raise ValueError("Invalid value for `risk_free_rate`, must not be `None`")

        self._risk_free_rate = risk_free_rate
