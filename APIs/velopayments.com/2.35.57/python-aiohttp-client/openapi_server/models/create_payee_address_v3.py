# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreatePayeeAddressV3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, country: str=None, county_or_province: str=None, line1: str=None, line2: str=None, line3: str=None, line4: str=None, zip_or_postcode: str=None):
        """CreatePayeeAddressV3 - a model defined in OpenAPI

        :param city: The city of this CreatePayeeAddressV3.
        :param country: The country of this CreatePayeeAddressV3.
        :param county_or_province: The county_or_province of this CreatePayeeAddressV3.
        :param line1: The line1 of this CreatePayeeAddressV3.
        :param line2: The line2 of this CreatePayeeAddressV3.
        :param line3: The line3 of this CreatePayeeAddressV3.
        :param line4: The line4 of this CreatePayeeAddressV3.
        :param zip_or_postcode: The zip_or_postcode of this CreatePayeeAddressV3.
        """
        self.openapi_types = {
            'city': str,
            'country': str,
            'county_or_province': str,
            'line1': str,
            'line2': str,
            'line3': str,
            'line4': str,
            'zip_or_postcode': str
        }

        self.attribute_map = {
            'city': 'city',
            'country': 'country',
            'county_or_province': 'countyOrProvince',
            'line1': 'line1',
            'line2': 'line2',
            'line3': 'line3',
            'line4': 'line4',
            'zip_or_postcode': 'zipOrPostcode'
        }

        self._city = city
        self._country = country
        self._county_or_province = county_or_province
        self._line1 = line1
        self._line2 = line2
        self._line3 = line3
        self._line4 = line4
        self._zip_or_postcode = zip_or_postcode

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreatePayeeAddressV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreatePayeeAddressV3 of this CreatePayeeAddressV3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this CreatePayeeAddressV3.


        :return: The city of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreatePayeeAddressV3.


        :param city: The city of this CreatePayeeAddressV3.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")
        if city is not None and len(city) > 50:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")
        if city is not None and len(city) < 2:
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `2`")

        self._city = city

    @property
    def country(self):
        """Gets the country of this CreatePayeeAddressV3.

        2 letter ISO 3166-1 country code

        :return: The country of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreatePayeeAddressV3.

        2 letter ISO 3166-1 country code

        :param country: The country of this CreatePayeeAddressV3.
        :type country: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")

        self._country = country

    @property
    def county_or_province(self):
        """Gets the county_or_province of this CreatePayeeAddressV3.


        :return: The county_or_province of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._county_or_province

    @county_or_province.setter
    def county_or_province(self, county_or_province):
        """Sets the county_or_province of this CreatePayeeAddressV3.


        :param county_or_province: The county_or_province of this CreatePayeeAddressV3.
        :type county_or_province: str
        """
        if county_or_province is not None and len(county_or_province) > 50:
            raise ValueError("Invalid value for `county_or_province`, length must be less than or equal to `50`")
        if county_or_province is not None and len(county_or_province) < 2:
            raise ValueError("Invalid value for `county_or_province`, length must be greater than or equal to `2`")

        self._county_or_province = county_or_province

    @property
    def line1(self):
        """Gets the line1 of this CreatePayeeAddressV3.


        :return: The line1 of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this CreatePayeeAddressV3.


        :param line1: The line1 of this CreatePayeeAddressV3.
        :type line1: str
        """
        if line1 is None:
            raise ValueError("Invalid value for `line1`, must not be `None`")
        if line1 is not None and len(line1) > 100:
            raise ValueError("Invalid value for `line1`, length must be less than or equal to `100`")
        if line1 is not None and len(line1) < 1:
            raise ValueError("Invalid value for `line1`, length must be greater than or equal to `1`")

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this CreatePayeeAddressV3.


        :return: The line2 of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this CreatePayeeAddressV3.


        :param line2: The line2 of this CreatePayeeAddressV3.
        :type line2: str
        """
        if line2 is not None and len(line2) > 100:
            raise ValueError("Invalid value for `line2`, length must be less than or equal to `100`")
        if line2 is not None and len(line2) < 0:
            raise ValueError("Invalid value for `line2`, length must be greater than or equal to `0`")

        self._line2 = line2

    @property
    def line3(self):
        """Gets the line3 of this CreatePayeeAddressV3.


        :return: The line3 of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """Sets the line3 of this CreatePayeeAddressV3.


        :param line3: The line3 of this CreatePayeeAddressV3.
        :type line3: str
        """
        if line3 is not None and len(line3) > 100:
            raise ValueError("Invalid value for `line3`, length must be less than or equal to `100`")
        if line3 is not None and len(line3) < 0:
            raise ValueError("Invalid value for `line3`, length must be greater than or equal to `0`")

        self._line3 = line3

    @property
    def line4(self):
        """Gets the line4 of this CreatePayeeAddressV3.


        :return: The line4 of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """Sets the line4 of this CreatePayeeAddressV3.


        :param line4: The line4 of this CreatePayeeAddressV3.
        :type line4: str
        """
        if line4 is not None and len(line4) > 100:
            raise ValueError("Invalid value for `line4`, length must be less than or equal to `100`")
        if line4 is not None and len(line4) < 0:
            raise ValueError("Invalid value for `line4`, length must be greater than or equal to `0`")

        self._line4 = line4

    @property
    def zip_or_postcode(self):
        """Gets the zip_or_postcode of this CreatePayeeAddressV3.


        :return: The zip_or_postcode of this CreatePayeeAddressV3.
        :rtype: str
        """
        return self._zip_or_postcode

    @zip_or_postcode.setter
    def zip_or_postcode(self, zip_or_postcode):
        """Sets the zip_or_postcode of this CreatePayeeAddressV3.


        :param zip_or_postcode: The zip_or_postcode of this CreatePayeeAddressV3.
        :type zip_or_postcode: str
        """
        if zip_or_postcode is not None and len(zip_or_postcode) > 60:
            raise ValueError("Invalid value for `zip_or_postcode`, length must be less than or equal to `60`")
        if zip_or_postcode is not None and len(zip_or_postcode) < 2:
            raise ValueError("Invalid value for `zip_or_postcode`, length must be greater than or equal to `2`")

        self._zip_or_postcode = zip_or_postcode
