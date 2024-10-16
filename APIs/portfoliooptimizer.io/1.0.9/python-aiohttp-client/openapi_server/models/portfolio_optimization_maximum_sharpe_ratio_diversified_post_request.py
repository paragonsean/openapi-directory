# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_optimization_maximum_sharpe_ratio_diversified_post_request_constraints import PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints
from openapi_server import util


class PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: int=None, assets_covariance_matrix: List[List[float]]=None, assets_returns: List[float]=None, constraints: PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints=None, risk_free_rate: float=None):
        """PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest - a model defined in OpenAPI

        :param assets: The assets of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :param assets_returns: The assets_returns of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :param constraints: The constraints of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :param risk_free_rate: The risk_free_rate of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        """
        self.openapi_types = {
            'assets': int,
            'assets_covariance_matrix': List[List[float]],
            'assets_returns': List[float],
            'constraints': PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints,
            'risk_free_rate': float
        }

        self.attribute_map = {
            'assets': 'assets',
            'assets_covariance_matrix': 'assetsCovarianceMatrix',
            'assets_returns': 'assetsReturns',
            'constraints': 'constraints',
            'risk_free_rate': 'riskFreeRate'
        }

        self._assets = assets
        self._assets_covariance_matrix = assets_covariance_matrix
        self._assets_returns = assets_returns
        self._constraints = constraints
        self._risk_free_rate = risk_free_rate

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_optimization_maximum_sharpe_ratio_diversified_post_request of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        The number of assets

        :return: The assets of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        The number of assets

        :param assets: The assets of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and assets < 2:
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `2`")

        self._assets = assets

    @property
    def assets_covariance_matrix(self):
        """Gets the assets_covariance_matrix of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :return: The assets_covariance_matrix of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :rtype: List[List[float]]
        """
        return self._assets_covariance_matrix

    @assets_covariance_matrix.setter
    def assets_covariance_matrix(self, assets_covariance_matrix):
        """Sets the assets_covariance_matrix of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :type assets_covariance_matrix: List[List[float]]
        """
        if assets_covariance_matrix is None:
            raise ValueError("Invalid value for `assets_covariance_matrix`, must not be `None`")
        if assets_covariance_matrix is not None and len(assets_covariance_matrix) < 2:
            raise ValueError("Invalid value for `assets_covariance_matrix`, number of items must be greater than or equal to `2`")

        self._assets_covariance_matrix = assets_covariance_matrix

    @property
    def assets_returns(self):
        """Gets the assets_returns of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        assetsReturns[i] is the arithmetic return of asset i

        :return: The assets_returns of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :rtype: List[float]
        """
        return self._assets_returns

    @assets_returns.setter
    def assets_returns(self, assets_returns):
        """Sets the assets_returns of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        assetsReturns[i] is the arithmetic return of asset i

        :param assets_returns: The assets_returns of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :type assets_returns: List[float]
        """
        if assets_returns is None:
            raise ValueError("Invalid value for `assets_returns`, must not be `None`")
        if assets_returns is not None and len(assets_returns) < 1:
            raise ValueError("Invalid value for `assets_returns`, number of items must be greater than or equal to `1`")

        self._assets_returns = assets_returns

    @property
    def constraints(self):
        """Gets the constraints of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.


        :return: The constraints of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :rtype: PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.


        :param constraints: The constraints of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :type constraints: PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints
        """

        self._constraints = constraints

    @property
    def risk_free_rate(self):
        """Gets the risk_free_rate of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        The risk free rate

        :return: The risk_free_rate of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :rtype: float
        """
        return self._risk_free_rate

    @risk_free_rate.setter
    def risk_free_rate(self, risk_free_rate):
        """Sets the risk_free_rate of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.

        The risk free rate

        :param risk_free_rate: The risk_free_rate of this PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest.
        :type risk_free_rate: float
        """
        if risk_free_rate is None:
            raise ValueError("Invalid value for `risk_free_rate`, must not be `None`")

        self._risk_free_rate = risk_free_rate
