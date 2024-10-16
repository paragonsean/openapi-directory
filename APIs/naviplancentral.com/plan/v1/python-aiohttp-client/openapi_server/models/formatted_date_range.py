# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.model_date import ModelDate
from openapi_server import util


class FormattedDateRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_date: ModelDate=None, start_date: ModelDate=None):
        """FormattedDateRange - a model defined in OpenAPI

        :param end_date: The end_date of this FormattedDateRange.
        :param start_date: The start_date of this FormattedDateRange.
        """
        self.openapi_types = {
            'end_date': ModelDate,
            'start_date': ModelDate
        }

        self.attribute_map = {
            'end_date': 'endDate',
            'start_date': 'startDate'
        }

        self._end_date = end_date
        self._start_date = start_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FormattedDateRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FormattedDateRange of this FormattedDateRange.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_date(self):
        """Gets the end_date of this FormattedDateRange.


        :return: The end_date of this FormattedDateRange.
        :rtype: ModelDate
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FormattedDateRange.


        :param end_date: The end_date of this FormattedDateRange.
        :type end_date: ModelDate
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this FormattedDateRange.


        :return: The start_date of this FormattedDateRange.
        :rtype: ModelDate
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FormattedDateRange.


        :param start_date: The start_date of this FormattedDateRange.
        :type start_date: ModelDate
        """

        self._start_date = start_date
