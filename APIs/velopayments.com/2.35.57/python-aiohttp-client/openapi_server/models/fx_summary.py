# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FxSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, creation_date_time: datetime=None, funding_status: str=None, inverted_rate: float=None, payment_currency: str=None, quote_id: str=None, rate: float=None, source_currency: str=None, status: str=None, total_cost: int=None, total_payment_amount: int=None):
        """FxSummary - a model defined in OpenAPI

        :param creation_date_time: The creation_date_time of this FxSummary.
        :param funding_status: The funding_status of this FxSummary.
        :param inverted_rate: The inverted_rate of this FxSummary.
        :param payment_currency: The payment_currency of this FxSummary.
        :param quote_id: The quote_id of this FxSummary.
        :param rate: The rate of this FxSummary.
        :param source_currency: The source_currency of this FxSummary.
        :param status: The status of this FxSummary.
        :param total_cost: The total_cost of this FxSummary.
        :param total_payment_amount: The total_payment_amount of this FxSummary.
        """
        self.openapi_types = {
            'creation_date_time': datetime,
            'funding_status': str,
            'inverted_rate': float,
            'payment_currency': str,
            'quote_id': str,
            'rate': float,
            'source_currency': str,
            'status': str,
            'total_cost': int,
            'total_payment_amount': int
        }

        self.attribute_map = {
            'creation_date_time': 'creationDateTime',
            'funding_status': 'fundingStatus',
            'inverted_rate': 'invertedRate',
            'payment_currency': 'paymentCurrency',
            'quote_id': 'quoteId',
            'rate': 'rate',
            'source_currency': 'sourceCurrency',
            'status': 'status',
            'total_cost': 'totalCost',
            'total_payment_amount': 'totalPaymentAmount'
        }

        self._creation_date_time = creation_date_time
        self._funding_status = funding_status
        self._inverted_rate = inverted_rate
        self._payment_currency = payment_currency
        self._quote_id = quote_id
        self._rate = rate
        self._source_currency = source_currency
        self._status = status
        self._total_cost = total_cost
        self._total_payment_amount = total_payment_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FxSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FxSummary of this FxSummary.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this FxSummary.


        :return: The creation_date_time of this FxSummary.
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this FxSummary.


        :param creation_date_time: The creation_date_time of this FxSummary.
        :type creation_date_time: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")

        self._creation_date_time = creation_date_time

    @property
    def funding_status(self):
        """Gets the funding_status of this FxSummary.

        Current status of the funding. One of the following values: FUNDED, INSTRUCTED, UNFUNDED

        :return: The funding_status of this FxSummary.
        :rtype: str
        """
        return self._funding_status

    @funding_status.setter
    def funding_status(self, funding_status):
        """Sets the funding_status of this FxSummary.

        Current status of the funding. One of the following values: FUNDED, INSTRUCTED, UNFUNDED

        :param funding_status: The funding_status of this FxSummary.
        :type funding_status: str
        """
        if funding_status is None:
            raise ValueError("Invalid value for `funding_status`, must not be `None`")

        self._funding_status = funding_status

    @property
    def inverted_rate(self):
        """Gets the inverted_rate of this FxSummary.


        :return: The inverted_rate of this FxSummary.
        :rtype: float
        """
        return self._inverted_rate

    @inverted_rate.setter
    def inverted_rate(self, inverted_rate):
        """Sets the inverted_rate of this FxSummary.


        :param inverted_rate: The inverted_rate of this FxSummary.
        :type inverted_rate: float
        """
        if inverted_rate is None:
            raise ValueError("Invalid value for `inverted_rate`, must not be `None`")

        self._inverted_rate = inverted_rate

    @property
    def payment_currency(self):
        """Gets the payment_currency of this FxSummary.

        ISO-4217 3 character currency code

        :return: The payment_currency of this FxSummary.
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this FxSummary.

        ISO-4217 3 character currency code

        :param payment_currency: The payment_currency of this FxSummary.
        :type payment_currency: str
        """
        if payment_currency is not None and len(payment_currency) > 3:
            raise ValueError("Invalid value for `payment_currency`, length must be less than or equal to `3`")
        if payment_currency is not None and len(payment_currency) < 3:
            raise ValueError("Invalid value for `payment_currency`, length must be greater than or equal to `3`")

        self._payment_currency = payment_currency

    @property
    def quote_id(self):
        """Gets the quote_id of this FxSummary.


        :return: The quote_id of this FxSummary.
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this FxSummary.


        :param quote_id: The quote_id of this FxSummary.
        :type quote_id: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")

        self._quote_id = quote_id

    @property
    def rate(self):
        """Gets the rate of this FxSummary.


        :return: The rate of this FxSummary.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FxSummary.


        :param rate: The rate of this FxSummary.
        :type rate: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")

        self._rate = rate

    @property
    def source_currency(self):
        """Gets the source_currency of this FxSummary.

        ISO-4217 3 character currency code

        :return: The source_currency of this FxSummary.
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this FxSummary.

        ISO-4217 3 character currency code

        :param source_currency: The source_currency of this FxSummary.
        :type source_currency: str
        """
        if source_currency is not None and len(source_currency) > 3:
            raise ValueError("Invalid value for `source_currency`, length must be less than or equal to `3`")
        if source_currency is not None and len(source_currency) < 3:
            raise ValueError("Invalid value for `source_currency`, length must be greater than or equal to `3`")

        self._source_currency = source_currency

    @property
    def status(self):
        """Gets the status of this FxSummary.

        Current status of the FX Summary. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED

        :return: The status of this FxSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FxSummary.

        Current status of the FX Summary. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED

        :param status: The status of this FxSummary.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def total_cost(self):
        """Gets the total_cost of this FxSummary.


        :return: The total_cost of this FxSummary.
        :rtype: int
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this FxSummary.


        :param total_cost: The total_cost of this FxSummary.
        :type total_cost: int
        """
        if total_cost is None:
            raise ValueError("Invalid value for `total_cost`, must not be `None`")

        self._total_cost = total_cost

    @property
    def total_payment_amount(self):
        """Gets the total_payment_amount of this FxSummary.


        :return: The total_payment_amount of this FxSummary.
        :rtype: int
        """
        return self._total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, total_payment_amount):
        """Sets the total_payment_amount of this FxSummary.


        :param total_payment_amount: The total_payment_amount of this FxSummary.
        :type total_payment_amount: int
        """
        if total_payment_amount is None:
            raise ValueError("Invalid value for `total_payment_amount`, must not be `None`")

        self._total_payment_amount = total_payment_amount
