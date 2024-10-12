# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SearchRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order: str=None, order_by: str=None, page: int=None, page_size: int=None, query: str=None):
        """SearchRequest - a model defined in OpenAPI

        :param order: The order of this SearchRequest.
        :param order_by: The order_by of this SearchRequest.
        :param page: The page of this SearchRequest.
        :param page_size: The page_size of this SearchRequest.
        :param query: The query of this SearchRequest.
        """
        self.openapi_types = {
            'order': str,
            'order_by': str,
            'page': int,
            'page_size': int,
            'query': str
        }

        self.attribute_map = {
            'order': 'Order',
            'order_by': 'OrderBy',
            'page': 'Page',
            'page_size': 'PageSize',
            'query': 'Query'
        }

        self._order = order
        self._order_by = order_by
        self._page = page
        self._page_size = page_size
        self._query = query

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SearchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SearchRequest of this SearchRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order(self):
        """Gets the order of this SearchRequest.


        :return: The order of this SearchRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this SearchRequest.


        :param order: The order of this SearchRequest.
        :type order: str
        """
        allowed_values = ["None", "Asc", "Desc"]  # noqa: E501
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def order_by(self):
        """Gets the order_by of this SearchRequest.


        :return: The order_by of this SearchRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this SearchRequest.


        :param order_by: The order_by of this SearchRequest.
        :type order_by: str
        """

        self._order_by = order_by

    @property
    def page(self):
        """Gets the page of this SearchRequest.


        :return: The page of this SearchRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SearchRequest.


        :param page: The page of this SearchRequest.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this SearchRequest.


        :return: The page_size of this SearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchRequest.


        :param page_size: The page_size of this SearchRequest.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def query(self):
        """Gets the query of this SearchRequest.


        :return: The query of this SearchRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchRequest.


        :param query: The query of this SearchRequest.
        :type query: str
        """

        self._query = query
