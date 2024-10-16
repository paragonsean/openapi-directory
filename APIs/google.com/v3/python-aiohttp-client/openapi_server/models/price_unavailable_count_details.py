# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PriceUnavailableCountDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, participation_not_likely_count: str=None, price_unavailable_count: str=None):
        """PriceUnavailableCountDetails - a model defined in OpenAPI

        :param participation_not_likely_count: The participation_not_likely_count of this PriceUnavailableCountDetails.
        :param price_unavailable_count: The price_unavailable_count of this PriceUnavailableCountDetails.
        """
        self.openapi_types = {
            'participation_not_likely_count': str,
            'price_unavailable_count': str
        }

        self.attribute_map = {
            'participation_not_likely_count': 'participationNotLikelyCount',
            'price_unavailable_count': 'priceUnavailableCount'
        }

        self._participation_not_likely_count = participation_not_likely_count
        self._price_unavailable_count = price_unavailable_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PriceUnavailableCountDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PriceUnavailableCountDetails of this PriceUnavailableCountDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def participation_not_likely_count(self):
        """Gets the participation_not_likely_count of this PriceUnavailableCountDetails.

        No price was cached for this itinerary, and no live query was done because your server usually tells us the hotel is unavailable or sold out.

        :return: The participation_not_likely_count of this PriceUnavailableCountDetails.
        :rtype: str
        """
        return self._participation_not_likely_count

    @participation_not_likely_count.setter
    def participation_not_likely_count(self, participation_not_likely_count):
        """Sets the participation_not_likely_count of this PriceUnavailableCountDetails.

        No price was cached for this itinerary, and no live query was done because your server usually tells us the hotel is unavailable or sold out.

        :param participation_not_likely_count: The participation_not_likely_count of this PriceUnavailableCountDetails.
        :type participation_not_likely_count: str
        """

        self._participation_not_likely_count = participation_not_likely_count

    @property
    def price_unavailable_count(self):
        """Gets the price_unavailable_count of this PriceUnavailableCountDetails.

        Hotel did not participate because it wasn't available for the itinerary dates.

        :return: The price_unavailable_count of this PriceUnavailableCountDetails.
        :rtype: str
        """
        return self._price_unavailable_count

    @price_unavailable_count.setter
    def price_unavailable_count(self, price_unavailable_count):
        """Sets the price_unavailable_count of this PriceUnavailableCountDetails.

        Hotel did not participate because it wasn't available for the itinerary dates.

        :param price_unavailable_count: The price_unavailable_count of this PriceUnavailableCountDetails.
        :type price_unavailable_count: str
        """

        self._price_unavailable_count = price_unavailable_count
