# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CancelTransactionOut(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, success: bool=None):
        """CancelTransactionOut - a model defined in OpenAPI

        :param success: The success of this CancelTransactionOut.
        """
        self.openapi_types = {
            'success': bool
        }

        self.attribute_map = {
            'success': 'success'
        }

        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CancelTransactionOut':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The cancelTransactionOut of this CancelTransactionOut.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def success(self):
        """Gets the success of this CancelTransactionOut.

        Was operation successful?

        :return: The success of this CancelTransactionOut.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CancelTransactionOut.

        Was operation successful?

        :param success: The success of this CancelTransactionOut.
        :type success: bool
        """

        self._success = success
