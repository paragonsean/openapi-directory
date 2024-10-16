# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CalculateSimpleTaxIn(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: float=None, billing_country_code: str=None, buyer_credit_card_prefix: str=None, buyer_tax_number: str=None, currency_code: str=None, force_country_code: str=None, invoice_address_city: str=None, invoice_address_postal_code: str=None, invoice_address_region: str=None, order_date: str=None, product_type: str=None, quantity: float=None, tax_deducted: bool=None, total_amount: float=None, unit_price: float=None):
        """CalculateSimpleTaxIn - a model defined in OpenAPI

        :param amount: The amount of this CalculateSimpleTaxIn.
        :param billing_country_code: The billing_country_code of this CalculateSimpleTaxIn.
        :param buyer_credit_card_prefix: The buyer_credit_card_prefix of this CalculateSimpleTaxIn.
        :param buyer_tax_number: The buyer_tax_number of this CalculateSimpleTaxIn.
        :param currency_code: The currency_code of this CalculateSimpleTaxIn.
        :param force_country_code: The force_country_code of this CalculateSimpleTaxIn.
        :param invoice_address_city: The invoice_address_city of this CalculateSimpleTaxIn.
        :param invoice_address_postal_code: The invoice_address_postal_code of this CalculateSimpleTaxIn.
        :param invoice_address_region: The invoice_address_region of this CalculateSimpleTaxIn.
        :param order_date: The order_date of this CalculateSimpleTaxIn.
        :param product_type: The product_type of this CalculateSimpleTaxIn.
        :param quantity: The quantity of this CalculateSimpleTaxIn.
        :param tax_deducted: The tax_deducted of this CalculateSimpleTaxIn.
        :param total_amount: The total_amount of this CalculateSimpleTaxIn.
        :param unit_price: The unit_price of this CalculateSimpleTaxIn.
        """
        self.openapi_types = {
            'amount': float,
            'billing_country_code': str,
            'buyer_credit_card_prefix': str,
            'buyer_tax_number': str,
            'currency_code': str,
            'force_country_code': str,
            'invoice_address_city': str,
            'invoice_address_postal_code': str,
            'invoice_address_region': str,
            'order_date': str,
            'product_type': str,
            'quantity': float,
            'tax_deducted': bool,
            'total_amount': float,
            'unit_price': float
        }

        self.attribute_map = {
            'amount': 'amount',
            'billing_country_code': 'billing_country_code',
            'buyer_credit_card_prefix': 'buyer_credit_card_prefix',
            'buyer_tax_number': 'buyer_tax_number',
            'currency_code': 'currency_code',
            'force_country_code': 'force_country_code',
            'invoice_address_city': 'invoice_address_city',
            'invoice_address_postal_code': 'invoice_address_postal_code',
            'invoice_address_region': 'invoice_address_region',
            'order_date': 'order_date',
            'product_type': 'product_type',
            'quantity': 'quantity',
            'tax_deducted': 'tax_deducted',
            'total_amount': 'total_amount',
            'unit_price': 'unit_price'
        }

        self._amount = amount
        self._billing_country_code = billing_country_code
        self._buyer_credit_card_prefix = buyer_credit_card_prefix
        self._buyer_tax_number = buyer_tax_number
        self._currency_code = currency_code
        self._force_country_code = force_country_code
        self._invoice_address_city = invoice_address_city
        self._invoice_address_postal_code = invoice_address_postal_code
        self._invoice_address_region = invoice_address_region
        self._order_date = order_date
        self._product_type = product_type
        self._quantity = quantity
        self._tax_deducted = tax_deducted
        self._total_amount = total_amount
        self._unit_price = unit_price

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CalculateSimpleTaxIn':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The calculateSimpleTaxIn of this CalculateSimpleTaxIn.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this CalculateSimpleTaxIn.

        Amount. Required if total amount or both unit price and quantity are not provided.

        :return: The amount of this CalculateSimpleTaxIn.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CalculateSimpleTaxIn.

        Amount. Required if total amount or both unit price and quantity are not provided.

        :param amount: The amount of this CalculateSimpleTaxIn.
        :type amount: float
        """

        self._amount = amount

    @property
    def billing_country_code(self):
        """Gets the billing_country_code of this CalculateSimpleTaxIn.

        Billing two letter ISO country code.

        :return: The billing_country_code of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._billing_country_code

    @billing_country_code.setter
    def billing_country_code(self, billing_country_code):
        """Sets the billing_country_code of this CalculateSimpleTaxIn.

        Billing two letter ISO country code.

        :param billing_country_code: The billing_country_code of this CalculateSimpleTaxIn.
        :type billing_country_code: str
        """

        self._billing_country_code = billing_country_code

    @property
    def buyer_credit_card_prefix(self):
        """Gets the buyer_credit_card_prefix of this CalculateSimpleTaxIn.

        First 6 digits of buyer's credit card prefix.

        :return: The buyer_credit_card_prefix of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._buyer_credit_card_prefix

    @buyer_credit_card_prefix.setter
    def buyer_credit_card_prefix(self, buyer_credit_card_prefix):
        """Sets the buyer_credit_card_prefix of this CalculateSimpleTaxIn.

        First 6 digits of buyer's credit card prefix.

        :param buyer_credit_card_prefix: The buyer_credit_card_prefix of this CalculateSimpleTaxIn.
        :type buyer_credit_card_prefix: str
        """

        self._buyer_credit_card_prefix = buyer_credit_card_prefix

    @property
    def buyer_tax_number(self):
        """Gets the buyer_tax_number of this CalculateSimpleTaxIn.

         Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.

        :return: The buyer_tax_number of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._buyer_tax_number

    @buyer_tax_number.setter
    def buyer_tax_number(self, buyer_tax_number):
        """Sets the buyer_tax_number of this CalculateSimpleTaxIn.

         Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.

        :param buyer_tax_number: The buyer_tax_number of this CalculateSimpleTaxIn.
        :type buyer_tax_number: str
        """

        self._buyer_tax_number = buyer_tax_number

    @property
    def currency_code(self):
        """Gets the currency_code of this CalculateSimpleTaxIn.

        Currency code for transaction - e.g. EUR.

        :return: The currency_code of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CalculateSimpleTaxIn.

        Currency code for transaction - e.g. EUR.

        :param currency_code: The currency_code of this CalculateSimpleTaxIn.
        :type currency_code: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def force_country_code(self):
        """Gets the force_country_code of this CalculateSimpleTaxIn.

        Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.

        :return: The force_country_code of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._force_country_code

    @force_country_code.setter
    def force_country_code(self, force_country_code):
        """Sets the force_country_code of this CalculateSimpleTaxIn.

        Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.

        :param force_country_code: The force_country_code of this CalculateSimpleTaxIn.
        :type force_country_code: str
        """

        self._force_country_code = force_country_code

    @property
    def invoice_address_city(self):
        """Gets the invoice_address_city of this CalculateSimpleTaxIn.

        Invoice address/postal_code

        :return: The invoice_address_city of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._invoice_address_city

    @invoice_address_city.setter
    def invoice_address_city(self, invoice_address_city):
        """Sets the invoice_address_city of this CalculateSimpleTaxIn.

        Invoice address/postal_code

        :param invoice_address_city: The invoice_address_city of this CalculateSimpleTaxIn.
        :type invoice_address_city: str
        """

        self._invoice_address_city = invoice_address_city

    @property
    def invoice_address_postal_code(self):
        """Gets the invoice_address_postal_code of this CalculateSimpleTaxIn.

        Invoice address/postal_code

        :return: The invoice_address_postal_code of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._invoice_address_postal_code

    @invoice_address_postal_code.setter
    def invoice_address_postal_code(self, invoice_address_postal_code):
        """Sets the invoice_address_postal_code of this CalculateSimpleTaxIn.

        Invoice address/postal_code

        :param invoice_address_postal_code: The invoice_address_postal_code of this CalculateSimpleTaxIn.
        :type invoice_address_postal_code: str
        """

        self._invoice_address_postal_code = invoice_address_postal_code

    @property
    def invoice_address_region(self):
        """Gets the invoice_address_region of this CalculateSimpleTaxIn.

        Invoice address/region

        :return: The invoice_address_region of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._invoice_address_region

    @invoice_address_region.setter
    def invoice_address_region(self, invoice_address_region):
        """Sets the invoice_address_region of this CalculateSimpleTaxIn.

        Invoice address/region

        :param invoice_address_region: The invoice_address_region of this CalculateSimpleTaxIn.
        :type invoice_address_region: str
        """

        self._invoice_address_region = invoice_address_region

    @property
    def order_date(self):
        """Gets the order_date of this CalculateSimpleTaxIn.

        Order date in yyyy-MM-dd format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.

        :return: The order_date of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this CalculateSimpleTaxIn.

        Order date in yyyy-MM-dd format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.

        :param order_date: The order_date of this CalculateSimpleTaxIn.
        :type order_date: str
        """

        self._order_date = order_date

    @property
    def product_type(self):
        """Gets the product_type of this CalculateSimpleTaxIn.

        Product type, according to dictionary /dictionaries/product_types. 

        :return: The product_type of this CalculateSimpleTaxIn.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this CalculateSimpleTaxIn.

        Product type, according to dictionary /dictionaries/product_types. 

        :param product_type: The product_type of this CalculateSimpleTaxIn.
        :type product_type: str
        """

        self._product_type = product_type

    @property
    def quantity(self):
        """Gets the quantity of this CalculateSimpleTaxIn.

        Quantity Defaults to 1.

        :return: The quantity of this CalculateSimpleTaxIn.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CalculateSimpleTaxIn.

        Quantity Defaults to 1.

        :param quantity: The quantity of this CalculateSimpleTaxIn.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def tax_deducted(self):
        """Gets the tax_deducted of this CalculateSimpleTaxIn.

        If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.

        :return: The tax_deducted of this CalculateSimpleTaxIn.
        :rtype: bool
        """
        return self._tax_deducted

    @tax_deducted.setter
    def tax_deducted(self, tax_deducted):
        """Sets the tax_deducted of this CalculateSimpleTaxIn.

        If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.

        :param tax_deducted: The tax_deducted of this CalculateSimpleTaxIn.
        :type tax_deducted: bool
        """

        self._tax_deducted = tax_deducted

    @property
    def total_amount(self):
        """Gets the total_amount of this CalculateSimpleTaxIn.

        Total amount. Required if amount or both unit price and quantity are not provided.

        :return: The total_amount of this CalculateSimpleTaxIn.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CalculateSimpleTaxIn.

        Total amount. Required if amount or both unit price and quantity are not provided.

        :param total_amount: The total_amount of this CalculateSimpleTaxIn.
        :type total_amount: float
        """

        self._total_amount = total_amount

    @property
    def unit_price(self):
        """Gets the unit_price of this CalculateSimpleTaxIn.

        Unit price.

        :return: The unit_price of this CalculateSimpleTaxIn.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this CalculateSimpleTaxIn.

        Unit price.

        :param unit_price: The unit_price of this CalculateSimpleTaxIn.
        :type unit_price: float
        """

        self._unit_price = unit_price
