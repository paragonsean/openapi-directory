from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post_request_portfolios_inner import PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner
from openapi_server import util

from openapi_server.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post_request_portfolios_inner import PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner  # noqa: E501

class PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, benchmark_sharpe_ratio=None, confidence_level=0.95, portfolios=None, risk_free_rate=None):  # noqa: E501
        """PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf - a model defined in OpenAPI

        :param benchmark_sharpe_ratio: The benchmark_sharpe_ratio of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.  # noqa: E501
        :type benchmark_sharpe_ratio: float
        :param confidence_level: The confidence_level of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.  # noqa: E501
        :type confidence_level: float
        :param portfolios: The portfolios of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.  # noqa: E501
        :type portfolios: List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner]
        :param risk_free_rate: The risk_free_rate of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.  # noqa: E501
        :type risk_free_rate: float
        """
        self.openapi_types = {
            'benchmark_sharpe_ratio': float,
            'confidence_level': float,
            'portfolios': List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner],
            'risk_free_rate': float
        }

        self.attribute_map = {
            'benchmark_sharpe_ratio': 'benchmarkSharpeRatio',
            'confidence_level': 'confidenceLevel',
            'portfolios': 'portfolios',
            'risk_free_rate': 'riskFreeRate'
        }

        self._benchmark_sharpe_ratio = benchmark_sharpe_ratio
        self._confidence_level = confidence_level
        self._portfolios = portfolios
        self._risk_free_rate = risk_free_rate

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post_request_oneOf of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.  # noqa: E501
        :rtype: PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def benchmark_sharpe_ratio(self) -> float:
        """Gets the benchmark_sharpe_ratio of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The Sharpe ratio of the benchmark, in the same sampling frequency as the sampling frequency of the portfolio values  # noqa: E501

        :return: The benchmark_sharpe_ratio of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :rtype: float
        """
        return self._benchmark_sharpe_ratio

    @benchmark_sharpe_ratio.setter
    def benchmark_sharpe_ratio(self, benchmark_sharpe_ratio: float):
        """Sets the benchmark_sharpe_ratio of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The Sharpe ratio of the benchmark, in the same sampling frequency as the sampling frequency of the portfolio values  # noqa: E501

        :param benchmark_sharpe_ratio: The benchmark_sharpe_ratio of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :type benchmark_sharpe_ratio: float
        """
        if benchmark_sharpe_ratio is None:
            raise ValueError("Invalid value for `benchmark_sharpe_ratio`, must not be `None`")  # noqa: E501

        self._benchmark_sharpe_ratio = benchmark_sharpe_ratio

    @property
    def confidence_level(self) -> float:
        """Gets the confidence_level of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The confidence level of the minimum track record length, in percentage  # noqa: E501

        :return: The confidence_level of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :rtype: float
        """
        return self._confidence_level

    @confidence_level.setter
    def confidence_level(self, confidence_level: float):
        """Sets the confidence_level of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The confidence level of the minimum track record length, in percentage  # noqa: E501

        :param confidence_level: The confidence_level of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :type confidence_level: float
        """
        if confidence_level is not None and confidence_level >= 1:  # noqa: E501
            raise ValueError("Invalid value for `confidence_level`, must be a value less than `1`")  # noqa: E501
        if confidence_level is not None and confidence_level <= 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence_level`, must be a value greater than `0`")  # noqa: E501

        self._confidence_level = confidence_level

    @property
    def portfolios(self) -> List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner]:
        """Gets the portfolios of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.


        :return: The portfolios of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :rtype: List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios: List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner]):
        """Sets the portfolios of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.


        :param portfolios: The portfolios of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :type portfolios: List[PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner]
        """
        if portfolios is None:
            raise ValueError("Invalid value for `portfolios`, must not be `None`")  # noqa: E501
        if portfolios is not None and len(portfolios) < 1:
            raise ValueError("Invalid value for `portfolios`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._portfolios = portfolios

    @property
    def risk_free_rate(self) -> float:
        """Gets the risk_free_rate of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The risk free rate  # noqa: E501

        :return: The risk_free_rate of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :rtype: float
        """
        return self._risk_free_rate

    @risk_free_rate.setter
    def risk_free_rate(self, risk_free_rate: float):
        """Sets the risk_free_rate of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.

        The risk free rate  # noqa: E501

        :param risk_free_rate: The risk_free_rate of this PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf.
        :type risk_free_rate: float
        """
        if risk_free_rate is None:
            raise ValueError("Invalid value for `risk_free_rate`, must not be `None`")  # noqa: E501

        self._risk_free_rate = risk_free_rate
