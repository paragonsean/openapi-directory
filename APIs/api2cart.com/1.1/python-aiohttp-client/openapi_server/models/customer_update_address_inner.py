# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CustomerUpdateAddressInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address_book_address1: str=None, address_book_address2: str=None, address_book_city: str=None, address_book_company: str=None, address_book_country: str=None, address_book_default: bool=None, address_book_fax: str=None, address_book_first_name: str=None, address_book_id: str=None, address_book_identification_number: str=None, address_book_last_name: str=None, address_book_phone: str=None, address_book_phone_mobile: str=None, address_book_postcode: str=None, address_book_state: str=None, address_book_tax_id: str=None, address_book_type: str=None):
        """CustomerUpdateAddressInner - a model defined in OpenAPI

        :param address_book_address1: The address_book_address1 of this CustomerUpdateAddressInner.
        :param address_book_address2: The address_book_address2 of this CustomerUpdateAddressInner.
        :param address_book_city: The address_book_city of this CustomerUpdateAddressInner.
        :param address_book_company: The address_book_company of this CustomerUpdateAddressInner.
        :param address_book_country: The address_book_country of this CustomerUpdateAddressInner.
        :param address_book_default: The address_book_default of this CustomerUpdateAddressInner.
        :param address_book_fax: The address_book_fax of this CustomerUpdateAddressInner.
        :param address_book_first_name: The address_book_first_name of this CustomerUpdateAddressInner.
        :param address_book_id: The address_book_id of this CustomerUpdateAddressInner.
        :param address_book_identification_number: The address_book_identification_number of this CustomerUpdateAddressInner.
        :param address_book_last_name: The address_book_last_name of this CustomerUpdateAddressInner.
        :param address_book_phone: The address_book_phone of this CustomerUpdateAddressInner.
        :param address_book_phone_mobile: The address_book_phone_mobile of this CustomerUpdateAddressInner.
        :param address_book_postcode: The address_book_postcode of this CustomerUpdateAddressInner.
        :param address_book_state: The address_book_state of this CustomerUpdateAddressInner.
        :param address_book_tax_id: The address_book_tax_id of this CustomerUpdateAddressInner.
        :param address_book_type: The address_book_type of this CustomerUpdateAddressInner.
        """
        self.openapi_types = {
            'address_book_address1': str,
            'address_book_address2': str,
            'address_book_city': str,
            'address_book_company': str,
            'address_book_country': str,
            'address_book_default': bool,
            'address_book_fax': str,
            'address_book_first_name': str,
            'address_book_id': str,
            'address_book_identification_number': str,
            'address_book_last_name': str,
            'address_book_phone': str,
            'address_book_phone_mobile': str,
            'address_book_postcode': str,
            'address_book_state': str,
            'address_book_tax_id': str,
            'address_book_type': str
        }

        self.attribute_map = {
            'address_book_address1': 'address_book_address1',
            'address_book_address2': 'address_book_address2',
            'address_book_city': 'address_book_city',
            'address_book_company': 'address_book_company',
            'address_book_country': 'address_book_country',
            'address_book_default': 'address_book_default',
            'address_book_fax': 'address_book_fax',
            'address_book_first_name': 'address_book_first_name',
            'address_book_id': 'address_book_id',
            'address_book_identification_number': 'address_book_identification_number',
            'address_book_last_name': 'address_book_last_name',
            'address_book_phone': 'address_book_phone',
            'address_book_phone_mobile': 'address_book_phone_mobile',
            'address_book_postcode': 'address_book_postcode',
            'address_book_state': 'address_book_state',
            'address_book_tax_id': 'address_book_tax_id',
            'address_book_type': 'address_book_type'
        }

        self._address_book_address1 = address_book_address1
        self._address_book_address2 = address_book_address2
        self._address_book_city = address_book_city
        self._address_book_company = address_book_company
        self._address_book_country = address_book_country
        self._address_book_default = address_book_default
        self._address_book_fax = address_book_fax
        self._address_book_first_name = address_book_first_name
        self._address_book_id = address_book_id
        self._address_book_identification_number = address_book_identification_number
        self._address_book_last_name = address_book_last_name
        self._address_book_phone = address_book_phone
        self._address_book_phone_mobile = address_book_phone_mobile
        self._address_book_postcode = address_book_postcode
        self._address_book_state = address_book_state
        self._address_book_tax_id = address_book_tax_id
        self._address_book_type = address_book_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CustomerUpdateAddressInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CustomerUpdate_address_inner of this CustomerUpdateAddressInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_book_address1(self):
        """Gets the address_book_address1 of this CustomerUpdateAddressInner.

        Specifies customer's first address in the address book

        :return: The address_book_address1 of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_address1

    @address_book_address1.setter
    def address_book_address1(self, address_book_address1):
        """Sets the address_book_address1 of this CustomerUpdateAddressInner.

        Specifies customer's first address in the address book

        :param address_book_address1: The address_book_address1 of this CustomerUpdateAddressInner.
        :type address_book_address1: str
        """

        self._address_book_address1 = address_book_address1

    @property
    def address_book_address2(self):
        """Gets the address_book_address2 of this CustomerUpdateAddressInner.

        Specifies customer's second address in the address book

        :return: The address_book_address2 of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_address2

    @address_book_address2.setter
    def address_book_address2(self, address_book_address2):
        """Sets the address_book_address2 of this CustomerUpdateAddressInner.

        Specifies customer's second address in the address book

        :param address_book_address2: The address_book_address2 of this CustomerUpdateAddressInner.
        :type address_book_address2: str
        """

        self._address_book_address2 = address_book_address2

    @property
    def address_book_city(self):
        """Gets the address_book_city of this CustomerUpdateAddressInner.

        Specifies customer's city in the address book

        :return: The address_book_city of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_city

    @address_book_city.setter
    def address_book_city(self, address_book_city):
        """Sets the address_book_city of this CustomerUpdateAddressInner.

        Specifies customer's city in the address book

        :param address_book_city: The address_book_city of this CustomerUpdateAddressInner.
        :type address_book_city: str
        """

        self._address_book_city = address_book_city

    @property
    def address_book_company(self):
        """Gets the address_book_company of this CustomerUpdateAddressInner.

        Specifies customer's company name in the address book

        :return: The address_book_company of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_company

    @address_book_company.setter
    def address_book_company(self, address_book_company):
        """Sets the address_book_company of this CustomerUpdateAddressInner.

        Specifies customer's company name in the address book

        :param address_book_company: The address_book_company of this CustomerUpdateAddressInner.
        :type address_book_company: str
        """

        self._address_book_company = address_book_company

    @property
    def address_book_country(self):
        """Gets the address_book_country of this CustomerUpdateAddressInner.

        ISO code or name of country

        :return: The address_book_country of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_country

    @address_book_country.setter
    def address_book_country(self, address_book_country):
        """Sets the address_book_country of this CustomerUpdateAddressInner.

        ISO code or name of country

        :param address_book_country: The address_book_country of this CustomerUpdateAddressInner.
        :type address_book_country: str
        """

        self._address_book_country = address_book_country

    @property
    def address_book_default(self):
        """Gets the address_book_default of this CustomerUpdateAddressInner.

        Defines whether the address is used by default

        :return: The address_book_default of this CustomerUpdateAddressInner.
        :rtype: bool
        """
        return self._address_book_default

    @address_book_default.setter
    def address_book_default(self, address_book_default):
        """Sets the address_book_default of this CustomerUpdateAddressInner.

        Defines whether the address is used by default

        :param address_book_default: The address_book_default of this CustomerUpdateAddressInner.
        :type address_book_default: bool
        """

        self._address_book_default = address_book_default

    @property
    def address_book_fax(self):
        """Gets the address_book_fax of this CustomerUpdateAddressInner.

        Specifies customer's fax in the address book

        :return: The address_book_fax of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_fax

    @address_book_fax.setter
    def address_book_fax(self, address_book_fax):
        """Sets the address_book_fax of this CustomerUpdateAddressInner.

        Specifies customer's fax in the address book

        :param address_book_fax: The address_book_fax of this CustomerUpdateAddressInner.
        :type address_book_fax: str
        """

        self._address_book_fax = address_book_fax

    @property
    def address_book_first_name(self):
        """Gets the address_book_first_name of this CustomerUpdateAddressInner.

        Specifies customer's first name in the address book

        :return: The address_book_first_name of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_first_name

    @address_book_first_name.setter
    def address_book_first_name(self, address_book_first_name):
        """Sets the address_book_first_name of this CustomerUpdateAddressInner.

        Specifies customer's first name in the address book

        :param address_book_first_name: The address_book_first_name of this CustomerUpdateAddressInner.
        :type address_book_first_name: str
        """

        self._address_book_first_name = address_book_first_name

    @property
    def address_book_id(self):
        """Gets the address_book_id of this CustomerUpdateAddressInner.

        The ID of the address.

        :return: The address_book_id of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_id

    @address_book_id.setter
    def address_book_id(self, address_book_id):
        """Sets the address_book_id of this CustomerUpdateAddressInner.

        The ID of the address.

        :param address_book_id: The address_book_id of this CustomerUpdateAddressInner.
        :type address_book_id: str
        """

        self._address_book_id = address_book_id

    @property
    def address_book_identification_number(self):
        """Gets the address_book_identification_number of this CustomerUpdateAddressInner.

        The national ID card number of this person, or a unique tax identification number.

        :return: The address_book_identification_number of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_identification_number

    @address_book_identification_number.setter
    def address_book_identification_number(self, address_book_identification_number):
        """Sets the address_book_identification_number of this CustomerUpdateAddressInner.

        The national ID card number of this person, or a unique tax identification number.

        :param address_book_identification_number: The address_book_identification_number of this CustomerUpdateAddressInner.
        :type address_book_identification_number: str
        """

        self._address_book_identification_number = address_book_identification_number

    @property
    def address_book_last_name(self):
        """Gets the address_book_last_name of this CustomerUpdateAddressInner.

        Specifies customer's last name in the address book

        :return: The address_book_last_name of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_last_name

    @address_book_last_name.setter
    def address_book_last_name(self, address_book_last_name):
        """Sets the address_book_last_name of this CustomerUpdateAddressInner.

        Specifies customer's last name in the address book

        :param address_book_last_name: The address_book_last_name of this CustomerUpdateAddressInner.
        :type address_book_last_name: str
        """

        self._address_book_last_name = address_book_last_name

    @property
    def address_book_phone(self):
        """Gets the address_book_phone of this CustomerUpdateAddressInner.

        Specifies customer's phone number in the address book

        :return: The address_book_phone of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_phone

    @address_book_phone.setter
    def address_book_phone(self, address_book_phone):
        """Sets the address_book_phone of this CustomerUpdateAddressInner.

        Specifies customer's phone number in the address book

        :param address_book_phone: The address_book_phone of this CustomerUpdateAddressInner.
        :type address_book_phone: str
        """

        self._address_book_phone = address_book_phone

    @property
    def address_book_phone_mobile(self):
        """Gets the address_book_phone_mobile of this CustomerUpdateAddressInner.

        Specifies customer's mobile phone number in the address book

        :return: The address_book_phone_mobile of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_phone_mobile

    @address_book_phone_mobile.setter
    def address_book_phone_mobile(self, address_book_phone_mobile):
        """Sets the address_book_phone_mobile of this CustomerUpdateAddressInner.

        Specifies customer's mobile phone number in the address book

        :param address_book_phone_mobile: The address_book_phone_mobile of this CustomerUpdateAddressInner.
        :type address_book_phone_mobile: str
        """

        self._address_book_phone_mobile = address_book_phone_mobile

    @property
    def address_book_postcode(self):
        """Gets the address_book_postcode of this CustomerUpdateAddressInner.

        Specifies customer's postcode

        :return: The address_book_postcode of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_postcode

    @address_book_postcode.setter
    def address_book_postcode(self, address_book_postcode):
        """Sets the address_book_postcode of this CustomerUpdateAddressInner.

        Specifies customer's postcode

        :param address_book_postcode: The address_book_postcode of this CustomerUpdateAddressInner.
        :type address_book_postcode: str
        """

        self._address_book_postcode = address_book_postcode

    @property
    def address_book_state(self):
        """Gets the address_book_state of this CustomerUpdateAddressInner.

        ISO code or name of state.

        :return: The address_book_state of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_state

    @address_book_state.setter
    def address_book_state(self, address_book_state):
        """Sets the address_book_state of this CustomerUpdateAddressInner.

        ISO code or name of state.

        :param address_book_state: The address_book_state of this CustomerUpdateAddressInner.
        :type address_book_state: str
        """

        self._address_book_state = address_book_state

    @property
    def address_book_tax_id(self):
        """Gets the address_book_tax_id of this CustomerUpdateAddressInner.

        Add Tax Id

        :return: The address_book_tax_id of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_tax_id

    @address_book_tax_id.setter
    def address_book_tax_id(self, address_book_tax_id):
        """Sets the address_book_tax_id of this CustomerUpdateAddressInner.

        Add Tax Id

        :param address_book_tax_id: The address_book_tax_id of this CustomerUpdateAddressInner.
        :type address_book_tax_id: str
        """

        self._address_book_tax_id = address_book_tax_id

    @property
    def address_book_type(self):
        """Gets the address_book_type of this CustomerUpdateAddressInner.

        Specifies customer's address type

        :return: The address_book_type of this CustomerUpdateAddressInner.
        :rtype: str
        """
        return self._address_book_type

    @address_book_type.setter
    def address_book_type(self, address_book_type):
        """Sets the address_book_type of this CustomerUpdateAddressInner.

        Specifies customer's address type

        :param address_book_type: The address_book_type of this CustomerUpdateAddressInner.
        :type address_book_type: str
        """

        self._address_book_type = address_book_type
