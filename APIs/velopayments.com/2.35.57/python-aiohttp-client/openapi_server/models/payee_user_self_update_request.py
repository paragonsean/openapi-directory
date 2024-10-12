# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class PayeeUserSelfUpdateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email: str=None, first_name: str=None, last_name: str=None, primary_contact_number: str=None, secondary_contact_number: str=None, sms_number: str=None):
        """PayeeUserSelfUpdateRequest - a model defined in OpenAPI

        :param email: The email of this PayeeUserSelfUpdateRequest.
        :param first_name: The first_name of this PayeeUserSelfUpdateRequest.
        :param last_name: The last_name of this PayeeUserSelfUpdateRequest.
        :param primary_contact_number: The primary_contact_number of this PayeeUserSelfUpdateRequest.
        :param secondary_contact_number: The secondary_contact_number of this PayeeUserSelfUpdateRequest.
        :param sms_number: The sms_number of this PayeeUserSelfUpdateRequest.
        """
        self.openapi_types = {
            'email': str,
            'first_name': str,
            'last_name': str,
            'primary_contact_number': str,
            'secondary_contact_number': str,
            'sms_number': str
        }

        self.attribute_map = {
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'primary_contact_number': 'primaryContactNumber',
            'secondary_contact_number': 'secondaryContactNumber',
            'sms_number': 'smsNumber'
        }

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._primary_contact_number = primary_contact_number
        self._secondary_contact_number = secondary_contact_number
        self._sms_number = sms_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayeeUserSelfUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayeeUserSelfUpdateRequest of this PayeeUserSelfUpdateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this PayeeUserSelfUpdateRequest.

        the email address of the user

        :return: The email of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayeeUserSelfUpdateRequest.

        the email address of the user

        :param email: The email of this PayeeUserSelfUpdateRequest.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this PayeeUserSelfUpdateRequest.


        :return: The first_name of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PayeeUserSelfUpdateRequest.


        :param first_name: The first_name of this PayeeUserSelfUpdateRequest.
        :type first_name: str
        """
        if first_name is not None and len(first_name) > 128:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `128`")
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PayeeUserSelfUpdateRequest.


        :return: The last_name of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PayeeUserSelfUpdateRequest.


        :param last_name: The last_name of this PayeeUserSelfUpdateRequest.
        :type last_name: str
        """
        if last_name is not None and len(last_name) > 128:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `128`")
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")

        self._last_name = last_name

    @property
    def primary_contact_number(self):
        """Gets the primary_contact_number of this PayeeUserSelfUpdateRequest.

        The main contact number for the user 

        :return: The primary_contact_number of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._primary_contact_number

    @primary_contact_number.setter
    def primary_contact_number(self, primary_contact_number):
        """Sets the primary_contact_number of this PayeeUserSelfUpdateRequest.

        The main contact number for the user 

        :param primary_contact_number: The primary_contact_number of this PayeeUserSelfUpdateRequest.
        :type primary_contact_number: str
        """
        if primary_contact_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', primary_contact_number):
            raise ValueError("Invalid value for `primary_contact_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")

        self._primary_contact_number = primary_contact_number

    @property
    def secondary_contact_number(self):
        """Gets the secondary_contact_number of this PayeeUserSelfUpdateRequest.

        The secondary contact number for the user 

        :return: The secondary_contact_number of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._secondary_contact_number

    @secondary_contact_number.setter
    def secondary_contact_number(self, secondary_contact_number):
        """Sets the secondary_contact_number of this PayeeUserSelfUpdateRequest.

        The secondary contact number for the user 

        :param secondary_contact_number: The secondary_contact_number of this PayeeUserSelfUpdateRequest.
        :type secondary_contact_number: str
        """
        if secondary_contact_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', secondary_contact_number):
            raise ValueError("Invalid value for `secondary_contact_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")

        self._secondary_contact_number = secondary_contact_number

    @property
    def sms_number(self):
        """Gets the sms_number of this PayeeUserSelfUpdateRequest.

        The phone number of a device that the user can receive sms messages on 

        :return: The sms_number of this PayeeUserSelfUpdateRequest.
        :rtype: str
        """
        return self._sms_number

    @sms_number.setter
    def sms_number(self, sms_number):
        """Sets the sms_number of this PayeeUserSelfUpdateRequest.

        The phone number of a device that the user can receive sms messages on 

        :param sms_number: The sms_number of this PayeeUserSelfUpdateRequest.
        :type sms_number: str
        """
        if sms_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', sms_number):
            raise ValueError("Invalid value for `sms_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")

        self._sms_number = sms_number
