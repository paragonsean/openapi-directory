# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sales_credit_note_query_dto import SalesCreditNoteQueryDto
from openapi_server import util


class PageResultSalesCreditNoteQueryDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, items: List[SalesCreditNoteQueryDto]=None, next_page_link: str=None):
        """PageResultSalesCreditNoteQueryDto - a model defined in OpenAPI

        :param count: The count of this PageResultSalesCreditNoteQueryDto.
        :param items: The items of this PageResultSalesCreditNoteQueryDto.
        :param next_page_link: The next_page_link of this PageResultSalesCreditNoteQueryDto.
        """
        self.openapi_types = {
            'count': int,
            'items': List[SalesCreditNoteQueryDto],
            'next_page_link': str
        }

        self.attribute_map = {
            'count': 'Count',
            'items': 'Items',
            'next_page_link': 'NextPageLink'
        }

        self._count = count
        self._items = items
        self._next_page_link = next_page_link

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PageResultSalesCreditNoteQueryDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PageResult_SalesCreditNoteQueryDto_ of this PageResultSalesCreditNoteQueryDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this PageResultSalesCreditNoteQueryDto.


        :return: The count of this PageResultSalesCreditNoteQueryDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PageResultSalesCreditNoteQueryDto.


        :param count: The count of this PageResultSalesCreditNoteQueryDto.
        :type count: int
        """

        self._count = count

    @property
    def items(self):
        """Gets the items of this PageResultSalesCreditNoteQueryDto.


        :return: The items of this PageResultSalesCreditNoteQueryDto.
        :rtype: List[SalesCreditNoteQueryDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageResultSalesCreditNoteQueryDto.


        :param items: The items of this PageResultSalesCreditNoteQueryDto.
        :type items: List[SalesCreditNoteQueryDto]
        """

        self._items = items

    @property
    def next_page_link(self):
        """Gets the next_page_link of this PageResultSalesCreditNoteQueryDto.


        :return: The next_page_link of this PageResultSalesCreditNoteQueryDto.
        :rtype: str
        """
        return self._next_page_link

    @next_page_link.setter
    def next_page_link(self, next_page_link):
        """Sets the next_page_link of this PageResultSalesCreditNoteQueryDto.


        :param next_page_link: The next_page_link of this PageResultSalesCreditNoteQueryDto.
        :type next_page_link: str
        """

        self._next_page_link = next_page_link
