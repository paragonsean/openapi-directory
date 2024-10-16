# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_contributions_return_post_request_portfolios_inner import PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner
from openapi_server import util


class PortfolioAnalysisContributionsRiskPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: int=None, assets_covariance_matrix: List[List[float]]=None, assets_groups: List[list[int]]=None, portfolios: List[PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner]=None):
        """PortfolioAnalysisContributionsRiskPostRequest - a model defined in OpenAPI

        :param assets: The assets of this PortfolioAnalysisContributionsRiskPostRequest.
        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioAnalysisContributionsRiskPostRequest.
        :param assets_groups: The assets_groups of this PortfolioAnalysisContributionsRiskPostRequest.
        :param portfolios: The portfolios of this PortfolioAnalysisContributionsRiskPostRequest.
        """
        self.openapi_types = {
            'assets': int,
            'assets_covariance_matrix': List[List[float]],
            'assets_groups': List[list[int]],
            'portfolios': List[PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner]
        }

        self.attribute_map = {
            'assets': 'assets',
            'assets_covariance_matrix': 'assetsCovarianceMatrix',
            'assets_groups': 'assetsGroups',
            'portfolios': 'portfolios'
        }

        self._assets = assets
        self._assets_covariance_matrix = assets_covariance_matrix
        self._assets_groups = assets_groups
        self._portfolios = portfolios

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioAnalysisContributionsRiskPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_analysis_contributions_risk_post_request of this PortfolioAnalysisContributionsRiskPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this PortfolioAnalysisContributionsRiskPostRequest.

        The number of assets

        :return: The assets of this PortfolioAnalysisContributionsRiskPostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this PortfolioAnalysisContributionsRiskPostRequest.

        The number of assets

        :param assets: The assets of this PortfolioAnalysisContributionsRiskPostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and assets < 1:
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `1`")

        self._assets = assets

    @property
    def assets_covariance_matrix(self):
        """Gets the assets_covariance_matrix of this PortfolioAnalysisContributionsRiskPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :return: The assets_covariance_matrix of this PortfolioAnalysisContributionsRiskPostRequest.
        :rtype: List[List[float]]
        """
        return self._assets_covariance_matrix

    @assets_covariance_matrix.setter
    def assets_covariance_matrix(self, assets_covariance_matrix):
        """Sets the assets_covariance_matrix of this PortfolioAnalysisContributionsRiskPostRequest.

        assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        :param assets_covariance_matrix: The assets_covariance_matrix of this PortfolioAnalysisContributionsRiskPostRequest.
        :type assets_covariance_matrix: List[List[float]]
        """
        if assets_covariance_matrix is None:
            raise ValueError("Invalid value for `assets_covariance_matrix`, must not be `None`")
        if assets_covariance_matrix is not None and len(assets_covariance_matrix) < 2:
            raise ValueError("Invalid value for `assets_covariance_matrix`, number of items must be greater than or equal to `2`")

        self._assets_covariance_matrix = assets_covariance_matrix

    @property
    def assets_groups(self):
        """Gets the assets_groups of this PortfolioAnalysisContributionsRiskPostRequest.


        :return: The assets_groups of this PortfolioAnalysisContributionsRiskPostRequest.
        :rtype: List[list[int]]
        """
        return self._assets_groups

    @assets_groups.setter
    def assets_groups(self, assets_groups):
        """Sets the assets_groups of this PortfolioAnalysisContributionsRiskPostRequest.


        :param assets_groups: The assets_groups of this PortfolioAnalysisContributionsRiskPostRequest.
        :type assets_groups: List[list[int]]
        """
        if assets_groups is not None and len(assets_groups) < 1:
            raise ValueError("Invalid value for `assets_groups`, number of items must be greater than or equal to `1`")

        self._assets_groups = assets_groups

    @property
    def portfolios(self):
        """Gets the portfolios of this PortfolioAnalysisContributionsRiskPostRequest.


        :return: The portfolios of this PortfolioAnalysisContributionsRiskPostRequest.
        :rtype: List[PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios):
        """Sets the portfolios of this PortfolioAnalysisContributionsRiskPostRequest.


        :param portfolios: The portfolios of this PortfolioAnalysisContributionsRiskPostRequest.
        :type portfolios: List[PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")
        if portfolios is not None and len(portfolios) < 1:
            raise ValueError("Invalid value for `portfolios`, number of items must be greater than or equal to `1`")

        self._portfolios = portfolios
