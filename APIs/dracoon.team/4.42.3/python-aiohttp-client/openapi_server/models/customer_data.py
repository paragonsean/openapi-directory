# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CustomerData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accounts_limit: int=None, accounts_used: int=None, cnt_guest_user: int=None, cnt_internal_user: int=None, customer_encryption_enabled: bool=None, id: int=None, is_provider_customer: bool=None, name: str=None, space_limit: int=None, space_used: int=None):
        """CustomerData - a model defined in OpenAPI

        :param accounts_limit: The accounts_limit of this CustomerData.
        :param accounts_used: The accounts_used of this CustomerData.
        :param cnt_guest_user: The cnt_guest_user of this CustomerData.
        :param cnt_internal_user: The cnt_internal_user of this CustomerData.
        :param customer_encryption_enabled: The customer_encryption_enabled of this CustomerData.
        :param id: The id of this CustomerData.
        :param is_provider_customer: The is_provider_customer of this CustomerData.
        :param name: The name of this CustomerData.
        :param space_limit: The space_limit of this CustomerData.
        :param space_used: The space_used of this CustomerData.
        """
        self.openapi_types = {
            'accounts_limit': int,
            'accounts_used': int,
            'cnt_guest_user': int,
            'cnt_internal_user': int,
            'customer_encryption_enabled': bool,
            'id': int,
            'is_provider_customer': bool,
            'name': str,
            'space_limit': int,
            'space_used': int
        }

        self.attribute_map = {
            'accounts_limit': 'accountsLimit',
            'accounts_used': 'accountsUsed',
            'cnt_guest_user': 'cntGuestUser',
            'cnt_internal_user': 'cntInternalUser',
            'customer_encryption_enabled': 'customerEncryptionEnabled',
            'id': 'id',
            'is_provider_customer': 'isProviderCustomer',
            'name': 'name',
            'space_limit': 'spaceLimit',
            'space_used': 'spaceUsed'
        }

        self._accounts_limit = accounts_limit
        self._accounts_used = accounts_used
        self._cnt_guest_user = cnt_guest_user
        self._cnt_internal_user = cnt_internal_user
        self._customer_encryption_enabled = customer_encryption_enabled
        self._id = id
        self._is_provider_customer = is_provider_customer
        self._name = name
        self._space_limit = space_limit
        self._space_used = space_used

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CustomerData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CustomerData of this CustomerData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accounts_limit(self):
        """Gets the accounts_limit of this CustomerData.

        User accounts limit

        :return: The accounts_limit of this CustomerData.
        :rtype: int
        """
        return self._accounts_limit

    @accounts_limit.setter
    def accounts_limit(self, accounts_limit):
        """Sets the accounts_limit of this CustomerData.

        User accounts limit

        :param accounts_limit: The accounts_limit of this CustomerData.
        :type accounts_limit: int
        """
        if accounts_limit is None:
            raise ValueError("Invalid value for `accounts_limit`, must not be `None`")

        self._accounts_limit = accounts_limit

    @property
    def accounts_used(self):
        """Gets the accounts_used of this CustomerData.

        User accounts used

        :return: The accounts_used of this CustomerData.
        :rtype: int
        """
        return self._accounts_used

    @accounts_used.setter
    def accounts_used(self, accounts_used):
        """Sets the accounts_used of this CustomerData.

        User accounts used

        :param accounts_used: The accounts_used of this CustomerData.
        :type accounts_used: int
        """
        if accounts_used is None:
            raise ValueError("Invalid value for `accounts_used`, must not be `None`")

        self._accounts_used = accounts_used

    @property
    def cnt_guest_user(self):
        """Gets the cnt_guest_user of this CustomerData.

        Number of guest user accounts

        :return: The cnt_guest_user of this CustomerData.
        :rtype: int
        """
        return self._cnt_guest_user

    @cnt_guest_user.setter
    def cnt_guest_user(self, cnt_guest_user):
        """Sets the cnt_guest_user of this CustomerData.

        Number of guest user accounts

        :param cnt_guest_user: The cnt_guest_user of this CustomerData.
        :type cnt_guest_user: int
        """
        if cnt_guest_user is None:
            raise ValueError("Invalid value for `cnt_guest_user`, must not be `None`")

        self._cnt_guest_user = cnt_guest_user

    @property
    def cnt_internal_user(self):
        """Gets the cnt_internal_user of this CustomerData.

        Number of internal user accounts

        :return: The cnt_internal_user of this CustomerData.
        :rtype: int
        """
        return self._cnt_internal_user

    @cnt_internal_user.setter
    def cnt_internal_user(self, cnt_internal_user):
        """Sets the cnt_internal_user of this CustomerData.

        Number of internal user accounts

        :param cnt_internal_user: The cnt_internal_user of this CustomerData.
        :type cnt_internal_user: int
        """
        if cnt_internal_user is None:
            raise ValueError("Invalid value for `cnt_internal_user`, must not be `None`")

        self._cnt_internal_user = cnt_internal_user

    @property
    def customer_encryption_enabled(self):
        """Gets the customer_encryption_enabled of this CustomerData.

        Clientside encryption for customer enabled

        :return: The customer_encryption_enabled of this CustomerData.
        :rtype: bool
        """
        return self._customer_encryption_enabled

    @customer_encryption_enabled.setter
    def customer_encryption_enabled(self, customer_encryption_enabled):
        """Sets the customer_encryption_enabled of this CustomerData.

        Clientside encryption for customer enabled

        :param customer_encryption_enabled: The customer_encryption_enabled of this CustomerData.
        :type customer_encryption_enabled: bool
        """
        if customer_encryption_enabled is None:
            raise ValueError("Invalid value for `customer_encryption_enabled`, must not be `None`")

        self._customer_encryption_enabled = customer_encryption_enabled

    @property
    def id(self):
        """Gets the id of this CustomerData.

        Unique identifier for the customer

        :return: The id of this CustomerData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerData.

        Unique identifier for the customer

        :param id: The id of this CustomerData.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_provider_customer(self):
        """Gets the is_provider_customer of this CustomerData.

        Customer is Provider Customer

        :return: The is_provider_customer of this CustomerData.
        :rtype: bool
        """
        return self._is_provider_customer

    @is_provider_customer.setter
    def is_provider_customer(self, is_provider_customer):
        """Sets the is_provider_customer of this CustomerData.

        Customer is Provider Customer

        :param is_provider_customer: The is_provider_customer of this CustomerData.
        :type is_provider_customer: bool
        """
        if is_provider_customer is None:
            raise ValueError("Invalid value for `is_provider_customer`, must not be `None`")

        self._is_provider_customer = is_provider_customer

    @property
    def name(self):
        """Gets the name of this CustomerData.

        Customer name

        :return: The name of this CustomerData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerData.

        Customer name

        :param name: The name of this CustomerData.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def space_limit(self):
        """Gets the space_limit of this CustomerData.

        Space limit (in bytes). -1 for unlimited

        :return: The space_limit of this CustomerData.
        :rtype: int
        """
        return self._space_limit

    @space_limit.setter
    def space_limit(self, space_limit):
        """Sets the space_limit of this CustomerData.

        Space limit (in bytes). -1 for unlimited

        :param space_limit: The space_limit of this CustomerData.
        :type space_limit: int
        """
        if space_limit is None:
            raise ValueError("Invalid value for `space_limit`, must not be `None`")

        self._space_limit = space_limit

    @property
    def space_used(self):
        """Gets the space_used of this CustomerData.

        Space used (in bytes)

        :return: The space_used of this CustomerData.
        :rtype: int
        """
        return self._space_used

    @space_used.setter
    def space_used(self, space_used):
        """Sets the space_used of this CustomerData.

        Space used (in bytes)

        :param space_used: The space_used of this CustomerData.
        :type space_used: int
        """
        if space_used is None:
            raise ValueError("Invalid value for `space_used`, must not be `None`")

        self._space_used = space_used
