# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_reference16_ch import AccountReference16CH
from openapi_server.models.balance import Balance
from openapi_server import util


class ReadCardAccountBalanceResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, balances: List[Balance]=None, card_account: AccountReference16CH=None, debit_accounting: bool=None):
        """ReadCardAccountBalanceResponse200 - a model defined in OpenAPI

        :param balances: The balances of this ReadCardAccountBalanceResponse200.
        :param card_account: The card_account of this ReadCardAccountBalanceResponse200.
        :param debit_accounting: The debit_accounting of this ReadCardAccountBalanceResponse200.
        """
        self.openapi_types = {
            'balances': List[Balance],
            'card_account': AccountReference16CH,
            'debit_accounting': bool
        }

        self.attribute_map = {
            'balances': 'balances',
            'card_account': 'cardAccount',
            'debit_accounting': 'debitAccounting'
        }

        self._balances = balances
        self._card_account = card_account
        self._debit_accounting = debit_accounting

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReadCardAccountBalanceResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The readCardAccountBalanceResponse-200 of this ReadCardAccountBalanceResponse200.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def balances(self):
        """Gets the balances of this ReadCardAccountBalanceResponse200.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :return: The balances of this ReadCardAccountBalanceResponse200.
        :rtype: List[Balance]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this ReadCardAccountBalanceResponse200.

        A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance. 

        :param balances: The balances of this ReadCardAccountBalanceResponse200.
        :type balances: List[Balance]
        """
        if balances is None:
            raise ValueError("Invalid value for `balances`, must not be `None`")

        self._balances = balances

    @property
    def card_account(self):
        """Gets the card_account of this ReadCardAccountBalanceResponse200.


        :return: The card_account of this ReadCardAccountBalanceResponse200.
        :rtype: AccountReference16CH
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this ReadCardAccountBalanceResponse200.


        :param card_account: The card_account of this ReadCardAccountBalanceResponse200.
        :type card_account: AccountReference16CH
        """

        self._card_account = card_account

    @property
    def debit_accounting(self):
        """Gets the debit_accounting of this ReadCardAccountBalanceResponse200.

        If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative. 

        :return: The debit_accounting of this ReadCardAccountBalanceResponse200.
        :rtype: bool
        """
        return self._debit_accounting

    @debit_accounting.setter
    def debit_accounting(self, debit_accounting):
        """Sets the debit_accounting of this ReadCardAccountBalanceResponse200.

        If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative. 

        :param debit_accounting: The debit_accounting of this ReadCardAccountBalanceResponse200.
        :type debit_accounting: bool
        """

        self._debit_accounting = debit_accounting
