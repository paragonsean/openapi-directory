# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sales_data_invoice_item_extension_interface import SalesDataInvoiceItemExtensionInterface
from openapi_server import util


class SalesDataInvoiceItemInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_data: str=None, base_cost: float=None, base_discount_amount: float=None, base_discount_tax_compensation_amount: float=None, base_price: float=None, base_price_incl_tax: float=None, base_row_total: float=None, base_row_total_incl_tax: float=None, base_tax_amount: float=None, description: str=None, discount_amount: float=None, discount_tax_compensation_amount: float=None, entity_id: int=None, extension_attributes: SalesDataInvoiceItemExtensionInterface=None, name: str=None, order_item_id: int=None, parent_id: int=None, price: float=None, price_incl_tax: float=None, product_id: int=None, qty: float=None, row_total: float=None, row_total_incl_tax: float=None, sku: str=None, tax_amount: float=None):
        """SalesDataInvoiceItemInterface - a model defined in OpenAPI

        :param additional_data: The additional_data of this SalesDataInvoiceItemInterface.
        :param base_cost: The base_cost of this SalesDataInvoiceItemInterface.
        :param base_discount_amount: The base_discount_amount of this SalesDataInvoiceItemInterface.
        :param base_discount_tax_compensation_amount: The base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :param base_price: The base_price of this SalesDataInvoiceItemInterface.
        :param base_price_incl_tax: The base_price_incl_tax of this SalesDataInvoiceItemInterface.
        :param base_row_total: The base_row_total of this SalesDataInvoiceItemInterface.
        :param base_row_total_incl_tax: The base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :param base_tax_amount: The base_tax_amount of this SalesDataInvoiceItemInterface.
        :param description: The description of this SalesDataInvoiceItemInterface.
        :param discount_amount: The discount_amount of this SalesDataInvoiceItemInterface.
        :param discount_tax_compensation_amount: The discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :param entity_id: The entity_id of this SalesDataInvoiceItemInterface.
        :param extension_attributes: The extension_attributes of this SalesDataInvoiceItemInterface.
        :param name: The name of this SalesDataInvoiceItemInterface.
        :param order_item_id: The order_item_id of this SalesDataInvoiceItemInterface.
        :param parent_id: The parent_id of this SalesDataInvoiceItemInterface.
        :param price: The price of this SalesDataInvoiceItemInterface.
        :param price_incl_tax: The price_incl_tax of this SalesDataInvoiceItemInterface.
        :param product_id: The product_id of this SalesDataInvoiceItemInterface.
        :param qty: The qty of this SalesDataInvoiceItemInterface.
        :param row_total: The row_total of this SalesDataInvoiceItemInterface.
        :param row_total_incl_tax: The row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :param sku: The sku of this SalesDataInvoiceItemInterface.
        :param tax_amount: The tax_amount of this SalesDataInvoiceItemInterface.
        """
        self.openapi_types = {
            'additional_data': str,
            'base_cost': float,
            'base_discount_amount': float,
            'base_discount_tax_compensation_amount': float,
            'base_price': float,
            'base_price_incl_tax': float,
            'base_row_total': float,
            'base_row_total_incl_tax': float,
            'base_tax_amount': float,
            'description': str,
            'discount_amount': float,
            'discount_tax_compensation_amount': float,
            'entity_id': int,
            'extension_attributes': SalesDataInvoiceItemExtensionInterface,
            'name': str,
            'order_item_id': int,
            'parent_id': int,
            'price': float,
            'price_incl_tax': float,
            'product_id': int,
            'qty': float,
            'row_total': float,
            'row_total_incl_tax': float,
            'sku': str,
            'tax_amount': float
        }

        self.attribute_map = {
            'additional_data': 'additional_data',
            'base_cost': 'base_cost',
            'base_discount_amount': 'base_discount_amount',
            'base_discount_tax_compensation_amount': 'base_discount_tax_compensation_amount',
            'base_price': 'base_price',
            'base_price_incl_tax': 'base_price_incl_tax',
            'base_row_total': 'base_row_total',
            'base_row_total_incl_tax': 'base_row_total_incl_tax',
            'base_tax_amount': 'base_tax_amount',
            'description': 'description',
            'discount_amount': 'discount_amount',
            'discount_tax_compensation_amount': 'discount_tax_compensation_amount',
            'entity_id': 'entity_id',
            'extension_attributes': 'extension_attributes',
            'name': 'name',
            'order_item_id': 'order_item_id',
            'parent_id': 'parent_id',
            'price': 'price',
            'price_incl_tax': 'price_incl_tax',
            'product_id': 'product_id',
            'qty': 'qty',
            'row_total': 'row_total',
            'row_total_incl_tax': 'row_total_incl_tax',
            'sku': 'sku',
            'tax_amount': 'tax_amount'
        }

        self._additional_data = additional_data
        self._base_cost = base_cost
        self._base_discount_amount = base_discount_amount
        self._base_discount_tax_compensation_amount = base_discount_tax_compensation_amount
        self._base_price = base_price
        self._base_price_incl_tax = base_price_incl_tax
        self._base_row_total = base_row_total
        self._base_row_total_incl_tax = base_row_total_incl_tax
        self._base_tax_amount = base_tax_amount
        self._description = description
        self._discount_amount = discount_amount
        self._discount_tax_compensation_amount = discount_tax_compensation_amount
        self._entity_id = entity_id
        self._extension_attributes = extension_attributes
        self._name = name
        self._order_item_id = order_item_id
        self._parent_id = parent_id
        self._price = price
        self._price_incl_tax = price_incl_tax
        self._product_id = product_id
        self._qty = qty
        self._row_total = row_total
        self._row_total_incl_tax = row_total_incl_tax
        self._sku = sku
        self._tax_amount = tax_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataInvoiceItemInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-invoice-item-interface of this SalesDataInvoiceItemInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_data(self):
        """Gets the additional_data of this SalesDataInvoiceItemInterface.

        Additional data.

        :return: The additional_data of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this SalesDataInvoiceItemInterface.

        Additional data.

        :param additional_data: The additional_data of this SalesDataInvoiceItemInterface.
        :type additional_data: str
        """

        self._additional_data = additional_data

    @property
    def base_cost(self):
        """Gets the base_cost of this SalesDataInvoiceItemInterface.

        Base cost.

        :return: The base_cost of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_cost

    @base_cost.setter
    def base_cost(self, base_cost):
        """Sets the base_cost of this SalesDataInvoiceItemInterface.

        Base cost.

        :param base_cost: The base_cost of this SalesDataInvoiceItemInterface.
        :type base_cost: float
        """

        self._base_cost = base_cost

    @property
    def base_discount_amount(self):
        """Gets the base_discount_amount of this SalesDataInvoiceItemInterface.

        Base discount amount.

        :return: The base_discount_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_discount_amount

    @base_discount_amount.setter
    def base_discount_amount(self, base_discount_amount):
        """Sets the base_discount_amount of this SalesDataInvoiceItemInterface.

        Base discount amount.

        :param base_discount_amount: The base_discount_amount of this SalesDataInvoiceItemInterface.
        :type base_discount_amount: float
        """

        self._base_discount_amount = base_discount_amount

    @property
    def base_discount_tax_compensation_amount(self):
        """Gets the base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.

        Base discount tax compensation amount.

        :return: The base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_discount_tax_compensation_amount

    @base_discount_tax_compensation_amount.setter
    def base_discount_tax_compensation_amount(self, base_discount_tax_compensation_amount):
        """Sets the base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.

        Base discount tax compensation amount.

        :param base_discount_tax_compensation_amount: The base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :type base_discount_tax_compensation_amount: float
        """

        self._base_discount_tax_compensation_amount = base_discount_tax_compensation_amount

    @property
    def base_price(self):
        """Gets the base_price of this SalesDataInvoiceItemInterface.

        Base price.

        :return: The base_price of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this SalesDataInvoiceItemInterface.

        Base price.

        :param base_price: The base_price of this SalesDataInvoiceItemInterface.
        :type base_price: float
        """

        self._base_price = base_price

    @property
    def base_price_incl_tax(self):
        """Gets the base_price_incl_tax of this SalesDataInvoiceItemInterface.

        Base price including tax.

        :return: The base_price_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_price_incl_tax

    @base_price_incl_tax.setter
    def base_price_incl_tax(self, base_price_incl_tax):
        """Sets the base_price_incl_tax of this SalesDataInvoiceItemInterface.

        Base price including tax.

        :param base_price_incl_tax: The base_price_incl_tax of this SalesDataInvoiceItemInterface.
        :type base_price_incl_tax: float
        """

        self._base_price_incl_tax = base_price_incl_tax

    @property
    def base_row_total(self):
        """Gets the base_row_total of this SalesDataInvoiceItemInterface.

        Base row total.

        :return: The base_row_total of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_row_total

    @base_row_total.setter
    def base_row_total(self, base_row_total):
        """Sets the base_row_total of this SalesDataInvoiceItemInterface.

        Base row total.

        :param base_row_total: The base_row_total of this SalesDataInvoiceItemInterface.
        :type base_row_total: float
        """

        self._base_row_total = base_row_total

    @property
    def base_row_total_incl_tax(self):
        """Gets the base_row_total_incl_tax of this SalesDataInvoiceItemInterface.

        Base row total including tax.

        :return: The base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_row_total_incl_tax

    @base_row_total_incl_tax.setter
    def base_row_total_incl_tax(self, base_row_total_incl_tax):
        """Sets the base_row_total_incl_tax of this SalesDataInvoiceItemInterface.

        Base row total including tax.

        :param base_row_total_incl_tax: The base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :type base_row_total_incl_tax: float
        """

        self._base_row_total_incl_tax = base_row_total_incl_tax

    @property
    def base_tax_amount(self):
        """Gets the base_tax_amount of this SalesDataInvoiceItemInterface.

        Base tax amount.

        :return: The base_tax_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_tax_amount

    @base_tax_amount.setter
    def base_tax_amount(self, base_tax_amount):
        """Sets the base_tax_amount of this SalesDataInvoiceItemInterface.

        Base tax amount.

        :param base_tax_amount: The base_tax_amount of this SalesDataInvoiceItemInterface.
        :type base_tax_amount: float
        """

        self._base_tax_amount = base_tax_amount

    @property
    def description(self):
        """Gets the description of this SalesDataInvoiceItemInterface.

        Description.

        :return: The description of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SalesDataInvoiceItemInterface.

        Description.

        :param description: The description of this SalesDataInvoiceItemInterface.
        :type description: str
        """

        self._description = description

    @property
    def discount_amount(self):
        """Gets the discount_amount of this SalesDataInvoiceItemInterface.

        Discount amount.

        :return: The discount_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this SalesDataInvoiceItemInterface.

        Discount amount.

        :param discount_amount: The discount_amount of this SalesDataInvoiceItemInterface.
        :type discount_amount: float
        """

        self._discount_amount = discount_amount

    @property
    def discount_tax_compensation_amount(self):
        """Gets the discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.

        Discount tax compensation amount.

        :return: The discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._discount_tax_compensation_amount

    @discount_tax_compensation_amount.setter
    def discount_tax_compensation_amount(self, discount_tax_compensation_amount):
        """Sets the discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.

        Discount tax compensation amount.

        :param discount_tax_compensation_amount: The discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :type discount_tax_compensation_amount: float
        """

        self._discount_tax_compensation_amount = discount_tax_compensation_amount

    @property
    def entity_id(self):
        """Gets the entity_id of this SalesDataInvoiceItemInterface.

        Invoice item ID.

        :return: The entity_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this SalesDataInvoiceItemInterface.

        Invoice item ID.

        :param entity_id: The entity_id of this SalesDataInvoiceItemInterface.
        :type entity_id: int
        """

        self._entity_id = entity_id

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this SalesDataInvoiceItemInterface.


        :return: The extension_attributes of this SalesDataInvoiceItemInterface.
        :rtype: SalesDataInvoiceItemExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this SalesDataInvoiceItemInterface.


        :param extension_attributes: The extension_attributes of this SalesDataInvoiceItemInterface.
        :type extension_attributes: SalesDataInvoiceItemExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def name(self):
        """Gets the name of this SalesDataInvoiceItemInterface.

        Name.

        :return: The name of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SalesDataInvoiceItemInterface.

        Name.

        :param name: The name of this SalesDataInvoiceItemInterface.
        :type name: str
        """

        self._name = name

    @property
    def order_item_id(self):
        """Gets the order_item_id of this SalesDataInvoiceItemInterface.

        Order item ID.

        :return: The order_item_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """Sets the order_item_id of this SalesDataInvoiceItemInterface.

        Order item ID.

        :param order_item_id: The order_item_id of this SalesDataInvoiceItemInterface.
        :type order_item_id: int
        """
        if order_item_id is None:
            raise ValueError("Invalid value for `order_item_id`, must not be `None`")

        self._order_item_id = order_item_id

    @property
    def parent_id(self):
        """Gets the parent_id of this SalesDataInvoiceItemInterface.

        Parent ID.

        :return: The parent_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SalesDataInvoiceItemInterface.

        Parent ID.

        :param parent_id: The parent_id of this SalesDataInvoiceItemInterface.
        :type parent_id: int
        """

        self._parent_id = parent_id

    @property
    def price(self):
        """Gets the price of this SalesDataInvoiceItemInterface.

        Price.

        :return: The price of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SalesDataInvoiceItemInterface.

        Price.

        :param price: The price of this SalesDataInvoiceItemInterface.
        :type price: float
        """

        self._price = price

    @property
    def price_incl_tax(self):
        """Gets the price_incl_tax of this SalesDataInvoiceItemInterface.

        Price including tax.

        :return: The price_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._price_incl_tax

    @price_incl_tax.setter
    def price_incl_tax(self, price_incl_tax):
        """Sets the price_incl_tax of this SalesDataInvoiceItemInterface.

        Price including tax.

        :param price_incl_tax: The price_incl_tax of this SalesDataInvoiceItemInterface.
        :type price_incl_tax: float
        """

        self._price_incl_tax = price_incl_tax

    @property
    def product_id(self):
        """Gets the product_id of this SalesDataInvoiceItemInterface.

        Product ID.

        :return: The product_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this SalesDataInvoiceItemInterface.

        Product ID.

        :param product_id: The product_id of this SalesDataInvoiceItemInterface.
        :type product_id: int
        """

        self._product_id = product_id

    @property
    def qty(self):
        """Gets the qty of this SalesDataInvoiceItemInterface.

        Quantity.

        :return: The qty of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this SalesDataInvoiceItemInterface.

        Quantity.

        :param qty: The qty of this SalesDataInvoiceItemInterface.
        :type qty: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

    @property
    def row_total(self):
        """Gets the row_total of this SalesDataInvoiceItemInterface.

        Row total.

        :return: The row_total of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._row_total

    @row_total.setter
    def row_total(self, row_total):
        """Sets the row_total of this SalesDataInvoiceItemInterface.

        Row total.

        :param row_total: The row_total of this SalesDataInvoiceItemInterface.
        :type row_total: float
        """

        self._row_total = row_total

    @property
    def row_total_incl_tax(self):
        """Gets the row_total_incl_tax of this SalesDataInvoiceItemInterface.

        Row total including tax.

        :return: The row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._row_total_incl_tax

    @row_total_incl_tax.setter
    def row_total_incl_tax(self, row_total_incl_tax):
        """Sets the row_total_incl_tax of this SalesDataInvoiceItemInterface.

        Row total including tax.

        :param row_total_incl_tax: The row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :type row_total_incl_tax: float
        """

        self._row_total_incl_tax = row_total_incl_tax

    @property
    def sku(self):
        """Gets the sku of this SalesDataInvoiceItemInterface.

        SKU.

        :return: The sku of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this SalesDataInvoiceItemInterface.

        SKU.

        :param sku: The sku of this SalesDataInvoiceItemInterface.
        :type sku: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def tax_amount(self):
        """Gets the tax_amount of this SalesDataInvoiceItemInterface.

        Tax amount.

        :return: The tax_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this SalesDataInvoiceItemInterface.

        Tax amount.

        :param tax_amount: The tax_amount of this SalesDataInvoiceItemInterface.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount
