# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PriceMissingCountDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bandwidth_depleted_count: str=None, cache_rate_missing_count: str=None, itinerary_blocked_count: str=None, live_pricing_error_count: str=None, live_pricing_not_setup_count: str=None, live_pricing_timeout_count: str=None):
        """PriceMissingCountDetails - a model defined in OpenAPI

        :param bandwidth_depleted_count: The bandwidth_depleted_count of this PriceMissingCountDetails.
        :param cache_rate_missing_count: The cache_rate_missing_count of this PriceMissingCountDetails.
        :param itinerary_blocked_count: The itinerary_blocked_count of this PriceMissingCountDetails.
        :param live_pricing_error_count: The live_pricing_error_count of this PriceMissingCountDetails.
        :param live_pricing_not_setup_count: The live_pricing_not_setup_count of this PriceMissingCountDetails.
        :param live_pricing_timeout_count: The live_pricing_timeout_count of this PriceMissingCountDetails.
        """
        self.openapi_types = {
            'bandwidth_depleted_count': str,
            'cache_rate_missing_count': str,
            'itinerary_blocked_count': str,
            'live_pricing_error_count': str,
            'live_pricing_not_setup_count': str,
            'live_pricing_timeout_count': str
        }

        self.attribute_map = {
            'bandwidth_depleted_count': 'bandwidthDepletedCount',
            'cache_rate_missing_count': 'cacheRateMissingCount',
            'itinerary_blocked_count': 'itineraryBlockedCount',
            'live_pricing_error_count': 'livePricingErrorCount',
            'live_pricing_not_setup_count': 'livePricingNotSetupCount',
            'live_pricing_timeout_count': 'livePricingTimeoutCount'
        }

        self._bandwidth_depleted_count = bandwidth_depleted_count
        self._cache_rate_missing_count = cache_rate_missing_count
        self._itinerary_blocked_count = itinerary_blocked_count
        self._live_pricing_error_count = live_pricing_error_count
        self._live_pricing_not_setup_count = live_pricing_not_setup_count
        self._live_pricing_timeout_count = live_pricing_timeout_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PriceMissingCountDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PriceMissingCountDetails of this PriceMissingCountDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bandwidth_depleted_count(self):
        """Gets the bandwidth_depleted_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and there was no live query quota remaining.

        :return: The bandwidth_depleted_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._bandwidth_depleted_count

    @bandwidth_depleted_count.setter
    def bandwidth_depleted_count(self, bandwidth_depleted_count):
        """Sets the bandwidth_depleted_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and there was no live query quota remaining.

        :param bandwidth_depleted_count: The bandwidth_depleted_count of this PriceMissingCountDetails.
        :type bandwidth_depleted_count: str
        """

        self._bandwidth_depleted_count = bandwidth_depleted_count

    @property
    def cache_rate_missing_count(self):
        """Gets the cache_rate_missing_count of this PriceMissingCountDetails.

        No price exists in the cache for this itinerary. A live query was not done due to page constraints.

        :return: The cache_rate_missing_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._cache_rate_missing_count

    @cache_rate_missing_count.setter
    def cache_rate_missing_count(self, cache_rate_missing_count):
        """Sets the cache_rate_missing_count of this PriceMissingCountDetails.

        No price exists in the cache for this itinerary. A live query was not done due to page constraints.

        :param cache_rate_missing_count: The cache_rate_missing_count of this PriceMissingCountDetails.
        :type cache_rate_missing_count: str
        """

        self._cache_rate_missing_count = cache_rate_missing_count

    @property
    def itinerary_blocked_count(self):
        """Gets the itinerary_blocked_count of this PriceMissingCountDetails.

        The itinerary was outside of your basic parameters, so no price was pulled for the itinerary from either live query or cache fill.

        :return: The itinerary_blocked_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._itinerary_blocked_count

    @itinerary_blocked_count.setter
    def itinerary_blocked_count(self, itinerary_blocked_count):
        """Sets the itinerary_blocked_count of this PriceMissingCountDetails.

        The itinerary was outside of your basic parameters, so no price was pulled for the itinerary from either live query or cache fill.

        :param itinerary_blocked_count: The itinerary_blocked_count of this PriceMissingCountDetails.
        :type itinerary_blocked_count: str
        """

        self._itinerary_blocked_count = itinerary_blocked_count

    @property
    def live_pricing_error_count(self):
        """Gets the live_pricing_error_count of this PriceMissingCountDetails.

        No price was cached for this itinerary. A live query did not time out, but your system returned an error.

        :return: The live_pricing_error_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._live_pricing_error_count

    @live_pricing_error_count.setter
    def live_pricing_error_count(self, live_pricing_error_count):
        """Sets the live_pricing_error_count of this PriceMissingCountDetails.

        No price was cached for this itinerary. A live query did not time out, but your system returned an error.

        :param live_pricing_error_count: The live_pricing_error_count of this PriceMissingCountDetails.
        :type live_pricing_error_count: str
        """

        self._live_pricing_error_count = live_pricing_error_count

    @property
    def live_pricing_not_setup_count(self):
        """Gets the live_pricing_not_setup_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and live query was not configured for this account.

        :return: The live_pricing_not_setup_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._live_pricing_not_setup_count

    @live_pricing_not_setup_count.setter
    def live_pricing_not_setup_count(self, live_pricing_not_setup_count):
        """Sets the live_pricing_not_setup_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and live query was not configured for this account.

        :param live_pricing_not_setup_count: The live_pricing_not_setup_count of this PriceMissingCountDetails.
        :type live_pricing_not_setup_count: str
        """

        self._live_pricing_not_setup_count = live_pricing_not_setup_count

    @property
    def live_pricing_timeout_count(self):
        """Gets the live_pricing_timeout_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and a live query sent to your system timed out.

        :return: The live_pricing_timeout_count of this PriceMissingCountDetails.
        :rtype: str
        """
        return self._live_pricing_timeout_count

    @live_pricing_timeout_count.setter
    def live_pricing_timeout_count(self, live_pricing_timeout_count):
        """Sets the live_pricing_timeout_count of this PriceMissingCountDetails.

        No price was cached for this itinerary, and a live query sent to your system timed out.

        :param live_pricing_timeout_count: The live_pricing_timeout_count of this PriceMissingCountDetails.
        :type live_pricing_timeout_count: str
        """

        self._live_pricing_timeout_count = live_pricing_timeout_count
