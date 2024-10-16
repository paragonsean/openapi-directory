from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolio_volatility=None):  # noqa: E501
        """PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner - a model defined in OpenAPI

        :param portfolio_volatility: The portfolio_volatility of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.  # noqa: E501
        :type portfolio_volatility: float
        """
        self.openapi_types = {
            'portfolio_volatility': float
        }

        self.attribute_map = {
            'portfolio_volatility': 'portfolioVolatility'
        }

        self._portfolio_volatility = portfolio_volatility

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_volatility_post_200_response_portfolios_inner of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.  # noqa: E501
        :rtype: PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolio_volatility(self) -> float:
        """Gets the portfolio_volatility of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.

        The volatility of the portfolio  # noqa: E501

        :return: The portfolio_volatility of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.
        :rtype: float
        """
        return self._portfolio_volatility

    @portfolio_volatility.setter
    def portfolio_volatility(self, portfolio_volatility: float):
        """Sets the portfolio_volatility of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.

        The volatility of the portfolio  # noqa: E501

        :param portfolio_volatility: The portfolio_volatility of this PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner.
        :type portfolio_volatility: float
        """
        if portfolio_volatility is None:
            raise ValueError("Invalid value for `portfolio_volatility`, must not be `None`")  # noqa: E501
        if portfolio_volatility is not None and portfolio_volatility < 0:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_volatility`, must be a value greater than or equal to `0`")  # noqa: E501

        self._portfolio_volatility = portfolio_volatility
