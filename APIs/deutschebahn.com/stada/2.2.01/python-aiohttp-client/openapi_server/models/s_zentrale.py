# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.address import Address
from openapi_server import util


class SZentrale(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: Address=None, email: str=None, internal_fax_number: str=None, internal_phone_number: str=None, mobile_phone_number: str=None, name: str=None, number: int=None, public_fax_number: str=None, public_phone_number: str=None):
        """SZentrale - a model defined in OpenAPI

        :param address: The address of this SZentrale.
        :param email: The email of this SZentrale.
        :param internal_fax_number: The internal_fax_number of this SZentrale.
        :param internal_phone_number: The internal_phone_number of this SZentrale.
        :param mobile_phone_number: The mobile_phone_number of this SZentrale.
        :param name: The name of this SZentrale.
        :param number: The number of this SZentrale.
        :param public_fax_number: The public_fax_number of this SZentrale.
        :param public_phone_number: The public_phone_number of this SZentrale.
        """
        self.openapi_types = {
            'address': Address,
            'email': str,
            'internal_fax_number': str,
            'internal_phone_number': str,
            'mobile_phone_number': str,
            'name': str,
            'number': int,
            'public_fax_number': str,
            'public_phone_number': str
        }

        self.attribute_map = {
            'address': 'address',
            'email': 'email',
            'internal_fax_number': 'internalFaxNumber',
            'internal_phone_number': 'internalPhoneNumber',
            'mobile_phone_number': 'mobilePhoneNumber',
            'name': 'name',
            'number': 'number',
            'public_fax_number': 'publicFaxNumber',
            'public_phone_number': 'publicPhoneNumber'
        }

        self._address = address
        self._email = email
        self._internal_fax_number = internal_fax_number
        self._internal_phone_number = internal_phone_number
        self._mobile_phone_number = mobile_phone_number
        self._name = name
        self._number = number
        self._public_fax_number = public_fax_number
        self._public_phone_number = public_phone_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SZentrale':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SZentrale of this SZentrale.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this SZentrale.


        :return: The address of this SZentrale.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SZentrale.


        :param address: The address of this SZentrale.
        :type address: Address
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this SZentrale.

        email adress of the 3-S-Zentrale (no longer supported!)

        :return: The email of this SZentrale.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SZentrale.

        email adress of the 3-S-Zentrale (no longer supported!)

        :param email: The email of this SZentrale.
        :type email: str
        """

        self._email = email

    @property
    def internal_fax_number(self):
        """Gets the internal_fax_number of this SZentrale.

        internal fax number

        :return: The internal_fax_number of this SZentrale.
        :rtype: str
        """
        return self._internal_fax_number

    @internal_fax_number.setter
    def internal_fax_number(self, internal_fax_number):
        """Sets the internal_fax_number of this SZentrale.

        internal fax number

        :param internal_fax_number: The internal_fax_number of this SZentrale.
        :type internal_fax_number: str
        """

        self._internal_fax_number = internal_fax_number

    @property
    def internal_phone_number(self):
        """Gets the internal_phone_number of this SZentrale.

        internal phone number

        :return: The internal_phone_number of this SZentrale.
        :rtype: str
        """
        return self._internal_phone_number

    @internal_phone_number.setter
    def internal_phone_number(self, internal_phone_number):
        """Sets the internal_phone_number of this SZentrale.

        internal phone number

        :param internal_phone_number: The internal_phone_number of this SZentrale.
        :type internal_phone_number: str
        """

        self._internal_phone_number = internal_phone_number

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this SZentrale.

        mobile phone number (no longer supported!)

        :return: The mobile_phone_number of this SZentrale.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this SZentrale.

        mobile phone number (no longer supported!)

        :param mobile_phone_number: The mobile_phone_number of this SZentrale.
        :type mobile_phone_number: str
        """

        self._mobile_phone_number = mobile_phone_number

    @property
    def name(self):
        """Gets the name of this SZentrale.

        unique identifier of 3SZentrale

        :return: The name of this SZentrale.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SZentrale.

        unique identifier of 3SZentrale

        :param name: The name of this SZentrale.
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this SZentrale.

        unique identifier for SZentrale

        :return: The number of this SZentrale.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SZentrale.

        unique identifier for SZentrale

        :param number: The number of this SZentrale.
        :type number: int
        """

        self._number = number

    @property
    def public_fax_number(self):
        """Gets the public_fax_number of this SZentrale.

        public fax number

        :return: The public_fax_number of this SZentrale.
        :rtype: str
        """
        return self._public_fax_number

    @public_fax_number.setter
    def public_fax_number(self, public_fax_number):
        """Sets the public_fax_number of this SZentrale.

        public fax number

        :param public_fax_number: The public_fax_number of this SZentrale.
        :type public_fax_number: str
        """

        self._public_fax_number = public_fax_number

    @property
    def public_phone_number(self):
        """Gets the public_phone_number of this SZentrale.


        :return: The public_phone_number of this SZentrale.
        :rtype: str
        """
        return self._public_phone_number

    @public_phone_number.setter
    def public_phone_number(self, public_phone_number):
        """Sets the public_phone_number of this SZentrale.


        :param public_phone_number: The public_phone_number of this SZentrale.
        :type public_phone_number: str
        """

        self._public_phone_number = public_phone_number
