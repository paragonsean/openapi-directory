# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolio_value_at_risk: float=None):
        """PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner - a model defined in OpenAPI

        :param portfolio_value_at_risk: The portfolio_value_at_risk of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.
        """
        self.openapi_types = {
            'portfolio_value_at_risk': float
        }

        self.attribute_map = {
            'portfolio_value_at_risk': 'portfolioValueAtRisk'
        }

        self._portfolio_value_at_risk = portfolio_value_at_risk

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _portfolio_analysis_value_at_risk_cornish_fisher_post_200_response_portfolios_inner of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolio_value_at_risk(self):
        """Gets the portfolio_value_at_risk of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.

        The value at risk of the portfolio

        :return: The portfolio_value_at_risk of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.
        :rtype: float
        """
        return self._portfolio_value_at_risk

    @portfolio_value_at_risk.setter
    def portfolio_value_at_risk(self, portfolio_value_at_risk):
        """Sets the portfolio_value_at_risk of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.

        The value at risk of the portfolio

        :param portfolio_value_at_risk: The portfolio_value_at_risk of this PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner.
        :type portfolio_value_at_risk: float
        """
        if portfolio_value_at_risk is None:
            raise ValueError("Invalid value for `portfolio_value_at_risk`, must not be `None`")

        self._portfolio_value_at_risk = portfolio_value_at_risk
