# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.client_details_api_model import ClientDetailsApiModel
from openapi_server.models.currency_details_api_model import CurrencyDetailsApiModel
from openapi_server.models.invoice_recurring_api_model import InvoiceRecurringApiModel
from openapi_server import util


class InvoiceDetailsApiModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_token: str=None, client: ClientDetailsApiModel=None, cloned_from_id: int=None, currency: CurrencyDetailsApiModel=None, discount_amount: float=None, duedate: datetime=None, enable_partial_payments: bool=None, id: int=None, invoice_category_id: int=None, issued_on: datetime=None, notes: str=None, number: str=None, po_number: str=None, recurring_profile: InvoiceRecurringApiModel=None, recurring_profile_id: int=None, should_send_reminders: bool=None, status: str=None, sub_total_amount: float=None, tax_amount: float=None, terms: str=None, total_amount: float=None):
        """InvoiceDetailsApiModel - a model defined in OpenAPI

        :param access_token: The access_token of this InvoiceDetailsApiModel.
        :param client: The client of this InvoiceDetailsApiModel.
        :param cloned_from_id: The cloned_from_id of this InvoiceDetailsApiModel.
        :param currency: The currency of this InvoiceDetailsApiModel.
        :param discount_amount: The discount_amount of this InvoiceDetailsApiModel.
        :param duedate: The duedate of this InvoiceDetailsApiModel.
        :param enable_partial_payments: The enable_partial_payments of this InvoiceDetailsApiModel.
        :param id: The id of this InvoiceDetailsApiModel.
        :param invoice_category_id: The invoice_category_id of this InvoiceDetailsApiModel.
        :param issued_on: The issued_on of this InvoiceDetailsApiModel.
        :param notes: The notes of this InvoiceDetailsApiModel.
        :param number: The number of this InvoiceDetailsApiModel.
        :param po_number: The po_number of this InvoiceDetailsApiModel.
        :param recurring_profile: The recurring_profile of this InvoiceDetailsApiModel.
        :param recurring_profile_id: The recurring_profile_id of this InvoiceDetailsApiModel.
        :param should_send_reminders: The should_send_reminders of this InvoiceDetailsApiModel.
        :param status: The status of this InvoiceDetailsApiModel.
        :param sub_total_amount: The sub_total_amount of this InvoiceDetailsApiModel.
        :param tax_amount: The tax_amount of this InvoiceDetailsApiModel.
        :param terms: The terms of this InvoiceDetailsApiModel.
        :param total_amount: The total_amount of this InvoiceDetailsApiModel.
        """
        self.openapi_types = {
            'access_token': str,
            'client': ClientDetailsApiModel,
            'cloned_from_id': int,
            'currency': CurrencyDetailsApiModel,
            'discount_amount': float,
            'duedate': datetime,
            'enable_partial_payments': bool,
            'id': int,
            'invoice_category_id': int,
            'issued_on': datetime,
            'notes': str,
            'number': str,
            'po_number': str,
            'recurring_profile': InvoiceRecurringApiModel,
            'recurring_profile_id': int,
            'should_send_reminders': bool,
            'status': str,
            'sub_total_amount': float,
            'tax_amount': float,
            'terms': str,
            'total_amount': float
        }

        self.attribute_map = {
            'access_token': 'AccessToken',
            'client': 'Client',
            'cloned_from_id': 'ClonedFromId',
            'currency': 'Currency',
            'discount_amount': 'DiscountAmount',
            'duedate': 'Duedate',
            'enable_partial_payments': 'EnablePartialPayments',
            'id': 'Id',
            'invoice_category_id': 'InvoiceCategoryId',
            'issued_on': 'IssuedOn',
            'notes': 'Notes',
            'number': 'Number',
            'po_number': 'PoNumber',
            'recurring_profile': 'RecurringProfile',
            'recurring_profile_id': 'RecurringProfileId',
            'should_send_reminders': 'ShouldSendReminders',
            'status': 'Status',
            'sub_total_amount': 'SubTotalAmount',
            'tax_amount': 'TaxAmount',
            'terms': 'Terms',
            'total_amount': 'TotalAmount'
        }

        self._access_token = access_token
        self._client = client
        self._cloned_from_id = cloned_from_id
        self._currency = currency
        self._discount_amount = discount_amount
        self._duedate = duedate
        self._enable_partial_payments = enable_partial_payments
        self._id = id
        self._invoice_category_id = invoice_category_id
        self._issued_on = issued_on
        self._notes = notes
        self._number = number
        self._po_number = po_number
        self._recurring_profile = recurring_profile
        self._recurring_profile_id = recurring_profile_id
        self._should_send_reminders = should_send_reminders
        self._status = status
        self._sub_total_amount = sub_total_amount
        self._tax_amount = tax_amount
        self._terms = terms
        self._total_amount = total_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InvoiceDetailsApiModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InvoiceDetailsApiModel of this InvoiceDetailsApiModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self):
        """Gets the access_token of this InvoiceDetailsApiModel.

        Security access token used for accessing the invoice anonymously

        :return: The access_token of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this InvoiceDetailsApiModel.

        Security access token used for accessing the invoice anonymously

        :param access_token: The access_token of this InvoiceDetailsApiModel.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def client(self):
        """Gets the client of this InvoiceDetailsApiModel.


        :return: The client of this InvoiceDetailsApiModel.
        :rtype: ClientDetailsApiModel
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this InvoiceDetailsApiModel.


        :param client: The client of this InvoiceDetailsApiModel.
        :type client: ClientDetailsApiModel
        """

        self._client = client

    @property
    def cloned_from_id(self):
        """Gets the cloned_from_id of this InvoiceDetailsApiModel.

        Indicate from which invoice this invoice has been cloned from

        :return: The cloned_from_id of this InvoiceDetailsApiModel.
        :rtype: int
        """
        return self._cloned_from_id

    @cloned_from_id.setter
    def cloned_from_id(self, cloned_from_id):
        """Sets the cloned_from_id of this InvoiceDetailsApiModel.

        Indicate from which invoice this invoice has been cloned from

        :param cloned_from_id: The cloned_from_id of this InvoiceDetailsApiModel.
        :type cloned_from_id: int
        """

        self._cloned_from_id = cloned_from_id

    @property
    def currency(self):
        """Gets the currency of this InvoiceDetailsApiModel.


        :return: The currency of this InvoiceDetailsApiModel.
        :rtype: CurrencyDetailsApiModel
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceDetailsApiModel.


        :param currency: The currency of this InvoiceDetailsApiModel.
        :type currency: CurrencyDetailsApiModel
        """

        self._currency = currency

    @property
    def discount_amount(self):
        """Gets the discount_amount of this InvoiceDetailsApiModel.

        Amount that goes as a discount

        :return: The discount_amount of this InvoiceDetailsApiModel.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this InvoiceDetailsApiModel.

        Amount that goes as a discount

        :param discount_amount: The discount_amount of this InvoiceDetailsApiModel.
        :type discount_amount: float
        """

        self._discount_amount = discount_amount

    @property
    def duedate(self):
        """Gets the duedate of this InvoiceDetailsApiModel.

        Indicates when the invoice will be proclamed as due

        :return: The duedate of this InvoiceDetailsApiModel.
        :rtype: datetime
        """
        return self._duedate

    @duedate.setter
    def duedate(self, duedate):
        """Sets the duedate of this InvoiceDetailsApiModel.

        Indicates when the invoice will be proclamed as due

        :param duedate: The duedate of this InvoiceDetailsApiModel.
        :type duedate: datetime
        """

        self._duedate = duedate

    @property
    def enable_partial_payments(self):
        """Gets the enable_partial_payments of this InvoiceDetailsApiModel.

        Indicate that the invoice allows the user to pay the invoice partially

        :return: The enable_partial_payments of this InvoiceDetailsApiModel.
        :rtype: bool
        """
        return self._enable_partial_payments

    @enable_partial_payments.setter
    def enable_partial_payments(self, enable_partial_payments):
        """Sets the enable_partial_payments of this InvoiceDetailsApiModel.

        Indicate that the invoice allows the user to pay the invoice partially

        :param enable_partial_payments: The enable_partial_payments of this InvoiceDetailsApiModel.
        :type enable_partial_payments: bool
        """

        self._enable_partial_payments = enable_partial_payments

    @property
    def id(self):
        """Gets the id of this InvoiceDetailsApiModel.

        Invoice id

        :return: The id of this InvoiceDetailsApiModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceDetailsApiModel.

        Invoice id

        :param id: The id of this InvoiceDetailsApiModel.
        :type id: int
        """

        self._id = id

    @property
    def invoice_category_id(self):
        """Gets the invoice_category_id of this InvoiceDetailsApiModel.

        Hold the id of the invoice category

        :return: The invoice_category_id of this InvoiceDetailsApiModel.
        :rtype: int
        """
        return self._invoice_category_id

    @invoice_category_id.setter
    def invoice_category_id(self, invoice_category_id):
        """Sets the invoice_category_id of this InvoiceDetailsApiModel.

        Hold the id of the invoice category

        :param invoice_category_id: The invoice_category_id of this InvoiceDetailsApiModel.
        :type invoice_category_id: int
        """

        self._invoice_category_id = invoice_category_id

    @property
    def issued_on(self):
        """Gets the issued_on of this InvoiceDetailsApiModel.

        Indicates when the invoice was issued

        :return: The issued_on of this InvoiceDetailsApiModel.
        :rtype: datetime
        """
        return self._issued_on

    @issued_on.setter
    def issued_on(self, issued_on):
        """Sets the issued_on of this InvoiceDetailsApiModel.

        Indicates when the invoice was issued

        :param issued_on: The issued_on of this InvoiceDetailsApiModel.
        :type issued_on: datetime
        """

        self._issued_on = issued_on

    @property
    def notes(self):
        """Gets the notes of this InvoiceDetailsApiModel.

        Internal note regarding the invoice

        :return: The notes of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InvoiceDetailsApiModel.

        Internal note regarding the invoice

        :param notes: The notes of this InvoiceDetailsApiModel.
        :type notes: str
        """

        self._notes = notes

    @property
    def number(self):
        """Gets the number of this InvoiceDetailsApiModel.

        Unique invoice number

        :return: The number of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InvoiceDetailsApiModel.

        Unique invoice number

        :param number: The number of this InvoiceDetailsApiModel.
        :type number: str
        """

        self._number = number

    @property
    def po_number(self):
        """Gets the po_number of this InvoiceDetailsApiModel.

        Unique number generated by the buyer

        :return: The po_number of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this InvoiceDetailsApiModel.

        Unique number generated by the buyer

        :param po_number: The po_number of this InvoiceDetailsApiModel.
        :type po_number: str
        """

        self._po_number = po_number

    @property
    def recurring_profile(self):
        """Gets the recurring_profile of this InvoiceDetailsApiModel.


        :return: The recurring_profile of this InvoiceDetailsApiModel.
        :rtype: InvoiceRecurringApiModel
        """
        return self._recurring_profile

    @recurring_profile.setter
    def recurring_profile(self, recurring_profile):
        """Sets the recurring_profile of this InvoiceDetailsApiModel.


        :param recurring_profile: The recurring_profile of this InvoiceDetailsApiModel.
        :type recurring_profile: InvoiceRecurringApiModel
        """

        self._recurring_profile = recurring_profile

    @property
    def recurring_profile_id(self):
        """Gets the recurring_profile_id of this InvoiceDetailsApiModel.

        Hold the id of the recurring profile

        :return: The recurring_profile_id of this InvoiceDetailsApiModel.
        :rtype: int
        """
        return self._recurring_profile_id

    @recurring_profile_id.setter
    def recurring_profile_id(self, recurring_profile_id):
        """Sets the recurring_profile_id of this InvoiceDetailsApiModel.

        Hold the id of the recurring profile

        :param recurring_profile_id: The recurring_profile_id of this InvoiceDetailsApiModel.
        :type recurring_profile_id: int
        """

        self._recurring_profile_id = recurring_profile_id

    @property
    def should_send_reminders(self):
        """Gets the should_send_reminders of this InvoiceDetailsApiModel.

        Should send email reminders to client?

        :return: The should_send_reminders of this InvoiceDetailsApiModel.
        :rtype: bool
        """
        return self._should_send_reminders

    @should_send_reminders.setter
    def should_send_reminders(self, should_send_reminders):
        """Sets the should_send_reminders of this InvoiceDetailsApiModel.

        Should send email reminders to client?

        :param should_send_reminders: The should_send_reminders of this InvoiceDetailsApiModel.
        :type should_send_reminders: bool
        """

        self._should_send_reminders = should_send_reminders

    @property
    def status(self):
        """Gets the status of this InvoiceDetailsApiModel.

        Indicate the status of the invoice (paid/unpaid/overdue)

        :return: The status of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvoiceDetailsApiModel.

        Indicate the status of the invoice (paid/unpaid/overdue)

        :param status: The status of this InvoiceDetailsApiModel.
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
        """Gets the sub_total_amount of this InvoiceDetailsApiModel.

        Total amount of the invoice without tax

        :return: The sub_total_amount of this InvoiceDetailsApiModel.
        :rtype: float
        """
        return self._sub_total_amount

    @sub_total_amount.setter
    def sub_total_amount(self, sub_total_amount):
        """Sets the sub_total_amount of this InvoiceDetailsApiModel.

        Total amount of the invoice without tax

        :param sub_total_amount: The sub_total_amount of this InvoiceDetailsApiModel.
        :type sub_total_amount: float
        """

        self._sub_total_amount = sub_total_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this InvoiceDetailsApiModel.

        Amount that goes to the tax

        :return: The tax_amount of this InvoiceDetailsApiModel.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this InvoiceDetailsApiModel.

        Amount that goes to the tax

        :param tax_amount: The tax_amount of this InvoiceDetailsApiModel.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount

    @property
    def terms(self):
        """Gets the terms of this InvoiceDetailsApiModel.

        Terms of agreement

        :return: The terms of this InvoiceDetailsApiModel.
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this InvoiceDetailsApiModel.

        Terms of agreement

        :param terms: The terms of this InvoiceDetailsApiModel.
        :type terms: str
        """

        self._terms = terms

    @property
    def total_amount(self):
        """Gets the total_amount of this InvoiceDetailsApiModel.

        Total amount of the invoice with tax

        :return: The total_amount of this InvoiceDetailsApiModel.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this InvoiceDetailsApiModel.

        Total amount of the invoice with tax

        :param total_amount: The total_amount of this InvoiceDetailsApiModel.
        :type total_amount: float
        """

        self._total_amount = total_amount
