# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PortfolioAnalysisReturnPost200ResponsePortfoliosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolio_return: float=None):
        """PortfolioAnalysisReturnPost200ResponsePortfoliosInner - a model defined in OpenAPI

        :param portfolio_return: The portfolio_return of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.
        """
        self.openapi_types = {
            'portfolio_return': float
        }

        self.attribute_map = {
            'portfolio_return': 'portfolioReturn'
        }

        self._portfolio_return = portfolio_return

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioAnalysisReturnPost200ResponsePortfoliosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_analysis_return_post_200_response_portfolios_inner of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolio_return(self):
        """Gets the portfolio_return of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.

        The arithmetic return of the portfolio

        :return: The portfolio_return of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.
        :rtype: float
        """
        return self._portfolio_return

    @portfolio_return.setter
    def portfolio_return(self, portfolio_return):
        """Sets the portfolio_return of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.

        The arithmetic return of the portfolio

        :param portfolio_return: The portfolio_return of this PortfolioAnalysisReturnPost200ResponsePortfoliosInner.
        :type portfolio_return: float
        """
        if portfolio_return is None:
            raise ValueError("Invalid value for `portfolio_return`, must not be `None`")

        self._portfolio_return = portfolio_return
