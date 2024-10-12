# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateCompany(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, billing_address: str=None, billing_address_city: str=None, billing_address_line: str=None, billing_address_post_code: str=None, billing_address_state: str=None, billing_country_code: str=None, comments: str=None, company_id: int=None, company_name: str=None, fax: str=None, fields_to_update: List[str]=None, phone: str=None, tax_number: str=None, website: str=None):
        """UpdateCompany - a model defined in OpenAPI

        :param billing_address: The billing_address of this UpdateCompany.
        :param billing_address_city: The billing_address_city of this UpdateCompany.
        :param billing_address_line: The billing_address_line of this UpdateCompany.
        :param billing_address_post_code: The billing_address_post_code of this UpdateCompany.
        :param billing_address_state: The billing_address_state of this UpdateCompany.
        :param billing_country_code: The billing_country_code of this UpdateCompany.
        :param comments: The comments of this UpdateCompany.
        :param company_id: The company_id of this UpdateCompany.
        :param company_name: The company_name of this UpdateCompany.
        :param fax: The fax of this UpdateCompany.
        :param fields_to_update: The fields_to_update of this UpdateCompany.
        :param phone: The phone of this UpdateCompany.
        :param tax_number: The tax_number of this UpdateCompany.
        :param website: The website of this UpdateCompany.
        """
        self.openapi_types = {
            'billing_address': str,
            'billing_address_city': str,
            'billing_address_line': str,
            'billing_address_post_code': str,
            'billing_address_state': str,
            'billing_country_code': str,
            'comments': str,
            'company_id': int,
            'company_name': str,
            'fax': str,
            'fields_to_update': List[str],
            'phone': str,
            'tax_number': str,
            'website': str
        }

        self.attribute_map = {
            'billing_address': 'BillingAddress',
            'billing_address_city': 'BillingAddressCity',
            'billing_address_line': 'BillingAddressLine',
            'billing_address_post_code': 'BillingAddressPostCode',
            'billing_address_state': 'BillingAddressState',
            'billing_country_code': 'BillingCountryCode',
            'comments': 'Comments',
            'company_id': 'CompanyID',
            'company_name': 'CompanyName',
            'fax': 'Fax',
            'fields_to_update': 'FieldsToUpdate',
            'phone': 'Phone',
            'tax_number': 'TaxNumber',
            'website': 'website'
        }

        self._billing_address = billing_address
        self._billing_address_city = billing_address_city
        self._billing_address_line = billing_address_line
        self._billing_address_post_code = billing_address_post_code
        self._billing_address_state = billing_address_state
        self._billing_country_code = billing_country_code
        self._comments = comments
        self._company_id = company_id
        self._company_name = company_name
        self._fax = fax
        self._fields_to_update = fields_to_update
        self._phone = phone
        self._tax_number = tax_number
        self._website = website

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateCompany':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateCompany of this UpdateCompany.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def billing_address(self):
        """Gets the billing_address of this UpdateCompany.


        :return: The billing_address of this UpdateCompany.
        :rtype: str
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this UpdateCompany.


        :param billing_address: The billing_address of this UpdateCompany.
        :type billing_address: str
        """

        self._billing_address = billing_address

    @property
    def billing_address_city(self):
        """Gets the billing_address_city of this UpdateCompany.


        :return: The billing_address_city of this UpdateCompany.
        :rtype: str
        """
        return self._billing_address_city

    @billing_address_city.setter
    def billing_address_city(self, billing_address_city):
        """Sets the billing_address_city of this UpdateCompany.


        :param billing_address_city: The billing_address_city of this UpdateCompany.
        :type billing_address_city: str
        """

        self._billing_address_city = billing_address_city

    @property
    def billing_address_line(self):
        """Gets the billing_address_line of this UpdateCompany.


        :return: The billing_address_line of this UpdateCompany.
        :rtype: str
        """
        return self._billing_address_line

    @billing_address_line.setter
    def billing_address_line(self, billing_address_line):
        """Sets the billing_address_line of this UpdateCompany.


        :param billing_address_line: The billing_address_line of this UpdateCompany.
        :type billing_address_line: str
        """

        self._billing_address_line = billing_address_line

    @property
    def billing_address_post_code(self):
        """Gets the billing_address_post_code of this UpdateCompany.


        :return: The billing_address_post_code of this UpdateCompany.
        :rtype: str
        """
        return self._billing_address_post_code

    @billing_address_post_code.setter
    def billing_address_post_code(self, billing_address_post_code):
        """Sets the billing_address_post_code of this UpdateCompany.


        :param billing_address_post_code: The billing_address_post_code of this UpdateCompany.
        :type billing_address_post_code: str
        """

        self._billing_address_post_code = billing_address_post_code

    @property
    def billing_address_state(self):
        """Gets the billing_address_state of this UpdateCompany.


        :return: The billing_address_state of this UpdateCompany.
        :rtype: str
        """
        return self._billing_address_state

    @billing_address_state.setter
    def billing_address_state(self, billing_address_state):
        """Sets the billing_address_state of this UpdateCompany.


        :param billing_address_state: The billing_address_state of this UpdateCompany.
        :type billing_address_state: str
        """

        self._billing_address_state = billing_address_state

    @property
    def billing_country_code(self):
        """Gets the billing_country_code of this UpdateCompany.


        :return: The billing_country_code of this UpdateCompany.
        :rtype: str
        """
        return self._billing_country_code

    @billing_country_code.setter
    def billing_country_code(self, billing_country_code):
        """Sets the billing_country_code of this UpdateCompany.


        :param billing_country_code: The billing_country_code of this UpdateCompany.
        :type billing_country_code: str
        """

        self._billing_country_code = billing_country_code

    @property
    def comments(self):
        """Gets the comments of this UpdateCompany.


        :return: The comments of this UpdateCompany.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this UpdateCompany.


        :param comments: The comments of this UpdateCompany.
        :type comments: str
        """

        self._comments = comments

    @property
    def company_id(self):
        """Gets the company_id of this UpdateCompany.


        :return: The company_id of this UpdateCompany.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UpdateCompany.


        :param company_id: The company_id of this UpdateCompany.
        :type company_id: int
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this UpdateCompany.


        :return: The company_name of this UpdateCompany.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UpdateCompany.


        :param company_name: The company_name of this UpdateCompany.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def fax(self):
        """Gets the fax of this UpdateCompany.


        :return: The fax of this UpdateCompany.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this UpdateCompany.


        :param fax: The fax of this UpdateCompany.
        :type fax: str
        """

        self._fax = fax

    @property
    def fields_to_update(self):
        """Gets the fields_to_update of this UpdateCompany.


        :return: The fields_to_update of this UpdateCompany.
        :rtype: List[str]
        """
        return self._fields_to_update

    @fields_to_update.setter
    def fields_to_update(self, fields_to_update):
        """Sets the fields_to_update of this UpdateCompany.


        :param fields_to_update: The fields_to_update of this UpdateCompany.
        :type fields_to_update: List[str]
        """

        self._fields_to_update = fields_to_update

    @property
    def phone(self):
        """Gets the phone of this UpdateCompany.


        :return: The phone of this UpdateCompany.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateCompany.


        :param phone: The phone of this UpdateCompany.
        :type phone: str
        """

        self._phone = phone

    @property
    def tax_number(self):
        """Gets the tax_number of this UpdateCompany.


        :return: The tax_number of this UpdateCompany.
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this UpdateCompany.


        :param tax_number: The tax_number of this UpdateCompany.
        :type tax_number: str
        """

        self._tax_number = tax_number

    @property
    def website(self):
        """Gets the website of this UpdateCompany.


        :return: The website of this UpdateCompany.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this UpdateCompany.


        :param website: The website of this UpdateCompany.
        :type website: str
        """

        self._website = website
