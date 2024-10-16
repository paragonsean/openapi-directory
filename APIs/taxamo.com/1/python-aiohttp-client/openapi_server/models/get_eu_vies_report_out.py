# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.report import Report
from openapi_server import util


class GetEuViesReportOut(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, currency_code: str=None, end_date: str=None, report: List[Report]=None, start_date: str=None):
        """GetEuViesReportOut - a model defined in OpenAPI

        :param currency_code: The currency_code of this GetEuViesReportOut.
        :param end_date: The end_date of this GetEuViesReportOut.
        :param report: The report of this GetEuViesReportOut.
        :param start_date: The start_date of this GetEuViesReportOut.
        """
        self.openapi_types = {
            'currency_code': str,
            'end_date': str,
            'report': List[Report],
            'start_date': str
        }

        self.attribute_map = {
            'currency_code': 'currency_code',
            'end_date': 'end_date',
            'report': 'report',
            'start_date': 'start_date'
        }

        self._currency_code = currency_code
        self._end_date = end_date
        self._report = report
        self._start_date = start_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetEuViesReportOut':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getEuViesReportOut of this GetEuViesReportOut.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def currency_code(self):
        """Gets the currency_code of this GetEuViesReportOut.

        Three-letter ISO currency code.

        :return: The currency_code of this GetEuViesReportOut.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this GetEuViesReportOut.

        Three-letter ISO currency code.

        :param currency_code: The currency_code of this GetEuViesReportOut.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def end_date(self):
        """Gets the end_date of this GetEuViesReportOut.

        Period end date in yyyy-MM-dd'T'hh:mm:ss'Z' format.

        :return: The end_date of this GetEuViesReportOut.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetEuViesReportOut.

        Period end date in yyyy-MM-dd'T'hh:mm:ss'Z' format.

        :param end_date: The end_date of this GetEuViesReportOut.
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def report(self):
        """Gets the report of this GetEuViesReportOut.

        Settlement report.

        :return: The report of this GetEuViesReportOut.
        :rtype: List[Report]
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this GetEuViesReportOut.

        Settlement report.

        :param report: The report of this GetEuViesReportOut.
        :type report: List[Report]
        """

        self._report = report

    @property
    def start_date(self):
        """Gets the start_date of this GetEuViesReportOut.

        Period start date in yyyy-MM-dd'T'hh:mm:ss'Z' format.

        :return: The start_date of this GetEuViesReportOut.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetEuViesReportOut.

        Period start date in yyyy-MM-dd'T'hh:mm:ss'Z' format.

        :param start_date: The start_date of this GetEuViesReportOut.
        :type start_date: str
        """

        self._start_date = start_date
