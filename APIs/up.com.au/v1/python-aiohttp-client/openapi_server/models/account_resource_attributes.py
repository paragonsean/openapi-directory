# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_type_enum import AccountTypeEnum
from openapi_server.models.money_object import MoneyObject
from openapi_server.models.ownership_type_enum import OwnershipTypeEnum
from openapi_server import util


class AccountResourceAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_type: AccountTypeEnum=None, balance: MoneyObject=None, created_at: datetime=None, display_name: str=None, ownership_type: OwnershipTypeEnum=None):
        """AccountResourceAttributes - a model defined in OpenAPI

        :param account_type: The account_type of this AccountResourceAttributes.
        :param balance: The balance of this AccountResourceAttributes.
        :param created_at: The created_at of this AccountResourceAttributes.
        :param display_name: The display_name of this AccountResourceAttributes.
        :param ownership_type: The ownership_type of this AccountResourceAttributes.
        """
        self.openapi_types = {
            'account_type': AccountTypeEnum,
            'balance': MoneyObject,
            'created_at': datetime,
            'display_name': str,
            'ownership_type': OwnershipTypeEnum
        }

        self.attribute_map = {
            'account_type': 'accountType',
            'balance': 'balance',
            'created_at': 'createdAt',
            'display_name': 'displayName',
            'ownership_type': 'ownershipType'
        }

        self._account_type = account_type
        self._balance = balance
        self._created_at = created_at
        self._display_name = display_name
        self._ownership_type = ownership_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccountResourceAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AccountResource_attributes of this AccountResourceAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_type(self):
        """Gets the account_type of this AccountResourceAttributes.

        The bank account type of this account. 

        :return: The account_type of this AccountResourceAttributes.
        :rtype: AccountTypeEnum
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountResourceAttributes.

        The bank account type of this account. 

        :param account_type: The account_type of this AccountResourceAttributes.
        :type account_type: AccountTypeEnum
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")

        self._account_type = account_type

    @property
    def balance(self):
        """Gets the balance of this AccountResourceAttributes.

        The available balance of the account, taking into account any amounts that are currently on hold. 

        :return: The balance of this AccountResourceAttributes.
        :rtype: MoneyObject
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountResourceAttributes.

        The available balance of the account, taking into account any amounts that are currently on hold. 

        :param balance: The balance of this AccountResourceAttributes.
        :type balance: MoneyObject
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")

        self._balance = balance

    @property
    def created_at(self):
        """Gets the created_at of this AccountResourceAttributes.

        The date-time at which this account was first opened. 

        :return: The created_at of this AccountResourceAttributes.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountResourceAttributes.

        The date-time at which this account was first opened. 

        :param created_at: The created_at of this AccountResourceAttributes.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def display_name(self):
        """Gets the display_name of this AccountResourceAttributes.

        The name associated with the account in the Up application. 

        :return: The display_name of this AccountResourceAttributes.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AccountResourceAttributes.

        The name associated with the account in the Up application. 

        :param display_name: The display_name of this AccountResourceAttributes.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def ownership_type(self):
        """Gets the ownership_type of this AccountResourceAttributes.

        The ownership structure for this account. 

        :return: The ownership_type of this AccountResourceAttributes.
        :rtype: OwnershipTypeEnum
        """
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, ownership_type):
        """Sets the ownership_type of this AccountResourceAttributes.

        The ownership structure for this account. 

        :param ownership_type: The ownership_type of this AccountResourceAttributes.
        :type ownership_type: OwnershipTypeEnum
        """
        if ownership_type is None:
            raise ValueError("Invalid value for `ownership_type`, must not be `None`")

        self._ownership_type = ownership_type
