# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PaymentDataPaymentAdditionalInfoInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, value: str=None):
        """PaymentDataPaymentAdditionalInfoInterface - a model defined in OpenAPI

        :param key: The key of this PaymentDataPaymentAdditionalInfoInterface.
        :param value: The value of this PaymentDataPaymentAdditionalInfoInterface.
        """
        self.openapi_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentDataPaymentAdditionalInfoInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The payment-data-payment-additional-info-interface of this PaymentDataPaymentAdditionalInfoInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this PaymentDataPaymentAdditionalInfoInterface.

        Object key

        :return: The key of this PaymentDataPaymentAdditionalInfoInterface.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PaymentDataPaymentAdditionalInfoInterface.

        Object key

        :param key: The key of this PaymentDataPaymentAdditionalInfoInterface.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def value(self):
        """Gets the value of this PaymentDataPaymentAdditionalInfoInterface.

        Object value

        :return: The value of this PaymentDataPaymentAdditionalInfoInterface.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PaymentDataPaymentAdditionalInfoInterface.

        Object value

        :param value: The value of this PaymentDataPaymentAdditionalInfoInterface.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
