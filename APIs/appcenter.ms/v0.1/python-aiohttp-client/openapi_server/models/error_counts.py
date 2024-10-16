# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.errors_counts_per_day200_response_errors_inner import ErrorsCountsPerDay200ResponseErrorsInner
from openapi_server import util


class ErrorCounts(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, errors: List[ErrorsCountsPerDay200ResponseErrorsInner]=None):
        """ErrorCounts - a model defined in OpenAPI

        :param count: The count of this ErrorCounts.
        :param errors: The errors of this ErrorCounts.
        """
        self.openapi_types = {
            'count': int,
            'errors': List[ErrorsCountsPerDay200ResponseErrorsInner]
        }

        self.attribute_map = {
            'count': 'count',
            'errors': 'errors'
        }

        self._count = count
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorCounts':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorCounts of this ErrorCounts.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ErrorCounts.

        total error count

        :return: The count of this ErrorCounts.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ErrorCounts.

        total error count

        :param count: The count of this ErrorCounts.
        :type count: int
        """

        self._count = count

    @property
    def errors(self):
        """Gets the errors of this ErrorCounts.

        the total error count for day

        :return: The errors of this ErrorCounts.
        :rtype: List[ErrorsCountsPerDay200ResponseErrorsInner]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ErrorCounts.

        the total error count for day

        :param errors: The errors of this ErrorCounts.
        :type errors: List[ErrorsCountsPerDay200ResponseErrorsInner]
        """

        self._errors = errors
