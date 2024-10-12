# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NewBillPaymentAllocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allocation_amount: float=None, allocation_date: datetime=None, bill_transaction_idfk: int=None):
        """NewBillPaymentAllocation - a model defined in OpenAPI

        :param allocation_amount: The allocation_amount of this NewBillPaymentAllocation.
        :param allocation_date: The allocation_date of this NewBillPaymentAllocation.
        :param bill_transaction_idfk: The bill_transaction_idfk of this NewBillPaymentAllocation.
        """
        self.openapi_types = {
            'allocation_amount': float,
            'allocation_date': datetime,
            'bill_transaction_idfk': int
        }

        self.attribute_map = {
            'allocation_amount': 'AllocationAmount',
            'allocation_date': 'AllocationDate',
            'bill_transaction_idfk': 'BillTransactionIDFK'
        }

        self._allocation_amount = allocation_amount
        self._allocation_date = allocation_date
        self._bill_transaction_idfk = bill_transaction_idfk

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NewBillPaymentAllocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NewBillPaymentAllocation of this NewBillPaymentAllocation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allocation_amount(self):
        """Gets the allocation_amount of this NewBillPaymentAllocation.

        The Amount being allocated to the bill. Expects same currency as bill currency

        :return: The allocation_amount of this NewBillPaymentAllocation.
        :rtype: float
        """
        return self._allocation_amount

    @allocation_amount.setter
    def allocation_amount(self, allocation_amount):
        """Sets the allocation_amount of this NewBillPaymentAllocation.

        The Amount being allocated to the bill. Expects same currency as bill currency

        :param allocation_amount: The allocation_amount of this NewBillPaymentAllocation.
        :type allocation_amount: float
        """

        self._allocation_amount = allocation_amount

    @property
    def allocation_date(self):
        """Gets the allocation_date of this NewBillPaymentAllocation.

        Optional. Defaults to the current time in the Avaza account's timezone. The date the allocation is applied to the bill. Can be different from the Payment Date when doing prepayments etc.

        :return: The allocation_date of this NewBillPaymentAllocation.
        :rtype: datetime
        """
        return self._allocation_date

    @allocation_date.setter
    def allocation_date(self, allocation_date):
        """Sets the allocation_date of this NewBillPaymentAllocation.

        Optional. Defaults to the current time in the Avaza account's timezone. The date the allocation is applied to the bill. Can be different from the Payment Date when doing prepayments etc.

        :param allocation_date: The allocation_date of this NewBillPaymentAllocation.
        :type allocation_date: datetime
        """

        self._allocation_date = allocation_date

    @property
    def bill_transaction_idfk(self):
        """Gets the bill_transaction_idfk of this NewBillPaymentAllocation.

        The Avaza Bill TransactionID that is having a payment amount allocated to it.

        :return: The bill_transaction_idfk of this NewBillPaymentAllocation.
        :rtype: int
        """
        return self._bill_transaction_idfk

    @bill_transaction_idfk.setter
    def bill_transaction_idfk(self, bill_transaction_idfk):
        """Sets the bill_transaction_idfk of this NewBillPaymentAllocation.

        The Avaza Bill TransactionID that is having a payment amount allocated to it.

        :param bill_transaction_idfk: The bill_transaction_idfk of this NewBillPaymentAllocation.
        :type bill_transaction_idfk: int
        """

        self._bill_transaction_idfk = bill_transaction_idfk
