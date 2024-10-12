# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.money_object import MoneyObject
from openapi_server import util


class CashbackObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: MoneyObject=None, description: str=None):
        """CashbackObject - a model defined in OpenAPI

        :param amount: The amount of this CashbackObject.
        :param description: The description of this CashbackObject.
        """
        self.openapi_types = {
            'amount': MoneyObject,
            'description': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'description': 'description'
        }

        self._amount = amount
        self._description = description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CashbackObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CashbackObject of this CashbackObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this CashbackObject.

        The total amount of cashback paid, represented as a positive value. 

        :return: The amount of this CashbackObject.
        :rtype: MoneyObject
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashbackObject.

        The total amount of cashback paid, represented as a positive value. 

        :param amount: The amount of this CashbackObject.
        :type amount: MoneyObject
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this CashbackObject.

        A brief description of why this cashback was paid. 

        :return: The description of this CashbackObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CashbackObject.

        A brief description of why this cashback was paid. 

        :param description: The description of this CashbackObject.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description
