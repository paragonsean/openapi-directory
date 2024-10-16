# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BusinessPermissionViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access: str=None, function: str=None, object: str=None, role: str=None):
        """BusinessPermissionViewModel - a model defined in OpenAPI

        :param access: The access of this BusinessPermissionViewModel.
        :param function: The function of this BusinessPermissionViewModel.
        :param object: The object of this BusinessPermissionViewModel.
        :param role: The role of this BusinessPermissionViewModel.
        """
        self.openapi_types = {
            'access': str,
            'function': str,
            'object': str,
            'role': str
        }

        self.attribute_map = {
            'access': 'access',
            'function': 'function',
            'object': 'object',
            'role': 'role'
        }

        self._access = access
        self._function = function
        self._object = object
        self._role = role

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BusinessPermissionViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BusinessPermissionViewModel of this BusinessPermissionViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access(self):
        """Gets the access of this BusinessPermissionViewModel.


        :return: The access of this BusinessPermissionViewModel.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this BusinessPermissionViewModel.


        :param access: The access of this BusinessPermissionViewModel.
        :type access: str
        """

        self._access = access

    @property
    def function(self):
        """Gets the function of this BusinessPermissionViewModel.


        :return: The function of this BusinessPermissionViewModel.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this BusinessPermissionViewModel.


        :param function: The function of this BusinessPermissionViewModel.
        :type function: str
        """

        self._function = function

    @property
    def object(self):
        """Gets the object of this BusinessPermissionViewModel.


        :return: The object of this BusinessPermissionViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this BusinessPermissionViewModel.


        :param object: The object of this BusinessPermissionViewModel.
        :type object: str
        """

        self._object = object

    @property
    def role(self):
        """Gets the role of this BusinessPermissionViewModel.


        :return: The role of this BusinessPermissionViewModel.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this BusinessPermissionViewModel.


        :param role: The role of this BusinessPermissionViewModel.
        :type role: str
        """

        self._role = role
