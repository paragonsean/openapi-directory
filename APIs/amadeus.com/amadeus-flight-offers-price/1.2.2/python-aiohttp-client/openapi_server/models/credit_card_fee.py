# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.payment_brand import PaymentBrand
from openapi_server import util


class CreditCardFee(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: str=None, brand: PaymentBrand=None, currency: str=None, flight_offer_id: str=None):
        """CreditCardFee - a model defined in OpenAPI

        :param amount: The amount of this CreditCardFee.
        :param brand: The brand of this CreditCardFee.
        :param currency: The currency of this CreditCardFee.
        :param flight_offer_id: The flight_offer_id of this CreditCardFee.
        """
        self.openapi_types = {
            'amount': str,
            'brand': PaymentBrand,
            'currency': str,
            'flight_offer_id': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'brand': 'brand',
            'currency': 'currency',
            'flight_offer_id': 'flightOfferId'
        }

        self._amount = amount
        self._brand = brand
        self._currency = currency
        self._flight_offer_id = flight_offer_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreditCardFee':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreditCardFee of this CreditCardFee.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this CreditCardFee.


        :return: The amount of this CreditCardFee.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditCardFee.


        :param amount: The amount of this CreditCardFee.
        :type amount: str
        """

        self._amount = amount

    @property
    def brand(self):
        """Gets the brand of this CreditCardFee.


        :return: The brand of this CreditCardFee.
        :rtype: PaymentBrand
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CreditCardFee.


        :param brand: The brand of this CreditCardFee.
        :type brand: PaymentBrand
        """

        self._brand = brand

    @property
    def currency(self):
        """Gets the currency of this CreditCardFee.


        :return: The currency of this CreditCardFee.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditCardFee.


        :param currency: The currency of this CreditCardFee.
        :type currency: str
        """

        self._currency = currency

    @property
    def flight_offer_id(self):
        """Gets the flight_offer_id of this CreditCardFee.

        Id of the flightOffer concerned by the credit card fee

        :return: The flight_offer_id of this CreditCardFee.
        :rtype: str
        """
        return self._flight_offer_id

    @flight_offer_id.setter
    def flight_offer_id(self, flight_offer_id):
        """Sets the flight_offer_id of this CreditCardFee.

        Id of the flightOffer concerned by the credit card fee

        :param flight_offer_id: The flight_offer_id of this CreditCardFee.
        :type flight_offer_id: str
        """

        self._flight_offer_id = flight_offer_id
