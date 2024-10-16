# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateStatistics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, clicks: float=None, favorites: float=None, mentions: float=None, reach: float=None, retweets: float=None):
        """UpdateStatistics - a model defined in OpenAPI

        :param clicks: The clicks of this UpdateStatistics.
        :param favorites: The favorites of this UpdateStatistics.
        :param mentions: The mentions of this UpdateStatistics.
        :param reach: The reach of this UpdateStatistics.
        :param retweets: The retweets of this UpdateStatistics.
        """
        self.openapi_types = {
            'clicks': float,
            'favorites': float,
            'mentions': float,
            'reach': float,
            'retweets': float
        }

        self.attribute_map = {
            'clicks': 'clicks',
            'favorites': 'favorites',
            'mentions': 'mentions',
            'reach': 'reach',
            'retweets': 'retweets'
        }

        self._clicks = clicks
        self._favorites = favorites
        self._mentions = mentions
        self._reach = reach
        self._retweets = retweets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateStatistics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The update_statistics of this UpdateStatistics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def clicks(self):
        """Gets the clicks of this UpdateStatistics.


        :return: The clicks of this UpdateStatistics.
        :rtype: float
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this UpdateStatistics.


        :param clicks: The clicks of this UpdateStatistics.
        :type clicks: float
        """

        self._clicks = clicks

    @property
    def favorites(self):
        """Gets the favorites of this UpdateStatistics.


        :return: The favorites of this UpdateStatistics.
        :rtype: float
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this UpdateStatistics.


        :param favorites: The favorites of this UpdateStatistics.
        :type favorites: float
        """

        self._favorites = favorites

    @property
    def mentions(self):
        """Gets the mentions of this UpdateStatistics.


        :return: The mentions of this UpdateStatistics.
        :rtype: float
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):
        """Sets the mentions of this UpdateStatistics.


        :param mentions: The mentions of this UpdateStatistics.
        :type mentions: float
        """

        self._mentions = mentions

    @property
    def reach(self):
        """Gets the reach of this UpdateStatistics.


        :return: The reach of this UpdateStatistics.
        :rtype: float
        """
        return self._reach

    @reach.setter
    def reach(self, reach):
        """Sets the reach of this UpdateStatistics.


        :param reach: The reach of this UpdateStatistics.
        :type reach: float
        """

        self._reach = reach

    @property
    def retweets(self):
        """Gets the retweets of this UpdateStatistics.


        :return: The retweets of this UpdateStatistics.
        :rtype: float
        """
        return self._retweets

    @retweets.setter
    def retweets(self, retweets):
        """Sets the retweets of this UpdateStatistics.


        :param retweets: The retweets of this UpdateStatistics.
        :type retweets: float
        """

        self._retweets = retweets
