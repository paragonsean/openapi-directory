# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NewCard(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accept_fees_and_charges: bool=None, address_type: str=None, card_pin: str=None, eur_ican: int=None, gbp_ican: int=None, user_id: int=None):
        """NewCard - a model defined in OpenAPI

        :param accept_fees_and_charges: The accept_fees_and_charges of this NewCard.
        :param address_type: The address_type of this NewCard.
        :param card_pin: The card_pin of this NewCard.
        :param eur_ican: The eur_ican of this NewCard.
        :param gbp_ican: The gbp_ican of this NewCard.
        :param user_id: The user_id of this NewCard.
        """
        self.openapi_types = {
            'accept_fees_and_charges': bool,
            'address_type': str,
            'card_pin': str,
            'eur_ican': int,
            'gbp_ican': int,
            'user_id': int
        }

        self.attribute_map = {
            'accept_fees_and_charges': 'acceptFeesAndCharges',
            'address_type': 'addressType',
            'card_pin': 'cardPin',
            'eur_ican': 'eurIcan',
            'gbp_ican': 'gbpIcan',
            'user_id': 'userId'
        }

        self._accept_fees_and_charges = accept_fees_and_charges
        self._address_type = address_type
        self._card_pin = card_pin
        self._eur_ican = eur_ican
        self._gbp_ican = gbp_ican
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NewCard':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The newCard of this NewCard.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accept_fees_and_charges(self):
        """Gets the accept_fees_and_charges of this NewCard.


        :return: The accept_fees_and_charges of this NewCard.
        :rtype: bool
        """
        return self._accept_fees_and_charges

    @accept_fees_and_charges.setter
    def accept_fees_and_charges(self, accept_fees_and_charges):
        """Sets the accept_fees_and_charges of this NewCard.


        :param accept_fees_and_charges: The accept_fees_and_charges of this NewCard.
        :type accept_fees_and_charges: bool
        """

        self._accept_fees_and_charges = accept_fees_and_charges

    @property
    def address_type(self):
        """Gets the address_type of this NewCard.


        :return: The address_type of this NewCard.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this NewCard.


        :param address_type: The address_type of this NewCard.
        :type address_type: str
        """
        allowed_values = ["HOME", "BUSINESS"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

    @property
    def card_pin(self):
        """Gets the card_pin of this NewCard.


        :return: The card_pin of this NewCard.
        :rtype: str
        """
        return self._card_pin

    @card_pin.setter
    def card_pin(self, card_pin):
        """Sets the card_pin of this NewCard.


        :param card_pin: The card_pin of this NewCard.
        :type card_pin: str
        """

        self._card_pin = card_pin

    @property
    def eur_ican(self):
        """Gets the eur_ican of this NewCard.


        :return: The eur_ican of this NewCard.
        :rtype: int
        """
        return self._eur_ican

    @eur_ican.setter
    def eur_ican(self, eur_ican):
        """Sets the eur_ican of this NewCard.


        :param eur_ican: The eur_ican of this NewCard.
        :type eur_ican: int
        """

        self._eur_ican = eur_ican

    @property
    def gbp_ican(self):
        """Gets the gbp_ican of this NewCard.


        :return: The gbp_ican of this NewCard.
        :rtype: int
        """
        return self._gbp_ican

    @gbp_ican.setter
    def gbp_ican(self, gbp_ican):
        """Sets the gbp_ican of this NewCard.


        :param gbp_ican: The gbp_ican of this NewCard.
        :type gbp_ican: int
        """

        self._gbp_ican = gbp_ican

    @property
    def user_id(self):
        """Gets the user_id of this NewCard.


        :return: The user_id of this NewCard.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NewCard.


        :param user_id: The user_id of this NewCard.
        :type user_id: int
        """

        self._user_id = user_id
