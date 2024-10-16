from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_drawdowns_post200_response_portfolios_inner import PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner
from openapi_server import util

from openapi_server.models.portfolio_analysis_drawdowns_post200_response_portfolios_inner import PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner  # noqa: E501

class PortfolioAnalysisDrawdownsPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolios=None):  # noqa: E501
        """PortfolioAnalysisDrawdownsPost200Response - a model defined in OpenAPI

        :param portfolios: The portfolios of this PortfolioAnalysisDrawdownsPost200Response.  # noqa: E501
        :type portfolios: List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]
        """
        self.openapi_types = {
            'portfolios': List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]
        }

        self.attribute_map = {
            'portfolios': 'portfolios'
        }

        self._portfolios = portfolios

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisDrawdownsPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_drawdowns_post_200_response of this PortfolioAnalysisDrawdownsPost200Response.  # noqa: E501
        :rtype: PortfolioAnalysisDrawdownsPost200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolios(self) -> List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]:
        """Gets the portfolios of this PortfolioAnalysisDrawdownsPost200Response.


        :return: The portfolios of this PortfolioAnalysisDrawdownsPost200Response.
        :rtype: List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios: List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]):
        """Sets the portfolios of this PortfolioAnalysisDrawdownsPost200Response.


        :param portfolios: The portfolios of this PortfolioAnalysisDrawdownsPost200Response.
        :type portfolios: List[PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")  # noqa: E501

        self._portfolios = portfolios
