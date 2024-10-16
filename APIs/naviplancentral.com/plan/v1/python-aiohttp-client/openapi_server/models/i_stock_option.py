# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.currency import Currency
from openapi_server.models.formatted_date_range import FormattedDateRange
from openapi_server.models.i_vesting_data import IVestingData
from openapi_server.models.model_date import ModelDate
from openapi_server.models.percent import Percent
from openapi_server import util


class IStockOption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annual_dividend_per_unit: Currency=None, applicable_range_retirement_liquidated_assets: FormattedDateRange=None, company: str=None, current_unit_price: Currency=None, current_unit_price_date: ModelDate=None, description: str=None, end_of_plan_year_exercisable_gross_value: Currency=None, exercise_cost: Currency=None, expiration_date: ModelDate=None, grant_date: ModelDate=None, granted_options: int=None, growth_rate: Percent=None, id: str=None, options_exercisable: int=None, options_exercised: int=None, options_vested: int=None, owner: str=None, pre_tax_profit: Currency=None, start_of_year_amt_basis: Currency=None, start_of_year_cost_basis: Currency=None, start_of_year_unit_price: Currency=None, strike_price: Currency=None, symbol: str=None, type: str=None, type_formatted: str=None, vesting_schedule: List[IVestingData]=None):
        """IStockOption - a model defined in OpenAPI

        :param annual_dividend_per_unit: The annual_dividend_per_unit of this IStockOption.
        :param applicable_range_retirement_liquidated_assets: The applicable_range_retirement_liquidated_assets of this IStockOption.
        :param company: The company of this IStockOption.
        :param current_unit_price: The current_unit_price of this IStockOption.
        :param current_unit_price_date: The current_unit_price_date of this IStockOption.
        :param description: The description of this IStockOption.
        :param end_of_plan_year_exercisable_gross_value: The end_of_plan_year_exercisable_gross_value of this IStockOption.
        :param exercise_cost: The exercise_cost of this IStockOption.
        :param expiration_date: The expiration_date of this IStockOption.
        :param grant_date: The grant_date of this IStockOption.
        :param granted_options: The granted_options of this IStockOption.
        :param growth_rate: The growth_rate of this IStockOption.
        :param id: The id of this IStockOption.
        :param options_exercisable: The options_exercisable of this IStockOption.
        :param options_exercised: The options_exercised of this IStockOption.
        :param options_vested: The options_vested of this IStockOption.
        :param owner: The owner of this IStockOption.
        :param pre_tax_profit: The pre_tax_profit of this IStockOption.
        :param start_of_year_amt_basis: The start_of_year_amt_basis of this IStockOption.
        :param start_of_year_cost_basis: The start_of_year_cost_basis of this IStockOption.
        :param start_of_year_unit_price: The start_of_year_unit_price of this IStockOption.
        :param strike_price: The strike_price of this IStockOption.
        :param symbol: The symbol of this IStockOption.
        :param type: The type of this IStockOption.
        :param type_formatted: The type_formatted of this IStockOption.
        :param vesting_schedule: The vesting_schedule of this IStockOption.
        """
        self.openapi_types = {
            'annual_dividend_per_unit': Currency,
            'applicable_range_retirement_liquidated_assets': FormattedDateRange,
            'company': str,
            'current_unit_price': Currency,
            'current_unit_price_date': ModelDate,
            'description': str,
            'end_of_plan_year_exercisable_gross_value': Currency,
            'exercise_cost': Currency,
            'expiration_date': ModelDate,
            'grant_date': ModelDate,
            'granted_options': int,
            'growth_rate': Percent,
            'id': str,
            'options_exercisable': int,
            'options_exercised': int,
            'options_vested': int,
            'owner': str,
            'pre_tax_profit': Currency,
            'start_of_year_amt_basis': Currency,
            'start_of_year_cost_basis': Currency,
            'start_of_year_unit_price': Currency,
            'strike_price': Currency,
            'symbol': str,
            'type': str,
            'type_formatted': str,
            'vesting_schedule': List[IVestingData]
        }

        self.attribute_map = {
            'annual_dividend_per_unit': 'annualDividendPerUnit',
            'applicable_range_retirement_liquidated_assets': 'applicableRangeRetirementLiquidatedAssets',
            'company': 'company',
            'current_unit_price': 'currentUnitPrice',
            'current_unit_price_date': 'currentUnitPriceDate',
            'description': 'description',
            'end_of_plan_year_exercisable_gross_value': 'endOfPlanYearExercisableGrossValue',
            'exercise_cost': 'exerciseCost',
            'expiration_date': 'expirationDate',
            'grant_date': 'grantDate',
            'granted_options': 'grantedOptions',
            'growth_rate': 'growthRate',
            'id': 'id',
            'options_exercisable': 'optionsExercisable',
            'options_exercised': 'optionsExercised',
            'options_vested': 'optionsVested',
            'owner': 'owner',
            'pre_tax_profit': 'preTaxProfit',
            'start_of_year_amt_basis': 'startOfYearAMTBasis',
            'start_of_year_cost_basis': 'startOfYearCostBasis',
            'start_of_year_unit_price': 'startOfYearUnitPrice',
            'strike_price': 'strikePrice',
            'symbol': 'symbol',
            'type': 'type',
            'type_formatted': 'typeFormatted',
            'vesting_schedule': 'vestingSchedule'
        }

        self._annual_dividend_per_unit = annual_dividend_per_unit
        self._applicable_range_retirement_liquidated_assets = applicable_range_retirement_liquidated_assets
        self._company = company
        self._current_unit_price = current_unit_price
        self._current_unit_price_date = current_unit_price_date
        self._description = description
        self._end_of_plan_year_exercisable_gross_value = end_of_plan_year_exercisable_gross_value
        self._exercise_cost = exercise_cost
        self._expiration_date = expiration_date
        self._grant_date = grant_date
        self._granted_options = granted_options
        self._growth_rate = growth_rate
        self._id = id
        self._options_exercisable = options_exercisable
        self._options_exercised = options_exercised
        self._options_vested = options_vested
        self._owner = owner
        self._pre_tax_profit = pre_tax_profit
        self._start_of_year_amt_basis = start_of_year_amt_basis
        self._start_of_year_cost_basis = start_of_year_cost_basis
        self._start_of_year_unit_price = start_of_year_unit_price
        self._strike_price = strike_price
        self._symbol = symbol
        self._type = type
        self._type_formatted = type_formatted
        self._vesting_schedule = vesting_schedule

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IStockOption':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IStockOption of this IStockOption.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annual_dividend_per_unit(self):
        """Gets the annual_dividend_per_unit of this IStockOption.


        :return: The annual_dividend_per_unit of this IStockOption.
        :rtype: Currency
        """
        return self._annual_dividend_per_unit

    @annual_dividend_per_unit.setter
    def annual_dividend_per_unit(self, annual_dividend_per_unit):
        """Sets the annual_dividend_per_unit of this IStockOption.


        :param annual_dividend_per_unit: The annual_dividend_per_unit of this IStockOption.
        :type annual_dividend_per_unit: Currency
        """

        self._annual_dividend_per_unit = annual_dividend_per_unit

    @property
    def applicable_range_retirement_liquidated_assets(self):
        """Gets the applicable_range_retirement_liquidated_assets of this IStockOption.


        :return: The applicable_range_retirement_liquidated_assets of this IStockOption.
        :rtype: FormattedDateRange
        """
        return self._applicable_range_retirement_liquidated_assets

    @applicable_range_retirement_liquidated_assets.setter
    def applicable_range_retirement_liquidated_assets(self, applicable_range_retirement_liquidated_assets):
        """Sets the applicable_range_retirement_liquidated_assets of this IStockOption.


        :param applicable_range_retirement_liquidated_assets: The applicable_range_retirement_liquidated_assets of this IStockOption.
        :type applicable_range_retirement_liquidated_assets: FormattedDateRange
        """

        self._applicable_range_retirement_liquidated_assets = applicable_range_retirement_liquidated_assets

    @property
    def company(self):
        """Gets the company of this IStockOption.


        :return: The company of this IStockOption.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this IStockOption.


        :param company: The company of this IStockOption.
        :type company: str
        """

        self._company = company

    @property
    def current_unit_price(self):
        """Gets the current_unit_price of this IStockOption.


        :return: The current_unit_price of this IStockOption.
        :rtype: Currency
        """
        return self._current_unit_price

    @current_unit_price.setter
    def current_unit_price(self, current_unit_price):
        """Sets the current_unit_price of this IStockOption.


        :param current_unit_price: The current_unit_price of this IStockOption.
        :type current_unit_price: Currency
        """

        self._current_unit_price = current_unit_price

    @property
    def current_unit_price_date(self):
        """Gets the current_unit_price_date of this IStockOption.


        :return: The current_unit_price_date of this IStockOption.
        :rtype: ModelDate
        """
        return self._current_unit_price_date

    @current_unit_price_date.setter
    def current_unit_price_date(self, current_unit_price_date):
        """Sets the current_unit_price_date of this IStockOption.


        :param current_unit_price_date: The current_unit_price_date of this IStockOption.
        :type current_unit_price_date: ModelDate
        """

        self._current_unit_price_date = current_unit_price_date

    @property
    def description(self):
        """Gets the description of this IStockOption.


        :return: The description of this IStockOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IStockOption.


        :param description: The description of this IStockOption.
        :type description: str
        """

        self._description = description

    @property
    def end_of_plan_year_exercisable_gross_value(self):
        """Gets the end_of_plan_year_exercisable_gross_value of this IStockOption.


        :return: The end_of_plan_year_exercisable_gross_value of this IStockOption.
        :rtype: Currency
        """
        return self._end_of_plan_year_exercisable_gross_value

    @end_of_plan_year_exercisable_gross_value.setter
    def end_of_plan_year_exercisable_gross_value(self, end_of_plan_year_exercisable_gross_value):
        """Sets the end_of_plan_year_exercisable_gross_value of this IStockOption.


        :param end_of_plan_year_exercisable_gross_value: The end_of_plan_year_exercisable_gross_value of this IStockOption.
        :type end_of_plan_year_exercisable_gross_value: Currency
        """

        self._end_of_plan_year_exercisable_gross_value = end_of_plan_year_exercisable_gross_value

    @property
    def exercise_cost(self):
        """Gets the exercise_cost of this IStockOption.


        :return: The exercise_cost of this IStockOption.
        :rtype: Currency
        """
        return self._exercise_cost

    @exercise_cost.setter
    def exercise_cost(self, exercise_cost):
        """Sets the exercise_cost of this IStockOption.


        :param exercise_cost: The exercise_cost of this IStockOption.
        :type exercise_cost: Currency
        """

        self._exercise_cost = exercise_cost

    @property
    def expiration_date(self):
        """Gets the expiration_date of this IStockOption.


        :return: The expiration_date of this IStockOption.
        :rtype: ModelDate
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this IStockOption.


        :param expiration_date: The expiration_date of this IStockOption.
        :type expiration_date: ModelDate
        """

        self._expiration_date = expiration_date

    @property
    def grant_date(self):
        """Gets the grant_date of this IStockOption.


        :return: The grant_date of this IStockOption.
        :rtype: ModelDate
        """
        return self._grant_date

    @grant_date.setter
    def grant_date(self, grant_date):
        """Sets the grant_date of this IStockOption.


        :param grant_date: The grant_date of this IStockOption.
        :type grant_date: ModelDate
        """

        self._grant_date = grant_date

    @property
    def granted_options(self):
        """Gets the granted_options of this IStockOption.


        :return: The granted_options of this IStockOption.
        :rtype: int
        """
        return self._granted_options

    @granted_options.setter
    def granted_options(self, granted_options):
        """Sets the granted_options of this IStockOption.


        :param granted_options: The granted_options of this IStockOption.
        :type granted_options: int
        """

        self._granted_options = granted_options

    @property
    def growth_rate(self):
        """Gets the growth_rate of this IStockOption.


        :return: The growth_rate of this IStockOption.
        :rtype: Percent
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate):
        """Sets the growth_rate of this IStockOption.


        :param growth_rate: The growth_rate of this IStockOption.
        :type growth_rate: Percent
        """

        self._growth_rate = growth_rate

    @property
    def id(self):
        """Gets the id of this IStockOption.


        :return: The id of this IStockOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IStockOption.


        :param id: The id of this IStockOption.
        :type id: str
        """

        self._id = id

    @property
    def options_exercisable(self):
        """Gets the options_exercisable of this IStockOption.


        :return: The options_exercisable of this IStockOption.
        :rtype: int
        """
        return self._options_exercisable

    @options_exercisable.setter
    def options_exercisable(self, options_exercisable):
        """Sets the options_exercisable of this IStockOption.


        :param options_exercisable: The options_exercisable of this IStockOption.
        :type options_exercisable: int
        """

        self._options_exercisable = options_exercisable

    @property
    def options_exercised(self):
        """Gets the options_exercised of this IStockOption.


        :return: The options_exercised of this IStockOption.
        :rtype: int
        """
        return self._options_exercised

    @options_exercised.setter
    def options_exercised(self, options_exercised):
        """Sets the options_exercised of this IStockOption.


        :param options_exercised: The options_exercised of this IStockOption.
        :type options_exercised: int
        """

        self._options_exercised = options_exercised

    @property
    def options_vested(self):
        """Gets the options_vested of this IStockOption.


        :return: The options_vested of this IStockOption.
        :rtype: int
        """
        return self._options_vested

    @options_vested.setter
    def options_vested(self, options_vested):
        """Sets the options_vested of this IStockOption.


        :param options_vested: The options_vested of this IStockOption.
        :type options_vested: int
        """

        self._options_vested = options_vested

    @property
    def owner(self):
        """Gets the owner of this IStockOption.


        :return: The owner of this IStockOption.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IStockOption.


        :param owner: The owner of this IStockOption.
        :type owner: str
        """

        self._owner = owner

    @property
    def pre_tax_profit(self):
        """Gets the pre_tax_profit of this IStockOption.


        :return: The pre_tax_profit of this IStockOption.
        :rtype: Currency
        """
        return self._pre_tax_profit

    @pre_tax_profit.setter
    def pre_tax_profit(self, pre_tax_profit):
        """Sets the pre_tax_profit of this IStockOption.


        :param pre_tax_profit: The pre_tax_profit of this IStockOption.
        :type pre_tax_profit: Currency
        """

        self._pre_tax_profit = pre_tax_profit

    @property
    def start_of_year_amt_basis(self):
        """Gets the start_of_year_amt_basis of this IStockOption.


        :return: The start_of_year_amt_basis of this IStockOption.
        :rtype: Currency
        """
        return self._start_of_year_amt_basis

    @start_of_year_amt_basis.setter
    def start_of_year_amt_basis(self, start_of_year_amt_basis):
        """Sets the start_of_year_amt_basis of this IStockOption.


        :param start_of_year_amt_basis: The start_of_year_amt_basis of this IStockOption.
        :type start_of_year_amt_basis: Currency
        """

        self._start_of_year_amt_basis = start_of_year_amt_basis

    @property
    def start_of_year_cost_basis(self):
        """Gets the start_of_year_cost_basis of this IStockOption.


        :return: The start_of_year_cost_basis of this IStockOption.
        :rtype: Currency
        """
        return self._start_of_year_cost_basis

    @start_of_year_cost_basis.setter
    def start_of_year_cost_basis(self, start_of_year_cost_basis):
        """Sets the start_of_year_cost_basis of this IStockOption.


        :param start_of_year_cost_basis: The start_of_year_cost_basis of this IStockOption.
        :type start_of_year_cost_basis: Currency
        """

        self._start_of_year_cost_basis = start_of_year_cost_basis

    @property
    def start_of_year_unit_price(self):
        """Gets the start_of_year_unit_price of this IStockOption.


        :return: The start_of_year_unit_price of this IStockOption.
        :rtype: Currency
        """
        return self._start_of_year_unit_price

    @start_of_year_unit_price.setter
    def start_of_year_unit_price(self, start_of_year_unit_price):
        """Sets the start_of_year_unit_price of this IStockOption.


        :param start_of_year_unit_price: The start_of_year_unit_price of this IStockOption.
        :type start_of_year_unit_price: Currency
        """

        self._start_of_year_unit_price = start_of_year_unit_price

    @property
    def strike_price(self):
        """Gets the strike_price of this IStockOption.


        :return: The strike_price of this IStockOption.
        :rtype: Currency
        """
        return self._strike_price

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this IStockOption.


        :param strike_price: The strike_price of this IStockOption.
        :type strike_price: Currency
        """

        self._strike_price = strike_price

    @property
    def symbol(self):
        """Gets the symbol of this IStockOption.


        :return: The symbol of this IStockOption.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this IStockOption.


        :param symbol: The symbol of this IStockOption.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def type(self):
        """Gets the type of this IStockOption.


        :return: The type of this IStockOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IStockOption.


        :param type: The type of this IStockOption.
        :type type: str
        """
        allowed_values = ["NonQualifiedStockOption", "IncentiveStockOption"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def type_formatted(self):
        """Gets the type_formatted of this IStockOption.


        :return: The type_formatted of this IStockOption.
        :rtype: str
        """
        return self._type_formatted

    @type_formatted.setter
    def type_formatted(self, type_formatted):
        """Sets the type_formatted of this IStockOption.


        :param type_formatted: The type_formatted of this IStockOption.
        :type type_formatted: str
        """

        self._type_formatted = type_formatted

    @property
    def vesting_schedule(self):
        """Gets the vesting_schedule of this IStockOption.


        :return: The vesting_schedule of this IStockOption.
        :rtype: List[IVestingData]
        """
        return self._vesting_schedule

    @vesting_schedule.setter
    def vesting_schedule(self, vesting_schedule):
        """Sets the vesting_schedule of this IStockOption.


        :param vesting_schedule: The vesting_schedule of this IStockOption.
        :type vesting_schedule: List[IVestingData]
        """

        self._vesting_schedule = vesting_schedule
