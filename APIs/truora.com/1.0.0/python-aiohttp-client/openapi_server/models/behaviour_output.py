# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.behavior import Behavior
from openapi_server import util


class BehaviourOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, behavior: List[Behavior]=None, _self: str=None):
        """BehaviourOutput - a model defined in OpenAPI

        :param behavior: The behavior of this BehaviourOutput.
        :param _self: The _self of this BehaviourOutput.
        """
        self.openapi_types = {
            'behavior': List[Behavior],
            '_self': str
        }

        self.attribute_map = {
            'behavior': 'behavior',
            '_self': 'self'
        }

        self._behavior = behavior
        self.__self = _self

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BehaviourOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BehaviourOutput of this BehaviourOutput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def behavior(self):
        """Gets the behavior of this BehaviourOutput.

        Behavior list

        :return: The behavior of this BehaviourOutput.
        :rtype: List[Behavior]
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this BehaviourOutput.

        Behavior list

        :param behavior: The behavior of this BehaviourOutput.
        :type behavior: List[Behavior]
        """
        if behavior is None:
            raise ValueError("Invalid value for `behavior`, must not be `None`")

        self._behavior = behavior

    @property
    def _self(self):
        """Gets the _self of this BehaviourOutput.

        Path to this resource

        :return: The _self of this BehaviourOutput.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this BehaviourOutput.

        Path to this resource

        :param _self: The _self of this BehaviourOutput.
        :type _self: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")

        self.__self = _self
