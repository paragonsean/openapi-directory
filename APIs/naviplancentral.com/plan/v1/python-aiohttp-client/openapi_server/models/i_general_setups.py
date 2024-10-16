# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.currency import Currency
from openapi_server.models.percent import Percent
from openapi_server import util


class IGeneralSetups(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, applied_business_limit: Currency=None, good_will_future_sales_market_value: Currency=None, percentage_of_limit_to_use: Percent=None, previous_year_adjusted_aggregate_investment_income: Currency=None):
        """IGeneralSetups - a model defined in OpenAPI

        :param applied_business_limit: The applied_business_limit of this IGeneralSetups.
        :param good_will_future_sales_market_value: The good_will_future_sales_market_value of this IGeneralSetups.
        :param percentage_of_limit_to_use: The percentage_of_limit_to_use of this IGeneralSetups.
        :param previous_year_adjusted_aggregate_investment_income: The previous_year_adjusted_aggregate_investment_income of this IGeneralSetups.
        """
        self.openapi_types = {
            'applied_business_limit': Currency,
            'good_will_future_sales_market_value': Currency,
            'percentage_of_limit_to_use': Percent,
            'previous_year_adjusted_aggregate_investment_income': Currency
        }

        self.attribute_map = {
            'applied_business_limit': 'appliedBusinessLimit',
            'good_will_future_sales_market_value': 'goodWillFutureSalesMarketValue',
            'percentage_of_limit_to_use': 'percentageOfLimitToUse',
            'previous_year_adjusted_aggregate_investment_income': 'previousYearAdjustedAggregateInvestmentIncome'
        }

        self._applied_business_limit = applied_business_limit
        self._good_will_future_sales_market_value = good_will_future_sales_market_value
        self._percentage_of_limit_to_use = percentage_of_limit_to_use
        self._previous_year_adjusted_aggregate_investment_income = previous_year_adjusted_aggregate_investment_income

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IGeneralSetups':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IGeneralSetups of this IGeneralSetups.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def applied_business_limit(self):
        """Gets the applied_business_limit of this IGeneralSetups.


        :return: The applied_business_limit of this IGeneralSetups.
        :rtype: Currency
        """
        return self._applied_business_limit

    @applied_business_limit.setter
    def applied_business_limit(self, applied_business_limit):
        """Sets the applied_business_limit of this IGeneralSetups.


        :param applied_business_limit: The applied_business_limit of this IGeneralSetups.
        :type applied_business_limit: Currency
        """

        self._applied_business_limit = applied_business_limit

    @property
    def good_will_future_sales_market_value(self):
        """Gets the good_will_future_sales_market_value of this IGeneralSetups.


        :return: The good_will_future_sales_market_value of this IGeneralSetups.
        :rtype: Currency
        """
        return self._good_will_future_sales_market_value

    @good_will_future_sales_market_value.setter
    def good_will_future_sales_market_value(self, good_will_future_sales_market_value):
        """Sets the good_will_future_sales_market_value of this IGeneralSetups.


        :param good_will_future_sales_market_value: The good_will_future_sales_market_value of this IGeneralSetups.
        :type good_will_future_sales_market_value: Currency
        """

        self._good_will_future_sales_market_value = good_will_future_sales_market_value

    @property
    def percentage_of_limit_to_use(self):
        """Gets the percentage_of_limit_to_use of this IGeneralSetups.


        :return: The percentage_of_limit_to_use of this IGeneralSetups.
        :rtype: Percent
        """
        return self._percentage_of_limit_to_use

    @percentage_of_limit_to_use.setter
    def percentage_of_limit_to_use(self, percentage_of_limit_to_use):
        """Sets the percentage_of_limit_to_use of this IGeneralSetups.


        :param percentage_of_limit_to_use: The percentage_of_limit_to_use of this IGeneralSetups.
        :type percentage_of_limit_to_use: Percent
        """

        self._percentage_of_limit_to_use = percentage_of_limit_to_use

    @property
    def previous_year_adjusted_aggregate_investment_income(self):
        """Gets the previous_year_adjusted_aggregate_investment_income of this IGeneralSetups.


        :return: The previous_year_adjusted_aggregate_investment_income of this IGeneralSetups.
        :rtype: Currency
        """
        return self._previous_year_adjusted_aggregate_investment_income

    @previous_year_adjusted_aggregate_investment_income.setter
    def previous_year_adjusted_aggregate_investment_income(self, previous_year_adjusted_aggregate_investment_income):
        """Sets the previous_year_adjusted_aggregate_investment_income of this IGeneralSetups.


        :param previous_year_adjusted_aggregate_investment_income: The previous_year_adjusted_aggregate_investment_income of this IGeneralSetups.
        :type previous_year_adjusted_aggregate_investment_income: Currency
        """

        self._previous_year_adjusted_aggregate_investment_income = previous_year_adjusted_aggregate_investment_income
