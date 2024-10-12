# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NewPaymentAllocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allocation_amount: float=None, allocation_date: datetime=None, invoice_transaction_idfk: int=None):
        """NewPaymentAllocation - a model defined in OpenAPI

        :param allocation_amount: The allocation_amount of this NewPaymentAllocation.
        :param allocation_date: The allocation_date of this NewPaymentAllocation.
        :param invoice_transaction_idfk: The invoice_transaction_idfk of this NewPaymentAllocation.
        """
        self.openapi_types = {
            'allocation_amount': float,
            'allocation_date': datetime,
            'invoice_transaction_idfk': int
        }

        self.attribute_map = {
            'allocation_amount': 'AllocationAmount',
            'allocation_date': 'AllocationDate',
            'invoice_transaction_idfk': 'InvoiceTransactionIDFK'
        }

        self._allocation_amount = allocation_amount
        self._allocation_date = allocation_date
        self._invoice_transaction_idfk = invoice_transaction_idfk

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NewPaymentAllocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NewPaymentAllocation of this NewPaymentAllocation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allocation_amount(self):
        """Gets the allocation_amount of this NewPaymentAllocation.

        The Amount being allocated to the invoice. Expects same currency as invoice currency

        :return: The allocation_amount of this NewPaymentAllocation.
        :rtype: float
        """
        return self._allocation_amount

    @allocation_amount.setter
    def allocation_amount(self, allocation_amount):
        """Sets the allocation_amount of this NewPaymentAllocation.

        The Amount being allocated to the invoice. Expects same currency as invoice currency

        :param allocation_amount: The allocation_amount of this NewPaymentAllocation.
        :type allocation_amount: float
        """

        self._allocation_amount = allocation_amount

    @property
    def allocation_date(self):
        """Gets the allocation_date of this NewPaymentAllocation.

        Optional. Defaults to the current time in the Avaza account's timezone. The date the allocation is applied to the invoice. Can be difference from the Payment Date when doing prepayments etc.

        :return: The allocation_date of this NewPaymentAllocation.
        :rtype: datetime
        """
        return self._allocation_date

    @allocation_date.setter
    def allocation_date(self, allocation_date):
        """Sets the allocation_date of this NewPaymentAllocation.

        Optional. Defaults to the current time in the Avaza account's timezone. The date the allocation is applied to the invoice. Can be difference from the Payment Date when doing prepayments etc.

        :param allocation_date: The allocation_date of this NewPaymentAllocation.
        :type allocation_date: datetime
        """

        self._allocation_date = allocation_date

    @property
    def invoice_transaction_idfk(self):
        """Gets the invoice_transaction_idfk of this NewPaymentAllocation.

        The Avaza Invoice TransactionID that is having a payment amount allocated to it.

        :return: The invoice_transaction_idfk of this NewPaymentAllocation.
        :rtype: int
        """
        return self._invoice_transaction_idfk

    @invoice_transaction_idfk.setter
    def invoice_transaction_idfk(self, invoice_transaction_idfk):
        """Sets the invoice_transaction_idfk of this NewPaymentAllocation.

        The Avaza Invoice TransactionID that is having a payment amount allocated to it.

        :param invoice_transaction_idfk: The invoice_transaction_idfk of this NewPaymentAllocation.
        :type invoice_transaction_idfk: int
        """

        self._invoice_transaction_idfk = invoice_transaction_idfk
