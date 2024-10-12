# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PatchInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, op: str=None, path: str=None, value: object=None):
        """PatchInner - a model defined in OpenAPI

        :param op: The op of this PatchInner.
        :param path: The path of this PatchInner.
        :param value: The value of this PatchInner.
        """
        self.openapi_types = {
            'op': str,
            'path': str,
            'value': object
        }

        self.attribute_map = {
            'op': 'op',
            'path': 'path',
            'value': 'value'
        }

        self._op = op
        self._path = path
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Patch_inner of this PatchInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def op(self):
        """Gets the op of this PatchInner.


        :return: The op of this PatchInner.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this PatchInner.


        :param op: The op of this PatchInner.
        :type op: str
        """
        allowed_values = ["add", "replace", "remove", "copy", "test"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def path(self):
        """Gets the path of this PatchInner.


        :return: The path of this PatchInner.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PatchInner.


        :param path: The path of this PatchInner.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def value(self):
        """Gets the value of this PatchInner.


        :return: The value of this PatchInner.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PatchInner.


        :param value: The value of this PatchInner.
        :type value: object
        """

        self._value = value
