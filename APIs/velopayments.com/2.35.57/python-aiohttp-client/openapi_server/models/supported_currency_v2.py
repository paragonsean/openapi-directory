# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class SupportedCurrencyV2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, currency: str=None, max_payment_amount: int=None):
        """SupportedCurrencyV2 - a model defined in OpenAPI

        :param currency: The currency of this SupportedCurrencyV2.
        :param max_payment_amount: The max_payment_amount of this SupportedCurrencyV2.
        """
        self.openapi_types = {
            'currency': str,
            'max_payment_amount': int
        }

        self.attribute_map = {
            'currency': 'currency',
            'max_payment_amount': 'maxPaymentAmount'
        }

        self._currency = currency
        self._max_payment_amount = max_payment_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SupportedCurrencyV2':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SupportedCurrencyV2 of this SupportedCurrencyV2.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def currency(self):
        """Gets the currency of this SupportedCurrencyV2.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :return: The currency of this SupportedCurrencyV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SupportedCurrencyV2.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :param currency: The currency of this SupportedCurrencyV2.
        :type currency: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")
        if currency is not None and not re.search(r'^[A-Z]{3}$', currency):
            raise ValueError("Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")

        self._currency = currency

    @property
    def max_payment_amount(self):
        """Gets the max_payment_amount of this SupportedCurrencyV2.

        The max amount allowed in this currency

        :return: The max_payment_amount of this SupportedCurrencyV2.
        :rtype: int
        """
        return self._max_payment_amount

    @max_payment_amount.setter
    def max_payment_amount(self, max_payment_amount):
        """Sets the max_payment_amount of this SupportedCurrencyV2.

        The max amount allowed in this currency

        :param max_payment_amount: The max_payment_amount of this SupportedCurrencyV2.
        :type max_payment_amount: int
        """

        self._max_payment_amount = max_payment_amount
