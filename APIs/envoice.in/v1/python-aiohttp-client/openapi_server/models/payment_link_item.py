# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tax import Tax
from openapi_server.models.work_type import WorkType
from openapi_server import util


class PaymentLinkItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cost: float=None, discount_amount: float=None, discount_percentage: float=None, id: int=None, payment_link_id: int=None, quantity: float=None, sub_total_amount: float=None, tax: Tax=None, tax_amount: float=None, tax_id: int=None, tax_percentage: float=None, total_amount: float=None, work_type: WorkType=None, work_type_id: int=None):
        """PaymentLinkItem - a model defined in OpenAPI

        :param cost: The cost of this PaymentLinkItem.
        :param discount_amount: The discount_amount of this PaymentLinkItem.
        :param discount_percentage: The discount_percentage of this PaymentLinkItem.
        :param id: The id of this PaymentLinkItem.
        :param payment_link_id: The payment_link_id of this PaymentLinkItem.
        :param quantity: The quantity of this PaymentLinkItem.
        :param sub_total_amount: The sub_total_amount of this PaymentLinkItem.
        :param tax: The tax of this PaymentLinkItem.
        :param tax_amount: The tax_amount of this PaymentLinkItem.
        :param tax_id: The tax_id of this PaymentLinkItem.
        :param tax_percentage: The tax_percentage of this PaymentLinkItem.
        :param total_amount: The total_amount of this PaymentLinkItem.
        :param work_type: The work_type of this PaymentLinkItem.
        :param work_type_id: The work_type_id of this PaymentLinkItem.
        """
        self.openapi_types = {
            'cost': float,
            'discount_amount': float,
            'discount_percentage': float,
            'id': int,
            'payment_link_id': int,
            'quantity': float,
            'sub_total_amount': float,
            'tax': Tax,
            'tax_amount': float,
            'tax_id': int,
            'tax_percentage': float,
            'total_amount': float,
            'work_type': WorkType,
            'work_type_id': int
        }

        self.attribute_map = {
            'cost': 'Cost',
            'discount_amount': 'DiscountAmount',
            'discount_percentage': 'DiscountPercentage',
            'id': 'Id',
            'payment_link_id': 'PaymentLinkId',
            'quantity': 'Quantity',
            'sub_total_amount': 'SubTotalAmount',
            'tax': 'Tax',
            'tax_amount': 'TaxAmount',
            'tax_id': 'TaxId',
            'tax_percentage': 'TaxPercentage',
            'total_amount': 'TotalAmount',
            'work_type': 'WorkType',
            'work_type_id': 'WorkTypeId'
        }

        self._cost = cost
        self._discount_amount = discount_amount
        self._discount_percentage = discount_percentage
        self._id = id
        self._payment_link_id = payment_link_id
        self._quantity = quantity
        self._sub_total_amount = sub_total_amount
        self._tax = tax
        self._tax_amount = tax_amount
        self._tax_id = tax_id
        self._tax_percentage = tax_percentage
        self._total_amount = total_amount
        self._work_type = work_type
        self._work_type_id = work_type_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentLinkItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaymentLinkItem of this PaymentLinkItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cost(self):
        """Gets the cost of this PaymentLinkItem.


        :return: The cost of this PaymentLinkItem.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PaymentLinkItem.


        :param cost: The cost of this PaymentLinkItem.
        :type cost: float
        """

        self._cost = cost

    @property
    def discount_amount(self):
        """Gets the discount_amount of this PaymentLinkItem.


        :return: The discount_amount of this PaymentLinkItem.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this PaymentLinkItem.


        :param discount_amount: The discount_amount of this PaymentLinkItem.
        :type discount_amount: float
        """

        self._discount_amount = discount_amount

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this PaymentLinkItem.


        :return: The discount_percentage of this PaymentLinkItem.
        :rtype: float
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this PaymentLinkItem.


        :param discount_percentage: The discount_percentage of this PaymentLinkItem.
        :type discount_percentage: float
        """

        self._discount_percentage = discount_percentage

    @property
    def id(self):
        """Gets the id of this PaymentLinkItem.


        :return: The id of this PaymentLinkItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentLinkItem.


        :param id: The id of this PaymentLinkItem.
        :type id: int
        """

        self._id = id

    @property
    def payment_link_id(self):
        """Gets the payment_link_id of this PaymentLinkItem.


        :return: The payment_link_id of this PaymentLinkItem.
        :rtype: int
        """
        return self._payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, payment_link_id):
        """Sets the payment_link_id of this PaymentLinkItem.


        :param payment_link_id: The payment_link_id of this PaymentLinkItem.
        :type payment_link_id: int
        """

        self._payment_link_id = payment_link_id

    @property
    def quantity(self):
        """Gets the quantity of this PaymentLinkItem.


        :return: The quantity of this PaymentLinkItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PaymentLinkItem.


        :param quantity: The quantity of this PaymentLinkItem.
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def sub_total_amount(self):
        """Gets the sub_total_amount of this PaymentLinkItem.


        :return: The sub_total_amount of this PaymentLinkItem.
        :rtype: float
        """
        return self._sub_total_amount

    @sub_total_amount.setter
    def sub_total_amount(self, sub_total_amount):
        """Sets the sub_total_amount of this PaymentLinkItem.


        :param sub_total_amount: The sub_total_amount of this PaymentLinkItem.
        :type sub_total_amount: float
        """

        self._sub_total_amount = sub_total_amount

    @property
    def tax(self):
        """Gets the tax of this PaymentLinkItem.


        :return: The tax of this PaymentLinkItem.
        :rtype: Tax
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PaymentLinkItem.


        :param tax: The tax of this PaymentLinkItem.
        :type tax: Tax
        """

        self._tax = tax

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PaymentLinkItem.


        :return: The tax_amount of this PaymentLinkItem.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PaymentLinkItem.


        :param tax_amount: The tax_amount of this PaymentLinkItem.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount

    @property
    def tax_id(self):
        """Gets the tax_id of this PaymentLinkItem.


        :return: The tax_id of this PaymentLinkItem.
        :rtype: int
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this PaymentLinkItem.


        :param tax_id: The tax_id of this PaymentLinkItem.
        :type tax_id: int
        """

        self._tax_id = tax_id

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this PaymentLinkItem.


        :return: The tax_percentage of this PaymentLinkItem.
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this PaymentLinkItem.


        :param tax_percentage: The tax_percentage of this PaymentLinkItem.
        :type tax_percentage: float
        """

        self._tax_percentage = tax_percentage

    @property
    def total_amount(self):
        """Gets the total_amount of this PaymentLinkItem.


        :return: The total_amount of this PaymentLinkItem.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PaymentLinkItem.


        :param total_amount: The total_amount of this PaymentLinkItem.
        :type total_amount: float
        """

        self._total_amount = total_amount

    @property
    def work_type(self):
        """Gets the work_type of this PaymentLinkItem.


        :return: The work_type of this PaymentLinkItem.
        :rtype: WorkType
        """
        return self._work_type

    @work_type.setter
    def work_type(self, work_type):
        """Sets the work_type of this PaymentLinkItem.


        :param work_type: The work_type of this PaymentLinkItem.
        :type work_type: WorkType
        """

        self._work_type = work_type

    @property
    def work_type_id(self):
        """Gets the work_type_id of this PaymentLinkItem.


        :return: The work_type_id of this PaymentLinkItem.
        :rtype: int
        """
        return self._work_type_id

    @work_type_id.setter
    def work_type_id(self, work_type_id):
        """Sets the work_type_id of this PaymentLinkItem.


        :param work_type_id: The work_type_id of this PaymentLinkItem.
        :type work_type_id: int
        """

        self._work_type_id = work_type_id
