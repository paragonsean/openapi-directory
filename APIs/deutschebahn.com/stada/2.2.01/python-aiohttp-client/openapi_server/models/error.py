# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Error(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, err_msg: str=None, err_no: int=None):
        """Error - a model defined in OpenAPI

        :param err_msg: The err_msg of this Error.
        :param err_no: The err_no of this Error.
        """
        self.openapi_types = {
            'err_msg': str,
            'err_no': int
        }

        self.attribute_map = {
            'err_msg': 'errMsg',
            'err_no': 'errNo'
        }

        self._err_msg = err_msg
        self._err_no = err_no

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error of this Error.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def err_msg(self):
        """Gets the err_msg of this Error.

        error message

        :return: The err_msg of this Error.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this Error.

        error message

        :param err_msg: The err_msg of this Error.
        :type err_msg: str
        """

        self._err_msg = err_msg

    @property
    def err_no(self):
        """Gets the err_no of this Error.

        error number

        :return: The err_no of this Error.
        :rtype: int
        """
        return self._err_no

    @err_no.setter
    def err_no(self, err_no):
        """Sets the err_no of this Error.

        error number

        :param err_no: The err_no of this Error.
        :type err_no: int
        """

        self._err_no = err_no
