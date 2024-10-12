# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.serial_console_operations_value_inner import SerialConsoleOperationsValueInner
from openapi_server import util


class SerialConsoleOperations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[SerialConsoleOperationsValueInner]=None):
        """SerialConsoleOperations - a model defined in OpenAPI

        :param value: The value of this SerialConsoleOperations.
        """
        self.openapi_types = {
            'value': List[SerialConsoleOperationsValueInner]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SerialConsoleOperations':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SerialConsoleOperations of this SerialConsoleOperations.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this SerialConsoleOperations.

        A list of Serial Console operations

        :return: The value of this SerialConsoleOperations.
        :rtype: List[SerialConsoleOperationsValueInner]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SerialConsoleOperations.

        A list of Serial Console operations

        :param value: The value of this SerialConsoleOperations.
        :type value: List[SerialConsoleOperationsValueInner]
        """

        self._value = value
