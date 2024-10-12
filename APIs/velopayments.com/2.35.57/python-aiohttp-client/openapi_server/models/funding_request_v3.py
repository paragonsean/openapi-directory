# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FundingRequestV3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: int=None, funding_account_id: str=None):
        """FundingRequestV3 - a model defined in OpenAPI

        :param amount: The amount of this FundingRequestV3.
        :param funding_account_id: The funding_account_id of this FundingRequestV3.
        """
        self.openapi_types = {
            'amount': int,
            'funding_account_id': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'funding_account_id': 'fundingAccountId'
        }

        self._amount = amount
        self._funding_account_id = funding_account_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FundingRequestV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FundingRequestV3 of this FundingRequestV3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this FundingRequestV3.

        Amount to fund in minor units

        :return: The amount of this FundingRequestV3.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FundingRequestV3.

        Amount to fund in minor units

        :param amount: The amount of this FundingRequestV3.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        if amount is not None and amount > 9999999999:
            raise ValueError("Invalid value for `amount`, must be a value less than or equal to `9999999999`")
        if amount is not None and amount < 1:
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `1`")

        self._amount = amount

    @property
    def funding_account_id(self):
        """Gets the funding_account_id of this FundingRequestV3.

        The funding account id

        :return: The funding_account_id of this FundingRequestV3.
        :rtype: str
        """
        return self._funding_account_id

    @funding_account_id.setter
    def funding_account_id(self, funding_account_id):
        """Sets the funding_account_id of this FundingRequestV3.

        The funding account id

        :param funding_account_id: The funding_account_id of this FundingRequestV3.
        :type funding_account_id: str
        """
        if funding_account_id is None:
            raise ValueError("Invalid value for `funding_account_id`, must not be `None`")

        self._funding_account_id = funding_account_id
