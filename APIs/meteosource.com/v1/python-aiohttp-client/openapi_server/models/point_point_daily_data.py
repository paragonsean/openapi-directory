# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.point_point_daily_afternoon_data import PointPointDailyAfternoonData
from openapi_server.models.point_point_daily_all_day_data import PointPointDailyAllDayData
from openapi_server.models.point_point_daily_astro_data import PointPointDailyAstroData
from openapi_server.models.point_point_daily_evening_data import PointPointDailyEveningData
from openapi_server.models.point_point_daily_morning_data import PointPointDailyMorningData
from openapi_server.models.point_point_daily_stats_data import PointPointDailyStatsData
from openapi_server import util


class PointPointDailyData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, afternoon: PointPointDailyAfternoonData=None, all_day: PointPointDailyAllDayData=None, astro: PointPointDailyAstroData=None, day: file=None, evening: PointPointDailyEveningData=None, icon: int=None, morning: PointPointDailyMorningData=None, predictability: int=None, statistics: PointPointDailyStatsData=None, summary: str=None, weather: str=None):
        """PointPointDailyData - a model defined in OpenAPI

        :param afternoon: The afternoon of this PointPointDailyData.
        :param all_day: The all_day of this PointPointDailyData.
        :param astro: The astro of this PointPointDailyData.
        :param day: The day of this PointPointDailyData.
        :param evening: The evening of this PointPointDailyData.
        :param icon: The icon of this PointPointDailyData.
        :param morning: The morning of this PointPointDailyData.
        :param predictability: The predictability of this PointPointDailyData.
        :param statistics: The statistics of this PointPointDailyData.
        :param summary: The summary of this PointPointDailyData.
        :param weather: The weather of this PointPointDailyData.
        """
        self.openapi_types = {
            'afternoon': PointPointDailyAfternoonData,
            'all_day': PointPointDailyAllDayData,
            'astro': PointPointDailyAstroData,
            'day': file,
            'evening': PointPointDailyEveningData,
            'icon': int,
            'morning': PointPointDailyMorningData,
            'predictability': int,
            'statistics': PointPointDailyStatsData,
            'summary': str,
            'weather': str
        }

        self.attribute_map = {
            'afternoon': 'afternoon',
            'all_day': 'all_day',
            'astro': 'astro',
            'day': 'day',
            'evening': 'evening',
            'icon': 'icon',
            'morning': 'morning',
            'predictability': 'predictability',
            'statistics': 'statistics',
            'summary': 'summary',
            'weather': 'weather'
        }

        self._afternoon = afternoon
        self._all_day = all_day
        self._astro = astro
        self._day = day
        self._evening = evening
        self._icon = icon
        self._morning = morning
        self._predictability = predictability
        self._statistics = statistics
        self._summary = summary
        self._weather = weather

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PointPointDailyData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Point_PointDailyData of this PointPointDailyData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def afternoon(self):
        """Gets the afternoon of this PointPointDailyData.


        :return: The afternoon of this PointPointDailyData.
        :rtype: PointPointDailyAfternoonData
        """
        return self._afternoon

    @afternoon.setter
    def afternoon(self, afternoon):
        """Sets the afternoon of this PointPointDailyData.


        :param afternoon: The afternoon of this PointPointDailyData.
        :type afternoon: PointPointDailyAfternoonData
        """

        self._afternoon = afternoon

    @property
    def all_day(self):
        """Gets the all_day of this PointPointDailyData.


        :return: The all_day of this PointPointDailyData.
        :rtype: PointPointDailyAllDayData
        """
        return self._all_day

    @all_day.setter
    def all_day(self, all_day):
        """Sets the all_day of this PointPointDailyData.


        :param all_day: The all_day of this PointPointDailyData.
        :type all_day: PointPointDailyAllDayData
        """
        if all_day is None:
            raise ValueError("Invalid value for `all_day`, must not be `None`")

        self._all_day = all_day

    @property
    def astro(self):
        """Gets the astro of this PointPointDailyData.


        :return: The astro of this PointPointDailyData.
        :rtype: PointPointDailyAstroData
        """
        return self._astro

    @astro.setter
    def astro(self, astro):
        """Sets the astro of this PointPointDailyData.


        :param astro: The astro of this PointPointDailyData.
        :type astro: PointPointDailyAstroData
        """
        if astro is None:
            raise ValueError("Invalid value for `astro`, must not be `None`")

        self._astro = astro

    @property
    def day(self):
        """Gets the day of this PointPointDailyData.

        Datetime in YYYY-MM-DDTHH:MM:SS format.

        :return: The day of this PointPointDailyData.
        :rtype: file
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this PointPointDailyData.

        Datetime in YYYY-MM-DDTHH:MM:SS format.

        :param day: The day of this PointPointDailyData.
        :type day: file
        """

        self._day = day

    @property
    def evening(self):
        """Gets the evening of this PointPointDailyData.


        :return: The evening of this PointPointDailyData.
        :rtype: PointPointDailyEveningData
        """
        return self._evening

    @evening.setter
    def evening(self, evening):
        """Sets the evening of this PointPointDailyData.


        :param evening: The evening of this PointPointDailyData.
        :type evening: PointPointDailyEveningData
        """

        self._evening = evening

    @property
    def icon(self):
        """Gets the icon of this PointPointDailyData.

        Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: icon

        :return: The icon of this PointPointDailyData.
        :rtype: int
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PointPointDailyData.

        Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: icon

        :param icon: The icon of this PointPointDailyData.
        :type icon: int
        """

        self._icon = icon

    @property
    def morning(self):
        """Gets the morning of this PointPointDailyData.


        :return: The morning of this PointPointDailyData.
        :rtype: PointPointDailyMorningData
        """
        return self._morning

    @morning.setter
    def morning(self, morning):
        """Sets the morning of this PointPointDailyData.


        :param morning: The morning of this PointPointDailyData.
        :type morning: PointPointDailyMorningData
        """

        self._morning = morning

    @property
    def predictability(self):
        """Gets the predictability of this PointPointDailyData.

        Weather predictability. Values from 1 (very high predictability) to 5 (very low predictability). Unit: 1-5

        :return: The predictability of this PointPointDailyData.
        :rtype: int
        """
        return self._predictability

    @predictability.setter
    def predictability(self, predictability):
        """Sets the predictability of this PointPointDailyData.

        Weather predictability. Values from 1 (very high predictability) to 5 (very low predictability). Unit: 1-5

        :param predictability: The predictability of this PointPointDailyData.
        :type predictability: int
        """

        self._predictability = predictability

    @property
    def statistics(self):
        """Gets the statistics of this PointPointDailyData.


        :return: The statistics of this PointPointDailyData.
        :rtype: PointPointDailyStatsData
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this PointPointDailyData.


        :param statistics: The statistics of this PointPointDailyData.
        :type statistics: PointPointDailyStatsData
        """
        if statistics is None:
            raise ValueError("Invalid value for `statistics`, must not be `None`")

        self._statistics = statistics

    @property
    def summary(self):
        """Gets the summary of this PointPointDailyData.

        Short text summary of the weather, e.g. `Light rain`.

        :return: The summary of this PointPointDailyData.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PointPointDailyData.

        Short text summary of the weather, e.g. `Light rain`.

        :param summary: The summary of this PointPointDailyData.
        :type summary: str
        """

        self._summary = summary

    @property
    def weather(self):
        """Gets the weather of this PointPointDailyData.

        All day string identifier of the weather icon, e.g. `light_rain`.

        :return: The weather of this PointPointDailyData.
        :rtype: str
        """
        return self._weather

    @weather.setter
    def weather(self, weather):
        """Sets the weather of this PointPointDailyData.

        All day string identifier of the weather icon, e.g. `light_rain`.

        :param weather: The weather of this PointPointDailyData.
        :type weather: str
        """

        self._weather = weather
