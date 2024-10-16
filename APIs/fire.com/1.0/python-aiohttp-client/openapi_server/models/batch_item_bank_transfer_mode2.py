# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BatchItemBankTransferMode2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: int=None, dest_account_holder_name: str=None, dest_account_number: str=None, dest_iban: str=None, dest_nsc: str=None, ican_from: int=None, my_ref: str=None, payee_type: str=None, your_ref: str=None):
        """BatchItemBankTransferMode2 - a model defined in OpenAPI

        :param amount: The amount of this BatchItemBankTransferMode2.
        :param dest_account_holder_name: The dest_account_holder_name of this BatchItemBankTransferMode2.
        :param dest_account_number: The dest_account_number of this BatchItemBankTransferMode2.
        :param dest_iban: The dest_iban of this BatchItemBankTransferMode2.
        :param dest_nsc: The dest_nsc of this BatchItemBankTransferMode2.
        :param ican_from: The ican_from of this BatchItemBankTransferMode2.
        :param my_ref: The my_ref of this BatchItemBankTransferMode2.
        :param payee_type: The payee_type of this BatchItemBankTransferMode2.
        :param your_ref: The your_ref of this BatchItemBankTransferMode2.
        """
        self.openapi_types = {
            'amount': int,
            'dest_account_holder_name': str,
            'dest_account_number': str,
            'dest_iban': str,
            'dest_nsc': str,
            'ican_from': int,
            'my_ref': str,
            'payee_type': str,
            'your_ref': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'dest_account_holder_name': 'destAccountHolderName',
            'dest_account_number': 'destAccountNumber',
            'dest_iban': 'destIban',
            'dest_nsc': 'destNsc',
            'ican_from': 'icanFrom',
            'my_ref': 'myRef',
            'payee_type': 'payeeType',
            'your_ref': 'yourRef'
        }

        self._amount = amount
        self._dest_account_holder_name = dest_account_holder_name
        self._dest_account_number = dest_account_number
        self._dest_iban = dest_iban
        self._dest_nsc = dest_nsc
        self._ican_from = ican_from
        self._my_ref = my_ref
        self._payee_type = payee_type
        self._your_ref = your_ref

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BatchItemBankTransferMode2':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The batchItemBankTransferMode2 of this BatchItemBankTransferMode2.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this BatchItemBankTransferMode2.

        The value of the transaction

        :return: The amount of this BatchItemBankTransferMode2.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BatchItemBankTransferMode2.

        The value of the transaction

        :param amount: The amount of this BatchItemBankTransferMode2.
        :type amount: int
        """

        self._amount = amount

    @property
    def dest_account_holder_name(self):
        """Gets the dest_account_holder_name of this BatchItemBankTransferMode2.

        The destination account holder name

        :return: The dest_account_holder_name of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._dest_account_holder_name

    @dest_account_holder_name.setter
    def dest_account_holder_name(self, dest_account_holder_name):
        """Sets the dest_account_holder_name of this BatchItemBankTransferMode2.

        The destination account holder name

        :param dest_account_holder_name: The dest_account_holder_name of this BatchItemBankTransferMode2.
        :type dest_account_holder_name: str
        """

        self._dest_account_holder_name = dest_account_holder_name

    @property
    def dest_account_number(self):
        """Gets the dest_account_number of this BatchItemBankTransferMode2.

        The destination Account Number if a GBP bank transfer

        :return: The dest_account_number of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._dest_account_number

    @dest_account_number.setter
    def dest_account_number(self, dest_account_number):
        """Sets the dest_account_number of this BatchItemBankTransferMode2.

        The destination Account Number if a GBP bank transfer

        :param dest_account_number: The dest_account_number of this BatchItemBankTransferMode2.
        :type dest_account_number: str
        """

        self._dest_account_number = dest_account_number

    @property
    def dest_iban(self):
        """Gets the dest_iban of this BatchItemBankTransferMode2.

        The destination IBAN if a Euro Bank transfer

        :return: The dest_iban of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._dest_iban

    @dest_iban.setter
    def dest_iban(self, dest_iban):
        """Sets the dest_iban of this BatchItemBankTransferMode2.

        The destination IBAN if a Euro Bank transfer

        :param dest_iban: The dest_iban of this BatchItemBankTransferMode2.
        :type dest_iban: str
        """

        self._dest_iban = dest_iban

    @property
    def dest_nsc(self):
        """Gets the dest_nsc of this BatchItemBankTransferMode2.

        The destination Nsc if a GBP bank transfer

        :return: The dest_nsc of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._dest_nsc

    @dest_nsc.setter
    def dest_nsc(self, dest_nsc):
        """Sets the dest_nsc of this BatchItemBankTransferMode2.

        The destination Nsc if a GBP bank transfer

        :param dest_nsc: The dest_nsc of this BatchItemBankTransferMode2.
        :type dest_nsc: str
        """

        self._dest_nsc = dest_nsc

    @property
    def ican_from(self):
        """Gets the ican_from of this BatchItemBankTransferMode2.

        The Fire account ID for the fire.com account the funds are taken from.

        :return: The ican_from of this BatchItemBankTransferMode2.
        :rtype: int
        """
        return self._ican_from

    @ican_from.setter
    def ican_from(self, ican_from):
        """Sets the ican_from of this BatchItemBankTransferMode2.

        The Fire account ID for the fire.com account the funds are taken from.

        :param ican_from: The ican_from of this BatchItemBankTransferMode2.
        :type ican_from: int
        """

        self._ican_from = ican_from

    @property
    def my_ref(self):
        """Gets the my_ref of this BatchItemBankTransferMode2.

        The reference on the transaction for your records - not shown to the beneficiary.

        :return: The my_ref of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._my_ref

    @my_ref.setter
    def my_ref(self, my_ref):
        """Sets the my_ref of this BatchItemBankTransferMode2.

        The reference on the transaction for your records - not shown to the beneficiary.

        :param my_ref: The my_ref of this BatchItemBankTransferMode2.
        :type my_ref: str
        """

        self._my_ref = my_ref

    @property
    def payee_type(self):
        """Gets the payee_type of this BatchItemBankTransferMode2.

        Use ACCOUNT_DETAILS if you are providing account numbers/sort codes/IBANs (Mode 2). Specify the account details in the destIban, destAccountHolderName, destNsc or destAccountNumber fields as appropriate.

        :return: The payee_type of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this BatchItemBankTransferMode2.

        Use ACCOUNT_DETAILS if you are providing account numbers/sort codes/IBANs (Mode 2). Specify the account details in the destIban, destAccountHolderName, destNsc or destAccountNumber fields as appropriate.

        :param payee_type: The payee_type of this BatchItemBankTransferMode2.
        :type payee_type: str
        """
        allowed_values = ["ACCOUNT_DETAILS"]  # noqa: E501
        if payee_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payee_type` ({0}), must be one of {1}"
                .format(payee_type, allowed_values)
            )

        self._payee_type = payee_type

    @property
    def your_ref(self):
        """Gets the your_ref of this BatchItemBankTransferMode2.

        The reference on the transaction - displayed on the beneficiary bank statement.

        :return: The your_ref of this BatchItemBankTransferMode2.
        :rtype: str
        """
        return self._your_ref

    @your_ref.setter
    def your_ref(self, your_ref):
        """Sets the your_ref of this BatchItemBankTransferMode2.

        The reference on the transaction - displayed on the beneficiary bank statement.

        :param your_ref: The your_ref of this BatchItemBankTransferMode2.
        :type your_ref: str
        """

        self._your_ref = your_ref
