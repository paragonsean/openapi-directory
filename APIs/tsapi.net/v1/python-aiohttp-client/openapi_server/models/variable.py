# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.label import Label
from openapi_server.models.parent_type import ParentType
from openapi_server.models.use_type import UseType
from openapi_server.models.variable_type import VariableType
from openapi_server.models.variable_values import VariableValues
from openapi_server import util


class Variable(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ident: str=None, label: Label=None, max_responses: int=None, name: str=None, parent_type: ParentType=None, questions: List[Variable]=None, type: VariableType=None, use: UseType=None, variable_values: VariableValues=None):
        """Variable - a model defined in OpenAPI

        :param ident: The ident of this Variable.
        :param label: The label of this Variable.
        :param max_responses: The max_responses of this Variable.
        :param name: The name of this Variable.
        :param parent_type: The parent_type of this Variable.
        :param questions: The questions of this Variable.
        :param type: The type of this Variable.
        :param use: The use of this Variable.
        :param variable_values: The variable_values of this Variable.
        """
        self.openapi_types = {
            'ident': str,
            'label': Label,
            'max_responses': int,
            'name': str,
            'parent_type': ParentType,
            'questions': List[Variable],
            'type': VariableType,
            'use': UseType,
            'variable_values': VariableValues
        }

        self.attribute_map = {
            'ident': 'ident',
            'label': 'label',
            'max_responses': 'maxResponses',
            'name': 'name',
            'parent_type': 'parentType',
            'questions': 'questions',
            'type': 'type',
            'use': 'use',
            'variable_values': 'variableValues'
        }

        self._ident = ident
        self._label = label
        self._max_responses = max_responses
        self._name = name
        self._parent_type = parent_type
        self._questions = questions
        self._type = type
        self._use = use
        self._variable_values = variable_values

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Variable':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Variable of this Variable.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ident(self):
        """Gets the ident of this Variable.


        :return: The ident of this Variable.
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident):
        """Sets the ident of this Variable.


        :param ident: The ident of this Variable.
        :type ident: str
        """

        self._ident = ident

    @property
    def label(self):
        """Gets the label of this Variable.


        :return: The label of this Variable.
        :rtype: Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Variable.


        :param label: The label of this Variable.
        :type label: Label
        """

        self._label = label

    @property
    def max_responses(self):
        """Gets the max_responses of this Variable.


        :return: The max_responses of this Variable.
        :rtype: int
        """
        return self._max_responses

    @max_responses.setter
    def max_responses(self, max_responses):
        """Sets the max_responses of this Variable.


        :param max_responses: The max_responses of this Variable.
        :type max_responses: int
        """

        self._max_responses = max_responses

    @property
    def name(self):
        """Gets the name of this Variable.


        :return: The name of this Variable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Variable.


        :param name: The name of this Variable.
        :type name: str
        """

        self._name = name

    @property
    def parent_type(self):
        """Gets the parent_type of this Variable.


        :return: The parent_type of this Variable.
        :rtype: ParentType
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """Sets the parent_type of this Variable.


        :param parent_type: The parent_type of this Variable.
        :type parent_type: ParentType
        """

        self._parent_type = parent_type

    @property
    def questions(self):
        """Gets the questions of this Variable.


        :return: The questions of this Variable.
        :rtype: List[Variable]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this Variable.


        :param questions: The questions of this Variable.
        :type questions: List[Variable]
        """

        self._questions = questions

    @property
    def type(self):
        """Gets the type of this Variable.


        :return: The type of this Variable.
        :rtype: VariableType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Variable.


        :param type: The type of this Variable.
        :type type: VariableType
        """

        self._type = type

    @property
    def use(self):
        """Gets the use of this Variable.


        :return: The use of this Variable.
        :rtype: UseType
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this Variable.


        :param use: The use of this Variable.
        :type use: UseType
        """

        self._use = use

    @property
    def variable_values(self):
        """Gets the variable_values of this Variable.


        :return: The variable_values of this Variable.
        :rtype: VariableValues
        """
        return self._variable_values

    @variable_values.setter
    def variable_values(self, variable_values):
        """Sets the variable_values of this Variable.


        :param variable_values: The variable_values of this Variable.
        :type variable_values: VariableValues
        """

        self._variable_values = variable_values
