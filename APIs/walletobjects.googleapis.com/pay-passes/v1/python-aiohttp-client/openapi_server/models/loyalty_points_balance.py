# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.money import Money
from openapi_server import util


class LoyaltyPointsBalance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, double: float=None, int: int=None, money: Money=None, string: str=None):
        """LoyaltyPointsBalance - a model defined in OpenAPI

        :param double: The double of this LoyaltyPointsBalance.
        :param int: The int of this LoyaltyPointsBalance.
        :param money: The money of this LoyaltyPointsBalance.
        :param string: The string of this LoyaltyPointsBalance.
        """
        self.openapi_types = {
            'double': float,
            'int': int,
            'money': Money,
            'string': str
        }

        self.attribute_map = {
            'double': 'double',
            'int': 'int',
            'money': 'money',
            'string': 'string'
        }

        self._double = double
        self._int = int
        self._money = money
        self._string = string

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LoyaltyPointsBalance':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LoyaltyPointsBalance of this LoyaltyPointsBalance.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def double(self):
        """Gets the double of this LoyaltyPointsBalance.

        The double form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :return: The double of this LoyaltyPointsBalance.
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this LoyaltyPointsBalance.

        The double form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :param double: The double of this LoyaltyPointsBalance.
        :type double: float
        """

        self._double = double

    @property
    def int(self):
        """Gets the int of this LoyaltyPointsBalance.

        The integer form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :return: The int of this LoyaltyPointsBalance.
        :rtype: int
        """
        return self._int

    @int.setter
    def int(self, int):
        """Sets the int of this LoyaltyPointsBalance.

        The integer form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :param int: The int of this LoyaltyPointsBalance.
        :type int: int
        """

        self._int = int

    @property
    def money(self):
        """Gets the money of this LoyaltyPointsBalance.


        :return: The money of this LoyaltyPointsBalance.
        :rtype: Money
        """
        return self._money

    @money.setter
    def money(self, money):
        """Sets the money of this LoyaltyPointsBalance.


        :param money: The money of this LoyaltyPointsBalance.
        :type money: Money
        """

        self._money = money

    @property
    def string(self):
        """Gets the string of this LoyaltyPointsBalance.

        The string form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :return: The string of this LoyaltyPointsBalance.
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this LoyaltyPointsBalance.

        The string form of a balance. Only one of these subtypes (string, int, double, money) should be populated.

        :param string: The string of this LoyaltyPointsBalance.
        :type string: str
        """

        self._string = string
