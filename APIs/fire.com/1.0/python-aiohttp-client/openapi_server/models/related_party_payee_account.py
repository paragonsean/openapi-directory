# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RelatedPartyPayeeAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_number: str=None, alias: str=None, bic: str=None, iban: str=None, id: int=None, nsc: str=None):
        """RelatedPartyPayeeAccount - a model defined in OpenAPI

        :param account_number: The account_number of this RelatedPartyPayeeAccount.
        :param alias: The alias of this RelatedPartyPayeeAccount.
        :param bic: The bic of this RelatedPartyPayeeAccount.
        :param iban: The iban of this RelatedPartyPayeeAccount.
        :param id: The id of this RelatedPartyPayeeAccount.
        :param nsc: The nsc of this RelatedPartyPayeeAccount.
        """
        self.openapi_types = {
            'account_number': str,
            'alias': str,
            'bic': str,
            'iban': str,
            'id': int,
            'nsc': str
        }

        self.attribute_map = {
            'account_number': 'accountNumber',
            'alias': 'alias',
            'bic': 'bic',
            'iban': 'iban',
            'id': 'id',
            'nsc': 'nsc'
        }

        self._account_number = account_number
        self._alias = alias
        self._bic = bic
        self._iban = iban
        self._id = id
        self._nsc = nsc

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RelatedPartyPayeeAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The relatedPartyPayee_account of this RelatedPartyPayeeAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_number(self):
        """Gets the account_number of this RelatedPartyPayeeAccount.

        The account number of the Withdrawl account in reference

        :return: The account_number of this RelatedPartyPayeeAccount.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this RelatedPartyPayeeAccount.

        The account number of the Withdrawl account in reference

        :param account_number: The account_number of this RelatedPartyPayeeAccount.
        :type account_number: str
        """

        self._account_number = account_number

    @property
    def alias(self):
        """Gets the alias of this RelatedPartyPayeeAccount.

        The Alias name of the Withdrawl account in reference

        :return: The alias of this RelatedPartyPayeeAccount.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this RelatedPartyPayeeAccount.

        The Alias name of the Withdrawl account in reference

        :param alias: The alias of this RelatedPartyPayeeAccount.
        :type alias: str
        """

        self._alias = alias

    @property
    def bic(self):
        """Gets the bic of this RelatedPartyPayeeAccount.

        The BIC of the Withdrawl account in reference

        :return: The bic of this RelatedPartyPayeeAccount.
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this RelatedPartyPayeeAccount.

        The BIC of the Withdrawl account in reference

        :param bic: The bic of this RelatedPartyPayeeAccount.
        :type bic: str
        """

        self._bic = bic

    @property
    def iban(self):
        """Gets the iban of this RelatedPartyPayeeAccount.

        The BIC of the Withdrawl account in reference

        :return: The iban of this RelatedPartyPayeeAccount.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this RelatedPartyPayeeAccount.

        The BIC of the Withdrawl account in reference

        :param iban: The iban of this RelatedPartyPayeeAccount.
        :type iban: str
        """

        self._iban = iban

    @property
    def id(self):
        """Gets the id of this RelatedPartyPayeeAccount.

        The ID number of the Withdrawl account in reference

        :return: The id of this RelatedPartyPayeeAccount.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelatedPartyPayeeAccount.

        The ID number of the Withdrawl account in reference

        :param id: The id of this RelatedPartyPayeeAccount.
        :type id: int
        """

        self._id = id

    @property
    def nsc(self):
        """Gets the nsc of this RelatedPartyPayeeAccount.

        (Conditional) Provide this field if using Mode 2 and the payee account is in GBP.

        :return: The nsc of this RelatedPartyPayeeAccount.
        :rtype: str
        """
        return self._nsc

    @nsc.setter
    def nsc(self, nsc):
        """Sets the nsc of this RelatedPartyPayeeAccount.

        (Conditional) Provide this field if using Mode 2 and the payee account is in GBP.

        :param nsc: The nsc of this RelatedPartyPayeeAccount.
        :type nsc: str
        """

        self._nsc = nsc
