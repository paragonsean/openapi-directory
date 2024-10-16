# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DiaryGuestDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allow_marketing_correspondence: bool=None, email_address: str=None, forename: str=None, mobile_phone: str=None, oid: str=None, surname: str=None):
        """DiaryGuestDetails - a model defined in OpenAPI

        :param allow_marketing_correspondence: The allow_marketing_correspondence of this DiaryGuestDetails.
        :param email_address: The email_address of this DiaryGuestDetails.
        :param forename: The forename of this DiaryGuestDetails.
        :param mobile_phone: The mobile_phone of this DiaryGuestDetails.
        :param oid: The oid of this DiaryGuestDetails.
        :param surname: The surname of this DiaryGuestDetails.
        """
        self.openapi_types = {
            'allow_marketing_correspondence': bool,
            'email_address': str,
            'forename': str,
            'mobile_phone': str,
            'oid': str,
            'surname': str
        }

        self.attribute_map = {
            'allow_marketing_correspondence': 'AllowMarketingCorrespondence',
            'email_address': 'EmailAddress',
            'forename': 'Forename',
            'mobile_phone': 'MobilePhone',
            'oid': 'OID',
            'surname': 'Surname'
        }

        self._allow_marketing_correspondence = allow_marketing_correspondence
        self._email_address = email_address
        self._forename = forename
        self._mobile_phone = mobile_phone
        self._oid = oid
        self._surname = surname

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DiaryGuestDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DiaryGuestDetails of this DiaryGuestDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allow_marketing_correspondence(self):
        """Gets the allow_marketing_correspondence of this DiaryGuestDetails.

        Marketing Correspondence Preferences

        :return: The allow_marketing_correspondence of this DiaryGuestDetails.
        :rtype: bool
        """
        return self._allow_marketing_correspondence

    @allow_marketing_correspondence.setter
    def allow_marketing_correspondence(self, allow_marketing_correspondence):
        """Sets the allow_marketing_correspondence of this DiaryGuestDetails.

        Marketing Correspondence Preferences

        :param allow_marketing_correspondence: The allow_marketing_correspondence of this DiaryGuestDetails.
        :type allow_marketing_correspondence: bool
        """

        self._allow_marketing_correspondence = allow_marketing_correspondence

    @property
    def email_address(self):
        """Gets the email_address of this DiaryGuestDetails.

        Email address

        :return: The email_address of this DiaryGuestDetails.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this DiaryGuestDetails.

        Email address

        :param email_address: The email_address of this DiaryGuestDetails.
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def forename(self):
        """Gets the forename of this DiaryGuestDetails.

        Forename

        :return: The forename of this DiaryGuestDetails.
        :rtype: str
        """
        return self._forename

    @forename.setter
    def forename(self, forename):
        """Sets the forename of this DiaryGuestDetails.

        Forename

        :param forename: The forename of this DiaryGuestDetails.
        :type forename: str
        """

        self._forename = forename

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this DiaryGuestDetails.

        Mobile phone

        :return: The mobile_phone of this DiaryGuestDetails.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this DiaryGuestDetails.

        Mobile phone

        :param mobile_phone: The mobile_phone of this DiaryGuestDetails.
        :type mobile_phone: str
        """

        self._mobile_phone = mobile_phone

    @property
    def oid(self):
        """Gets the oid of this DiaryGuestDetails.

        The unique identifier of a user, only submit this is known

        :return: The oid of this DiaryGuestDetails.
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this DiaryGuestDetails.

        The unique identifier of a user, only submit this is known

        :param oid: The oid of this DiaryGuestDetails.
        :type oid: str
        """

        self._oid = oid

    @property
    def surname(self):
        """Gets the surname of this DiaryGuestDetails.

        Surname

        :return: The surname of this DiaryGuestDetails.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this DiaryGuestDetails.

        Surname

        :param surname: The surname of this DiaryGuestDetails.
        :type surname: str
        """

        self._surname = surname
