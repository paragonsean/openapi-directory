# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.application_activity_summary import ApplicationActivitySummary
from openapi_server import util


class ApplicationActivities(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, results: List[ApplicationActivitySummary]=None):
        """ApplicationActivities - a model defined in OpenAPI

        :param results: The results of this ApplicationActivities.
        """
        self.openapi_types = {
            'results': List[ApplicationActivitySummary]
        }

        self.attribute_map = {
            'results': 'results'
        }

        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApplicationActivities':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApplicationActivities of this ApplicationActivities.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def results(self):
        """Gets the results of this ApplicationActivities.


        :return: The results of this ApplicationActivities.
        :rtype: List[ApplicationActivitySummary]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ApplicationActivities.


        :param results: The results of this ApplicationActivities.
        :type results: List[ApplicationActivitySummary]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
