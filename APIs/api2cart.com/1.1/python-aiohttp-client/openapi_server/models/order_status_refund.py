# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.a2_c_date_time import A2CDateTime
from openapi_server.models.order_status_refund_item import OrderStatusRefundItem
from openapi_server import util


class OrderStatusRefund(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_fields: object=None, comment: str=None, custom_fields: object=None, fee: float=None, refunded_items: List[OrderStatusRefundItem]=None, shipping: float=None, tax: float=None, time: A2CDateTime=None, total_refunded: float=None):
        """OrderStatusRefund - a model defined in OpenAPI

        :param additional_fields: The additional_fields of this OrderStatusRefund.
        :param comment: The comment of this OrderStatusRefund.
        :param custom_fields: The custom_fields of this OrderStatusRefund.
        :param fee: The fee of this OrderStatusRefund.
        :param refunded_items: The refunded_items of this OrderStatusRefund.
        :param shipping: The shipping of this OrderStatusRefund.
        :param tax: The tax of this OrderStatusRefund.
        :param time: The time of this OrderStatusRefund.
        :param total_refunded: The total_refunded of this OrderStatusRefund.
        """
        self.openapi_types = {
            'additional_fields': object,
            'comment': str,
            'custom_fields': object,
            'fee': float,
            'refunded_items': List[OrderStatusRefundItem],
            'shipping': float,
            'tax': float,
            'time': A2CDateTime,
            'total_refunded': float
        }

        self.attribute_map = {
            'additional_fields': 'additional_fields',
            'comment': 'comment',
            'custom_fields': 'custom_fields',
            'fee': 'fee',
            'refunded_items': 'refunded_items',
            'shipping': 'shipping',
            'tax': 'tax',
            'time': 'time',
            'total_refunded': 'total_refunded'
        }

        self._additional_fields = additional_fields
        self._comment = comment
        self._custom_fields = custom_fields
        self._fee = fee
        self._refunded_items = refunded_items
        self._shipping = shipping
        self._tax = tax
        self._time = time
        self._total_refunded = total_refunded

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderStatusRefund':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Order_Status_Refund of this OrderStatusRefund.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_fields(self):
        """Gets the additional_fields of this OrderStatusRefund.


        :return: The additional_fields of this OrderStatusRefund.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this OrderStatusRefund.


        :param additional_fields: The additional_fields of this OrderStatusRefund.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def comment(self):
        """Gets the comment of this OrderStatusRefund.


        :return: The comment of this OrderStatusRefund.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OrderStatusRefund.


        :param comment: The comment of this OrderStatusRefund.
        :type comment: str
        """

        self._comment = comment

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderStatusRefund.


        :return: The custom_fields of this OrderStatusRefund.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderStatusRefund.


        :param custom_fields: The custom_fields of this OrderStatusRefund.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def fee(self):
        """Gets the fee of this OrderStatusRefund.


        :return: The fee of this OrderStatusRefund.
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this OrderStatusRefund.


        :param fee: The fee of this OrderStatusRefund.
        :type fee: float
        """

        self._fee = fee

    @property
    def refunded_items(self):
        """Gets the refunded_items of this OrderStatusRefund.


        :return: The refunded_items of this OrderStatusRefund.
        :rtype: List[OrderStatusRefundItem]
        """
        return self._refunded_items

    @refunded_items.setter
    def refunded_items(self, refunded_items):
        """Sets the refunded_items of this OrderStatusRefund.


        :param refunded_items: The refunded_items of this OrderStatusRefund.
        :type refunded_items: List[OrderStatusRefundItem]
        """

        self._refunded_items = refunded_items

    @property
    def shipping(self):
        """Gets the shipping of this OrderStatusRefund.


        :return: The shipping of this OrderStatusRefund.
        :rtype: float
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this OrderStatusRefund.


        :param shipping: The shipping of this OrderStatusRefund.
        :type shipping: float
        """

        self._shipping = shipping

    @property
    def tax(self):
        """Gets the tax of this OrderStatusRefund.


        :return: The tax of this OrderStatusRefund.
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this OrderStatusRefund.


        :param tax: The tax of this OrderStatusRefund.
        :type tax: float
        """

        self._tax = tax

    @property
    def time(self):
        """Gets the time of this OrderStatusRefund.


        :return: The time of this OrderStatusRefund.
        :rtype: A2CDateTime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OrderStatusRefund.


        :param time: The time of this OrderStatusRefund.
        :type time: A2CDateTime
        """

        self._time = time

    @property
    def total_refunded(self):
        """Gets the total_refunded of this OrderStatusRefund.


        :return: The total_refunded of this OrderStatusRefund.
        :rtype: float
        """
        return self._total_refunded

    @total_refunded.setter
    def total_refunded(self, total_refunded):
        """Sets the total_refunded of this OrderStatusRefund.


        :param total_refunded: The total_refunded of this OrderStatusRefund.
        :type total_refunded: float
        """

        self._total_refunded = total_refunded
