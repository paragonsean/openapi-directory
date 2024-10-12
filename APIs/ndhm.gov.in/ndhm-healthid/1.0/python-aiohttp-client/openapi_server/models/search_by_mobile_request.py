# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SearchByMobileRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gender: str=None, mobile: str=None, name: str=None, year_of_birth: str=None):
        """SearchByMobileRequest - a model defined in OpenAPI

        :param gender: The gender of this SearchByMobileRequest.
        :param mobile: The mobile of this SearchByMobileRequest.
        :param name: The name of this SearchByMobileRequest.
        :param year_of_birth: The year_of_birth of this SearchByMobileRequest.
        """
        self.openapi_types = {
            'gender': str,
            'mobile': str,
            'name': str,
            'year_of_birth': str
        }

        self.attribute_map = {
            'gender': 'gender',
            'mobile': 'mobile',
            'name': 'name',
            'year_of_birth': 'yearOfBirth'
        }

        self._gender = gender
        self._mobile = mobile
        self._name = name
        self._year_of_birth = year_of_birth

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SearchByMobileRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SearchByMobileRequest of this SearchByMobileRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gender(self):
        """Gets the gender of this SearchByMobileRequest.


        :return: The gender of this SearchByMobileRequest.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this SearchByMobileRequest.


        :param gender: The gender of this SearchByMobileRequest.
        :type gender: str
        """

        self._gender = gender

    @property
    def mobile(self):
        """Gets the mobile of this SearchByMobileRequest.


        :return: The mobile of this SearchByMobileRequest.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this SearchByMobileRequest.


        :param mobile: The mobile of this SearchByMobileRequest.
        :type mobile: str
        """

        self._mobile = mobile

    @property
    def name(self):
        """Gets the name of this SearchByMobileRequest.


        :return: The name of this SearchByMobileRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchByMobileRequest.


        :param name: The name of this SearchByMobileRequest.
        :type name: str
        """

        self._name = name

    @property
    def year_of_birth(self):
        """Gets the year_of_birth of this SearchByMobileRequest.


        :return: The year_of_birth of this SearchByMobileRequest.
        :rtype: str
        """
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        """Sets the year_of_birth of this SearchByMobileRequest.


        :param year_of_birth: The year_of_birth of this SearchByMobileRequest.
        :type year_of_birth: str
        """

        self._year_of_birth = year_of_birth
