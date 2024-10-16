# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AccountHoldingModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cost_basis: float=None, cusip: str=None, description: str=None, external_destination_id: str=None, market_value: float=None, symbol: str=None, valuation_date: datetime=None):
        """AccountHoldingModel - a model defined in OpenAPI

        :param cost_basis: The cost_basis of this AccountHoldingModel.
        :param cusip: The cusip of this AccountHoldingModel.
        :param description: The description of this AccountHoldingModel.
        :param external_destination_id: The external_destination_id of this AccountHoldingModel.
        :param market_value: The market_value of this AccountHoldingModel.
        :param symbol: The symbol of this AccountHoldingModel.
        :param valuation_date: The valuation_date of this AccountHoldingModel.
        """
        self.openapi_types = {
            'cost_basis': float,
            'cusip': str,
            'description': str,
            'external_destination_id': str,
            'market_value': float,
            'symbol': str,
            'valuation_date': datetime
        }

        self.attribute_map = {
            'cost_basis': 'costBasis',
            'cusip': 'cusip',
            'description': 'description',
            'external_destination_id': 'externalDestinationId',
            'market_value': 'marketValue',
            'symbol': 'symbol',
            'valuation_date': 'valuationDate'
        }

        self._cost_basis = cost_basis
        self._cusip = cusip
        self._description = description
        self._external_destination_id = external_destination_id
        self._market_value = market_value
        self._symbol = symbol
        self._valuation_date = valuation_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccountHoldingModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AccountHoldingModel of this AccountHoldingModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cost_basis(self):
        """Gets the cost_basis of this AccountHoldingModel.


        :return: The cost_basis of this AccountHoldingModel.
        :rtype: float
        """
        return self._cost_basis

    @cost_basis.setter
    def cost_basis(self, cost_basis):
        """Sets the cost_basis of this AccountHoldingModel.


        :param cost_basis: The cost_basis of this AccountHoldingModel.
        :type cost_basis: float
        """

        self._cost_basis = cost_basis

    @property
    def cusip(self):
        """Gets the cusip of this AccountHoldingModel.


        :return: The cusip of this AccountHoldingModel.
        :rtype: str
        """
        return self._cusip

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this AccountHoldingModel.


        :param cusip: The cusip of this AccountHoldingModel.
        :type cusip: str
        """
        if cusip is not None and len(cusip) > 31:
            raise ValueError("Invalid value for `cusip`, length must be less than or equal to `31`")
        if cusip is not None and len(cusip) < 0:
            raise ValueError("Invalid value for `cusip`, length must be greater than or equal to `0`")

        self._cusip = cusip

    @property
    def description(self):
        """Gets the description of this AccountHoldingModel.


        :return: The description of this AccountHoldingModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountHoldingModel.


        :param description: The description of this AccountHoldingModel.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def external_destination_id(self):
        """Gets the external_destination_id of this AccountHoldingModel.


        :return: The external_destination_id of this AccountHoldingModel.
        :rtype: str
        """
        return self._external_destination_id

    @external_destination_id.setter
    def external_destination_id(self, external_destination_id):
        """Sets the external_destination_id of this AccountHoldingModel.


        :param external_destination_id: The external_destination_id of this AccountHoldingModel.
        :type external_destination_id: str
        """
        if external_destination_id is not None and len(external_destination_id) > 64:
            raise ValueError("Invalid value for `external_destination_id`, length must be less than or equal to `64`")
        if external_destination_id is not None and len(external_destination_id) < 0:
            raise ValueError("Invalid value for `external_destination_id`, length must be greater than or equal to `0`")

        self._external_destination_id = external_destination_id

    @property
    def market_value(self):
        """Gets the market_value of this AccountHoldingModel.


        :return: The market_value of this AccountHoldingModel.
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this AccountHoldingModel.


        :param market_value: The market_value of this AccountHoldingModel.
        :type market_value: float
        """

        self._market_value = market_value

    @property
    def symbol(self):
        """Gets the symbol of this AccountHoldingModel.


        :return: The symbol of this AccountHoldingModel.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this AccountHoldingModel.


        :param symbol: The symbol of this AccountHoldingModel.
        :type symbol: str
        """
        if symbol is not None and len(symbol) > 31:
            raise ValueError("Invalid value for `symbol`, length must be less than or equal to `31`")
        if symbol is not None and len(symbol) < 0:
            raise ValueError("Invalid value for `symbol`, length must be greater than or equal to `0`")

        self._symbol = symbol

    @property
    def valuation_date(self):
        """Gets the valuation_date of this AccountHoldingModel.


        :return: The valuation_date of this AccountHoldingModel.
        :rtype: datetime
        """
        return self._valuation_date

    @valuation_date.setter
    def valuation_date(self, valuation_date):
        """Sets the valuation_date of this AccountHoldingModel.


        :param valuation_date: The valuation_date of this AccountHoldingModel.
        :type valuation_date: datetime
        """

        self._valuation_date = valuation_date
