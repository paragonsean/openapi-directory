# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ViolatedPasswordPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, name: str=None):
        """ViolatedPasswordPolicy - a model defined in OpenAPI

        :param message: The message of this ViolatedPasswordPolicy.
        :param name: The name of this ViolatedPasswordPolicy.
        """
        self.openapi_types = {
            'message': str,
            'name': str
        }

        self.attribute_map = {
            'message': 'message',
            'name': 'name'
        }

        self._message = message
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ViolatedPasswordPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ViolatedPasswordPolicy of this ViolatedPasswordPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this ViolatedPasswordPolicy.

        Message from password validator

        :return: The message of this ViolatedPasswordPolicy.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ViolatedPasswordPolicy.

        Message from password validator

        :param message: The message of this ViolatedPasswordPolicy.
        :type message: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this ViolatedPasswordPolicy.

        Name of the violated password policy

        :return: The name of this ViolatedPasswordPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ViolatedPasswordPolicy.

        Name of the violated password policy

        :param name: The name of this ViolatedPasswordPolicy.
        :type name: str
        """

        self._name = name
