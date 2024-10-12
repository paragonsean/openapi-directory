# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.address import Address
from openapi_server.models.contact_purpose import ContactPurpose
from openapi_server.models.name import Name
from openapi_server.models.phone import Phone
from openapi_server import util


class Contact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: Address=None, addressee_name: Name=None, purpose: ContactPurpose=None, company_name: str=None, email_address: str=None, phones: List[Phone]=None):
        """Contact - a model defined in OpenAPI

        :param address: The address of this Contact.
        :param addressee_name: The addressee_name of this Contact.
        :param purpose: The purpose of this Contact.
        :param company_name: The company_name of this Contact.
        :param email_address: The email_address of this Contact.
        :param phones: The phones of this Contact.
        """
        self.openapi_types = {
            'address': Address,
            'addressee_name': Name,
            'purpose': ContactPurpose,
            'company_name': str,
            'email_address': str,
            'phones': List[Phone]
        }

        self.attribute_map = {
            'address': 'address',
            'addressee_name': 'addresseeName',
            'purpose': 'purpose',
            'company_name': 'companyName',
            'email_address': 'emailAddress',
            'phones': 'phones'
        }

        self._address = address
        self._addressee_name = addressee_name
        self._purpose = purpose
        self._company_name = company_name
        self._email_address = email_address
        self._phones = phones

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Contact':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Contact of this Contact.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this Contact.


        :return: The address of this Contact.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Contact.


        :param address: The address of this Contact.
        :type address: Address
        """

        self._address = address

    @property
    def addressee_name(self):
        """Gets the addressee_name of this Contact.


        :return: The addressee_name of this Contact.
        :rtype: Name
        """
        return self._addressee_name

    @addressee_name.setter
    def addressee_name(self, addressee_name):
        """Sets the addressee_name of this Contact.


        :param addressee_name: The addressee_name of this Contact.
        :type addressee_name: Name
        """

        self._addressee_name = addressee_name

    @property
    def purpose(self):
        """Gets the purpose of this Contact.


        :return: The purpose of this Contact.
        :rtype: ContactPurpose
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Contact.


        :param purpose: The purpose of this Contact.
        :type purpose: ContactPurpose
        """

        self._purpose = purpose

    @property
    def company_name(self):
        """Gets the company_name of this Contact.

        Name of the company

        :return: The company_name of this Contact.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Contact.

        Name of the company

        :param company_name: The company_name of this Contact.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def email_address(self):
        """Gets the email_address of this Contact.

        Email address (e.g. john@smith.com)

        :return: The email_address of this Contact.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Contact.

        Email address (e.g. john@smith.com)

        :param email_address: The email_address of this Contact.
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def phones(self):
        """Gets the phones of this Contact.

        Phone numbers

        :return: The phones of this Contact.
        :rtype: List[Phone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this Contact.

        Phone numbers

        :param phones: The phones of this Contact.
        :type phones: List[Phone]
        """
        if phones is not None and len(phones) > 3:
            raise ValueError("Invalid value for `phones`, number of items must be less than or equal to `3`")

        self._phones = phones
