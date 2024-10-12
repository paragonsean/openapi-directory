# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.activity import Activity
from openapi_server.models.invoice_attachment import InvoiceAttachment
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.payment import Payment
from openapi_server.models.payment_gateway_for_invoice import PaymentGatewayForInvoice
from openapi_server import util


class Invoice(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_token: str=None, activities: List[Activity]=None, attachments: List[InvoiceAttachment]=None, client_id: int=None, cloned_from_id: int=None, currency_id: int=None, discount_amount: float=None, duedate: datetime=None, enable_partial_payments: bool=None, estimation_id: int=None, id: int=None, invoice_category_id: int=None, is_digitally_signed: bool=None, issued_on: datetime=None, items: List[InvoiceItem]=None, notes: str=None, number: str=None, order_id: int=None, payment_gateways: List[PaymentGatewayForInvoice]=None, payment_link_id: int=None, payments: List[Payment]=None, po_number: str=None, recurring_profile_id: int=None, should_send_reminders: bool=None, status: str=None, sub_total_amount: float=None, tax_amount: float=None, terms: str=None, total_amount: float=None, user_id: int=None):
        """Invoice - a model defined in OpenAPI

        :param access_token: The access_token of this Invoice.
        :param activities: The activities of this Invoice.
        :param attachments: The attachments of this Invoice.
        :param client_id: The client_id of this Invoice.
        :param cloned_from_id: The cloned_from_id of this Invoice.
        :param currency_id: The currency_id of this Invoice.
        :param discount_amount: The discount_amount of this Invoice.
        :param duedate: The duedate of this Invoice.
        :param enable_partial_payments: The enable_partial_payments of this Invoice.
        :param estimation_id: The estimation_id of this Invoice.
        :param id: The id of this Invoice.
        :param invoice_category_id: The invoice_category_id of this Invoice.
        :param is_digitally_signed: The is_digitally_signed of this Invoice.
        :param issued_on: The issued_on of this Invoice.
        :param items: The items of this Invoice.
        :param notes: The notes of this Invoice.
        :param number: The number of this Invoice.
        :param order_id: The order_id of this Invoice.
        :param payment_gateways: The payment_gateways of this Invoice.
        :param payment_link_id: The payment_link_id of this Invoice.
        :param payments: The payments of this Invoice.
        :param po_number: The po_number of this Invoice.
        :param recurring_profile_id: The recurring_profile_id of this Invoice.
        :param should_send_reminders: The should_send_reminders of this Invoice.
        :param status: The status of this Invoice.
        :param sub_total_amount: The sub_total_amount of this Invoice.
        :param tax_amount: The tax_amount of this Invoice.
        :param terms: The terms of this Invoice.
        :param total_amount: The total_amount of this Invoice.
        :param user_id: The user_id of this Invoice.
        """
        self.openapi_types = {
            'access_token': str,
            'activities': List[Activity],
            'attachments': List[InvoiceAttachment],
            'client_id': int,
            'cloned_from_id': int,
            'currency_id': int,
            'discount_amount': float,
            'duedate': datetime,
            'enable_partial_payments': bool,
            'estimation_id': int,
            'id': int,
            'invoice_category_id': int,
            'is_digitally_signed': bool,
            'issued_on': datetime,
            'items': List[InvoiceItem],
            'notes': str,
            'number': str,
            'order_id': int,
            'payment_gateways': List[PaymentGatewayForInvoice],
            'payment_link_id': int,
            'payments': List[Payment],
            'po_number': str,
            'recurring_profile_id': int,
            'should_send_reminders': bool,
            'status': str,
            'sub_total_amount': float,
            'tax_amount': float,
            'terms': str,
            'total_amount': float,
            'user_id': int
        }

        self.attribute_map = {
            'access_token': 'AccessToken',
            'activities': 'Activities',
            'attachments': 'Attachments',
            'client_id': 'ClientId',
            'cloned_from_id': 'ClonedFromId',
            'currency_id': 'CurrencyId',
            'discount_amount': 'DiscountAmount',
            'duedate': 'Duedate',
            'enable_partial_payments': 'EnablePartialPayments',
            'estimation_id': 'EstimationId',
            'id': 'Id',
            'invoice_category_id': 'InvoiceCategoryId',
            'is_digitally_signed': 'IsDigitallySigned',
            'issued_on': 'IssuedOn',
            'items': 'Items',
            'notes': 'Notes',
            'number': 'Number',
            'order_id': 'OrderId',
            'payment_gateways': 'PaymentGateways',
            'payment_link_id': 'PaymentLinkId',
            'payments': 'Payments',
            'po_number': 'PoNumber',
            'recurring_profile_id': 'RecurringProfileId',
            'should_send_reminders': 'ShouldSendReminders',
            'status': 'Status',
            'sub_total_amount': 'SubTotalAmount',
            'tax_amount': 'TaxAmount',
            'terms': 'Terms',
            'total_amount': 'TotalAmount',
            'user_id': 'UserId'
        }

        self._access_token = access_token
        self._activities = activities
        self._attachments = attachments
        self._client_id = client_id
        self._cloned_from_id = cloned_from_id
        self._currency_id = currency_id
        self._discount_amount = discount_amount
        self._duedate = duedate
        self._enable_partial_payments = enable_partial_payments
        self._estimation_id = estimation_id
        self._id = id
        self._invoice_category_id = invoice_category_id
        self._is_digitally_signed = is_digitally_signed
        self._issued_on = issued_on
        self._items = items
        self._notes = notes
        self._number = number
        self._order_id = order_id
        self._payment_gateways = payment_gateways
        self._payment_link_id = payment_link_id
        self._payments = payments
        self._po_number = po_number
        self._recurring_profile_id = recurring_profile_id
        self._should_send_reminders = should_send_reminders
        self._status = status
        self._sub_total_amount = sub_total_amount
        self._tax_amount = tax_amount
        self._terms = terms
        self._total_amount = total_amount
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Invoice':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Invoice of this Invoice.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self):
        """Gets the access_token of this Invoice.


        :return: The access_token of this Invoice.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Invoice.


        :param access_token: The access_token of this Invoice.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def activities(self):
        """Gets the activities of this Invoice.


        :return: The activities of this Invoice.
        :rtype: List[Activity]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this Invoice.


        :param activities: The activities of this Invoice.
        :type activities: List[Activity]
        """

        self._activities = activities

    @property
    def attachments(self):
        """Gets the attachments of this Invoice.


        :return: The attachments of this Invoice.
        :rtype: List[InvoiceAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Invoice.


        :param attachments: The attachments of this Invoice.
        :type attachments: List[InvoiceAttachment]
        """

        self._attachments = attachments

    @property
    def client_id(self):
        """Gets the client_id of this Invoice.


        :return: The client_id of this Invoice.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Invoice.


        :param client_id: The client_id of this Invoice.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def cloned_from_id(self):
        """Gets the cloned_from_id of this Invoice.


        :return: The cloned_from_id of this Invoice.
        :rtype: int
        """
        return self._cloned_from_id

    @cloned_from_id.setter
    def cloned_from_id(self, cloned_from_id):
        """Sets the cloned_from_id of this Invoice.


        :param cloned_from_id: The cloned_from_id of this Invoice.
        :type cloned_from_id: int
        """

        self._cloned_from_id = cloned_from_id

    @property
    def currency_id(self):
        """Gets the currency_id of this Invoice.


        :return: The currency_id of this Invoice.
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Invoice.


        :param currency_id: The currency_id of this Invoice.
        :type currency_id: int
        """

        self._currency_id = currency_id

    @property
    def discount_amount(self):
        """Gets the discount_amount of this Invoice.


        :return: The discount_amount of this Invoice.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this Invoice.


        :param discount_amount: The discount_amount of this Invoice.
        :type discount_amount: float
        """

        self._discount_amount = discount_amount

    @property
    def duedate(self):
        """Gets the duedate of this Invoice.


        :return: The duedate of this Invoice.
        :rtype: datetime
        """
        return self._duedate

    @duedate.setter
    def duedate(self, duedate):
        """Sets the duedate of this Invoice.


        :param duedate: The duedate of this Invoice.
        :type duedate: datetime
        """

        self._duedate = duedate

    @property
    def enable_partial_payments(self):
        """Gets the enable_partial_payments of this Invoice.


        :return: The enable_partial_payments of this Invoice.
        :rtype: bool
        """
        return self._enable_partial_payments

    @enable_partial_payments.setter
    def enable_partial_payments(self, enable_partial_payments):
        """Sets the enable_partial_payments of this Invoice.


        :param enable_partial_payments: The enable_partial_payments of this Invoice.
        :type enable_partial_payments: bool
        """

        self._enable_partial_payments = enable_partial_payments

    @property
    def estimation_id(self):
        """Gets the estimation_id of this Invoice.


        :return: The estimation_id of this Invoice.
        :rtype: int
        """
        return self._estimation_id

    @estimation_id.setter
    def estimation_id(self, estimation_id):
        """Sets the estimation_id of this Invoice.


        :param estimation_id: The estimation_id of this Invoice.
        :type estimation_id: int
        """

        self._estimation_id = estimation_id

    @property
    def id(self):
        """Gets the id of this Invoice.


        :return: The id of this Invoice.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.


        :param id: The id of this Invoice.
        :type id: int
        """

        self._id = id

    @property
    def invoice_category_id(self):
        """Gets the invoice_category_id of this Invoice.


        :return: The invoice_category_id of this Invoice.
        :rtype: int
        """
        return self._invoice_category_id

    @invoice_category_id.setter
    def invoice_category_id(self, invoice_category_id):
        """Sets the invoice_category_id of this Invoice.


        :param invoice_category_id: The invoice_category_id of this Invoice.
        :type invoice_category_id: int
        """

        self._invoice_category_id = invoice_category_id

    @property
    def is_digitally_signed(self):
        """Gets the is_digitally_signed of this Invoice.


        :return: The is_digitally_signed of this Invoice.
        :rtype: bool
        """
        return self._is_digitally_signed

    @is_digitally_signed.setter
    def is_digitally_signed(self, is_digitally_signed):
        """Sets the is_digitally_signed of this Invoice.


        :param is_digitally_signed: The is_digitally_signed of this Invoice.
        :type is_digitally_signed: bool
        """

        self._is_digitally_signed = is_digitally_signed

    @property
    def issued_on(self):
        """Gets the issued_on of this Invoice.


        :return: The issued_on of this Invoice.
        :rtype: datetime
        """
        return self._issued_on

    @issued_on.setter
    def issued_on(self, issued_on):
        """Sets the issued_on of this Invoice.


        :param issued_on: The issued_on of this Invoice.
        :type issued_on: datetime
        """

        self._issued_on = issued_on

    @property
    def items(self):
        """Gets the items of this Invoice.


        :return: The items of this Invoice.
        :rtype: List[InvoiceItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Invoice.


        :param items: The items of this Invoice.
        :type items: List[InvoiceItem]
        """

        self._items = items

    @property
    def notes(self):
        """Gets the notes of this Invoice.


        :return: The notes of this Invoice.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Invoice.


        :param notes: The notes of this Invoice.
        :type notes: str
        """

        self._notes = notes

    @property
    def number(self):
        """Gets the number of this Invoice.


        :return: The number of this Invoice.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Invoice.


        :param number: The number of this Invoice.
        :type number: str
        """

        self._number = number

    @property
    def order_id(self):
        """Gets the order_id of this Invoice.


        :return: The order_id of this Invoice.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Invoice.


        :param order_id: The order_id of this Invoice.
        :type order_id: int
        """

        self._order_id = order_id

    @property
    def payment_gateways(self):
        """Gets the payment_gateways of this Invoice.


        :return: The payment_gateways of this Invoice.
        :rtype: List[PaymentGatewayForInvoice]
        """
        return self._payment_gateways

    @payment_gateways.setter
    def payment_gateways(self, payment_gateways):
        """Sets the payment_gateways of this Invoice.


        :param payment_gateways: The payment_gateways of this Invoice.
        :type payment_gateways: List[PaymentGatewayForInvoice]
        """

        self._payment_gateways = payment_gateways

    @property
    def payment_link_id(self):
        """Gets the payment_link_id of this Invoice.


        :return: The payment_link_id of this Invoice.
        :rtype: int
        """
        return self._payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, payment_link_id):
        """Sets the payment_link_id of this Invoice.


        :param payment_link_id: The payment_link_id of this Invoice.
        :type payment_link_id: int
        """

        self._payment_link_id = payment_link_id

    @property
    def payments(self):
        """Gets the payments of this Invoice.


        :return: The payments of this Invoice.
        :rtype: List[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Invoice.


        :param payments: The payments of this Invoice.
        :type payments: List[Payment]
        """

        self._payments = payments

    @property
    def po_number(self):
        """Gets the po_number of this Invoice.


        :return: The po_number of this Invoice.
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this Invoice.


        :param po_number: The po_number of this Invoice.
        :type po_number: str
        """

        self._po_number = po_number

    @property
    def recurring_profile_id(self):
        """Gets the recurring_profile_id of this Invoice.


        :return: The recurring_profile_id of this Invoice.
        :rtype: int
        """
        return self._recurring_profile_id

    @recurring_profile_id.setter
    def recurring_profile_id(self, recurring_profile_id):
        """Sets the recurring_profile_id of this Invoice.


        :param recurring_profile_id: The recurring_profile_id of this Invoice.
        :type recurring_profile_id: int
        """

        self._recurring_profile_id = recurring_profile_id

    @property
    def should_send_reminders(self):
        """Gets the should_send_reminders of this Invoice.


        :return: The should_send_reminders of this Invoice.
        :rtype: bool
        """
        return self._should_send_reminders

    @should_send_reminders.setter
    def should_send_reminders(self, should_send_reminders):
        """Sets the should_send_reminders of this Invoice.


        :param should_send_reminders: The should_send_reminders of this Invoice.
        :type should_send_reminders: bool
        """

        self._should_send_reminders = should_send_reminders

    @property
    def status(self):
        """Gets the status of this Invoice.


        :return: The status of this Invoice.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.
        :type status: str
        """
        allowed_values = ["Draft", "Paid", "Unpaid", "Overdue", "Void"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sub_total_amount(self):
        """Gets the sub_total_amount of this Invoice.


        :return: The sub_total_amount of this Invoice.
        :rtype: float
        """
        return self._sub_total_amount

    @sub_total_amount.setter
    def sub_total_amount(self, sub_total_amount):
        """Sets the sub_total_amount of this Invoice.


        :param sub_total_amount: The sub_total_amount of this Invoice.
        :type sub_total_amount: float
        """

        self._sub_total_amount = sub_total_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this Invoice.


        :return: The tax_amount of this Invoice.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this Invoice.


        :param tax_amount: The tax_amount of this Invoice.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount

    @property
    def terms(self):
        """Gets the terms of this Invoice.


        :return: The terms of this Invoice.
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this Invoice.


        :param terms: The terms of this Invoice.
        :type terms: str
        """

        self._terms = terms

    @property
    def total_amount(self):
        """Gets the total_amount of this Invoice.


        :return: The total_amount of this Invoice.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Invoice.


        :param total_amount: The total_amount of this Invoice.
        :type total_amount: float
        """

        self._total_amount = total_amount

    @property
    def user_id(self):
        """Gets the user_id of this Invoice.


        :return: The user_id of this Invoice.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Invoice.


        :param user_id: The user_id of this Invoice.
        :type user_id: int
        """

        self._user_id = user_id
