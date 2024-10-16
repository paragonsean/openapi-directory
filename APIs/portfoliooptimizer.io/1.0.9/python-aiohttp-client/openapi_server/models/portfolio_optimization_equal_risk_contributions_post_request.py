# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_optimization_equal_risk_contributions_post_request_constraints import PortfolioOptimizationEqualRiskContributionsPostRequestConstraints
from openapi_server import util


class PortfolioOptimizationEqualRiskContributionsPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: int=None, assets_covariance_matrix: List[List[float]]=None, constraints: PortfolioOptimizationEqualRiskContributionsPostRequestConstraints=None):
        """PortfolioOptimizationEqualRiskContributionsPostRequest - a model defined in OpenAPI

        :param assets: The assets of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :param constraints: The constraints of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        """
        self.openapi_types = {
            'assets': int,
            'assets_covariance_matrix': List[List[float]],
            'constraints': PortfolioOptimizationEqualRiskContributionsPostRequestConstraints
        }

        self.attribute_map = {
            'assets': 'assets',
            'assets_covariance_matrix': 'assetsCovarianceMatrix',
            'constraints': 'constraints'
        }

        self._assets = assets
        self._assets_covariance_matrix = assets_covariance_matrix
        self._constraints = constraints

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioOptimizationEqualRiskContributionsPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_optimization_equal_risk_contributions_post_request of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this PortfolioOptimizationEqualRiskContributionsPostRequest.

        The number of assets

        :return: The assets of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this PortfolioOptimizationEqualRiskContributionsPostRequest.

        The number of assets

        :param assets: The assets of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and assets < 2:
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `2`")

        self._assets = assets

    @property
    def assets_covariance_matrix(self):
        """Gets the assets_covariance_matrix of this PortfolioOptimizationEqualRiskContributionsPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :return: The assets_covariance_matrix of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :rtype: List[List[float]]
        """
        return self._assets_covariance_matrix

    @assets_covariance_matrix.setter
    def assets_covariance_matrix(self, assets_covariance_matrix):
        """Sets the assets_covariance_matrix of this PortfolioOptimizationEqualRiskContributionsPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :type assets_covariance_matrix: List[List[float]]
        """
        if assets_covariance_matrix is None:
            raise ValueError("Invalid value for `assets_covariance_matrix`, must not be `None`")
        if assets_covariance_matrix is not None and len(assets_covariance_matrix) < 2:
            raise ValueError("Invalid value for `assets_covariance_matrix`, number of items must be greater than or equal to `2`")

        self._assets_covariance_matrix = assets_covariance_matrix

    @property
    def constraints(self):
        """Gets the constraints of this PortfolioOptimizationEqualRiskContributionsPostRequest.


        :return: The constraints of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :rtype: PortfolioOptimizationEqualRiskContributionsPostRequestConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this PortfolioOptimizationEqualRiskContributionsPostRequest.


        :param constraints: The constraints of this PortfolioOptimizationEqualRiskContributionsPostRequest.
        :type constraints: PortfolioOptimizationEqualRiskContributionsPostRequestConstraints
        """

        self._constraints = constraints
