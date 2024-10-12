# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NewCompanyContact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_billing_address: str=None, company_billing_address_city: str=None, company_billing_address_country_code: str=None, company_billing_address_line: str=None, company_billing_address_post_code: str=None, company_billing_address_state: str=None, company_idfk: int=None, company_name: str=None, contact_email: str=None, currency_code: str=None, firstname: str=None, lastname: str=None, mobile: str=None, phone: str=None, position_title: str=None, update_existing: bool=None):
        """NewCompanyContact - a model defined in OpenAPI

        :param company_billing_address: The company_billing_address of this NewCompanyContact.
        :param company_billing_address_city: The company_billing_address_city of this NewCompanyContact.
        :param company_billing_address_country_code: The company_billing_address_country_code of this NewCompanyContact.
        :param company_billing_address_line: The company_billing_address_line of this NewCompanyContact.
        :param company_billing_address_post_code: The company_billing_address_post_code of this NewCompanyContact.
        :param company_billing_address_state: The company_billing_address_state of this NewCompanyContact.
        :param company_idfk: The company_idfk of this NewCompanyContact.
        :param company_name: The company_name of this NewCompanyContact.
        :param contact_email: The contact_email of this NewCompanyContact.
        :param currency_code: The currency_code of this NewCompanyContact.
        :param firstname: The firstname of this NewCompanyContact.
        :param lastname: The lastname of this NewCompanyContact.
        :param mobile: The mobile of this NewCompanyContact.
        :param phone: The phone of this NewCompanyContact.
        :param position_title: The position_title of this NewCompanyContact.
        :param update_existing: The update_existing of this NewCompanyContact.
        """
        self.openapi_types = {
            'company_billing_address': str,
            'company_billing_address_city': str,
            'company_billing_address_country_code': str,
            'company_billing_address_line': str,
            'company_billing_address_post_code': str,
            'company_billing_address_state': str,
            'company_idfk': int,
            'company_name': str,
            'contact_email': str,
            'currency_code': str,
            'firstname': str,
            'lastname': str,
            'mobile': str,
            'phone': str,
            'position_title': str,
            'update_existing': bool
        }

        self.attribute_map = {
            'company_billing_address': 'CompanyBillingAddress',
            'company_billing_address_city': 'CompanyBillingAddressCity',
            'company_billing_address_country_code': 'CompanyBillingAddressCountryCode',
            'company_billing_address_line': 'CompanyBillingAddressLine',
            'company_billing_address_post_code': 'CompanyBillingAddressPostCode',
            'company_billing_address_state': 'CompanyBillingAddressState',
            'company_idfk': 'CompanyIDFK',
            'company_name': 'CompanyName',
            'contact_email': 'ContactEmail',
            'currency_code': 'CurrencyCode',
            'firstname': 'Firstname',
            'lastname': 'Lastname',
            'mobile': 'Mobile',
            'phone': 'Phone',
            'position_title': 'PositionTitle',
            'update_existing': 'UpdateExisting'
        }

        self._company_billing_address = company_billing_address
        self._company_billing_address_city = company_billing_address_city
        self._company_billing_address_country_code = company_billing_address_country_code
        self._company_billing_address_line = company_billing_address_line
        self._company_billing_address_post_code = company_billing_address_post_code
        self._company_billing_address_state = company_billing_address_state
        self._company_idfk = company_idfk
        self._company_name = company_name
        self._contact_email = contact_email
        self._currency_code = currency_code
        self._firstname = firstname
        self._lastname = lastname
        self._mobile = mobile
        self._phone = phone
        self._position_title = position_title
        self._update_existing = update_existing

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NewCompanyContact':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NewCompanyContact of this NewCompanyContact.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_billing_address(self):
        """Gets the company_billing_address of this NewCompanyContact.


        :return: The company_billing_address of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address

    @company_billing_address.setter
    def company_billing_address(self, company_billing_address):
        """Sets the company_billing_address of this NewCompanyContact.


        :param company_billing_address: The company_billing_address of this NewCompanyContact.
        :type company_billing_address: str
        """

        self._company_billing_address = company_billing_address

    @property
    def company_billing_address_city(self):
        """Gets the company_billing_address_city of this NewCompanyContact.


        :return: The company_billing_address_city of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address_city

    @company_billing_address_city.setter
    def company_billing_address_city(self, company_billing_address_city):
        """Sets the company_billing_address_city of this NewCompanyContact.


        :param company_billing_address_city: The company_billing_address_city of this NewCompanyContact.
        :type company_billing_address_city: str
        """

        self._company_billing_address_city = company_billing_address_city

    @property
    def company_billing_address_country_code(self):
        """Gets the company_billing_address_country_code of this NewCompanyContact.


        :return: The company_billing_address_country_code of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address_country_code

    @company_billing_address_country_code.setter
    def company_billing_address_country_code(self, company_billing_address_country_code):
        """Sets the company_billing_address_country_code of this NewCompanyContact.


        :param company_billing_address_country_code: The company_billing_address_country_code of this NewCompanyContact.
        :type company_billing_address_country_code: str
        """

        self._company_billing_address_country_code = company_billing_address_country_code

    @property
    def company_billing_address_line(self):
        """Gets the company_billing_address_line of this NewCompanyContact.


        :return: The company_billing_address_line of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address_line

    @company_billing_address_line.setter
    def company_billing_address_line(self, company_billing_address_line):
        """Sets the company_billing_address_line of this NewCompanyContact.


        :param company_billing_address_line: The company_billing_address_line of this NewCompanyContact.
        :type company_billing_address_line: str
        """

        self._company_billing_address_line = company_billing_address_line

    @property
    def company_billing_address_post_code(self):
        """Gets the company_billing_address_post_code of this NewCompanyContact.


        :return: The company_billing_address_post_code of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address_post_code

    @company_billing_address_post_code.setter
    def company_billing_address_post_code(self, company_billing_address_post_code):
        """Sets the company_billing_address_post_code of this NewCompanyContact.


        :param company_billing_address_post_code: The company_billing_address_post_code of this NewCompanyContact.
        :type company_billing_address_post_code: str
        """

        self._company_billing_address_post_code = company_billing_address_post_code

    @property
    def company_billing_address_state(self):
        """Gets the company_billing_address_state of this NewCompanyContact.


        :return: The company_billing_address_state of this NewCompanyContact.
        :rtype: str
        """
        return self._company_billing_address_state

    @company_billing_address_state.setter
    def company_billing_address_state(self, company_billing_address_state):
        """Sets the company_billing_address_state of this NewCompanyContact.


        :param company_billing_address_state: The company_billing_address_state of this NewCompanyContact.
        :type company_billing_address_state: str
        """

        self._company_billing_address_state = company_billing_address_state

    @property
    def company_idfk(self):
        """Gets the company_idfk of this NewCompanyContact.


        :return: The company_idfk of this NewCompanyContact.
        :rtype: int
        """
        return self._company_idfk

    @company_idfk.setter
    def company_idfk(self, company_idfk):
        """Sets the company_idfk of this NewCompanyContact.


        :param company_idfk: The company_idfk of this NewCompanyContact.
        :type company_idfk: int
        """

        self._company_idfk = company_idfk

    @property
    def company_name(self):
        """Gets the company_name of this NewCompanyContact.


        :return: The company_name of this NewCompanyContact.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this NewCompanyContact.


        :param company_name: The company_name of this NewCompanyContact.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def contact_email(self):
        """Gets the contact_email of this NewCompanyContact.


        :return: The contact_email of this NewCompanyContact.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this NewCompanyContact.


        :param contact_email: The contact_email of this NewCompanyContact.
        :type contact_email: str
        """
        if contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")

        self._contact_email = contact_email

    @property
    def currency_code(self):
        """Gets the currency_code of this NewCompanyContact.


        :return: The currency_code of this NewCompanyContact.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this NewCompanyContact.


        :param currency_code: The currency_code of this NewCompanyContact.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def firstname(self):
        """Gets the firstname of this NewCompanyContact.


        :return: The firstname of this NewCompanyContact.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this NewCompanyContact.


        :param firstname: The firstname of this NewCompanyContact.
        :type firstname: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this NewCompanyContact.


        :return: The lastname of this NewCompanyContact.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this NewCompanyContact.


        :param lastname: The lastname of this NewCompanyContact.
        :type lastname: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def mobile(self):
        """Gets the mobile of this NewCompanyContact.


        :return: The mobile of this NewCompanyContact.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this NewCompanyContact.


        :param mobile: The mobile of this NewCompanyContact.
        :type mobile: str
        """

        self._mobile = mobile

    @property
    def phone(self):
        """Gets the phone of this NewCompanyContact.


        :return: The phone of this NewCompanyContact.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this NewCompanyContact.


        :param phone: The phone of this NewCompanyContact.
        :type phone: str
        """

        self._phone = phone

    @property
    def position_title(self):
        """Gets the position_title of this NewCompanyContact.


        :return: The position_title of this NewCompanyContact.
        :rtype: str
        """
        return self._position_title

    @position_title.setter
    def position_title(self, position_title):
        """Sets the position_title of this NewCompanyContact.


        :param position_title: The position_title of this NewCompanyContact.
        :type position_title: str
        """

        self._position_title = position_title

    @property
    def update_existing(self):
        """Gets the update_existing of this NewCompanyContact.


        :return: The update_existing of this NewCompanyContact.
        :rtype: bool
        """
        return self._update_existing

    @update_existing.setter
    def update_existing(self, update_existing):
        """Sets the update_existing of this NewCompanyContact.


        :param update_existing: The update_existing of this NewCompanyContact.
        :type update_existing: bool
        """

        self._update_existing = update_existing
