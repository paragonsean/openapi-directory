from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_return_post_request_one_of import PortfolioAnalysisReturnPostRequestOneOf
from openapi_server.models.portfolio_analysis_return_post_request_one_of1 import PortfolioAnalysisReturnPostRequestOneOf1
from openapi_server.models.portfolio_analysis_return_post_request_one_of1_portfolios_inner import PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner
from openapi_server import util

from openapi_server.models.portfolio_analysis_return_post_request_one_of import PortfolioAnalysisReturnPostRequestOneOf  # noqa: E501
from openapi_server.models.portfolio_analysis_return_post_request_one_of1 import PortfolioAnalysisReturnPostRequestOneOf1  # noqa: E501
from openapi_server.models.portfolio_analysis_return_post_request_one_of1_portfolios_inner import PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner  # noqa: E501

class PortfolioAnalysisReturnPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets=None, assets_returns=None, portfolios=None):  # noqa: E501
        """PortfolioAnalysisReturnPostRequest - a model defined in OpenAPI

        :param assets: The assets of this PortfolioAnalysisReturnPostRequest.  # noqa: E501
        :type assets: int
        :param assets_returns: The assets_returns of this PortfolioAnalysisReturnPostRequest.  # noqa: E501
        :type assets_returns: List[float]
        :param portfolios: The portfolios of this PortfolioAnalysisReturnPostRequest.  # noqa: E501
        :type portfolios: List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]
        """
        self.openapi_types = {
            'assets': int,
            'assets_returns': List[float],
            'portfolios': List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]
        }

        self.attribute_map = {
            'assets': 'assets',
            'assets_returns': 'assetsReturns',
            'portfolios': 'portfolios'
        }

        self._assets = assets
        self._assets_returns = assets_returns
        self._portfolios = portfolios

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisReturnPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_return_post_request of this PortfolioAnalysisReturnPostRequest.  # noqa: E501
        :rtype: PortfolioAnalysisReturnPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self) -> int:
        """Gets the assets of this PortfolioAnalysisReturnPostRequest.

        The number of assets  # noqa: E501

        :return: The assets of this PortfolioAnalysisReturnPostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets: int):
        """Sets the assets of this PortfolioAnalysisReturnPostRequest.

        The number of assets  # noqa: E501

        :param assets: The assets of this PortfolioAnalysisReturnPostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501
        if assets is not None and assets < 1:  # noqa: E501
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `1`")  # noqa: E501

        self._assets = assets

    @property
    def assets_returns(self) -> List[float]:
        """Gets the assets_returns of this PortfolioAnalysisReturnPostRequest.

        assetsReturns[i] is the arithmetic return of asset i  # noqa: E501

        :return: The assets_returns of this PortfolioAnalysisReturnPostRequest.
        :rtype: List[float]
        """
        return self._assets_returns

    @assets_returns.setter
    def assets_returns(self, assets_returns: List[float]):
        """Sets the assets_returns of this PortfolioAnalysisReturnPostRequest.

        assetsReturns[i] is the arithmetic return of asset i  # noqa: E501

        :param assets_returns: The assets_returns of this PortfolioAnalysisReturnPostRequest.
        :type assets_returns: List[float]
        """
        if assets_returns is None:
            raise ValueError("Invalid value for `assets_returns`, must not be `None`")  # noqa: E501
        if assets_returns is not None and len(assets_returns) < 1:
            raise ValueError("Invalid value for `assets_returns`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._assets_returns = assets_returns

    @property
    def portfolios(self) -> List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]:
        """Gets the portfolios of this PortfolioAnalysisReturnPostRequest.


        :return: The portfolios of this PortfolioAnalysisReturnPostRequest.
        :rtype: List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios: List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]):
        """Sets the portfolios of this PortfolioAnalysisReturnPostRequest.


        :param portfolios: The portfolios of this PortfolioAnalysisReturnPostRequest.
        :type portfolios: List[PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")  # noqa: E501
        if portfolios is not None and len(portfolios) < 1:
            raise ValueError("Invalid value for `portfolios`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._portfolios = portfolios
