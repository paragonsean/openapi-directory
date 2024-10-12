# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ContactDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_name: str=None, contact_person: str=None, email_list: List[str]=None, phone: str=None):
        """ContactDetails - a model defined in OpenAPI

        :param company_name: The company_name of this ContactDetails.
        :param contact_person: The contact_person of this ContactDetails.
        :param email_list: The email_list of this ContactDetails.
        :param phone: The phone of this ContactDetails.
        """
        self.openapi_types = {
            'company_name': str,
            'contact_person': str,
            'email_list': List[str],
            'phone': str
        }

        self.attribute_map = {
            'company_name': 'companyName',
            'contact_person': 'contactPerson',
            'email_list': 'emailList',
            'phone': 'phone'
        }

        self._company_name = company_name
        self._contact_person = contact_person
        self._email_list = email_list
        self._phone = phone

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContactDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContactDetails of this ContactDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_name(self):
        """Gets the company_name of this ContactDetails.

        The name of the company.

        :return: The company_name of this ContactDetails.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ContactDetails.

        The name of the company.

        :param company_name: The company_name of this ContactDetails.
        :type company_name: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")

        self._company_name = company_name

    @property
    def contact_person(self):
        """Gets the contact_person of this ContactDetails.

        The contact person name.

        :return: The contact_person of this ContactDetails.
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this ContactDetails.

        The contact person name.

        :param contact_person: The contact_person of this ContactDetails.
        :type contact_person: str
        """
        if contact_person is None:
            raise ValueError("Invalid value for `contact_person`, must not be `None`")

        self._contact_person = contact_person

    @property
    def email_list(self):
        """Gets the email_list of this ContactDetails.

        The email list.

        :return: The email_list of this ContactDetails.
        :rtype: List[str]
        """
        return self._email_list

    @email_list.setter
    def email_list(self, email_list):
        """Sets the email_list of this ContactDetails.

        The email list.

        :param email_list: The email_list of this ContactDetails.
        :type email_list: List[str]
        """
        if email_list is None:
            raise ValueError("Invalid value for `email_list`, must not be `None`")

        self._email_list = email_list

    @property
    def phone(self):
        """Gets the phone of this ContactDetails.

        The phone number.

        :return: The phone of this ContactDetails.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactDetails.

        The phone number.

        :param phone: The phone of this ContactDetails.
        :type phone: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")

        self._phone = phone
