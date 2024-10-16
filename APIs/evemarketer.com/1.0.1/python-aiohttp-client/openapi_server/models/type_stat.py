# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.for_query import ForQuery
from openapi_server import util


class TypeStat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, avg: float=None, five_percent: float=None, for_query: ForQuery=None, generated: int=None, high_to_low: bool=None, max: float=None, median: float=None, min: float=None, std_dev: float=None, variance: float=None, volume: int=None, wavg: float=None):
        """TypeStat - a model defined in OpenAPI

        :param avg: The avg of this TypeStat.
        :param five_percent: The five_percent of this TypeStat.
        :param for_query: The for_query of this TypeStat.
        :param generated: The generated of this TypeStat.
        :param high_to_low: The high_to_low of this TypeStat.
        :param max: The max of this TypeStat.
        :param median: The median of this TypeStat.
        :param min: The min of this TypeStat.
        :param std_dev: The std_dev of this TypeStat.
        :param variance: The variance of this TypeStat.
        :param volume: The volume of this TypeStat.
        :param wavg: The wavg of this TypeStat.
        """
        self.openapi_types = {
            'avg': float,
            'five_percent': float,
            'for_query': ForQuery,
            'generated': int,
            'high_to_low': bool,
            'max': float,
            'median': float,
            'min': float,
            'std_dev': float,
            'variance': float,
            'volume': int,
            'wavg': float
        }

        self.attribute_map = {
            'avg': 'avg',
            'five_percent': 'fivePercent',
            'for_query': 'forQuery',
            'generated': 'generated',
            'high_to_low': 'highToLow',
            'max': 'max',
            'median': 'median',
            'min': 'min',
            'std_dev': 'stdDev',
            'variance': 'variance',
            'volume': 'volume',
            'wavg': 'wavg'
        }

        self._avg = avg
        self._five_percent = five_percent
        self._for_query = for_query
        self._generated = generated
        self._high_to_low = high_to_low
        self._max = max
        self._median = median
        self._min = min
        self._std_dev = std_dev
        self._variance = variance
        self._volume = volume
        self._wavg = wavg

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TypeStat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TypeStat of this TypeStat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def avg(self):
        """Gets the avg of this TypeStat.

        Average Price

        :return: The avg of this TypeStat.
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this TypeStat.

        Average Price

        :param avg: The avg of this TypeStat.
        :type avg: float
        """

        self._avg = avg

    @property
    def five_percent(self):
        """Gets the five_percent of this TypeStat.


        :return: The five_percent of this TypeStat.
        :rtype: float
        """
        return self._five_percent

    @five_percent.setter
    def five_percent(self, five_percent):
        """Sets the five_percent of this TypeStat.


        :param five_percent: The five_percent of this TypeStat.
        :type five_percent: float
        """

        self._five_percent = five_percent

    @property
    def for_query(self):
        """Gets the for_query of this TypeStat.


        :return: The for_query of this TypeStat.
        :rtype: ForQuery
        """
        return self._for_query

    @for_query.setter
    def for_query(self, for_query):
        """Sets the for_query of this TypeStat.


        :param for_query: The for_query of this TypeStat.
        :type for_query: ForQuery
        """

        self._for_query = for_query

    @property
    def generated(self):
        """Gets the generated of this TypeStat.

        Generated at (UNIX Timestamp msec)

        :return: The generated of this TypeStat.
        :rtype: int
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this TypeStat.

        Generated at (UNIX Timestamp msec)

        :param generated: The generated of this TypeStat.
        :type generated: int
        """

        self._generated = generated

    @property
    def high_to_low(self):
        """Gets the high_to_low of this TypeStat.


        :return: The high_to_low of this TypeStat.
        :rtype: bool
        """
        return self._high_to_low

    @high_to_low.setter
    def high_to_low(self, high_to_low):
        """Sets the high_to_low of this TypeStat.


        :param high_to_low: The high_to_low of this TypeStat.
        :type high_to_low: bool
        """

        self._high_to_low = high_to_low

    @property
    def max(self):
        """Gets the max of this TypeStat.


        :return: The max of this TypeStat.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this TypeStat.


        :param max: The max of this TypeStat.
        :type max: float
        """

        self._max = max

    @property
    def median(self):
        """Gets the median of this TypeStat.

        Median Price

        :return: The median of this TypeStat.
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this TypeStat.

        Median Price

        :param median: The median of this TypeStat.
        :type median: float
        """

        self._median = median

    @property
    def min(self):
        """Gets the min of this TypeStat.


        :return: The min of this TypeStat.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this TypeStat.


        :param min: The min of this TypeStat.
        :type min: float
        """

        self._min = min

    @property
    def std_dev(self):
        """Gets the std_dev of this TypeStat.

        Standard Deviation

        :return: The std_dev of this TypeStat.
        :rtype: float
        """
        return self._std_dev

    @std_dev.setter
    def std_dev(self, std_dev):
        """Sets the std_dev of this TypeStat.

        Standard Deviation

        :param std_dev: The std_dev of this TypeStat.
        :type std_dev: float
        """

        self._std_dev = std_dev

    @property
    def variance(self):
        """Gets the variance of this TypeStat.


        :return: The variance of this TypeStat.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this TypeStat.


        :param variance: The variance of this TypeStat.
        :type variance: float
        """

        self._variance = variance

    @property
    def volume(self):
        """Gets the volume of this TypeStat.

        Order Volume

        :return: The volume of this TypeStat.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this TypeStat.

        Order Volume

        :param volume: The volume of this TypeStat.
        :type volume: int
        """

        self._volume = volume

    @property
    def wavg(self):
        """Gets the wavg of this TypeStat.

        Weighted Average Price

        :return: The wavg of this TypeStat.
        :rtype: float
        """
        return self._wavg

    @wavg.setter
    def wavg(self, wavg):
        """Sets the wavg of this TypeStat.

        Weighted Average Price

        :param wavg: The wavg of this TypeStat.
        :type wavg: float
        """

        self._wavg = wavg
