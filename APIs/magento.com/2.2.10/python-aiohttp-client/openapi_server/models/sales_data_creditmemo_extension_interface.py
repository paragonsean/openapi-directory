# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SalesDataCreditmemoExtensionInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_customer_balance_amount: float=None, base_gift_cards_amount: float=None, customer_balance_amount: float=None, gift_cards_amount: float=None, gw_base_price: str=None, gw_base_tax_amount: str=None, gw_card_base_price: str=None, gw_card_base_tax_amount: str=None, gw_card_price: str=None, gw_card_tax_amount: str=None, gw_items_base_price: str=None, gw_items_base_tax_amount: str=None, gw_items_price: str=None, gw_items_tax_amount: str=None, gw_price: str=None, gw_tax_amount: str=None):
        """SalesDataCreditmemoExtensionInterface - a model defined in OpenAPI

        :param base_customer_balance_amount: The base_customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :param base_gift_cards_amount: The base_gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :param customer_balance_amount: The customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :param gift_cards_amount: The gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_base_price: The gw_base_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_base_tax_amount: The gw_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_card_base_price: The gw_card_base_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_card_base_tax_amount: The gw_card_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_card_price: The gw_card_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_card_tax_amount: The gw_card_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_items_base_price: The gw_items_base_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_items_base_tax_amount: The gw_items_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_items_price: The gw_items_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_items_tax_amount: The gw_items_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :param gw_price: The gw_price of this SalesDataCreditmemoExtensionInterface.
        :param gw_tax_amount: The gw_tax_amount of this SalesDataCreditmemoExtensionInterface.
        """
        self.openapi_types = {
            'base_customer_balance_amount': float,
            'base_gift_cards_amount': float,
            'customer_balance_amount': float,
            'gift_cards_amount': float,
            'gw_base_price': str,
            'gw_base_tax_amount': str,
            'gw_card_base_price': str,
            'gw_card_base_tax_amount': str,
            'gw_card_price': str,
            'gw_card_tax_amount': str,
            'gw_items_base_price': str,
            'gw_items_base_tax_amount': str,
            'gw_items_price': str,
            'gw_items_tax_amount': str,
            'gw_price': str,
            'gw_tax_amount': str
        }

        self.attribute_map = {
            'base_customer_balance_amount': 'base_customer_balance_amount',
            'base_gift_cards_amount': 'base_gift_cards_amount',
            'customer_balance_amount': 'customer_balance_amount',
            'gift_cards_amount': 'gift_cards_amount',
            'gw_base_price': 'gw_base_price',
            'gw_base_tax_amount': 'gw_base_tax_amount',
            'gw_card_base_price': 'gw_card_base_price',
            'gw_card_base_tax_amount': 'gw_card_base_tax_amount',
            'gw_card_price': 'gw_card_price',
            'gw_card_tax_amount': 'gw_card_tax_amount',
            'gw_items_base_price': 'gw_items_base_price',
            'gw_items_base_tax_amount': 'gw_items_base_tax_amount',
            'gw_items_price': 'gw_items_price',
            'gw_items_tax_amount': 'gw_items_tax_amount',
            'gw_price': 'gw_price',
            'gw_tax_amount': 'gw_tax_amount'
        }

        self._base_customer_balance_amount = base_customer_balance_amount
        self._base_gift_cards_amount = base_gift_cards_amount
        self._customer_balance_amount = customer_balance_amount
        self._gift_cards_amount = gift_cards_amount
        self._gw_base_price = gw_base_price
        self._gw_base_tax_amount = gw_base_tax_amount
        self._gw_card_base_price = gw_card_base_price
        self._gw_card_base_tax_amount = gw_card_base_tax_amount
        self._gw_card_price = gw_card_price
        self._gw_card_tax_amount = gw_card_tax_amount
        self._gw_items_base_price = gw_items_base_price
        self._gw_items_base_tax_amount = gw_items_base_tax_amount
        self._gw_items_price = gw_items_price
        self._gw_items_tax_amount = gw_items_tax_amount
        self._gw_price = gw_price
        self._gw_tax_amount = gw_tax_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataCreditmemoExtensionInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-creditmemo-extension-interface of this SalesDataCreditmemoExtensionInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_customer_balance_amount(self):
        """Gets the base_customer_balance_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The base_customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: float
        """
        return self._base_customer_balance_amount

    @base_customer_balance_amount.setter
    def base_customer_balance_amount(self, base_customer_balance_amount):
        """Sets the base_customer_balance_amount of this SalesDataCreditmemoExtensionInterface.


        :param base_customer_balance_amount: The base_customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :type base_customer_balance_amount: float
        """

        self._base_customer_balance_amount = base_customer_balance_amount

    @property
    def base_gift_cards_amount(self):
        """Gets the base_gift_cards_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The base_gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: float
        """
        return self._base_gift_cards_amount

    @base_gift_cards_amount.setter
    def base_gift_cards_amount(self, base_gift_cards_amount):
        """Sets the base_gift_cards_amount of this SalesDataCreditmemoExtensionInterface.


        :param base_gift_cards_amount: The base_gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :type base_gift_cards_amount: float
        """

        self._base_gift_cards_amount = base_gift_cards_amount

    @property
    def customer_balance_amount(self):
        """Gets the customer_balance_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: float
        """
        return self._customer_balance_amount

    @customer_balance_amount.setter
    def customer_balance_amount(self, customer_balance_amount):
        """Sets the customer_balance_amount of this SalesDataCreditmemoExtensionInterface.


        :param customer_balance_amount: The customer_balance_amount of this SalesDataCreditmemoExtensionInterface.
        :type customer_balance_amount: float
        """

        self._customer_balance_amount = customer_balance_amount

    @property
    def gift_cards_amount(self):
        """Gets the gift_cards_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: float
        """
        return self._gift_cards_amount

    @gift_cards_amount.setter
    def gift_cards_amount(self, gift_cards_amount):
        """Sets the gift_cards_amount of this SalesDataCreditmemoExtensionInterface.


        :param gift_cards_amount: The gift_cards_amount of this SalesDataCreditmemoExtensionInterface.
        :type gift_cards_amount: float
        """

        self._gift_cards_amount = gift_cards_amount

    @property
    def gw_base_price(self):
        """Gets the gw_base_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_base_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_base_price

    @gw_base_price.setter
    def gw_base_price(self, gw_base_price):
        """Sets the gw_base_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_base_price: The gw_base_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_base_price: str
        """

        self._gw_base_price = gw_base_price

    @property
    def gw_base_tax_amount(self):
        """Gets the gw_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_base_tax_amount

    @gw_base_tax_amount.setter
    def gw_base_tax_amount(self, gw_base_tax_amount):
        """Sets the gw_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_base_tax_amount: The gw_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_base_tax_amount: str
        """

        self._gw_base_tax_amount = gw_base_tax_amount

    @property
    def gw_card_base_price(self):
        """Gets the gw_card_base_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_card_base_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_card_base_price

    @gw_card_base_price.setter
    def gw_card_base_price(self, gw_card_base_price):
        """Sets the gw_card_base_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_card_base_price: The gw_card_base_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_card_base_price: str
        """

        self._gw_card_base_price = gw_card_base_price

    @property
    def gw_card_base_tax_amount(self):
        """Gets the gw_card_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_card_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_card_base_tax_amount

    @gw_card_base_tax_amount.setter
    def gw_card_base_tax_amount(self, gw_card_base_tax_amount):
        """Sets the gw_card_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_card_base_tax_amount: The gw_card_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_card_base_tax_amount: str
        """

        self._gw_card_base_tax_amount = gw_card_base_tax_amount

    @property
    def gw_card_price(self):
        """Gets the gw_card_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_card_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_card_price

    @gw_card_price.setter
    def gw_card_price(self, gw_card_price):
        """Sets the gw_card_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_card_price: The gw_card_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_card_price: str
        """

        self._gw_card_price = gw_card_price

    @property
    def gw_card_tax_amount(self):
        """Gets the gw_card_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_card_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_card_tax_amount

    @gw_card_tax_amount.setter
    def gw_card_tax_amount(self, gw_card_tax_amount):
        """Sets the gw_card_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_card_tax_amount: The gw_card_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_card_tax_amount: str
        """

        self._gw_card_tax_amount = gw_card_tax_amount

    @property
    def gw_items_base_price(self):
        """Gets the gw_items_base_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_items_base_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_items_base_price

    @gw_items_base_price.setter
    def gw_items_base_price(self, gw_items_base_price):
        """Sets the gw_items_base_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_items_base_price: The gw_items_base_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_items_base_price: str
        """

        self._gw_items_base_price = gw_items_base_price

    @property
    def gw_items_base_tax_amount(self):
        """Gets the gw_items_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_items_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_items_base_tax_amount

    @gw_items_base_tax_amount.setter
    def gw_items_base_tax_amount(self, gw_items_base_tax_amount):
        """Sets the gw_items_base_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_items_base_tax_amount: The gw_items_base_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_items_base_tax_amount: str
        """

        self._gw_items_base_tax_amount = gw_items_base_tax_amount

    @property
    def gw_items_price(self):
        """Gets the gw_items_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_items_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_items_price

    @gw_items_price.setter
    def gw_items_price(self, gw_items_price):
        """Sets the gw_items_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_items_price: The gw_items_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_items_price: str
        """

        self._gw_items_price = gw_items_price

    @property
    def gw_items_tax_amount(self):
        """Gets the gw_items_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_items_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_items_tax_amount

    @gw_items_tax_amount.setter
    def gw_items_tax_amount(self, gw_items_tax_amount):
        """Sets the gw_items_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_items_tax_amount: The gw_items_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_items_tax_amount: str
        """

        self._gw_items_tax_amount = gw_items_tax_amount

    @property
    def gw_price(self):
        """Gets the gw_price of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_price of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_price

    @gw_price.setter
    def gw_price(self, gw_price):
        """Sets the gw_price of this SalesDataCreditmemoExtensionInterface.


        :param gw_price: The gw_price of this SalesDataCreditmemoExtensionInterface.
        :type gw_price: str
        """

        self._gw_price = gw_price

    @property
    def gw_tax_amount(self):
        """Gets the gw_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :return: The gw_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :rtype: str
        """
        return self._gw_tax_amount

    @gw_tax_amount.setter
    def gw_tax_amount(self, gw_tax_amount):
        """Sets the gw_tax_amount of this SalesDataCreditmemoExtensionInterface.


        :param gw_tax_amount: The gw_tax_amount of this SalesDataCreditmemoExtensionInterface.
        :type gw_tax_amount: str
        """

        self._gw_tax_amount = gw_tax_amount
