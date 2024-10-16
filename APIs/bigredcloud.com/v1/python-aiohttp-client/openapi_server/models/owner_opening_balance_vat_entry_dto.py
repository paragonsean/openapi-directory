# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OwnerOpeningBalanceVatEntryDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: float=None, vat_rate_id: int=None):
        """OwnerOpeningBalanceVatEntryDto - a model defined in OpenAPI

        :param amount: The amount of this OwnerOpeningBalanceVatEntryDto.
        :param vat_rate_id: The vat_rate_id of this OwnerOpeningBalanceVatEntryDto.
        """
        self.openapi_types = {
            'amount': float,
            'vat_rate_id': int
        }

        self.attribute_map = {
            'amount': 'amount',
            'vat_rate_id': 'vatRateId'
        }

        self._amount = amount
        self._vat_rate_id = vat_rate_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OwnerOpeningBalanceVatEntryDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OwnerOpeningBalanceVatEntryDto of this OwnerOpeningBalanceVatEntryDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this OwnerOpeningBalanceVatEntryDto.


        :return: The amount of this OwnerOpeningBalanceVatEntryDto.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OwnerOpeningBalanceVatEntryDto.


        :param amount: The amount of this OwnerOpeningBalanceVatEntryDto.
        :type amount: float
        """

        self._amount = amount

    @property
    def vat_rate_id(self):
        """Gets the vat_rate_id of this OwnerOpeningBalanceVatEntryDto.


        :return: The vat_rate_id of this OwnerOpeningBalanceVatEntryDto.
        :rtype: int
        """
        return self._vat_rate_id

    @vat_rate_id.setter
    def vat_rate_id(self, vat_rate_id):
        """Sets the vat_rate_id of this OwnerOpeningBalanceVatEntryDto.


        :param vat_rate_id: The vat_rate_id of this OwnerOpeningBalanceVatEntryDto.
        :type vat_rate_id: int
        """

        self._vat_rate_id = vat_rate_id
