# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class Document(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_place: str=None, expiry_date: date=None, issuance_country: str=None, issuance_date: date=None, issuance_location: str=None, nationality: str=None, number: str=None):
        """Document - a model defined in OpenAPI

        :param birth_place: The birth_place of this Document.
        :param expiry_date: The expiry_date of this Document.
        :param issuance_country: The issuance_country of this Document.
        :param issuance_date: The issuance_date of this Document.
        :param issuance_location: The issuance_location of this Document.
        :param nationality: The nationality of this Document.
        :param number: The number of this Document.
        """
        self.openapi_types = {
            'birth_place': str,
            'expiry_date': date,
            'issuance_country': str,
            'issuance_date': date,
            'issuance_location': str,
            'nationality': str,
            'number': str
        }

        self.attribute_map = {
            'birth_place': 'birthPlace',
            'expiry_date': 'expiryDate',
            'issuance_country': 'issuanceCountry',
            'issuance_date': 'issuanceDate',
            'issuance_location': 'issuanceLocation',
            'nationality': 'nationality',
            'number': 'number'
        }

        self._birth_place = birth_place
        self._expiry_date = expiry_date
        self._issuance_country = issuance_country
        self._issuance_date = issuance_date
        self._issuance_location = issuance_location
        self._nationality = nationality
        self._number = number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Document':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Document of this Document.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_place(self):
        """Gets the birth_place of this Document.

        Birth place as indicated on the document

        :return: The birth_place of this Document.
        :rtype: str
        """
        return self._birth_place

    @birth_place.setter
    def birth_place(self, birth_place):
        """Sets the birth_place of this Document.

        Birth place as indicated on the document

        :param birth_place: The birth_place of this Document.
        :type birth_place: str
        """

        self._birth_place = birth_place

    @property
    def expiry_date(self):
        """Gets the expiry_date of this Document.

        Date after which the document is not valid anymore.

        :return: The expiry_date of this Document.
        :rtype: date
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this Document.

        Date after which the document is not valid anymore.

        :param expiry_date: The expiry_date of this Document.
        :type expiry_date: date
        """

        self._expiry_date = expiry_date

    @property
    def issuance_country(self):
        """Gets the issuance_country of this Document.

        [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country that issued the document

        :return: The issuance_country of this Document.
        :rtype: str
        """
        return self._issuance_country

    @issuance_country.setter
    def issuance_country(self, issuance_country):
        """Sets the issuance_country of this Document.

        [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country that issued the document

        :param issuance_country: The issuance_country of this Document.
        :type issuance_country: str
        """
        if issuance_country is not None and not re.search(r'[a-zA-Z]{2}', issuance_country):
            raise ValueError("Invalid value for `issuance_country`, must be a follow pattern or equal to `/[a-zA-Z]{2}/`")

        self._issuance_country = issuance_country

    @property
    def issuance_date(self):
        """Gets the issuance_date of this Document.

        Date at which the document has been issued.

        :return: The issuance_date of this Document.
        :rtype: date
        """
        return self._issuance_date

    @issuance_date.setter
    def issuance_date(self, issuance_date):
        """Sets the issuance_date of this Document.

        Date at which the document has been issued.

        :param issuance_date: The issuance_date of this Document.
        :type issuance_date: date
        """

        self._issuance_date = issuance_date

    @property
    def issuance_location(self):
        """Gets the issuance_location of this Document.

        A more precise information concerning the place where the document has been issued, when available. It may be a country, a state, a city or any other type of location. e.g. New-York

        :return: The issuance_location of this Document.
        :rtype: str
        """
        return self._issuance_location

    @issuance_location.setter
    def issuance_location(self, issuance_location):
        """Sets the issuance_location of this Document.

        A more precise information concerning the place where the document has been issued, when available. It may be a country, a state, a city or any other type of location. e.g. New-York

        :param issuance_location: The issuance_location of this Document.
        :type issuance_location: str
        """

        self._issuance_location = issuance_location

    @property
    def nationality(self):
        """Gets the nationality of this Document.

        [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the nationality appearing on the document

        :return: The nationality of this Document.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this Document.

        [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the nationality appearing on the document

        :param nationality: The nationality of this Document.
        :type nationality: str
        """
        if nationality is not None and not re.search(r'[a-zA-Z]{2}', nationality):
            raise ValueError("Invalid value for `nationality`, must be a follow pattern or equal to `/[a-zA-Z]{2}/`")

        self._nationality = nationality

    @property
    def number(self):
        """Gets the number of this Document.

        The document number (shown on the document) . E.g. QFU514563221J

        :return: The number of this Document.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Document.

        The document number (shown on the document) . E.g. QFU514563221J

        :param number: The number of this Document.
        :type number: str
        """

        self._number = number
