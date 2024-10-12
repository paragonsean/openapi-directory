# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Mnp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, country: str=None, international_formatted: str=None, is_ported: bool=None, mccmnc: str=None, national_format: str=None, network: str=None, number: str=None):
        """Mnp - a model defined in OpenAPI

        :param country: The country of this Mnp.
        :param international_formatted: The international_formatted of this Mnp.
        :param is_ported: The is_ported of this Mnp.
        :param mccmnc: The mccmnc of this Mnp.
        :param national_format: The national_format of this Mnp.
        :param network: The network of this Mnp.
        :param number: The number of this Mnp.
        """
        self.openapi_types = {
            'country': str,
            'international_formatted': str,
            'is_ported': bool,
            'mccmnc': str,
            'national_format': str,
            'network': str,
            'number': str
        }

        self.attribute_map = {
            'country': 'country',
            'international_formatted': 'international_formatted',
            'is_ported': 'isPorted',
            'mccmnc': 'mccmnc',
            'national_format': 'national_format',
            'network': 'network',
            'number': 'number'
        }

        self._country = country
        self._international_formatted = international_formatted
        self._is_ported = is_ported
        self._mccmnc = mccmnc
        self._national_format = national_format
        self._network = network
        self._number = number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Mnp':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Mnp of this Mnp.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country(self):
        """Gets the country of this Mnp.


        :return: The country of this Mnp.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Mnp.


        :param country: The country of this Mnp.
        :type country: str
        """

        self._country = country

    @property
    def international_formatted(self):
        """Gets the international_formatted of this Mnp.


        :return: The international_formatted of this Mnp.
        :rtype: str
        """
        return self._international_formatted

    @international_formatted.setter
    def international_formatted(self, international_formatted):
        """Sets the international_formatted of this Mnp.


        :param international_formatted: The international_formatted of this Mnp.
        :type international_formatted: str
        """

        self._international_formatted = international_formatted

    @property
    def is_ported(self):
        """Gets the is_ported of this Mnp.


        :return: The is_ported of this Mnp.
        :rtype: bool
        """
        return self._is_ported

    @is_ported.setter
    def is_ported(self, is_ported):
        """Sets the is_ported of this Mnp.


        :param is_ported: The is_ported of this Mnp.
        :type is_ported: bool
        """

        self._is_ported = is_ported

    @property
    def mccmnc(self):
        """Gets the mccmnc of this Mnp.


        :return: The mccmnc of this Mnp.
        :rtype: str
        """
        return self._mccmnc

    @mccmnc.setter
    def mccmnc(self, mccmnc):
        """Sets the mccmnc of this Mnp.


        :param mccmnc: The mccmnc of this Mnp.
        :type mccmnc: str
        """

        self._mccmnc = mccmnc

    @property
    def national_format(self):
        """Gets the national_format of this Mnp.


        :return: The national_format of this Mnp.
        :rtype: str
        """
        return self._national_format

    @national_format.setter
    def national_format(self, national_format):
        """Sets the national_format of this Mnp.


        :param national_format: The national_format of this Mnp.
        :type national_format: str
        """

        self._national_format = national_format

    @property
    def network(self):
        """Gets the network of this Mnp.


        :return: The network of this Mnp.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Mnp.


        :param network: The network of this Mnp.
        :type network: str
        """

        self._network = network

    @property
    def number(self):
        """Gets the number of this Mnp.


        :return: The number of this Mnp.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Mnp.


        :param number: The number of this Mnp.
        :type number: str
        """

        self._number = number
