# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.domain import Domain
from openapi_server import util


class DomainResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: Domain=None):
        """DomainResult - a model defined in OpenAPI

        :param result: The result of this DomainResult.
        """
        self.openapi_types = {
            'result': Domain
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DomainResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DomainResult of this DomainResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this DomainResult.


        :return: The result of this DomainResult.
        :rtype: Domain
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DomainResult.


        :param result: The result of this DomainResult.
        :type result: Domain
        """

        self._result = result
