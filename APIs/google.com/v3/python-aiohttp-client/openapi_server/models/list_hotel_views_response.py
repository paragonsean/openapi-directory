# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.hotel_view import HotelView
from openapi_server import util


class ListHotelViewsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hotel_views: List[HotelView]=None, next_page_token: str=None):
        """ListHotelViewsResponse - a model defined in OpenAPI

        :param hotel_views: The hotel_views of this ListHotelViewsResponse.
        :param next_page_token: The next_page_token of this ListHotelViewsResponse.
        """
        self.openapi_types = {
            'hotel_views': List[HotelView],
            'next_page_token': str
        }

        self.attribute_map = {
            'hotel_views': 'hotelViews',
            'next_page_token': 'nextPageToken'
        }

        self._hotel_views = hotel_views
        self._next_page_token = next_page_token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListHotelViewsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListHotelViewsResponse of this ListHotelViewsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hotel_views(self):
        """Gets the hotel_views of this ListHotelViewsResponse.

        The list of rows that match the query.

        :return: The hotel_views of this ListHotelViewsResponse.
        :rtype: List[HotelView]
        """
        return self._hotel_views

    @hotel_views.setter
    def hotel_views(self, hotel_views):
        """Sets the hotel_views of this ListHotelViewsResponse.

        The list of rows that match the query.

        :param hotel_views: The hotel_views of this ListHotelViewsResponse.
        :type hotel_views: List[HotelView]
        """

        self._hotel_views = hotel_views

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ListHotelViewsResponse.

        Pagination token used to retrieve the next page of results.

        :return: The next_page_token of this ListHotelViewsResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ListHotelViewsResponse.

        Pagination token used to retrieve the next page of results.

        :param next_page_token: The next_page_token of this ListHotelViewsResponse.
        :type next_page_token: str
        """

        self._next_page_token = next_page_token
