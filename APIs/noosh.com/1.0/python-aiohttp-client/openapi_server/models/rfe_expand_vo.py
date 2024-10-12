# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.rfe_details_vo import RfeDetailsVO
from openapi_server import util


class RfeExpandVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: RfeDetailsVO=None, status_code: int=None, status_reason: str=None):
        """RfeExpandVO - a model defined in OpenAPI

        :param result: The result of this RfeExpandVO.
        :param status_code: The status_code of this RfeExpandVO.
        :param status_reason: The status_reason of this RfeExpandVO.
        """
        self.openapi_types = {
            'result': RfeDetailsVO,
            'status_code': int,
            'status_reason': str
        }

        self.attribute_map = {
            'result': 'result',
            'status_code': 'status_code',
            'status_reason': 'status_reason'
        }

        self._result = result
        self._status_code = status_code
        self._status_reason = status_reason

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RfeExpandVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RfeExpandVO of this RfeExpandVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this RfeExpandVO.


        :return: The result of this RfeExpandVO.
        :rtype: RfeDetailsVO
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RfeExpandVO.


        :param result: The result of this RfeExpandVO.
        :type result: RfeDetailsVO
        """

        self._result = result

    @property
    def status_code(self):
        """Gets the status_code of this RfeExpandVO.

        

        :return: The status_code of this RfeExpandVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RfeExpandVO.

        

        :param status_code: The status_code of this RfeExpandVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this RfeExpandVO.

        

        :return: The status_reason of this RfeExpandVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this RfeExpandVO.

        

        :param status_reason: The status_reason of this RfeExpandVO.
        :type status_reason: str
        """

        self._status_reason = status_reason
