# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ODataError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, details: List[ODataError]=None, message: str=None, target: str=None):
        """ODataError - a model defined in OpenAPI

        :param code: The code of this ODataError.
        :param details: The details of this ODataError.
        :param message: The message of this ODataError.
        :param target: The target of this ODataError.
        """
        self.openapi_types = {
            'code': str,
            'details': List[ODataError],
            'message': str,
            'target': str
        }

        self.attribute_map = {
            'code': 'code',
            'details': 'details',
            'message': 'message',
            'target': 'target'
        }

        self._code = code
        self._details = details
        self._message = message
        self._target = target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ODataError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ODataError of this ODataError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this ODataError.

        A language-independent error name.

        :return: The code of this ODataError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ODataError.

        A language-independent error name.

        :param code: The code of this ODataError.
        :type code: str
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this ODataError.

        The error details.

        :return: The details of this ODataError.
        :rtype: List[ODataError]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ODataError.

        The error details.

        :param details: The details of this ODataError.
        :type details: List[ODataError]
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this ODataError.

        The error message.

        :return: The message of this ODataError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ODataError.

        The error message.

        :param message: The message of this ODataError.
        :type message: str
        """

        self._message = message

    @property
    def target(self):
        """Gets the target of this ODataError.

        The target of the error (for example, the name of the property in error).

        :return: The target of this ODataError.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ODataError.

        The target of the error (for example, the name of the property in error).

        :param target: The target of this ODataError.
        :type target: str
        """

        self._target = target
