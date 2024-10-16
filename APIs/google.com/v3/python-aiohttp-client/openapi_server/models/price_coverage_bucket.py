# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PriceCoverageBucket(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, advance_booking_window_range: str=None, available_price_count: str=None, length_of_stay_range: str=None, price_coverage_percent: float=None):
        """PriceCoverageBucket - a model defined in OpenAPI

        :param advance_booking_window_range: The advance_booking_window_range of this PriceCoverageBucket.
        :param available_price_count: The available_price_count of this PriceCoverageBucket.
        :param length_of_stay_range: The length_of_stay_range of this PriceCoverageBucket.
        :param price_coverage_percent: The price_coverage_percent of this PriceCoverageBucket.
        """
        self.openapi_types = {
            'advance_booking_window_range': str,
            'available_price_count': str,
            'length_of_stay_range': str,
            'price_coverage_percent': float
        }

        self.attribute_map = {
            'advance_booking_window_range': 'advanceBookingWindowRange',
            'available_price_count': 'availablePriceCount',
            'length_of_stay_range': 'lengthOfStayRange',
            'price_coverage_percent': 'priceCoveragePercent'
        }

        self._advance_booking_window_range = advance_booking_window_range
        self._available_price_count = available_price_count
        self._length_of_stay_range = length_of_stay_range
        self._price_coverage_percent = price_coverage_percent

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PriceCoverageBucket':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PriceCoverageBucket of this PriceCoverageBucket.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def advance_booking_window_range(self):
        """Gets the advance_booking_window_range of this PriceCoverageBucket.

        Advance booking window range.

        :return: The advance_booking_window_range of this PriceCoverageBucket.
        :rtype: str
        """
        return self._advance_booking_window_range

    @advance_booking_window_range.setter
    def advance_booking_window_range(self, advance_booking_window_range):
        """Sets the advance_booking_window_range of this PriceCoverageBucket.

        Advance booking window range.

        :param advance_booking_window_range: The advance_booking_window_range of this PriceCoverageBucket.
        :type advance_booking_window_range: str
        """
        allowed_values = ["ADVANCE_BOOKING_WINDOW_RANGE_UNSPECIFIED", "ADVANCE_BOOKING_WINDOW_RANGE_UNKNOWN", "DAYS_0_TO_30", "DAYS_31_TO_60", "DAYS_61_TO_90", "DAYS_91_TO_120", "DAYS_121_TO_150", "DAYS_151_TO_180", "DAYS_181_TO_210", "DAYS_211_TO_240", "DAYS_241_TO_270", "DAYS_271_TO_300", "DAYS_301_TO_330"]  # noqa: E501
        if advance_booking_window_range not in allowed_values:
            raise ValueError(
                "Invalid value for `advance_booking_window_range` ({0}), must be one of {1}"
                .format(advance_booking_window_range, allowed_values)
            )

        self._advance_booking_window_range = advance_booking_window_range

    @property
    def available_price_count(self):
        """Gets the available_price_count of this PriceCoverageBucket.

        Number of prices for this advance booking window bucket and length of stay bucket.

        :return: The available_price_count of this PriceCoverageBucket.
        :rtype: str
        """
        return self._available_price_count

    @available_price_count.setter
    def available_price_count(self, available_price_count):
        """Sets the available_price_count of this PriceCoverageBucket.

        Number of prices for this advance booking window bucket and length of stay bucket.

        :param available_price_count: The available_price_count of this PriceCoverageBucket.
        :type available_price_count: str
        """

        self._available_price_count = available_price_count

    @property
    def length_of_stay_range(self):
        """Gets the length_of_stay_range of this PriceCoverageBucket.

        Length of stay range.

        :return: The length_of_stay_range of this PriceCoverageBucket.
        :rtype: str
        """
        return self._length_of_stay_range

    @length_of_stay_range.setter
    def length_of_stay_range(self, length_of_stay_range):
        """Sets the length_of_stay_range of this PriceCoverageBucket.

        Length of stay range.

        :param length_of_stay_range: The length_of_stay_range of this PriceCoverageBucket.
        :type length_of_stay_range: str
        """
        allowed_values = ["LENGTH_OF_STAY_RANGE_UNSPECIFIED", "LENGTH_OF_STAY_RANGE_UNKNOWN", "LENGTH_OF_STAY_1_TO_7", "LENGTH_OF_STAY_8_TO_14", "LENGTH_OF_STAY_15_TO_30"]  # noqa: E501
        if length_of_stay_range not in allowed_values:
            raise ValueError(
                "Invalid value for `length_of_stay_range` ({0}), must be one of {1}"
                .format(length_of_stay_range, allowed_values)
            )

        self._length_of_stay_range = length_of_stay_range

    @property
    def price_coverage_percent(self):
        """Gets the price_coverage_percent of this PriceCoverageBucket.

        The percent of itineraries for which you have coverage for this advance booking window bucket and length of stay bucket.

        :return: The price_coverage_percent of this PriceCoverageBucket.
        :rtype: float
        """
        return self._price_coverage_percent

    @price_coverage_percent.setter
    def price_coverage_percent(self, price_coverage_percent):
        """Sets the price_coverage_percent of this PriceCoverageBucket.

        The percent of itineraries for which you have coverage for this advance booking window bucket and length of stay bucket.

        :param price_coverage_percent: The price_coverage_percent of this PriceCoverageBucket.
        :type price_coverage_percent: float
        """

        self._price_coverage_percent = price_coverage_percent
