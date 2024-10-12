# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_reference16_ch import AccountReference16CH
from openapi_server.models.balance import Balance
from openapi_server.models.card_account_report import CardAccountReport
from openapi_server.models.links_download import LinksDownload
from openapi_server import util


class CardAccountsTransactionsResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: LinksDownload=None, balances: List[Balance]=None, card_account: AccountReference16CH=None, card_transactions: CardAccountReport=None, debit_accounting: bool=None):
        """CardAccountsTransactionsResponse200 - a model defined in OpenAPI

        :param links: The links of this CardAccountsTransactionsResponse200.
        :param balances: The balances of this CardAccountsTransactionsResponse200.
        :param card_account: The card_account of this CardAccountsTransactionsResponse200.
        :param card_transactions: The card_transactions of this CardAccountsTransactionsResponse200.
        :param debit_accounting: The debit_accounting of this CardAccountsTransactionsResponse200.
        """
        self.openapi_types = {
            'links': LinksDownload,
            'balances': List[Balance],
            'card_account': AccountReference16CH,
            'card_transactions': CardAccountReport,
            'debit_accounting': bool
        }

        self.attribute_map = {
            'links': '_links',
            'balances': 'balances',
            'card_account': 'cardAccount',
            'card_transactions': 'cardTransactions',
            'debit_accounting': 'debitAccounting'
        }

        self._links = links
        self._balances = balances
        self._card_account = card_account
        self._card_transactions = card_transactions
        self._debit_accounting = debit_accounting

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CardAccountsTransactionsResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The cardAccountsTransactionsResponse200 of this CardAccountsTransactionsResponse200.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this CardAccountsTransactionsResponse200.


        :return: The links of this CardAccountsTransactionsResponse200.
        :rtype: LinksDownload
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CardAccountsTransactionsResponse200.


        :param links: The links of this CardAccountsTransactionsResponse200.
        :type links: LinksDownload
        """

        self._links = links

    @property
    def balances(self):
        """Gets the balances of this CardAccountsTransactionsResponse200.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :return: The balances of this CardAccountsTransactionsResponse200.
        :rtype: List[Balance]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this CardAccountsTransactionsResponse200.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :param balances: The balances of this CardAccountsTransactionsResponse200.
        :type balances: List[Balance]
        """

        self._balances = balances

    @property
    def card_account(self):
        """Gets the card_account of this CardAccountsTransactionsResponse200.


        :return: The card_account of this CardAccountsTransactionsResponse200.
        :rtype: AccountReference16CH
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this CardAccountsTransactionsResponse200.


        :param card_account: The card_account of this CardAccountsTransactionsResponse200.
        :type card_account: AccountReference16CH
        """

        self._card_account = card_account

    @property
    def card_transactions(self):
        """Gets the card_transactions of this CardAccountsTransactionsResponse200.


        :return: The card_transactions of this CardAccountsTransactionsResponse200.
        :rtype: CardAccountReport
        """
        return self._card_transactions

    @card_transactions.setter
    def card_transactions(self, card_transactions):
        """Sets the card_transactions of this CardAccountsTransactionsResponse200.


        :param card_transactions: The card_transactions of this CardAccountsTransactionsResponse200.
        :type card_transactions: CardAccountReport
        """

        self._card_transactions = card_transactions

    @property
    def debit_accounting(self):
        """Gets the debit_accounting of this CardAccountsTransactionsResponse200.

        If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative. 

        :return: The debit_accounting of this CardAccountsTransactionsResponse200.
        :rtype: bool
        """
        return self._debit_accounting

    @debit_accounting.setter
    def debit_accounting(self, debit_accounting):
        """Sets the debit_accounting of this CardAccountsTransactionsResponse200.

        If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative. 

        :param debit_accounting: The debit_accounting of this CardAccountsTransactionsResponse200.
        :type debit_accounting: bool
        """

        self._debit_accounting = debit_accounting
