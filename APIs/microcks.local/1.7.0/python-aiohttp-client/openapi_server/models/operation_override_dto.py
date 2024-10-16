# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.parameter_constraint import ParameterConstraint
from openapi_server import util


class OperationOverrideDTO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_delay: int=None, dispatcher: str=None, dispatcher_rules: str=None, parameter_constraints: List[ParameterConstraint]=None):
        """OperationOverrideDTO - a model defined in OpenAPI

        :param default_delay: The default_delay of this OperationOverrideDTO.
        :param dispatcher: The dispatcher of this OperationOverrideDTO.
        :param dispatcher_rules: The dispatcher_rules of this OperationOverrideDTO.
        :param parameter_constraints: The parameter_constraints of this OperationOverrideDTO.
        """
        self.openapi_types = {
            'default_delay': int,
            'dispatcher': str,
            'dispatcher_rules': str,
            'parameter_constraints': List[ParameterConstraint]
        }

        self.attribute_map = {
            'default_delay': 'defaultDelay',
            'dispatcher': 'dispatcher',
            'dispatcher_rules': 'dispatcherRules',
            'parameter_constraints': 'parameterConstraints'
        }

        self._default_delay = default_delay
        self._dispatcher = dispatcher
        self._dispatcher_rules = dispatcher_rules
        self._parameter_constraints = parameter_constraints

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationOverrideDTO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationOverrideDTO of this OperationOverrideDTO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_delay(self):
        """Gets the default_delay of this OperationOverrideDTO.

        Default delay in milliseconds to apply to mock responses on this operation

        :return: The default_delay of this OperationOverrideDTO.
        :rtype: int
        """
        return self._default_delay

    @default_delay.setter
    def default_delay(self, default_delay):
        """Sets the default_delay of this OperationOverrideDTO.

        Default delay in milliseconds to apply to mock responses on this operation

        :param default_delay: The default_delay of this OperationOverrideDTO.
        :type default_delay: int
        """

        self._default_delay = default_delay

    @property
    def dispatcher(self):
        """Gets the dispatcher of this OperationOverrideDTO.

        Type of dispatcher to apply for this operation

        :return: The dispatcher of this OperationOverrideDTO.
        :rtype: str
        """
        return self._dispatcher

    @dispatcher.setter
    def dispatcher(self, dispatcher):
        """Sets the dispatcher of this OperationOverrideDTO.

        Type of dispatcher to apply for this operation

        :param dispatcher: The dispatcher of this OperationOverrideDTO.
        :type dispatcher: str
        """

        self._dispatcher = dispatcher

    @property
    def dispatcher_rules(self):
        """Gets the dispatcher_rules of this OperationOverrideDTO.

        Rules of dispatcher for this operation

        :return: The dispatcher_rules of this OperationOverrideDTO.
        :rtype: str
        """
        return self._dispatcher_rules

    @dispatcher_rules.setter
    def dispatcher_rules(self, dispatcher_rules):
        """Sets the dispatcher_rules of this OperationOverrideDTO.

        Rules of dispatcher for this operation

        :param dispatcher_rules: The dispatcher_rules of this OperationOverrideDTO.
        :type dispatcher_rules: str
        """

        self._dispatcher_rules = dispatcher_rules

    @property
    def parameter_constraints(self):
        """Gets the parameter_constraints of this OperationOverrideDTO.

        Constraints that may apply to incoming parameters on this operation

        :return: The parameter_constraints of this OperationOverrideDTO.
        :rtype: List[ParameterConstraint]
        """
        return self._parameter_constraints

    @parameter_constraints.setter
    def parameter_constraints(self, parameter_constraints):
        """Sets the parameter_constraints of this OperationOverrideDTO.

        Constraints that may apply to incoming parameters on this operation

        :param parameter_constraints: The parameter_constraints of this OperationOverrideDTO.
        :type parameter_constraints: List[ParameterConstraint]
        """

        self._parameter_constraints = parameter_constraints
