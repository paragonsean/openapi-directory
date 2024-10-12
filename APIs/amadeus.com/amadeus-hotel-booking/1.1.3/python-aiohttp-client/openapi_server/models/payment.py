# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.card import Card
from openapi_server import util


class Payment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, card: Card=None, id: int=None, method: str=None):
        """Payment - a model defined in OpenAPI

        :param card: The card of this Payment.
        :param id: The id of this Payment.
        :param method: The method of this Payment.
        """
        self.openapi_types = {
            'card': Card,
            'id': int,
            'method': str
        }

        self.attribute_map = {
            'card': 'card',
            'id': 'id',
            'method': 'method'
        }

        self._card = card
        self._id = id
        self._method = method

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Payment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Payment of this Payment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card(self):
        """Gets the card of this Payment.


        :return: The card of this Payment.
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this Payment.


        :param card: The card of this Payment.
        :type card: Card
        """

        self._card = card

    @property
    def id(self):
        """Gets the id of this Payment.


        :return: The id of this Payment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.


        :param id: The id of this Payment.
        :type id: int
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this Payment.

        The Payment Methods:  * creditCard (CC) - Payment Cards in `creditCards` are accepted           

        :return: The method of this Payment.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Payment.

        The Payment Methods:  * creditCard (CC) - Payment Cards in `creditCards` are accepted           

        :param method: The method of this Payment.
        :type method: str
        """
        allowed_values = ["creditCard"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method
