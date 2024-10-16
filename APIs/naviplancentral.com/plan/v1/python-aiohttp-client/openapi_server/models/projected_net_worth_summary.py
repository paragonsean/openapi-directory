# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_net_worth_at_date import INetWorthAtDate
from openapi_server import util


class ProjectedNetWorthSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_age: int=None, co_client_age: int=None, end_of_year_net_worth: INetWorthAtDate=None, year: int=None):
        """ProjectedNetWorthSummary - a model defined in OpenAPI

        :param client_age: The client_age of this ProjectedNetWorthSummary.
        :param co_client_age: The co_client_age of this ProjectedNetWorthSummary.
        :param end_of_year_net_worth: The end_of_year_net_worth of this ProjectedNetWorthSummary.
        :param year: The year of this ProjectedNetWorthSummary.
        """
        self.openapi_types = {
            'client_age': int,
            'co_client_age': int,
            'end_of_year_net_worth': INetWorthAtDate,
            'year': int
        }

        self.attribute_map = {
            'client_age': 'clientAge',
            'co_client_age': 'coClientAge',
            'end_of_year_net_worth': 'endOfYearNetWorth',
            'year': 'year'
        }

        self._client_age = client_age
        self._co_client_age = co_client_age
        self._end_of_year_net_worth = end_of_year_net_worth
        self._year = year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectedNetWorthSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectedNetWorthSummary of this ProjectedNetWorthSummary.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_age(self):
        """Gets the client_age of this ProjectedNetWorthSummary.


        :return: The client_age of this ProjectedNetWorthSummary.
        :rtype: int
        """
        return self._client_age

    @client_age.setter
    def client_age(self, client_age):
        """Sets the client_age of this ProjectedNetWorthSummary.


        :param client_age: The client_age of this ProjectedNetWorthSummary.
        :type client_age: int
        """

        self._client_age = client_age

    @property
    def co_client_age(self):
        """Gets the co_client_age of this ProjectedNetWorthSummary.


        :return: The co_client_age of this ProjectedNetWorthSummary.
        :rtype: int
        """
        return self._co_client_age

    @co_client_age.setter
    def co_client_age(self, co_client_age):
        """Sets the co_client_age of this ProjectedNetWorthSummary.


        :param co_client_age: The co_client_age of this ProjectedNetWorthSummary.
        :type co_client_age: int
        """

        self._co_client_age = co_client_age

    @property
    def end_of_year_net_worth(self):
        """Gets the end_of_year_net_worth of this ProjectedNetWorthSummary.


        :return: The end_of_year_net_worth of this ProjectedNetWorthSummary.
        :rtype: INetWorthAtDate
        """
        return self._end_of_year_net_worth

    @end_of_year_net_worth.setter
    def end_of_year_net_worth(self, end_of_year_net_worth):
        """Sets the end_of_year_net_worth of this ProjectedNetWorthSummary.


        :param end_of_year_net_worth: The end_of_year_net_worth of this ProjectedNetWorthSummary.
        :type end_of_year_net_worth: INetWorthAtDate
        """

        self._end_of_year_net_worth = end_of_year_net_worth

    @property
    def year(self):
        """Gets the year of this ProjectedNetWorthSummary.


        :return: The year of this ProjectedNetWorthSummary.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ProjectedNetWorthSummary.


        :param year: The year of this ProjectedNetWorthSummary.
        :type year: int
        """

        self._year = year
