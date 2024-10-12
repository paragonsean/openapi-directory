# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_reference16_ch import AccountReference16CH
from openapi_server.models.account_report import AccountReport
from openapi_server.models.balance import Balance
from openapi_server.models.links_download import LinksDownload
from openapi_server import util


class TransactionsResponse200Json(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: LinksDownload=None, account: AccountReference16CH=None, balances: List[Balance]=None, transactions: AccountReport=None):
        """TransactionsResponse200Json - a model defined in OpenAPI

        :param links: The links of this TransactionsResponse200Json.
        :param account: The account of this TransactionsResponse200Json.
        :param balances: The balances of this TransactionsResponse200Json.
        :param transactions: The transactions of this TransactionsResponse200Json.
        """
        self.openapi_types = {
            'links': LinksDownload,
            'account': AccountReference16CH,
            'balances': List[Balance],
            'transactions': AccountReport
        }

        self.attribute_map = {
            'links': '_links',
            'account': 'account',
            'balances': 'balances',
            'transactions': 'transactions'
        }

        self._links = links
        self._account = account
        self._balances = balances
        self._transactions = transactions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionsResponse200Json':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The transactionsResponse-200_json of this TransactionsResponse200Json.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this TransactionsResponse200Json.


        :return: The links of this TransactionsResponse200Json.
        :rtype: LinksDownload
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionsResponse200Json.


        :param links: The links of this TransactionsResponse200Json.
        :type links: LinksDownload
        """

        self._links = links

    @property
    def account(self):
        """Gets the account of this TransactionsResponse200Json.


        :return: The account of this TransactionsResponse200Json.
        :rtype: AccountReference16CH
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TransactionsResponse200Json.


        :param account: The account of this TransactionsResponse200Json.
        :type account: AccountReference16CH
        """

        self._account = account

    @property
    def balances(self):
        """Gets the balances of this TransactionsResponse200Json.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :return: The balances of this TransactionsResponse200Json.
        :rtype: List[Balance]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this TransactionsResponse200Json.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :param balances: The balances of this TransactionsResponse200Json.
        :type balances: List[Balance]
        """

        self._balances = balances

    @property
    def transactions(self):
        """Gets the transactions of this TransactionsResponse200Json.


        :return: The transactions of this TransactionsResponse200Json.
        :rtype: AccountReport
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this TransactionsResponse200Json.


        :param transactions: The transactions of this TransactionsResponse200Json.
        :type transactions: AccountReport
        """

        self._transactions = transactions
