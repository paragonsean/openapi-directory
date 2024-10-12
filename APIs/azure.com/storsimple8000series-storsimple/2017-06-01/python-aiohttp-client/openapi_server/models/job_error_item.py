# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JobErrorItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None, recommendations: List[str]=None):
        """JobErrorItem - a model defined in OpenAPI

        :param code: The code of this JobErrorItem.
        :param message: The message of this JobErrorItem.
        :param recommendations: The recommendations of this JobErrorItem.
        """
        self.openapi_types = {
            'code': str,
            'message': str,
            'recommendations': List[str]
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'recommendations': 'recommendations'
        }

        self._code = code
        self._message = message
        self._recommendations = recommendations

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JobErrorItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JobErrorItem of this JobErrorItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this JobErrorItem.

        The error code intended for programmatic access.

        :return: The code of this JobErrorItem.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this JobErrorItem.

        The error code intended for programmatic access.

        :param code: The code of this JobErrorItem.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """Gets the message of this JobErrorItem.

        The error message intended to describe the error in detail.

        :return: The message of this JobErrorItem.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobErrorItem.

        The error message intended to describe the error in detail.

        :param message: The message of this JobErrorItem.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def recommendations(self):
        """Gets the recommendations of this JobErrorItem.

        The recommended actions.

        :return: The recommendations of this JobErrorItem.
        :rtype: List[str]
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations):
        """Sets the recommendations of this JobErrorItem.

        The recommended actions.

        :param recommendations: The recommendations of this JobErrorItem.
        :type recommendations: List[str]
        """

        self._recommendations = recommendations
