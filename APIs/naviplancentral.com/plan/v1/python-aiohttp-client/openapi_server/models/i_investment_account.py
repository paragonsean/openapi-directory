# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.currency import Currency
from openapi_server.models.i_holding import IHolding
from openapi_server.models.i_rate_of_return_details import IRateOfReturnDetails
from openapi_server.models.model_date import ModelDate
from openapi_server.models.percent import Percent
from openapi_server import util


class IInvestmentAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annual_fee: Percent=None, cost_basis: Currency=None, description: str=None, exclude_in_aa: bool=None, holdings: List[IHolding]=None, id: str=None, market_value: Currency=None, rate_of_return: IRateOfReturnDetails=None, type: str=None, valuation_date: ModelDate=None):
        """IInvestmentAccount - a model defined in OpenAPI

        :param annual_fee: The annual_fee of this IInvestmentAccount.
        :param cost_basis: The cost_basis of this IInvestmentAccount.
        :param description: The description of this IInvestmentAccount.
        :param exclude_in_aa: The exclude_in_aa of this IInvestmentAccount.
        :param holdings: The holdings of this IInvestmentAccount.
        :param id: The id of this IInvestmentAccount.
        :param market_value: The market_value of this IInvestmentAccount.
        :param rate_of_return: The rate_of_return of this IInvestmentAccount.
        :param type: The type of this IInvestmentAccount.
        :param valuation_date: The valuation_date of this IInvestmentAccount.
        """
        self.openapi_types = {
            'annual_fee': Percent,
            'cost_basis': Currency,
            'description': str,
            'exclude_in_aa': bool,
            'holdings': List[IHolding],
            'id': str,
            'market_value': Currency,
            'rate_of_return': IRateOfReturnDetails,
            'type': str,
            'valuation_date': ModelDate
        }

        self.attribute_map = {
            'annual_fee': 'annualFee',
            'cost_basis': 'costBasis',
            'description': 'description',
            'exclude_in_aa': 'excludeInAA',
            'holdings': 'holdings',
            'id': 'id',
            'market_value': 'marketValue',
            'rate_of_return': 'rateOfReturn',
            'type': 'type',
            'valuation_date': 'valuationDate'
        }

        self._annual_fee = annual_fee
        self._cost_basis = cost_basis
        self._description = description
        self._exclude_in_aa = exclude_in_aa
        self._holdings = holdings
        self._id = id
        self._market_value = market_value
        self._rate_of_return = rate_of_return
        self._type = type
        self._valuation_date = valuation_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IInvestmentAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IInvestmentAccount of this IInvestmentAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annual_fee(self):
        """Gets the annual_fee of this IInvestmentAccount.


        :return: The annual_fee of this IInvestmentAccount.
        :rtype: Percent
        """
        return self._annual_fee

    @annual_fee.setter
    def annual_fee(self, annual_fee):
        """Sets the annual_fee of this IInvestmentAccount.


        :param annual_fee: The annual_fee of this IInvestmentAccount.
        :type annual_fee: Percent
        """

        self._annual_fee = annual_fee

    @property
    def cost_basis(self):
        """Gets the cost_basis of this IInvestmentAccount.


        :return: The cost_basis of this IInvestmentAccount.
        :rtype: Currency
        """
        return self._cost_basis

    @cost_basis.setter
    def cost_basis(self, cost_basis):
        """Sets the cost_basis of this IInvestmentAccount.


        :param cost_basis: The cost_basis of this IInvestmentAccount.
        :type cost_basis: Currency
        """

        self._cost_basis = cost_basis

    @property
    def description(self):
        """Gets the description of this IInvestmentAccount.


        :return: The description of this IInvestmentAccount.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IInvestmentAccount.


        :param description: The description of this IInvestmentAccount.
        :type description: str
        """

        self._description = description

    @property
    def exclude_in_aa(self):
        """Gets the exclude_in_aa of this IInvestmentAccount.


        :return: The exclude_in_aa of this IInvestmentAccount.
        :rtype: bool
        """
        return self._exclude_in_aa

    @exclude_in_aa.setter
    def exclude_in_aa(self, exclude_in_aa):
        """Sets the exclude_in_aa of this IInvestmentAccount.


        :param exclude_in_aa: The exclude_in_aa of this IInvestmentAccount.
        :type exclude_in_aa: bool
        """

        self._exclude_in_aa = exclude_in_aa

    @property
    def holdings(self):
        """Gets the holdings of this IInvestmentAccount.


        :return: The holdings of this IInvestmentAccount.
        :rtype: List[IHolding]
        """
        return self._holdings

    @holdings.setter
    def holdings(self, holdings):
        """Sets the holdings of this IInvestmentAccount.


        :param holdings: The holdings of this IInvestmentAccount.
        :type holdings: List[IHolding]
        """

        self._holdings = holdings

    @property
    def id(self):
        """Gets the id of this IInvestmentAccount.


        :return: The id of this IInvestmentAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IInvestmentAccount.


        :param id: The id of this IInvestmentAccount.
        :type id: str
        """

        self._id = id

    @property
    def market_value(self):
        """Gets the market_value of this IInvestmentAccount.


        :return: The market_value of this IInvestmentAccount.
        :rtype: Currency
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this IInvestmentAccount.


        :param market_value: The market_value of this IInvestmentAccount.
        :type market_value: Currency
        """

        self._market_value = market_value

    @property
    def rate_of_return(self):
        """Gets the rate_of_return of this IInvestmentAccount.


        :return: The rate_of_return of this IInvestmentAccount.
        :rtype: IRateOfReturnDetails
        """
        return self._rate_of_return

    @rate_of_return.setter
    def rate_of_return(self, rate_of_return):
        """Sets the rate_of_return of this IInvestmentAccount.


        :param rate_of_return: The rate_of_return of this IInvestmentAccount.
        :type rate_of_return: IRateOfReturnDetails
        """

        self._rate_of_return = rate_of_return

    @property
    def type(self):
        """Gets the type of this IInvestmentAccount.


        :return: The type of this IInvestmentAccount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IInvestmentAccount.


        :param type: The type of this IInvestmentAccount.
        :type type: str
        """

        self._type = type

    @property
    def valuation_date(self):
        """Gets the valuation_date of this IInvestmentAccount.


        :return: The valuation_date of this IInvestmentAccount.
        :rtype: ModelDate
        """
        return self._valuation_date

    @valuation_date.setter
    def valuation_date(self, valuation_date):
        """Sets the valuation_date of this IInvestmentAccount.


        :param valuation_date: The valuation_date of this IInvestmentAccount.
        :type valuation_date: ModelDate
        """

        self._valuation_date = valuation_date
