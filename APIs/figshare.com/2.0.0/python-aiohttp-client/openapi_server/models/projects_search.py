# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProjectsSearch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order: str='published_date', group: int=None, institution: int=None, limit: int=None, modified_since: str=None, offset: int=None, order_direction: str='desc', page: int=None, page_size: int=10, published_since: str=None, search_for: str=None):
        """ProjectsSearch - a model defined in OpenAPI

        :param order: The order of this ProjectsSearch.
        :param group: The group of this ProjectsSearch.
        :param institution: The institution of this ProjectsSearch.
        :param limit: The limit of this ProjectsSearch.
        :param modified_since: The modified_since of this ProjectsSearch.
        :param offset: The offset of this ProjectsSearch.
        :param order_direction: The order_direction of this ProjectsSearch.
        :param page: The page of this ProjectsSearch.
        :param page_size: The page_size of this ProjectsSearch.
        :param published_since: The published_since of this ProjectsSearch.
        :param search_for: The search_for of this ProjectsSearch.
        """
        self.openapi_types = {
            'order': str,
            'group': int,
            'institution': int,
            'limit': int,
            'modified_since': str,
            'offset': int,
            'order_direction': str,
            'page': int,
            'page_size': int,
            'published_since': str,
            'search_for': str
        }

        self.attribute_map = {
            'order': 'order',
            'group': 'group',
            'institution': 'institution',
            'limit': 'limit',
            'modified_since': 'modified_since',
            'offset': 'offset',
            'order_direction': 'order_direction',
            'page': 'page',
            'page_size': 'page_size',
            'published_since': 'published_since',
            'search_for': 'search_for'
        }

        self._order = order
        self._group = group
        self._institution = institution
        self._limit = limit
        self._modified_since = modified_since
        self._offset = offset
        self._order_direction = order_direction
        self._page = page
        self._page_size = page_size
        self._published_since = published_since
        self._search_for = search_for

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectsSearch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectsSearch of this ProjectsSearch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order(self):
        """Gets the order of this ProjectsSearch.

        The field by which to order.

        :return: The order of this ProjectsSearch.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ProjectsSearch.

        The field by which to order.

        :param order: The order of this ProjectsSearch.
        :type order: str
        """
        allowed_values = ["published_date", "modified_date", "views"]  # noqa: E501
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def group(self):
        """Gets the group of this ProjectsSearch.

        only return collections from this group

        :return: The group of this ProjectsSearch.
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProjectsSearch.

        only return collections from this group

        :param group: The group of this ProjectsSearch.
        :type group: int
        """

        self._group = group

    @property
    def institution(self):
        """Gets the institution of this ProjectsSearch.

        only return collections from this institution

        :return: The institution of this ProjectsSearch.
        :rtype: int
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this ProjectsSearch.

        only return collections from this institution

        :param institution: The institution of this ProjectsSearch.
        :type institution: int
        """

        self._institution = institution

    @property
    def limit(self):
        """Gets the limit of this ProjectsSearch.

        Number of results included on a page. Used for pagination with query

        :return: The limit of this ProjectsSearch.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ProjectsSearch.

        Number of results included on a page. Used for pagination with query

        :param limit: The limit of this ProjectsSearch.
        :type limit: int
        """
        if limit is not None and limit > 1000:
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `1000`")
        if limit is not None and limit < 1:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1`")

        self._limit = limit

    @property
    def modified_since(self):
        """Gets the modified_since of this ProjectsSearch.

        Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :return: The modified_since of this ProjectsSearch.
        :rtype: str
        """
        return self._modified_since

    @modified_since.setter
    def modified_since(self, modified_since):
        """Sets the modified_since of this ProjectsSearch.

        Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :param modified_since: The modified_since of this ProjectsSearch.
        :type modified_since: str
        """

        self._modified_since = modified_since

    @property
    def offset(self):
        """Gets the offset of this ProjectsSearch.

        Where to start the listing(the offset of the first result). Used for pagination with limit

        :return: The offset of this ProjectsSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ProjectsSearch.

        Where to start the listing(the offset of the first result). Used for pagination with limit

        :param offset: The offset of this ProjectsSearch.
        :type offset: int
        """
        if offset is not None and offset > 5000:
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `5000`")
        if offset is not None and offset < 0:
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")

        self._offset = offset

    @property
    def order_direction(self):
        """Gets the order_direction of this ProjectsSearch.

        Direction of ordering

        :return: The order_direction of this ProjectsSearch.
        :rtype: str
        """
        return self._order_direction

    @order_direction.setter
    def order_direction(self, order_direction):
        """Sets the order_direction of this ProjectsSearch.

        Direction of ordering

        :param order_direction: The order_direction of this ProjectsSearch.
        :type order_direction: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if order_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `order_direction` ({0}), must be one of {1}"
                .format(order_direction, allowed_values)
            )

        self._order_direction = order_direction

    @property
    def page(self):
        """Gets the page of this ProjectsSearch.

        Page number. Used for pagination with page_size

        :return: The page of this ProjectsSearch.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ProjectsSearch.

        Page number. Used for pagination with page_size

        :param page: The page of this ProjectsSearch.
        :type page: int
        """
        if page is not None and page > 5000:
            raise ValueError("Invalid value for `page`, must be a value less than or equal to `5000`")
        if page is not None and page < 1:
            raise ValueError("Invalid value for `page`, must be a value greater than or equal to `1`")

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ProjectsSearch.

        The number of results included on a page. Used for pagination with page

        :return: The page_size of this ProjectsSearch.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ProjectsSearch.

        The number of results included on a page. Used for pagination with page

        :param page_size: The page_size of this ProjectsSearch.
        :type page_size: int
        """
        if page_size is not None and page_size > 1000:
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `1000`")
        if page_size is not None and page_size < 1:
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")

        self._page_size = page_size

    @property
    def published_since(self):
        """Gets the published_since of this ProjectsSearch.

        Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :return: The published_since of this ProjectsSearch.
        :rtype: str
        """
        return self._published_since

    @published_since.setter
    def published_since(self, published_since):
        """Sets the published_since of this ProjectsSearch.

        Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :param published_since: The published_since of this ProjectsSearch.
        :type published_since: str
        """

        self._published_since = published_since

    @property
    def search_for(self):
        """Gets the search_for of this ProjectsSearch.

        Search term

        :return: The search_for of this ProjectsSearch.
        :rtype: str
        """
        return self._search_for

    @search_for.setter
    def search_for(self, search_for):
        """Sets the search_for of this ProjectsSearch.

        Search term

        :param search_for: The search_for of this ProjectsSearch.
        :type search_for: str
        """

        self._search_for = search_for
