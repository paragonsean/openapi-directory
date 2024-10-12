# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ContactInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, business_phone: str=None, business_phone_ext: str=None, conference_info: str=None, home_phone: str=None, mobile_phone: str=None, preferred_phone_type: str=None, skype_username: str=None):
        """ContactInputModel - a model defined in OpenAPI

        :param business_phone: The business_phone of this ContactInputModel.
        :param business_phone_ext: The business_phone_ext of this ContactInputModel.
        :param conference_info: The conference_info of this ContactInputModel.
        :param home_phone: The home_phone of this ContactInputModel.
        :param mobile_phone: The mobile_phone of this ContactInputModel.
        :param preferred_phone_type: The preferred_phone_type of this ContactInputModel.
        :param skype_username: The skype_username of this ContactInputModel.
        """
        self.openapi_types = {
            'business_phone': str,
            'business_phone_ext': str,
            'conference_info': str,
            'home_phone': str,
            'mobile_phone': str,
            'preferred_phone_type': str,
            'skype_username': str
        }

        self.attribute_map = {
            'business_phone': 'businessPhone',
            'business_phone_ext': 'businessPhoneExt',
            'conference_info': 'conferenceInfo',
            'home_phone': 'homePhone',
            'mobile_phone': 'mobilePhone',
            'preferred_phone_type': 'preferredPhoneType',
            'skype_username': 'skypeUsername'
        }

        self._business_phone = business_phone
        self._business_phone_ext = business_phone_ext
        self._conference_info = conference_info
        self._home_phone = home_phone
        self._mobile_phone = mobile_phone
        self._preferred_phone_type = preferred_phone_type
        self._skype_username = skype_username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContactInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContactInputModel of this ContactInputModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_phone(self):
        """Gets the business_phone of this ContactInputModel.


        :return: The business_phone of this ContactInputModel.
        :rtype: str
        """
        return self._business_phone

    @business_phone.setter
    def business_phone(self, business_phone):
        """Sets the business_phone of this ContactInputModel.


        :param business_phone: The business_phone of this ContactInputModel.
        :type business_phone: str
        """

        self._business_phone = business_phone

    @property
    def business_phone_ext(self):
        """Gets the business_phone_ext of this ContactInputModel.


        :return: The business_phone_ext of this ContactInputModel.
        :rtype: str
        """
        return self._business_phone_ext

    @business_phone_ext.setter
    def business_phone_ext(self, business_phone_ext):
        """Sets the business_phone_ext of this ContactInputModel.


        :param business_phone_ext: The business_phone_ext of this ContactInputModel.
        :type business_phone_ext: str
        """

        self._business_phone_ext = business_phone_ext

    @property
    def conference_info(self):
        """Gets the conference_info of this ContactInputModel.


        :return: The conference_info of this ContactInputModel.
        :rtype: str
        """
        return self._conference_info

    @conference_info.setter
    def conference_info(self, conference_info):
        """Sets the conference_info of this ContactInputModel.


        :param conference_info: The conference_info of this ContactInputModel.
        :type conference_info: str
        """

        self._conference_info = conference_info

    @property
    def home_phone(self):
        """Gets the home_phone of this ContactInputModel.


        :return: The home_phone of this ContactInputModel.
        :rtype: str
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this ContactInputModel.


        :param home_phone: The home_phone of this ContactInputModel.
        :type home_phone: str
        """

        self._home_phone = home_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this ContactInputModel.


        :return: The mobile_phone of this ContactInputModel.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this ContactInputModel.


        :param mobile_phone: The mobile_phone of this ContactInputModel.
        :type mobile_phone: str
        """

        self._mobile_phone = mobile_phone

    @property
    def preferred_phone_type(self):
        """Gets the preferred_phone_type of this ContactInputModel.


        :return: The preferred_phone_type of this ContactInputModel.
        :rtype: str
        """
        return self._preferred_phone_type

    @preferred_phone_type.setter
    def preferred_phone_type(self, preferred_phone_type):
        """Sets the preferred_phone_type of this ContactInputModel.


        :param preferred_phone_type: The preferred_phone_type of this ContactInputModel.
        :type preferred_phone_type: str
        """

        self._preferred_phone_type = preferred_phone_type

    @property
    def skype_username(self):
        """Gets the skype_username of this ContactInputModel.


        :return: The skype_username of this ContactInputModel.
        :rtype: str
        """
        return self._skype_username

    @skype_username.setter
    def skype_username(self, skype_username):
        """Sets the skype_username of this ContactInputModel.


        :param skype_username: The skype_username of this ContactInputModel.
        :type skype_username: str
        """

        self._skype_username = skype_username
