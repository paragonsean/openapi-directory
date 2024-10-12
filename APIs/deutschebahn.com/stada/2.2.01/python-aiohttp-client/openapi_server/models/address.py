# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Address(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, house_number: str=None, street: str=None, zipcode: int=None):
        """Address - a model defined in OpenAPI

        :param city: The city of this Address.
        :param house_number: The house_number of this Address.
        :param street: The street of this Address.
        :param zipcode: The zipcode of this Address.
        """
        self.openapi_types = {
            'city': str,
            'house_number': str,
            'street': str,
            'zipcode': int
        }

        self.attribute_map = {
            'city': 'city',
            'house_number': 'houseNumber',
            'street': 'street',
            'zipcode': 'zipcode'
        }

        self._city = city
        self._house_number = house_number
        self._street = street
        self._zipcode = zipcode

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Address':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Address of this Address.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this Address.


        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.
        :type city: str
        """

        self._city = city

    @property
    def house_number(self):
        """Gets the house_number of this Address.


        :return: The house_number of this Address.
        :rtype: str
        """
        return self._house_number

    @house_number.setter
    def house_number(self, house_number):
        """Sets the house_number of this Address.


        :param house_number: The house_number of this Address.
        :type house_number: str
        """

        self._house_number = house_number

    @property
    def street(self):
        """Gets the street of this Address.


        :return: The street of this Address.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Address.


        :param street: The street of this Address.
        :type street: str
        """

        self._street = street

    @property
    def zipcode(self):
        """Gets the zipcode of this Address.


        :return: The zipcode of this Address.
        :rtype: int
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this Address.


        :param zipcode: The zipcode of this Address.
        :type zipcode: int
        """

        self._zipcode = zipcode
