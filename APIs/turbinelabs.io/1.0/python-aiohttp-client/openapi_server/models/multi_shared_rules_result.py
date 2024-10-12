# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.shared_rules import SharedRules
from openapi_server import util


class MultiSharedRulesResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: List[SharedRules]=None):
        """MultiSharedRulesResult - a model defined in OpenAPI

        :param result: The result of this MultiSharedRulesResult.
        """
        self.openapi_types = {
            'result': List[SharedRules]
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MultiSharedRulesResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MultiSharedRulesResult of this MultiSharedRulesResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this MultiSharedRulesResult.


        :return: The result of this MultiSharedRulesResult.
        :rtype: List[SharedRules]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MultiSharedRulesResult.


        :param result: The result of this MultiSharedRulesResult.
        :type result: List[SharedRules]
        """

        self._result = result
