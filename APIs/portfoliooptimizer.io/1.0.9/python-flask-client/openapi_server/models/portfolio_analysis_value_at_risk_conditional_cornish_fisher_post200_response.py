from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post200_response_portfolios_inner import PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner
from openapi_server import util

from openapi_server.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post200_response_portfolios_inner import PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner  # noqa: E501

class PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolios=None):  # noqa: E501
        """PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response - a model defined in OpenAPI

        :param portfolios: The portfolios of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.  # noqa: E501
        :type portfolios: List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]
        """
        self.openapi_types = {
            'portfolios': List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]
        }

        self.attribute_map = {
            'portfolios': 'portfolios'
        }

        self._portfolios = portfolios

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_value_at_risk_conditional_cornish_fisher_post_200_response of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.  # noqa: E501
        :rtype: PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolios(self) -> List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]:
        """Gets the portfolios of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.


        :return: The portfolios of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.
        :rtype: List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios: List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]):
        """Sets the portfolios of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.


        :param portfolios: The portfolios of this PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response.
        :type portfolios: List[PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")  # noqa: E501
        if portfolios is not None and len(portfolios) < 1:
            raise ValueError("Invalid value for `portfolios`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._portfolios = portfolios
