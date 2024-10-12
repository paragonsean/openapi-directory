# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.price_accuracy_view import PriceAccuracyView
from openapi_server import util


class ListPriceAccuracyViewsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, price_accuracy_views: List[PriceAccuracyView]=None):
        """ListPriceAccuracyViewsResponse - a model defined in OpenAPI

        :param price_accuracy_views: The price_accuracy_views of this ListPriceAccuracyViewsResponse.
        """
        self.openapi_types = {
            'price_accuracy_views': List[PriceAccuracyView]
        }

        self.attribute_map = {
            'price_accuracy_views': 'priceAccuracyViews'
        }

        self._price_accuracy_views = price_accuracy_views

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListPriceAccuracyViewsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListPriceAccuracyViewsResponse of this ListPriceAccuracyViewsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def price_accuracy_views(self):
        """Gets the price_accuracy_views of this ListPriceAccuracyViewsResponse.

        The list of rows that match the query.

        :return: The price_accuracy_views of this ListPriceAccuracyViewsResponse.
        :rtype: List[PriceAccuracyView]
        """
        return self._price_accuracy_views

    @price_accuracy_views.setter
    def price_accuracy_views(self, price_accuracy_views):
        """Sets the price_accuracy_views of this ListPriceAccuracyViewsResponse.

        The list of rows that match the query.

        :param price_accuracy_views: The price_accuracy_views of this ListPriceAccuracyViewsResponse.
        :type price_accuracy_views: List[PriceAccuracyView]
        """

        self._price_accuracy_views = price_accuracy_views
