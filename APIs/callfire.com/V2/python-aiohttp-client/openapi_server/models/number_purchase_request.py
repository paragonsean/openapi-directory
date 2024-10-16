# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NumberPurchaseRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, local_count: int=None, numbers: List[str]=None, prefix: str=None, promo: str=None, state: str=None, toll_free_count: int=None, zipcode: str=None):
        """NumberPurchaseRequest - a model defined in OpenAPI

        :param city: The city of this NumberPurchaseRequest.
        :param local_count: The local_count of this NumberPurchaseRequest.
        :param numbers: The numbers of this NumberPurchaseRequest.
        :param prefix: The prefix of this NumberPurchaseRequest.
        :param promo: The promo of this NumberPurchaseRequest.
        :param state: The state of this NumberPurchaseRequest.
        :param toll_free_count: The toll_free_count of this NumberPurchaseRequest.
        :param zipcode: The zipcode of this NumberPurchaseRequest.
        """
        self.openapi_types = {
            'city': str,
            'local_count': int,
            'numbers': List[str],
            'prefix': str,
            'promo': str,
            'state': str,
            'toll_free_count': int,
            'zipcode': str
        }

        self.attribute_map = {
            'city': 'city',
            'local_count': 'localCount',
            'numbers': 'numbers',
            'prefix': 'prefix',
            'promo': 'promo',
            'state': 'state',
            'toll_free_count': 'tollFreeCount',
            'zipcode': 'zipcode'
        }

        self._city = city
        self._local_count = local_count
        self._numbers = numbers
        self._prefix = prefix
        self._promo = promo
        self._state = state
        self._toll_free_count = toll_free_count
        self._zipcode = zipcode

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NumberPurchaseRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NumberPurchaseRequest of this NumberPurchaseRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this NumberPurchaseRequest.

        City of requested numbers

        :return: The city of this NumberPurchaseRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this NumberPurchaseRequest.

        City of requested numbers

        :param city: The city of this NumberPurchaseRequest.
        :type city: str
        """

        self._city = city

    @property
    def local_count(self):
        """Gets the local_count of this NumberPurchaseRequest.

        Total count of local numbers requested

        :return: The local_count of this NumberPurchaseRequest.
        :rtype: int
        """
        return self._local_count

    @local_count.setter
    def local_count(self, local_count):
        """Sets the local_count of this NumberPurchaseRequest.

        Total count of local numbers requested

        :param local_count: The local_count of this NumberPurchaseRequest.
        :type local_count: int
        """

        self._local_count = local_count

    @property
    def numbers(self):
        """Gets the numbers of this NumberPurchaseRequest.

        A list of phone numbers in E.164 format (11-digit) to buy. Example: 12132000384

        :return: The numbers of this NumberPurchaseRequest.
        :rtype: List[str]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this NumberPurchaseRequest.

        A list of phone numbers in E.164 format (11-digit) to buy. Example: 12132000384

        :param numbers: The numbers of this NumberPurchaseRequest.
        :type numbers: List[str]
        """

        self._numbers = numbers

    @property
    def prefix(self):
        """Gets the prefix of this NumberPurchaseRequest.

        Country prefix of requested numbers

        :return: The prefix of this NumberPurchaseRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this NumberPurchaseRequest.

        Country prefix of requested numbers

        :param prefix: The prefix of this NumberPurchaseRequest.
        :type prefix: str
        """

        self._prefix = prefix

    @property
    def promo(self):
        """Gets the promo of this NumberPurchaseRequest.

        ~

        :return: The promo of this NumberPurchaseRequest.
        :rtype: str
        """
        return self._promo

    @promo.setter
    def promo(self, promo):
        """Sets the promo of this NumberPurchaseRequest.

        ~

        :param promo: The promo of this NumberPurchaseRequest.
        :type promo: str
        """

        self._promo = promo

    @property
    def state(self):
        """Gets the state of this NumberPurchaseRequest.

        A two-letter state code of requested numbers

        :return: The state of this NumberPurchaseRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NumberPurchaseRequest.

        A two-letter state code of requested numbers

        :param state: The state of this NumberPurchaseRequest.
        :type state: str
        """

        self._state = state

    @property
    def toll_free_count(self):
        """Gets the toll_free_count of this NumberPurchaseRequest.

        Total count of toll-free numbers requested

        :return: The toll_free_count of this NumberPurchaseRequest.
        :rtype: int
        """
        return self._toll_free_count

    @toll_free_count.setter
    def toll_free_count(self, toll_free_count):
        """Sets the toll_free_count of this NumberPurchaseRequest.

        Total count of toll-free numbers requested

        :param toll_free_count: The toll_free_count of this NumberPurchaseRequest.
        :type toll_free_count: int
        """

        self._toll_free_count = toll_free_count

    @property
    def zipcode(self):
        """Gets the zipcode of this NumberPurchaseRequest.

        A five-digit Zip code of requested numbers

        :return: The zipcode of this NumberPurchaseRequest.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this NumberPurchaseRequest.

        A five-digit Zip code of requested numbers

        :param zipcode: The zipcode of this NumberPurchaseRequest.
        :type zipcode: str
        """

        self._zipcode = zipcode
