# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.test_run_summary import TestRunSummary
from openapi_server import util


class TestSeries(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, most_recent_activity: str=None, name: str=None, slug: str=None, test_runs: List[TestRunSummary]=None):
        """TestSeries - a model defined in OpenAPI

        :param most_recent_activity: The most_recent_activity of this TestSeries.
        :param name: The name of this TestSeries.
        :param slug: The slug of this TestSeries.
        :param test_runs: The test_runs of this TestSeries.
        """
        self.openapi_types = {
            'most_recent_activity': str,
            'name': str,
            'slug': str,
            'test_runs': List[TestRunSummary]
        }

        self.attribute_map = {
            'most_recent_activity': 'mostRecentActivity',
            'name': 'name',
            'slug': 'slug',
            'test_runs': 'testRuns'
        }

        self._most_recent_activity = most_recent_activity
        self._name = name
        self._slug = slug
        self._test_runs = test_runs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestSeries':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Test_Series of this TestSeries.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def most_recent_activity(self):
        """Gets the most_recent_activity of this TestSeries.

        Date of the latest test run that used this test series

        :return: The most_recent_activity of this TestSeries.
        :rtype: str
        """
        return self._most_recent_activity

    @most_recent_activity.setter
    def most_recent_activity(self, most_recent_activity):
        """Sets the most_recent_activity of this TestSeries.

        Date of the latest test run that used this test series

        :param most_recent_activity: The most_recent_activity of this TestSeries.
        :type most_recent_activity: str
        """

        self._most_recent_activity = most_recent_activity

    @property
    def name(self):
        """Gets the name of this TestSeries.

        Name of the test series

        :return: The name of this TestSeries.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestSeries.

        Name of the test series

        :param name: The name of this TestSeries.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this TestSeries.

        Unique, human-readable identifier of the test series

        :return: The slug of this TestSeries.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this TestSeries.

        Unique, human-readable identifier of the test series

        :param slug: The slug of this TestSeries.
        :type slug: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")

        self._slug = slug

    @property
    def test_runs(self):
        """Gets the test_runs of this TestSeries.

        Most recent test runs

        :return: The test_runs of this TestSeries.
        :rtype: List[TestRunSummary]
        """
        return self._test_runs

    @test_runs.setter
    def test_runs(self, test_runs):
        """Sets the test_runs of this TestSeries.

        Most recent test runs

        :param test_runs: The test_runs of this TestSeries.
        :type test_runs: List[TestRunSummary]
        """

        self._test_runs = test_runs
