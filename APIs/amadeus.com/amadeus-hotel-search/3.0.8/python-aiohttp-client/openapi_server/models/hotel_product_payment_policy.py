# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.method import Method
from openapi_server import util


class HotelProductPaymentPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, credit_cards: List[str]=None, methods: List[Method]=None):
        """HotelProductPaymentPolicy - a model defined in OpenAPI

        :param credit_cards: The credit_cards of this HotelProductPaymentPolicy.
        :param methods: The methods of this HotelProductPaymentPolicy.
        """
        self.openapi_types = {
            'credit_cards': List[str],
            'methods': List[Method]
        }

        self.attribute_map = {
            'credit_cards': 'creditCards',
            'methods': 'methods'
        }

        self._credit_cards = credit_cards
        self._methods = methods

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HotelProductPaymentPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HotelProduct_PaymentPolicy of this HotelProductPaymentPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credit_cards(self):
        """Gets the credit_cards of this HotelProductPaymentPolicy.

        Accepted Payment Card Types for the `method` CREDIT_CARD

        :return: The credit_cards of this HotelProductPaymentPolicy.
        :rtype: List[str]
        """
        return self._credit_cards

    @credit_cards.setter
    def credit_cards(self, credit_cards):
        """Sets the credit_cards of this HotelProductPaymentPolicy.

        Accepted Payment Card Types for the `method` CREDIT_CARD

        :param credit_cards: The credit_cards of this HotelProductPaymentPolicy.
        :type credit_cards: List[str]
        """

        self._credit_cards = credit_cards

    @property
    def methods(self):
        """Gets the methods of this HotelProductPaymentPolicy.

        Accepted Payment Methods

        :return: The methods of this HotelProductPaymentPolicy.
        :rtype: List[Method]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this HotelProductPaymentPolicy.

        Accepted Payment Methods

        :param methods: The methods of this HotelProductPaymentPolicy.
        :type methods: List[Method]
        """

        self._methods = methods
