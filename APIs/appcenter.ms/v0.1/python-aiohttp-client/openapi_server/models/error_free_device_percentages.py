# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.errors_group_error_free_device_percentages200_response_daily_percentages_inner import ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner
from openapi_server import util


class ErrorFreeDevicePercentages(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, average_percentage: float=None, daily_percentages: List[ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner]=None):
        """ErrorFreeDevicePercentages - a model defined in OpenAPI

        :param average_percentage: The average_percentage of this ErrorFreeDevicePercentages.
        :param daily_percentages: The daily_percentages of this ErrorFreeDevicePercentages.
        """
        self.openapi_types = {
            'average_percentage': float,
            'daily_percentages': List[ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner]
        }

        self.attribute_map = {
            'average_percentage': 'averagePercentage',
            'daily_percentages': 'dailyPercentages'
        }

        self._average_percentage = average_percentage
        self._daily_percentages = daily_percentages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorFreeDevicePercentages':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorFreeDevicePercentages of this ErrorFreeDevicePercentages.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_percentage(self):
        """Gets the average_percentage of this ErrorFreeDevicePercentages.

        Average percentage

        :return: The average_percentage of this ErrorFreeDevicePercentages.
        :rtype: float
        """
        return self._average_percentage

    @average_percentage.setter
    def average_percentage(self, average_percentage):
        """Sets the average_percentage of this ErrorFreeDevicePercentages.

        Average percentage

        :param average_percentage: The average_percentage of this ErrorFreeDevicePercentages.
        :type average_percentage: float
        """

        self._average_percentage = average_percentage

    @property
    def daily_percentages(self):
        """Gets the daily_percentages of this ErrorFreeDevicePercentages.

        The error-free percentage per day.

        :return: The daily_percentages of this ErrorFreeDevicePercentages.
        :rtype: List[ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner]
        """
        return self._daily_percentages

    @daily_percentages.setter
    def daily_percentages(self, daily_percentages):
        """Sets the daily_percentages of this ErrorFreeDevicePercentages.

        The error-free percentage per day.

        :param daily_percentages: The daily_percentages of this ErrorFreeDevicePercentages.
        :type daily_percentages: List[ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner]
        """

        self._daily_percentages = daily_percentages
