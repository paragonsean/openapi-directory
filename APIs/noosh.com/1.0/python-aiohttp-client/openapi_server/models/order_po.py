# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.custom_field_persist_vo import CustomFieldPersistVO
from openapi_server.models.order_item_persist_vo import OrderItemPersistVO
from openapi_server import util


class OrderPO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, buyer_user_id: int=None, comments: str=None, custom_fields: List[CustomFieldPersistVO]=None, invoice_or_billing_recipient: int=None, order_completion_date: date=None, order_items: List[OrderItemPersistVO]=None, other_selection_reason: str=None, payment_method_id: int=None, payment_reference_no: str=None, sell_order: bool=None, shipping: object=None, supplier_reference: str=None, supplier_selection_reason_id: int=None, supplier_user_id: int=None, tax: str=None, title: str=None):
        """OrderPO - a model defined in OpenAPI

        :param buyer_user_id: The buyer_user_id of this OrderPO.
        :param comments: The comments of this OrderPO.
        :param custom_fields: The custom_fields of this OrderPO.
        :param invoice_or_billing_recipient: The invoice_or_billing_recipient of this OrderPO.
        :param order_completion_date: The order_completion_date of this OrderPO.
        :param order_items: The order_items of this OrderPO.
        :param other_selection_reason: The other_selection_reason of this OrderPO.
        :param payment_method_id: The payment_method_id of this OrderPO.
        :param payment_reference_no: The payment_reference_no of this OrderPO.
        :param sell_order: The sell_order of this OrderPO.
        :param shipping: The shipping of this OrderPO.
        :param supplier_reference: The supplier_reference of this OrderPO.
        :param supplier_selection_reason_id: The supplier_selection_reason_id of this OrderPO.
        :param supplier_user_id: The supplier_user_id of this OrderPO.
        :param tax: The tax of this OrderPO.
        :param title: The title of this OrderPO.
        """
        self.openapi_types = {
            'buyer_user_id': int,
            'comments': str,
            'custom_fields': List[CustomFieldPersistVO],
            'invoice_or_billing_recipient': int,
            'order_completion_date': date,
            'order_items': List[OrderItemPersistVO],
            'other_selection_reason': str,
            'payment_method_id': int,
            'payment_reference_no': str,
            'sell_order': bool,
            'shipping': object,
            'supplier_reference': str,
            'supplier_selection_reason_id': int,
            'supplier_user_id': int,
            'tax': str,
            'title': str
        }

        self.attribute_map = {
            'buyer_user_id': 'buyer_user_id',
            'comments': 'comments',
            'custom_fields': 'custom_fields',
            'invoice_or_billing_recipient': 'invoice_or_billing_recipient',
            'order_completion_date': 'order_completion_date',
            'order_items': 'order_items',
            'other_selection_reason': 'other_selection_reason',
            'payment_method_id': 'payment_method_id',
            'payment_reference_no': 'payment_reference_no',
            'sell_order': 'sellOrder',
            'shipping': 'shipping',
            'supplier_reference': 'supplier_reference',
            'supplier_selection_reason_id': 'supplier_selection_reason_id',
            'supplier_user_id': 'supplier_user_id',
            'tax': 'tax',
            'title': 'title'
        }

        self._buyer_user_id = buyer_user_id
        self._comments = comments
        self._custom_fields = custom_fields
        self._invoice_or_billing_recipient = invoice_or_billing_recipient
        self._order_completion_date = order_completion_date
        self._order_items = order_items
        self._other_selection_reason = other_selection_reason
        self._payment_method_id = payment_method_id
        self._payment_reference_no = payment_reference_no
        self._sell_order = sell_order
        self._shipping = shipping
        self._supplier_reference = supplier_reference
        self._supplier_selection_reason_id = supplier_selection_reason_id
        self._supplier_user_id = supplier_user_id
        self._tax = tax
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderPO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderPO of this OrderPO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def buyer_user_id(self):
        """Gets the buyer_user_id of this OrderPO.

        

        :return: The buyer_user_id of this OrderPO.
        :rtype: int
        """
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, buyer_user_id):
        """Sets the buyer_user_id of this OrderPO.

        

        :param buyer_user_id: The buyer_user_id of this OrderPO.
        :type buyer_user_id: int
        """

        self._buyer_user_id = buyer_user_id

    @property
    def comments(self):
        """Gets the comments of this OrderPO.

        

        :return: The comments of this OrderPO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this OrderPO.

        

        :param comments: The comments of this OrderPO.
        :type comments: str
        """

        self._comments = comments

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderPO.

        

        :return: The custom_fields of this OrderPO.
        :rtype: List[CustomFieldPersistVO]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderPO.

        

        :param custom_fields: The custom_fields of this OrderPO.
        :type custom_fields: List[CustomFieldPersistVO]
        """

        self._custom_fields = custom_fields

    @property
    def invoice_or_billing_recipient(self):
        """Gets the invoice_or_billing_recipient of this OrderPO.

        

        :return: The invoice_or_billing_recipient of this OrderPO.
        :rtype: int
        """
        return self._invoice_or_billing_recipient

    @invoice_or_billing_recipient.setter
    def invoice_or_billing_recipient(self, invoice_or_billing_recipient):
        """Sets the invoice_or_billing_recipient of this OrderPO.

        

        :param invoice_or_billing_recipient: The invoice_or_billing_recipient of this OrderPO.
        :type invoice_or_billing_recipient: int
        """

        self._invoice_or_billing_recipient = invoice_or_billing_recipient

    @property
    def order_completion_date(self):
        """Gets the order_completion_date of this OrderPO.

        

        :return: The order_completion_date of this OrderPO.
        :rtype: date
        """
        return self._order_completion_date

    @order_completion_date.setter
    def order_completion_date(self, order_completion_date):
        """Sets the order_completion_date of this OrderPO.

        

        :param order_completion_date: The order_completion_date of this OrderPO.
        :type order_completion_date: date
        """

        self._order_completion_date = order_completion_date

    @property
    def order_items(self):
        """Gets the order_items of this OrderPO.

        

        :return: The order_items of this OrderPO.
        :rtype: List[OrderItemPersistVO]
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this OrderPO.

        

        :param order_items: The order_items of this OrderPO.
        :type order_items: List[OrderItemPersistVO]
        """

        self._order_items = order_items

    @property
    def other_selection_reason(self):
        """Gets the other_selection_reason of this OrderPO.

        

        :return: The other_selection_reason of this OrderPO.
        :rtype: str
        """
        return self._other_selection_reason

    @other_selection_reason.setter
    def other_selection_reason(self, other_selection_reason):
        """Sets the other_selection_reason of this OrderPO.

        

        :param other_selection_reason: The other_selection_reason of this OrderPO.
        :type other_selection_reason: str
        """

        self._other_selection_reason = other_selection_reason

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this OrderPO.

        

        :return: The payment_method_id of this OrderPO.
        :rtype: int
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this OrderPO.

        

        :param payment_method_id: The payment_method_id of this OrderPO.
        :type payment_method_id: int
        """

        self._payment_method_id = payment_method_id

    @property
    def payment_reference_no(self):
        """Gets the payment_reference_no of this OrderPO.

        

        :return: The payment_reference_no of this OrderPO.
        :rtype: str
        """
        return self._payment_reference_no

    @payment_reference_no.setter
    def payment_reference_no(self, payment_reference_no):
        """Sets the payment_reference_no of this OrderPO.

        

        :param payment_reference_no: The payment_reference_no of this OrderPO.
        :type payment_reference_no: str
        """

        self._payment_reference_no = payment_reference_no

    @property
    def sell_order(self):
        """Gets the sell_order of this OrderPO.

        

        :return: The sell_order of this OrderPO.
        :rtype: bool
        """
        return self._sell_order

    @sell_order.setter
    def sell_order(self, sell_order):
        """Sets the sell_order of this OrderPO.

        

        :param sell_order: The sell_order of this OrderPO.
        :type sell_order: bool
        """

        self._sell_order = sell_order

    @property
    def shipping(self):
        """Gets the shipping of this OrderPO.

        Java type: java.math.BigDecimal

        :return: The shipping of this OrderPO.
        :rtype: object
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this OrderPO.

        Java type: java.math.BigDecimal

        :param shipping: The shipping of this OrderPO.
        :type shipping: object
        """

        self._shipping = shipping

    @property
    def supplier_reference(self):
        """Gets the supplier_reference of this OrderPO.

        

        :return: The supplier_reference of this OrderPO.
        :rtype: str
        """
        return self._supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, supplier_reference):
        """Sets the supplier_reference of this OrderPO.

        

        :param supplier_reference: The supplier_reference of this OrderPO.
        :type supplier_reference: str
        """

        self._supplier_reference = supplier_reference

    @property
    def supplier_selection_reason_id(self):
        """Gets the supplier_selection_reason_id of this OrderPO.

        

        :return: The supplier_selection_reason_id of this OrderPO.
        :rtype: int
        """
        return self._supplier_selection_reason_id

    @supplier_selection_reason_id.setter
    def supplier_selection_reason_id(self, supplier_selection_reason_id):
        """Sets the supplier_selection_reason_id of this OrderPO.

        

        :param supplier_selection_reason_id: The supplier_selection_reason_id of this OrderPO.
        :type supplier_selection_reason_id: int
        """

        self._supplier_selection_reason_id = supplier_selection_reason_id

    @property
    def supplier_user_id(self):
        """Gets the supplier_user_id of this OrderPO.

        

        :return: The supplier_user_id of this OrderPO.
        :rtype: int
        """
        return self._supplier_user_id

    @supplier_user_id.setter
    def supplier_user_id(self, supplier_user_id):
        """Sets the supplier_user_id of this OrderPO.

        

        :param supplier_user_id: The supplier_user_id of this OrderPO.
        :type supplier_user_id: int
        """

        self._supplier_user_id = supplier_user_id

    @property
    def tax(self):
        """Gets the tax of this OrderPO.

        

        :return: The tax of this OrderPO.
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this OrderPO.

        

        :param tax: The tax of this OrderPO.
        :type tax: str
        """

        self._tax = tax

    @property
    def title(self):
        """Gets the title of this OrderPO.

        

        :return: The title of this OrderPO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OrderPO.

        

        :param title: The title of this OrderPO.
        :type title: str
        """

        self._title = title
