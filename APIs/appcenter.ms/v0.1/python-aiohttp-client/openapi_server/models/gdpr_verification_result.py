# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GdprVerificationResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, status: bool=None):
        """GdprVerificationResult - a model defined in OpenAPI

        :param message: The message of this GdprVerificationResult.
        :param status: The status of this GdprVerificationResult.
        """
        self.openapi_types = {
            'message': str,
            'status': bool
        }

        self.attribute_map = {
            'message': 'message',
            'status': 'status'
        }

        self._message = message
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GdprVerificationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GdprVerificationResult of this GdprVerificationResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this GdprVerificationResult.

        Optional error message if the verification failed.

        :return: The message of this GdprVerificationResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GdprVerificationResult.

        Optional error message if the verification failed.

        :param message: The message of this GdprVerificationResult.
        :type message: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this GdprVerificationResult.

        Verification status. True means that the verification was successfull.

        :return: The status of this GdprVerificationResult.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GdprVerificationResult.

        Verification status. True means that the verification was successfull.

        :param status: The status of this GdprVerificationResult.
        :type status: bool
        """

        self._status = status
