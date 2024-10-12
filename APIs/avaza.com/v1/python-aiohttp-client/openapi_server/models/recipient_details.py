# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RecipientDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_idfk: int=None, company_name: str=None, recipient_billing_address_city: str=None, recipient_billing_address_country_code: str=None, recipient_billing_address_line: str=None, recipient_billing_address_post_code: str=None, recipient_billing_address_state: str=None, recipient_formatted_billing_address: str=None):
        """RecipientDetails - a model defined in OpenAPI

        :param company_idfk: The company_idfk of this RecipientDetails.
        :param company_name: The company_name of this RecipientDetails.
        :param recipient_billing_address_city: The recipient_billing_address_city of this RecipientDetails.
        :param recipient_billing_address_country_code: The recipient_billing_address_country_code of this RecipientDetails.
        :param recipient_billing_address_line: The recipient_billing_address_line of this RecipientDetails.
        :param recipient_billing_address_post_code: The recipient_billing_address_post_code of this RecipientDetails.
        :param recipient_billing_address_state: The recipient_billing_address_state of this RecipientDetails.
        :param recipient_formatted_billing_address: The recipient_formatted_billing_address of this RecipientDetails.
        """
        self.openapi_types = {
            'company_idfk': int,
            'company_name': str,
            'recipient_billing_address_city': str,
            'recipient_billing_address_country_code': str,
            'recipient_billing_address_line': str,
            'recipient_billing_address_post_code': str,
            'recipient_billing_address_state': str,
            'recipient_formatted_billing_address': str
        }

        self.attribute_map = {
            'company_idfk': 'CompanyIDFK',
            'company_name': 'CompanyName',
            'recipient_billing_address_city': 'RecipientBillingAddressCity',
            'recipient_billing_address_country_code': 'RecipientBillingAddressCountryCode',
            'recipient_billing_address_line': 'RecipientBillingAddressLine',
            'recipient_billing_address_post_code': 'RecipientBillingAddressPostCode',
            'recipient_billing_address_state': 'RecipientBillingAddressState',
            'recipient_formatted_billing_address': 'RecipientFormattedBillingAddress'
        }

        self._company_idfk = company_idfk
        self._company_name = company_name
        self._recipient_billing_address_city = recipient_billing_address_city
        self._recipient_billing_address_country_code = recipient_billing_address_country_code
        self._recipient_billing_address_line = recipient_billing_address_line
        self._recipient_billing_address_post_code = recipient_billing_address_post_code
        self._recipient_billing_address_state = recipient_billing_address_state
        self._recipient_formatted_billing_address = recipient_formatted_billing_address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RecipientDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RecipientDetails of this RecipientDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_idfk(self):
        """Gets the company_idfk of this RecipientDetails.


        :return: The company_idfk of this RecipientDetails.
        :rtype: int
        """
        return self._company_idfk

    @company_idfk.setter
    def company_idfk(self, company_idfk):
        """Sets the company_idfk of this RecipientDetails.


        :param company_idfk: The company_idfk of this RecipientDetails.
        :type company_idfk: int
        """

        self._company_idfk = company_idfk

    @property
    def company_name(self):
        """Gets the company_name of this RecipientDetails.


        :return: The company_name of this RecipientDetails.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this RecipientDetails.


        :param company_name: The company_name of this RecipientDetails.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def recipient_billing_address_city(self):
        """Gets the recipient_billing_address_city of this RecipientDetails.


        :return: The recipient_billing_address_city of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_billing_address_city

    @recipient_billing_address_city.setter
    def recipient_billing_address_city(self, recipient_billing_address_city):
        """Sets the recipient_billing_address_city of this RecipientDetails.


        :param recipient_billing_address_city: The recipient_billing_address_city of this RecipientDetails.
        :type recipient_billing_address_city: str
        """

        self._recipient_billing_address_city = recipient_billing_address_city

    @property
    def recipient_billing_address_country_code(self):
        """Gets the recipient_billing_address_country_code of this RecipientDetails.


        :return: The recipient_billing_address_country_code of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_billing_address_country_code

    @recipient_billing_address_country_code.setter
    def recipient_billing_address_country_code(self, recipient_billing_address_country_code):
        """Sets the recipient_billing_address_country_code of this RecipientDetails.


        :param recipient_billing_address_country_code: The recipient_billing_address_country_code of this RecipientDetails.
        :type recipient_billing_address_country_code: str
        """

        self._recipient_billing_address_country_code = recipient_billing_address_country_code

    @property
    def recipient_billing_address_line(self):
        """Gets the recipient_billing_address_line of this RecipientDetails.


        :return: The recipient_billing_address_line of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_billing_address_line

    @recipient_billing_address_line.setter
    def recipient_billing_address_line(self, recipient_billing_address_line):
        """Sets the recipient_billing_address_line of this RecipientDetails.


        :param recipient_billing_address_line: The recipient_billing_address_line of this RecipientDetails.
        :type recipient_billing_address_line: str
        """

        self._recipient_billing_address_line = recipient_billing_address_line

    @property
    def recipient_billing_address_post_code(self):
        """Gets the recipient_billing_address_post_code of this RecipientDetails.


        :return: The recipient_billing_address_post_code of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_billing_address_post_code

    @recipient_billing_address_post_code.setter
    def recipient_billing_address_post_code(self, recipient_billing_address_post_code):
        """Sets the recipient_billing_address_post_code of this RecipientDetails.


        :param recipient_billing_address_post_code: The recipient_billing_address_post_code of this RecipientDetails.
        :type recipient_billing_address_post_code: str
        """

        self._recipient_billing_address_post_code = recipient_billing_address_post_code

    @property
    def recipient_billing_address_state(self):
        """Gets the recipient_billing_address_state of this RecipientDetails.


        :return: The recipient_billing_address_state of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_billing_address_state

    @recipient_billing_address_state.setter
    def recipient_billing_address_state(self, recipient_billing_address_state):
        """Sets the recipient_billing_address_state of this RecipientDetails.


        :param recipient_billing_address_state: The recipient_billing_address_state of this RecipientDetails.
        :type recipient_billing_address_state: str
        """

        self._recipient_billing_address_state = recipient_billing_address_state

    @property
    def recipient_formatted_billing_address(self):
        """Gets the recipient_formatted_billing_address of this RecipientDetails.


        :return: The recipient_formatted_billing_address of this RecipientDetails.
        :rtype: str
        """
        return self._recipient_formatted_billing_address

    @recipient_formatted_billing_address.setter
    def recipient_formatted_billing_address(self, recipient_formatted_billing_address):
        """Sets the recipient_formatted_billing_address of this RecipientDetails.


        :param recipient_formatted_billing_address: The recipient_formatted_billing_address of this RecipientDetails.
        :type recipient_formatted_billing_address: str
        """

        self._recipient_formatted_billing_address = recipient_formatted_billing_address
