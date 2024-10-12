# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bill_issuer_details import BillIssuerDetails
from openapi_server.models.bill_line_item import BillLineItem
from openapi_server.models.bill_links import BillLinks
from openapi_server.models.bill_recipient_details import BillRecipientDetails
from openapi_server import util


class Bill(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_idfk: int=None, balance: float=None, bill_number: str=None, company_idfk: int=None, company_name: str=None, currency_code: str=None, date_created: datetime=None, date_issued: datetime=None, date_updated: datetime=None, date_verified: datetime=None, due_date: datetime=None, exchange_rate: float=None, issuer: BillIssuerDetails=None, line_items: List[BillLineItem]=None, links: BillLinks=None, notes: str=None, recipient: BillRecipientDetails=None, subject: str=None, supplier_po_number: str=None, tax_amount: float=None, total_amount: float=None, transaction_id: int=None, transaction_prefix: str=None, transaction_status_code: str=None, transaction_tax_config_code: str=None):
        """Bill - a model defined in OpenAPI

        :param account_idfk: The account_idfk of this Bill.
        :param balance: The balance of this Bill.
        :param bill_number: The bill_number of this Bill.
        :param company_idfk: The company_idfk of this Bill.
        :param company_name: The company_name of this Bill.
        :param currency_code: The currency_code of this Bill.
        :param date_created: The date_created of this Bill.
        :param date_issued: The date_issued of this Bill.
        :param date_updated: The date_updated of this Bill.
        :param date_verified: The date_verified of this Bill.
        :param due_date: The due_date of this Bill.
        :param exchange_rate: The exchange_rate of this Bill.
        :param issuer: The issuer of this Bill.
        :param line_items: The line_items of this Bill.
        :param links: The links of this Bill.
        :param notes: The notes of this Bill.
        :param recipient: The recipient of this Bill.
        :param subject: The subject of this Bill.
        :param supplier_po_number: The supplier_po_number of this Bill.
        :param tax_amount: The tax_amount of this Bill.
        :param total_amount: The total_amount of this Bill.
        :param transaction_id: The transaction_id of this Bill.
        :param transaction_prefix: The transaction_prefix of this Bill.
        :param transaction_status_code: The transaction_status_code of this Bill.
        :param transaction_tax_config_code: The transaction_tax_config_code of this Bill.
        """
        self.openapi_types = {
            'account_idfk': int,
            'balance': float,
            'bill_number': str,
            'company_idfk': int,
            'company_name': str,
            'currency_code': str,
            'date_created': datetime,
            'date_issued': datetime,
            'date_updated': datetime,
            'date_verified': datetime,
            'due_date': datetime,
            'exchange_rate': float,
            'issuer': BillIssuerDetails,
            'line_items': List[BillLineItem],
            'links': BillLinks,
            'notes': str,
            'recipient': BillRecipientDetails,
            'subject': str,
            'supplier_po_number': str,
            'tax_amount': float,
            'total_amount': float,
            'transaction_id': int,
            'transaction_prefix': str,
            'transaction_status_code': str,
            'transaction_tax_config_code': str
        }

        self.attribute_map = {
            'account_idfk': 'AccountIDFK',
            'balance': 'Balance',
            'bill_number': 'BillNumber',
            'company_idfk': 'CompanyIDFK',
            'company_name': 'CompanyName',
            'currency_code': 'CurrencyCode',
            'date_created': 'DateCreated',
            'date_issued': 'DateIssued',
            'date_updated': 'DateUpdated',
            'date_verified': 'DateVerified',
            'due_date': 'DueDate',
            'exchange_rate': 'ExchangeRate',
            'issuer': 'Issuer',
            'line_items': 'LineItems',
            'links': 'Links',
            'notes': 'Notes',
            'recipient': 'Recipient',
            'subject': 'Subject',
            'supplier_po_number': 'SupplierPONumber',
            'tax_amount': 'TaxAmount',
            'total_amount': 'TotalAmount',
            'transaction_id': 'TransactionID',
            'transaction_prefix': 'TransactionPrefix',
            'transaction_status_code': 'TransactionStatusCode',
            'transaction_tax_config_code': 'TransactionTaxConfigCode'
        }

        self._account_idfk = account_idfk
        self._balance = balance
        self._bill_number = bill_number
        self._company_idfk = company_idfk
        self._company_name = company_name
        self._currency_code = currency_code
        self._date_created = date_created
        self._date_issued = date_issued
        self._date_updated = date_updated
        self._date_verified = date_verified
        self._due_date = due_date
        self._exchange_rate = exchange_rate
        self._issuer = issuer
        self._line_items = line_items
        self._links = links
        self._notes = notes
        self._recipient = recipient
        self._subject = subject
        self._supplier_po_number = supplier_po_number
        self._tax_amount = tax_amount
        self._total_amount = total_amount
        self._transaction_id = transaction_id
        self._transaction_prefix = transaction_prefix
        self._transaction_status_code = transaction_status_code
        self._transaction_tax_config_code = transaction_tax_config_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Bill':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Bill of this Bill.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_idfk(self):
        """Gets the account_idfk of this Bill.


        :return: The account_idfk of this Bill.
        :rtype: int
        """
        return self._account_idfk

    @account_idfk.setter
    def account_idfk(self, account_idfk):
        """Sets the account_idfk of this Bill.


        :param account_idfk: The account_idfk of this Bill.
        :type account_idfk: int
        """

        self._account_idfk = account_idfk

    @property
    def balance(self):
        """Gets the balance of this Bill.


        :return: The balance of this Bill.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Bill.


        :param balance: The balance of this Bill.
        :type balance: float
        """

        self._balance = balance

    @property
    def bill_number(self):
        """Gets the bill_number of this Bill.


        :return: The bill_number of this Bill.
        :rtype: str
        """
        return self._bill_number

    @bill_number.setter
    def bill_number(self, bill_number):
        """Sets the bill_number of this Bill.


        :param bill_number: The bill_number of this Bill.
        :type bill_number: str
        """

        self._bill_number = bill_number

    @property
    def company_idfk(self):
        """Gets the company_idfk of this Bill.


        :return: The company_idfk of this Bill.
        :rtype: int
        """
        return self._company_idfk

    @company_idfk.setter
    def company_idfk(self, company_idfk):
        """Sets the company_idfk of this Bill.


        :param company_idfk: The company_idfk of this Bill.
        :type company_idfk: int
        """

        self._company_idfk = company_idfk

    @property
    def company_name(self):
        """Gets the company_name of this Bill.


        :return: The company_name of this Bill.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Bill.


        :param company_name: The company_name of this Bill.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def currency_code(self):
        """Gets the currency_code of this Bill.


        :return: The currency_code of this Bill.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Bill.


        :param currency_code: The currency_code of this Bill.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def date_created(self):
        """Gets the date_created of this Bill.


        :return: The date_created of this Bill.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Bill.


        :param date_created: The date_created of this Bill.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_issued(self):
        """Gets the date_issued of this Bill.


        :return: The date_issued of this Bill.
        :rtype: datetime
        """
        return self._date_issued

    @date_issued.setter
    def date_issued(self, date_issued):
        """Sets the date_issued of this Bill.


        :param date_issued: The date_issued of this Bill.
        :type date_issued: datetime
        """

        self._date_issued = date_issued

    @property
    def date_updated(self):
        """Gets the date_updated of this Bill.


        :return: The date_updated of this Bill.
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this Bill.


        :param date_updated: The date_updated of this Bill.
        :type date_updated: datetime
        """

        self._date_updated = date_updated

    @property
    def date_verified(self):
        """Gets the date_verified of this Bill.


        :return: The date_verified of this Bill.
        :rtype: datetime
        """
        return self._date_verified

    @date_verified.setter
    def date_verified(self, date_verified):
        """Sets the date_verified of this Bill.


        :param date_verified: The date_verified of this Bill.
        :type date_verified: datetime
        """

        self._date_verified = date_verified

    @property
    def due_date(self):
        """Gets the due_date of this Bill.


        :return: The due_date of this Bill.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Bill.


        :param due_date: The due_date of this Bill.
        :type due_date: datetime
        """

        self._due_date = due_date

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Bill.


        :return: The exchange_rate of this Bill.
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Bill.


        :param exchange_rate: The exchange_rate of this Bill.
        :type exchange_rate: float
        """

        self._exchange_rate = exchange_rate

    @property
    def issuer(self):
        """Gets the issuer of this Bill.


        :return: The issuer of this Bill.
        :rtype: BillIssuerDetails
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Bill.


        :param issuer: The issuer of this Bill.
        :type issuer: BillIssuerDetails
        """

        self._issuer = issuer

    @property
    def line_items(self):
        """Gets the line_items of this Bill.


        :return: The line_items of this Bill.
        :rtype: List[BillLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Bill.


        :param line_items: The line_items of this Bill.
        :type line_items: List[BillLineItem]
        """

        self._line_items = line_items

    @property
    def links(self):
        """Gets the links of this Bill.


        :return: The links of this Bill.
        :rtype: BillLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Bill.


        :param links: The links of this Bill.
        :type links: BillLinks
        """

        self._links = links

    @property
    def notes(self):
        """Gets the notes of this Bill.


        :return: The notes of this Bill.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Bill.


        :param notes: The notes of this Bill.
        :type notes: str
        """

        self._notes = notes

    @property
    def recipient(self):
        """Gets the recipient of this Bill.


        :return: The recipient of this Bill.
        :rtype: BillRecipientDetails
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Bill.


        :param recipient: The recipient of this Bill.
        :type recipient: BillRecipientDetails
        """

        self._recipient = recipient

    @property
    def subject(self):
        """Gets the subject of this Bill.


        :return: The subject of this Bill.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Bill.


        :param subject: The subject of this Bill.
        :type subject: str
        """

        self._subject = subject

    @property
    def supplier_po_number(self):
        """Gets the supplier_po_number of this Bill.


        :return: The supplier_po_number of this Bill.
        :rtype: str
        """
        return self._supplier_po_number

    @supplier_po_number.setter
    def supplier_po_number(self, supplier_po_number):
        """Sets the supplier_po_number of this Bill.


        :param supplier_po_number: The supplier_po_number of this Bill.
        :type supplier_po_number: str
        """

        self._supplier_po_number = supplier_po_number

    @property
    def tax_amount(self):
        """Gets the tax_amount of this Bill.


        :return: The tax_amount of this Bill.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this Bill.


        :param tax_amount: The tax_amount of this Bill.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this Bill.


        :return: The total_amount of this Bill.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Bill.


        :param total_amount: The total_amount of this Bill.
        :type total_amount: float
        """

        self._total_amount = total_amount

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Bill.


        :return: The transaction_id of this Bill.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Bill.


        :param transaction_id: The transaction_id of this Bill.
        :type transaction_id: int
        """

        self._transaction_id = transaction_id

    @property
    def transaction_prefix(self):
        """Gets the transaction_prefix of this Bill.


        :return: The transaction_prefix of this Bill.
        :rtype: str
        """
        return self._transaction_prefix

    @transaction_prefix.setter
    def transaction_prefix(self, transaction_prefix):
        """Sets the transaction_prefix of this Bill.


        :param transaction_prefix: The transaction_prefix of this Bill.
        :type transaction_prefix: str
        """

        self._transaction_prefix = transaction_prefix

    @property
    def transaction_status_code(self):
        """Gets the transaction_status_code of this Bill.


        :return: The transaction_status_code of this Bill.
        :rtype: str
        """
        return self._transaction_status_code

    @transaction_status_code.setter
    def transaction_status_code(self, transaction_status_code):
        """Sets the transaction_status_code of this Bill.


        :param transaction_status_code: The transaction_status_code of this Bill.
        :type transaction_status_code: str
        """

        self._transaction_status_code = transaction_status_code

    @property
    def transaction_tax_config_code(self):
        """Gets the transaction_tax_config_code of this Bill.


        :return: The transaction_tax_config_code of this Bill.
        :rtype: str
        """
        return self._transaction_tax_config_code

    @transaction_tax_config_code.setter
    def transaction_tax_config_code(self, transaction_tax_config_code):
        """Sets the transaction_tax_config_code of this Bill.


        :param transaction_tax_config_code: The transaction_tax_config_code of this Bill.
        :type transaction_tax_config_code: str
        """

        self._transaction_tax_config_code = transaction_tax_config_code
