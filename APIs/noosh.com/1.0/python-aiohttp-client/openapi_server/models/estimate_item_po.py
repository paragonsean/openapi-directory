# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.paper_item_po import PaperItemPO
from openapi_server import util


class EstimateItemPO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, paper_items: List[PaperItemPO]=None, quantity_1_price: object=None, quantity_1_shipping: object=None, quantity_1_tax: object=None, quantity_2_price: object=None, quantity_2_shipping: object=None, quantity_2_tax: object=None, quantity_3_price: object=None, quantity_3_shipping: object=None, quantity_3_tax: object=None, quantity_4_price: object=None, quantity_4_shipping: object=None, quantity_4_tax: object=None, quantity_5_price: object=None, quantity_5_shipping: object=None, quantity_5_tax: object=None, rfe_item_id: int=None):
        """EstimateItemPO - a model defined in OpenAPI

        :param paper_items: The paper_items of this EstimateItemPO.
        :param quantity_1_price: The quantity_1_price of this EstimateItemPO.
        :param quantity_1_shipping: The quantity_1_shipping of this EstimateItemPO.
        :param quantity_1_tax: The quantity_1_tax of this EstimateItemPO.
        :param quantity_2_price: The quantity_2_price of this EstimateItemPO.
        :param quantity_2_shipping: The quantity_2_shipping of this EstimateItemPO.
        :param quantity_2_tax: The quantity_2_tax of this EstimateItemPO.
        :param quantity_3_price: The quantity_3_price of this EstimateItemPO.
        :param quantity_3_shipping: The quantity_3_shipping of this EstimateItemPO.
        :param quantity_3_tax: The quantity_3_tax of this EstimateItemPO.
        :param quantity_4_price: The quantity_4_price of this EstimateItemPO.
        :param quantity_4_shipping: The quantity_4_shipping of this EstimateItemPO.
        :param quantity_4_tax: The quantity_4_tax of this EstimateItemPO.
        :param quantity_5_price: The quantity_5_price of this EstimateItemPO.
        :param quantity_5_shipping: The quantity_5_shipping of this EstimateItemPO.
        :param quantity_5_tax: The quantity_5_tax of this EstimateItemPO.
        :param rfe_item_id: The rfe_item_id of this EstimateItemPO.
        """
        self.openapi_types = {
            'paper_items': List[PaperItemPO],
            'quantity_1_price': object,
            'quantity_1_shipping': object,
            'quantity_1_tax': object,
            'quantity_2_price': object,
            'quantity_2_shipping': object,
            'quantity_2_tax': object,
            'quantity_3_price': object,
            'quantity_3_shipping': object,
            'quantity_3_tax': object,
            'quantity_4_price': object,
            'quantity_4_shipping': object,
            'quantity_4_tax': object,
            'quantity_5_price': object,
            'quantity_5_shipping': object,
            'quantity_5_tax': object,
            'rfe_item_id': int
        }

        self.attribute_map = {
            'paper_items': 'paper_items',
            'quantity_1_price': 'quantity_1_price',
            'quantity_1_shipping': 'quantity_1_shipping',
            'quantity_1_tax': 'quantity_1_tax',
            'quantity_2_price': 'quantity_2_price',
            'quantity_2_shipping': 'quantity_2_shipping',
            'quantity_2_tax': 'quantity_2_tax',
            'quantity_3_price': 'quantity_3_price',
            'quantity_3_shipping': 'quantity_3_shipping',
            'quantity_3_tax': 'quantity_3_tax',
            'quantity_4_price': 'quantity_4_price',
            'quantity_4_shipping': 'quantity_4_shipping',
            'quantity_4_tax': 'quantity_4_tax',
            'quantity_5_price': 'quantity_5_price',
            'quantity_5_shipping': 'quantity_5_shipping',
            'quantity_5_tax': 'quantity_5_tax',
            'rfe_item_id': 'rfe_item_id'
        }

        self._paper_items = paper_items
        self._quantity_1_price = quantity_1_price
        self._quantity_1_shipping = quantity_1_shipping
        self._quantity_1_tax = quantity_1_tax
        self._quantity_2_price = quantity_2_price
        self._quantity_2_shipping = quantity_2_shipping
        self._quantity_2_tax = quantity_2_tax
        self._quantity_3_price = quantity_3_price
        self._quantity_3_shipping = quantity_3_shipping
        self._quantity_3_tax = quantity_3_tax
        self._quantity_4_price = quantity_4_price
        self._quantity_4_shipping = quantity_4_shipping
        self._quantity_4_tax = quantity_4_tax
        self._quantity_5_price = quantity_5_price
        self._quantity_5_shipping = quantity_5_shipping
        self._quantity_5_tax = quantity_5_tax
        self._rfe_item_id = rfe_item_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EstimateItemPO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EstimateItemPO of this EstimateItemPO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paper_items(self):
        """Gets the paper_items of this EstimateItemPO.

        

        :return: The paper_items of this EstimateItemPO.
        :rtype: List[PaperItemPO]
        """
        return self._paper_items

    @paper_items.setter
    def paper_items(self, paper_items):
        """Sets the paper_items of this EstimateItemPO.

        

        :param paper_items: The paper_items of this EstimateItemPO.
        :type paper_items: List[PaperItemPO]
        """

        self._paper_items = paper_items

    @property
    def quantity_1_price(self):
        """Gets the quantity_1_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_1_price of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_1_price

    @quantity_1_price.setter
    def quantity_1_price(self, quantity_1_price):
        """Sets the quantity_1_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_1_price: The quantity_1_price of this EstimateItemPO.
        :type quantity_1_price: object
        """

        self._quantity_1_price = quantity_1_price

    @property
    def quantity_1_shipping(self):
        """Gets the quantity_1_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_1_shipping of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_1_shipping

    @quantity_1_shipping.setter
    def quantity_1_shipping(self, quantity_1_shipping):
        """Sets the quantity_1_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_1_shipping: The quantity_1_shipping of this EstimateItemPO.
        :type quantity_1_shipping: object
        """

        self._quantity_1_shipping = quantity_1_shipping

    @property
    def quantity_1_tax(self):
        """Gets the quantity_1_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_1_tax of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_1_tax

    @quantity_1_tax.setter
    def quantity_1_tax(self, quantity_1_tax):
        """Sets the quantity_1_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_1_tax: The quantity_1_tax of this EstimateItemPO.
        :type quantity_1_tax: object
        """

        self._quantity_1_tax = quantity_1_tax

    @property
    def quantity_2_price(self):
        """Gets the quantity_2_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_2_price of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_2_price

    @quantity_2_price.setter
    def quantity_2_price(self, quantity_2_price):
        """Sets the quantity_2_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_2_price: The quantity_2_price of this EstimateItemPO.
        :type quantity_2_price: object
        """

        self._quantity_2_price = quantity_2_price

    @property
    def quantity_2_shipping(self):
        """Gets the quantity_2_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_2_shipping of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_2_shipping

    @quantity_2_shipping.setter
    def quantity_2_shipping(self, quantity_2_shipping):
        """Sets the quantity_2_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_2_shipping: The quantity_2_shipping of this EstimateItemPO.
        :type quantity_2_shipping: object
        """

        self._quantity_2_shipping = quantity_2_shipping

    @property
    def quantity_2_tax(self):
        """Gets the quantity_2_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_2_tax of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_2_tax

    @quantity_2_tax.setter
    def quantity_2_tax(self, quantity_2_tax):
        """Sets the quantity_2_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_2_tax: The quantity_2_tax of this EstimateItemPO.
        :type quantity_2_tax: object
        """

        self._quantity_2_tax = quantity_2_tax

    @property
    def quantity_3_price(self):
        """Gets the quantity_3_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_3_price of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_3_price

    @quantity_3_price.setter
    def quantity_3_price(self, quantity_3_price):
        """Sets the quantity_3_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_3_price: The quantity_3_price of this EstimateItemPO.
        :type quantity_3_price: object
        """

        self._quantity_3_price = quantity_3_price

    @property
    def quantity_3_shipping(self):
        """Gets the quantity_3_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_3_shipping of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_3_shipping

    @quantity_3_shipping.setter
    def quantity_3_shipping(self, quantity_3_shipping):
        """Sets the quantity_3_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_3_shipping: The quantity_3_shipping of this EstimateItemPO.
        :type quantity_3_shipping: object
        """

        self._quantity_3_shipping = quantity_3_shipping

    @property
    def quantity_3_tax(self):
        """Gets the quantity_3_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_3_tax of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_3_tax

    @quantity_3_tax.setter
    def quantity_3_tax(self, quantity_3_tax):
        """Sets the quantity_3_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_3_tax: The quantity_3_tax of this EstimateItemPO.
        :type quantity_3_tax: object
        """

        self._quantity_3_tax = quantity_3_tax

    @property
    def quantity_4_price(self):
        """Gets the quantity_4_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_4_price of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_4_price

    @quantity_4_price.setter
    def quantity_4_price(self, quantity_4_price):
        """Sets the quantity_4_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_4_price: The quantity_4_price of this EstimateItemPO.
        :type quantity_4_price: object
        """

        self._quantity_4_price = quantity_4_price

    @property
    def quantity_4_shipping(self):
        """Gets the quantity_4_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_4_shipping of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_4_shipping

    @quantity_4_shipping.setter
    def quantity_4_shipping(self, quantity_4_shipping):
        """Sets the quantity_4_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_4_shipping: The quantity_4_shipping of this EstimateItemPO.
        :type quantity_4_shipping: object
        """

        self._quantity_4_shipping = quantity_4_shipping

    @property
    def quantity_4_tax(self):
        """Gets the quantity_4_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_4_tax of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_4_tax

    @quantity_4_tax.setter
    def quantity_4_tax(self, quantity_4_tax):
        """Sets the quantity_4_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_4_tax: The quantity_4_tax of this EstimateItemPO.
        :type quantity_4_tax: object
        """

        self._quantity_4_tax = quantity_4_tax

    @property
    def quantity_5_price(self):
        """Gets the quantity_5_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_5_price of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_5_price

    @quantity_5_price.setter
    def quantity_5_price(self, quantity_5_price):
        """Sets the quantity_5_price of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_5_price: The quantity_5_price of this EstimateItemPO.
        :type quantity_5_price: object
        """

        self._quantity_5_price = quantity_5_price

    @property
    def quantity_5_shipping(self):
        """Gets the quantity_5_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_5_shipping of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_5_shipping

    @quantity_5_shipping.setter
    def quantity_5_shipping(self, quantity_5_shipping):
        """Sets the quantity_5_shipping of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_5_shipping: The quantity_5_shipping of this EstimateItemPO.
        :type quantity_5_shipping: object
        """

        self._quantity_5_shipping = quantity_5_shipping

    @property
    def quantity_5_tax(self):
        """Gets the quantity_5_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :return: The quantity_5_tax of this EstimateItemPO.
        :rtype: object
        """
        return self._quantity_5_tax

    @quantity_5_tax.setter
    def quantity_5_tax(self, quantity_5_tax):
        """Sets the quantity_5_tax of this EstimateItemPO.

        Java type: java.math.BigDecimal

        :param quantity_5_tax: The quantity_5_tax of this EstimateItemPO.
        :type quantity_5_tax: object
        """

        self._quantity_5_tax = quantity_5_tax

    @property
    def rfe_item_id(self):
        """Gets the rfe_item_id of this EstimateItemPO.

        

        :return: The rfe_item_id of this EstimateItemPO.
        :rtype: int
        """
        return self._rfe_item_id

    @rfe_item_id.setter
    def rfe_item_id(self, rfe_item_id):
        """Sets the rfe_item_id of this EstimateItemPO.

        

        :param rfe_item_id: The rfe_item_id of this EstimateItemPO.
        :type rfe_item_id: int
        """

        self._rfe_item_id = rfe_item_id
