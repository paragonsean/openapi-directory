from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, portfolio_correlation_spectrum=None):  # noqa: E501
        """PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner - a model defined in OpenAPI

        :param portfolio_correlation_spectrum: The portfolio_correlation_spectrum of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.  # noqa: E501
        :type portfolio_correlation_spectrum: List[float]
        """
        self.openapi_types = {
            'portfolio_correlation_spectrum': List[float]
        }

        self.attribute_map = {
            'portfolio_correlation_spectrum': 'portfolioCorrelationSpectrum'
        }

        self._portfolio_correlation_spectrum = portfolio_correlation_spectrum

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_correlation_spectrum_post_200_response_portfolios_inner of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.  # noqa: E501
        :rtype: PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def portfolio_correlation_spectrum(self) -> List[float]:
        """Gets the portfolio_correlation_spectrum of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.

        The correlation spectrum of the portfolio  # noqa: E501

        :return: The portfolio_correlation_spectrum of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.
        :rtype: List[float]
        """
        return self._portfolio_correlation_spectrum

    @portfolio_correlation_spectrum.setter
    def portfolio_correlation_spectrum(self, portfolio_correlation_spectrum: List[float]):
        """Sets the portfolio_correlation_spectrum of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.

        The correlation spectrum of the portfolio  # noqa: E501

        :param portfolio_correlation_spectrum: The portfolio_correlation_spectrum of this PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner.
        :type portfolio_correlation_spectrum: List[float]
        """
        if portfolio_correlation_spectrum is None:
            raise ValueError("Invalid value for `portfolio_correlation_spectrum`, must not be `None`")  # noqa: E501
        if portfolio_correlation_spectrum is not None and len(portfolio_correlation_spectrum) < 2:
            raise ValueError("Invalid value for `portfolio_correlation_spectrum`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._portfolio_correlation_spectrum = portfolio_correlation_spectrum
