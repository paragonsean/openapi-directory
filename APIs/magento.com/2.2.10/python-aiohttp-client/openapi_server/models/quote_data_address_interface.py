# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_attribute_interface import FrameworkAttributeInterface
from openapi_server.models.quote_data_address_extension_interface import QuoteDataAddressExtensionInterface
from openapi_server import util


class QuoteDataAddressInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, company: str=None, country_id: str=None, custom_attributes: List[FrameworkAttributeInterface]=None, customer_address_id: int=None, customer_id: int=None, email: str=None, extension_attributes: QuoteDataAddressExtensionInterface=None, fax: str=None, firstname: str=None, id: int=None, lastname: str=None, middlename: str=None, postcode: str=None, prefix: str=None, region: str=None, region_code: str=None, region_id: int=None, same_as_billing: int=None, save_in_address_book: int=None, street: List[str]=None, suffix: str=None, telephone: str=None, vat_id: str=None):
        """QuoteDataAddressInterface - a model defined in OpenAPI

        :param city: The city of this QuoteDataAddressInterface.
        :param company: The company of this QuoteDataAddressInterface.
        :param country_id: The country_id of this QuoteDataAddressInterface.
        :param custom_attributes: The custom_attributes of this QuoteDataAddressInterface.
        :param customer_address_id: The customer_address_id of this QuoteDataAddressInterface.
        :param customer_id: The customer_id of this QuoteDataAddressInterface.
        :param email: The email of this QuoteDataAddressInterface.
        :param extension_attributes: The extension_attributes of this QuoteDataAddressInterface.
        :param fax: The fax of this QuoteDataAddressInterface.
        :param firstname: The firstname of this QuoteDataAddressInterface.
        :param id: The id of this QuoteDataAddressInterface.
        :param lastname: The lastname of this QuoteDataAddressInterface.
        :param middlename: The middlename of this QuoteDataAddressInterface.
        :param postcode: The postcode of this QuoteDataAddressInterface.
        :param prefix: The prefix of this QuoteDataAddressInterface.
        :param region: The region of this QuoteDataAddressInterface.
        :param region_code: The region_code of this QuoteDataAddressInterface.
        :param region_id: The region_id of this QuoteDataAddressInterface.
        :param same_as_billing: The same_as_billing of this QuoteDataAddressInterface.
        :param save_in_address_book: The save_in_address_book of this QuoteDataAddressInterface.
        :param street: The street of this QuoteDataAddressInterface.
        :param suffix: The suffix of this QuoteDataAddressInterface.
        :param telephone: The telephone of this QuoteDataAddressInterface.
        :param vat_id: The vat_id of this QuoteDataAddressInterface.
        """
        self.openapi_types = {
            'city': str,
            'company': str,
            'country_id': str,
            'custom_attributes': List[FrameworkAttributeInterface],
            'customer_address_id': int,
            'customer_id': int,
            'email': str,
            'extension_attributes': QuoteDataAddressExtensionInterface,
            'fax': str,
            'firstname': str,
            'id': int,
            'lastname': str,
            'middlename': str,
            'postcode': str,
            'prefix': str,
            'region': str,
            'region_code': str,
            'region_id': int,
            'same_as_billing': int,
            'save_in_address_book': int,
            'street': List[str],
            'suffix': str,
            'telephone': str,
            'vat_id': str
        }

        self.attribute_map = {
            'city': 'city',
            'company': 'company',
            'country_id': 'country_id',
            'custom_attributes': 'custom_attributes',
            'customer_address_id': 'customer_address_id',
            'customer_id': 'customer_id',
            'email': 'email',
            'extension_attributes': 'extension_attributes',
            'fax': 'fax',
            'firstname': 'firstname',
            'id': 'id',
            'lastname': 'lastname',
            'middlename': 'middlename',
            'postcode': 'postcode',
            'prefix': 'prefix',
            'region': 'region',
            'region_code': 'region_code',
            'region_id': 'region_id',
            'same_as_billing': 'same_as_billing',
            'save_in_address_book': 'save_in_address_book',
            'street': 'street',
            'suffix': 'suffix',
            'telephone': 'telephone',
            'vat_id': 'vat_id'
        }

        self._city = city
        self._company = company
        self._country_id = country_id
        self._custom_attributes = custom_attributes
        self._customer_address_id = customer_address_id
        self._customer_id = customer_id
        self._email = email
        self._extension_attributes = extension_attributes
        self._fax = fax
        self._firstname = firstname
        self._id = id
        self._lastname = lastname
        self._middlename = middlename
        self._postcode = postcode
        self._prefix = prefix
        self._region = region
        self._region_code = region_code
        self._region_id = region_id
        self._same_as_billing = same_as_billing
        self._save_in_address_book = save_in_address_book
        self._street = street
        self._suffix = suffix
        self._telephone = telephone
        self._vat_id = vat_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QuoteDataAddressInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The quote-data-address-interface of this QuoteDataAddressInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this QuoteDataAddressInterface.

        City name

        :return: The city of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this QuoteDataAddressInterface.

        City name

        :param city: The city of this QuoteDataAddressInterface.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")

        self._city = city

    @property
    def company(self):
        """Gets the company of this QuoteDataAddressInterface.

        Company

        :return: The company of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this QuoteDataAddressInterface.

        Company

        :param company: The company of this QuoteDataAddressInterface.
        :type company: str
        """

        self._company = company

    @property
    def country_id(self):
        """Gets the country_id of this QuoteDataAddressInterface.

        Country id

        :return: The country_id of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this QuoteDataAddressInterface.

        Country id

        :param country_id: The country_id of this QuoteDataAddressInterface.
        :type country_id: str
        """
        if country_id is None:
            raise ValueError("Invalid value for `country_id`, must not be `None`")

        self._country_id = country_id

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this QuoteDataAddressInterface.

        Custom attributes values.

        :return: The custom_attributes of this QuoteDataAddressInterface.
        :rtype: List[FrameworkAttributeInterface]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this QuoteDataAddressInterface.

        Custom attributes values.

        :param custom_attributes: The custom_attributes of this QuoteDataAddressInterface.
        :type custom_attributes: List[FrameworkAttributeInterface]
        """

        self._custom_attributes = custom_attributes

    @property
    def customer_address_id(self):
        """Gets the customer_address_id of this QuoteDataAddressInterface.

        Customer address id

        :return: The customer_address_id of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._customer_address_id

    @customer_address_id.setter
    def customer_address_id(self, customer_address_id):
        """Sets the customer_address_id of this QuoteDataAddressInterface.

        Customer address id

        :param customer_address_id: The customer_address_id of this QuoteDataAddressInterface.
        :type customer_address_id: int
        """

        self._customer_address_id = customer_address_id

    @property
    def customer_id(self):
        """Gets the customer_id of this QuoteDataAddressInterface.

        Customer id

        :return: The customer_id of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this QuoteDataAddressInterface.

        Customer id

        :param customer_id: The customer_id of this QuoteDataAddressInterface.
        :type customer_id: int
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """Gets the email of this QuoteDataAddressInterface.

        Billing/shipping email

        :return: The email of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this QuoteDataAddressInterface.

        Billing/shipping email

        :param email: The email of this QuoteDataAddressInterface.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this QuoteDataAddressInterface.


        :return: The extension_attributes of this QuoteDataAddressInterface.
        :rtype: QuoteDataAddressExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this QuoteDataAddressInterface.


        :param extension_attributes: The extension_attributes of this QuoteDataAddressInterface.
        :type extension_attributes: QuoteDataAddressExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def fax(self):
        """Gets the fax of this QuoteDataAddressInterface.

        Fax number

        :return: The fax of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this QuoteDataAddressInterface.

        Fax number

        :param fax: The fax of this QuoteDataAddressInterface.
        :type fax: str
        """

        self._fax = fax

    @property
    def firstname(self):
        """Gets the firstname of this QuoteDataAddressInterface.

        First name

        :return: The firstname of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this QuoteDataAddressInterface.

        First name

        :param firstname: The firstname of this QuoteDataAddressInterface.
        :type firstname: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def id(self):
        """Gets the id of this QuoteDataAddressInterface.

        Id

        :return: The id of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuoteDataAddressInterface.

        Id

        :param id: The id of this QuoteDataAddressInterface.
        :type id: int
        """

        self._id = id

    @property
    def lastname(self):
        """Gets the lastname of this QuoteDataAddressInterface.

        Last name

        :return: The lastname of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this QuoteDataAddressInterface.

        Last name

        :param lastname: The lastname of this QuoteDataAddressInterface.
        :type lastname: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def middlename(self):
        """Gets the middlename of this QuoteDataAddressInterface.

        Middle name

        :return: The middlename of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """Sets the middlename of this QuoteDataAddressInterface.

        Middle name

        :param middlename: The middlename of this QuoteDataAddressInterface.
        :type middlename: str
        """

        self._middlename = middlename

    @property
    def postcode(self):
        """Gets the postcode of this QuoteDataAddressInterface.

        Postcode

        :return: The postcode of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this QuoteDataAddressInterface.

        Postcode

        :param postcode: The postcode of this QuoteDataAddressInterface.
        :type postcode: str
        """
        if postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")

        self._postcode = postcode

    @property
    def prefix(self):
        """Gets the prefix of this QuoteDataAddressInterface.

        Prefix

        :return: The prefix of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this QuoteDataAddressInterface.

        Prefix

        :param prefix: The prefix of this QuoteDataAddressInterface.
        :type prefix: str
        """

        self._prefix = prefix

    @property
    def region(self):
        """Gets the region of this QuoteDataAddressInterface.

        Region name

        :return: The region of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this QuoteDataAddressInterface.

        Region name

        :param region: The region of this QuoteDataAddressInterface.
        :type region: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")

        self._region = region

    @property
    def region_code(self):
        """Gets the region_code of this QuoteDataAddressInterface.

        Region code

        :return: The region_code of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this QuoteDataAddressInterface.

        Region code

        :param region_code: The region_code of this QuoteDataAddressInterface.
        :type region_code: str
        """
        if region_code is None:
            raise ValueError("Invalid value for `region_code`, must not be `None`")

        self._region_code = region_code

    @property
    def region_id(self):
        """Gets the region_id of this QuoteDataAddressInterface.

        Region id

        :return: The region_id of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this QuoteDataAddressInterface.

        Region id

        :param region_id: The region_id of this QuoteDataAddressInterface.
        :type region_id: int
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")

        self._region_id = region_id

    @property
    def same_as_billing(self):
        """Gets the same_as_billing of this QuoteDataAddressInterface.

        Same as billing flag

        :return: The same_as_billing of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._same_as_billing

    @same_as_billing.setter
    def same_as_billing(self, same_as_billing):
        """Sets the same_as_billing of this QuoteDataAddressInterface.

        Same as billing flag

        :param same_as_billing: The same_as_billing of this QuoteDataAddressInterface.
        :type same_as_billing: int
        """

        self._same_as_billing = same_as_billing

    @property
    def save_in_address_book(self):
        """Gets the save_in_address_book of this QuoteDataAddressInterface.

        Save in address book flag

        :return: The save_in_address_book of this QuoteDataAddressInterface.
        :rtype: int
        """
        return self._save_in_address_book

    @save_in_address_book.setter
    def save_in_address_book(self, save_in_address_book):
        """Sets the save_in_address_book of this QuoteDataAddressInterface.

        Save in address book flag

        :param save_in_address_book: The save_in_address_book of this QuoteDataAddressInterface.
        :type save_in_address_book: int
        """

        self._save_in_address_book = save_in_address_book

    @property
    def street(self):
        """Gets the street of this QuoteDataAddressInterface.

        Street

        :return: The street of this QuoteDataAddressInterface.
        :rtype: List[str]
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this QuoteDataAddressInterface.

        Street

        :param street: The street of this QuoteDataAddressInterface.
        :type street: List[str]
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")

        self._street = street

    @property
    def suffix(self):
        """Gets the suffix of this QuoteDataAddressInterface.

        Suffix

        :return: The suffix of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this QuoteDataAddressInterface.

        Suffix

        :param suffix: The suffix of this QuoteDataAddressInterface.
        :type suffix: str
        """

        self._suffix = suffix

    @property
    def telephone(self):
        """Gets the telephone of this QuoteDataAddressInterface.

        Telephone number

        :return: The telephone of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this QuoteDataAddressInterface.

        Telephone number

        :param telephone: The telephone of this QuoteDataAddressInterface.
        :type telephone: str
        """
        if telephone is None:
            raise ValueError("Invalid value for `telephone`, must not be `None`")

        self._telephone = telephone

    @property
    def vat_id(self):
        """Gets the vat_id of this QuoteDataAddressInterface.

        Vat id

        :return: The vat_id of this QuoteDataAddressInterface.
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """Sets the vat_id of this QuoteDataAddressInterface.

        Vat id

        :param vat_id: The vat_id of this QuoteDataAddressInterface.
        :type vat_id: str
        """

        self._vat_id = vat_id
