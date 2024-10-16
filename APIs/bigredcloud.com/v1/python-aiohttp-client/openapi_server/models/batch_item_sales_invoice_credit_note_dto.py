# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sales_invoice_credit_note_dto import SalesInvoiceCreditNoteDto
from openapi_server import util


class BatchItemSalesInvoiceCreditNoteDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, item: SalesInvoiceCreditNoteDto=None, op_code: int=None):
        """BatchItemSalesInvoiceCreditNoteDto - a model defined in OpenAPI

        :param item: The item of this BatchItemSalesInvoiceCreditNoteDto.
        :param op_code: The op_code of this BatchItemSalesInvoiceCreditNoteDto.
        """
        self.openapi_types = {
            'item': SalesInvoiceCreditNoteDto,
            'op_code': int
        }

        self.attribute_map = {
            'item': 'item',
            'op_code': 'opCode'
        }

        self._item = item
        self._op_code = op_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BatchItemSalesInvoiceCreditNoteDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BatchItem_SalesInvoiceCreditNoteDto_ of this BatchItemSalesInvoiceCreditNoteDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item(self):
        """Gets the item of this BatchItemSalesInvoiceCreditNoteDto.


        :return: The item of this BatchItemSalesInvoiceCreditNoteDto.
        :rtype: SalesInvoiceCreditNoteDto
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this BatchItemSalesInvoiceCreditNoteDto.


        :param item: The item of this BatchItemSalesInvoiceCreditNoteDto.
        :type item: SalesInvoiceCreditNoteDto
        """

        self._item = item

    @property
    def op_code(self):
        """Gets the op_code of this BatchItemSalesInvoiceCreditNoteDto.

        1 - Create  2 - Update  3 - Delete

        :return: The op_code of this BatchItemSalesInvoiceCreditNoteDto.
        :rtype: int
        """
        return self._op_code

    @op_code.setter
    def op_code(self, op_code):
        """Sets the op_code of this BatchItemSalesInvoiceCreditNoteDto.

        1 - Create  2 - Update  3 - Delete

        :param op_code: The op_code of this BatchItemSalesInvoiceCreditNoteDto.
        :type op_code: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if op_code not in allowed_values:
            raise ValueError(
                "Invalid value for `op_code` ({0}), must be one of {1}"
                .format(op_code, allowed_values)
            )

        self._op_code = op_code
