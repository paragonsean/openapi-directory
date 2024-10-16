# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PaymentRefundRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: int=None, refund_amount_available: int=None):
        """PaymentRefundRequest - a model defined in OpenAPI

        :param amount: The amount of this PaymentRefundRequest.
        :param refund_amount_available: The refund_amount_available of this PaymentRefundRequest.
        """
        self.openapi_types = {
            'amount': int,
            'refund_amount_available': int
        }

        self.attribute_map = {
            'amount': 'amount',
            'refund_amount_available': 'refund_amount_available'
        }

        self._amount = amount
        self._refund_amount_available = refund_amount_available

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentRefundRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaymentRefundRequest of this PaymentRefundRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this PaymentRefundRequest.

        Amount in pence. Can't be more than the available amount for refunds

        :return: The amount of this PaymentRefundRequest.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRefundRequest.

        Amount in pence. Can't be more than the available amount for refunds

        :param amount: The amount of this PaymentRefundRequest.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        if amount is not None and amount > 10000000:
            raise ValueError("Invalid value for `amount`, must be a value less than or equal to `10000000`")
        if amount is not None and amount < 1:
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `1`")

        self._amount = amount

    @property
    def refund_amount_available(self):
        """Gets the refund_amount_available of this PaymentRefundRequest.

        Amount in pence. Total amount still available before issuing the refund

        :return: The refund_amount_available of this PaymentRefundRequest.
        :rtype: int
        """
        return self._refund_amount_available

    @refund_amount_available.setter
    def refund_amount_available(self, refund_amount_available):
        """Sets the refund_amount_available of this PaymentRefundRequest.

        Amount in pence. Total amount still available before issuing the refund

        :param refund_amount_available: The refund_amount_available of this PaymentRefundRequest.
        :type refund_amount_available: int
        """
        if refund_amount_available is not None and refund_amount_available > 10000000:
            raise ValueError("Invalid value for `refund_amount_available`, must be a value less than or equal to `10000000`")
        if refund_amount_available is not None and refund_amount_available < 1:
            raise ValueError("Invalid value for `refund_amount_available`, must be a value greater than or equal to `1`")

        self._refund_amount_available = refund_amount_available
