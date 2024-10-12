# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Rate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, delivery_date: str=None, display_name: str=None, guaranteed: bool=None, price: float=None, service: str=None, ship_date: str=None, value: str=None):
        """Rate - a model defined in OpenAPI

        :param delivery_date: The delivery_date of this Rate.
        :param display_name: The display_name of this Rate.
        :param guaranteed: The guaranteed of this Rate.
        :param price: The price of this Rate.
        :param service: The service of this Rate.
        :param ship_date: The ship_date of this Rate.
        :param value: The value of this Rate.
        """
        self.openapi_types = {
            'delivery_date': str,
            'display_name': str,
            'guaranteed': bool,
            'price': float,
            'service': str,
            'ship_date': str,
            'value': str
        }

        self.attribute_map = {
            'delivery_date': 'delivery_date',
            'display_name': 'display_name',
            'guaranteed': 'guaranteed',
            'price': 'price',
            'service': 'service',
            'ship_date': 'ship_date',
            'value': 'value'
        }

        self._delivery_date = delivery_date
        self._display_name = display_name
        self._guaranteed = guaranteed
        self._price = price
        self._service = service
        self._ship_date = ship_date
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Rate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Rate of this Rate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def delivery_date(self):
        """Gets the delivery_date of this Rate.

        The target delivery date for the shipping method. Formatted as a datetime string.

        :return: The delivery_date of this Rate.
        :rtype: str
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this Rate.

        The target delivery date for the shipping method. Formatted as a datetime string.

        :param delivery_date: The delivery_date of this Rate.
        :type delivery_date: str
        """

        self._delivery_date = delivery_date

    @property
    def display_name(self):
        """Gets the display_name of this Rate.

        The display name for this shipping service.

        :return: The display_name of this Rate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Rate.

        The display name for this shipping service.

        :param display_name: The display_name of this Rate.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def guaranteed(self):
        """Gets the guaranteed of this Rate.

        Certain shipping methods have guaranteed delivery dates. This field indicates whether delivery_date is guaranteed or if it is just an estimate.

        :return: The guaranteed of this Rate.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this Rate.

        Certain shipping methods have guaranteed delivery dates. This field indicates whether delivery_date is guaranteed or if it is just an estimate.

        :param guaranteed: The guaranteed of this Rate.
        :type guaranteed: bool
        """

        self._guaranteed = guaranteed

    @property
    def price(self):
        """Gets the price of this Rate.

        The price of this shipping option for the given set of items.

        :return: The price of this Rate.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Rate.

        The price of this shipping option for the given set of items.

        :param price: The price of this Rate.
        :type price: float
        """

        self._price = price

    @property
    def service(self):
        """Gets the service of this Rate.

        The identifier string for this shipping service. Use this value when creating an order with this as your requested shipping method.

        :return: The service of this Rate.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Rate.

        The identifier string for this shipping service. Use this value when creating an order with this as your requested shipping method.

        :param service: The service of this Rate.
        :type service: str
        """

        self._service = service

    @property
    def ship_date(self):
        """Gets the ship_date of this Rate.

        The target ship date for the shipping method. Formatted as a datetime string.

        :return: The ship_date of this Rate.
        :rtype: str
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this Rate.

        The target ship date for the shipping method. Formatted as a datetime string.

        :param ship_date: The ship_date of this Rate.
        :type ship_date: str
        """

        self._ship_date = ship_date

    @property
    def value(self):
        """Gets the value of this Rate.

        Reserved field. Do not use.

        :return: The value of this Rate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Rate.

        Reserved field. Do not use.

        :param value: The value of this Rate.
        :type value: str
        """

        self._value = value
