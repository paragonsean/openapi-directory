# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.quote_dto import QuoteDto
from openapi_server import util


class PageResultQuoteDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, items: List[QuoteDto]=None, next_page_link: str=None):
        """PageResultQuoteDto - a model defined in OpenAPI

        :param count: The count of this PageResultQuoteDto.
        :param items: The items of this PageResultQuoteDto.
        :param next_page_link: The next_page_link of this PageResultQuoteDto.
        """
        self.openapi_types = {
            'count': int,
            'items': List[QuoteDto],
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
    def from_dict(cls, dikt: dict) -> 'PageResultQuoteDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PageResult_QuoteDto_ of this PageResultQuoteDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this PageResultQuoteDto.


        :return: The count of this PageResultQuoteDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PageResultQuoteDto.


        :param count: The count of this PageResultQuoteDto.
        :type count: int
        """

        self._count = count

    @property
    def items(self):
        """Gets the items of this PageResultQuoteDto.


        :return: The items of this PageResultQuoteDto.
        :rtype: List[QuoteDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageResultQuoteDto.


        :param items: The items of this PageResultQuoteDto.
        :type items: List[QuoteDto]
        """

        self._items = items

    @property
    def next_page_link(self):
        """Gets the next_page_link of this PageResultQuoteDto.


        :return: The next_page_link of this PageResultQuoteDto.
        :rtype: str
        """
        return self._next_page_link

    @next_page_link.setter
    def next_page_link(self, next_page_link):
        """Sets the next_page_link of this PageResultQuoteDto.


        :param next_page_link: The next_page_link of this PageResultQuoteDto.
        :type next_page_link: str
        """

        self._next_page_link = next_page_link
