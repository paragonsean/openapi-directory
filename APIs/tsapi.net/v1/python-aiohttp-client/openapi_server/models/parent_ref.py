# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ParentRef(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parent_value_ident: str=None, parent_variable_ident: str=None):
        """ParentRef - a model defined in OpenAPI

        :param parent_value_ident: The parent_value_ident of this ParentRef.
        :param parent_variable_ident: The parent_variable_ident of this ParentRef.
        """
        self.openapi_types = {
            'parent_value_ident': str,
            'parent_variable_ident': str
        }

        self.attribute_map = {
            'parent_value_ident': 'parentValueIdent',
            'parent_variable_ident': 'parentVariableIdent'
        }

        self._parent_value_ident = parent_value_ident
        self._parent_variable_ident = parent_variable_ident

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ParentRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ParentRef of this ParentRef.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent_value_ident(self):
        """Gets the parent_value_ident of this ParentRef.


        :return: The parent_value_ident of this ParentRef.
        :rtype: str
        """
        return self._parent_value_ident

    @parent_value_ident.setter
    def parent_value_ident(self, parent_value_ident):
        """Sets the parent_value_ident of this ParentRef.


        :param parent_value_ident: The parent_value_ident of this ParentRef.
        :type parent_value_ident: str
        """

        self._parent_value_ident = parent_value_ident

    @property
    def parent_variable_ident(self):
        """Gets the parent_variable_ident of this ParentRef.


        :return: The parent_variable_ident of this ParentRef.
        :rtype: str
        """
        return self._parent_variable_ident

    @parent_variable_ident.setter
    def parent_variable_ident(self, parent_variable_ident):
        """Sets the parent_variable_ident of this ParentRef.


        :param parent_variable_ident: The parent_variable_ident of this ParentRef.
        :type parent_variable_ident: str
        """

        self._parent_variable_ident = parent_variable_ident
