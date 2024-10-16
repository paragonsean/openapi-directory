from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolio_sharpe_ratio=None):  # noqa: E501
        """PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner - a model defined in OpenAPI

        :param portfolio_sharpe_ratio: The portfolio_sharpe_ratio of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.  # noqa: E501
        :type portfolio_sharpe_ratio: float
        """
        self.openapi_types = {
            'portfolio_sharpe_ratio': float
        }

        self.attribute_map = {
            'portfolio_sharpe_ratio': 'portfolioSharpeRatio'
        }

        self._portfolio_sharpe_ratio = portfolio_sharpe_ratio

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_sharpe_ratio_post_200_response_portfolios_inner of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.  # noqa: E501
        :rtype: PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolio_sharpe_ratio(self) -> float:
        """Gets the portfolio_sharpe_ratio of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.

        The Sharpe ratio of the portfolio  # noqa: E501

        :return: The portfolio_sharpe_ratio of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.
        :rtype: float
        """
        return self._portfolio_sharpe_ratio

    @portfolio_sharpe_ratio.setter
    def portfolio_sharpe_ratio(self, portfolio_sharpe_ratio: float):
        """Sets the portfolio_sharpe_ratio of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.

        The Sharpe ratio of the portfolio  # noqa: E501

        :param portfolio_sharpe_ratio: The portfolio_sharpe_ratio of this PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner.
        :type portfolio_sharpe_ratio: float
        """
        if portfolio_sharpe_ratio is None:
            raise ValueError("Invalid value for `portfolio_sharpe_ratio`, must not be `None`")  # noqa: E501

        self._portfolio_sharpe_ratio = portfolio_sharpe_ratio
