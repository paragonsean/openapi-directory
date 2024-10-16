# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.property_param_simple_vo import PropertyParamSimpleVO
from openapi_server import util


class PropertyParamListVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: List[PropertyParamSimpleVO]=None, status_code: int=None, status_reason: str=None):
        """PropertyParamListVO - a model defined in OpenAPI

        :param result: The result of this PropertyParamListVO.
        :param status_code: The status_code of this PropertyParamListVO.
        :param status_reason: The status_reason of this PropertyParamListVO.
        """
        self.openapi_types = {
            'result': List[PropertyParamSimpleVO],
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
    def from_dict(cls, dikt: dict) -> 'PropertyParamListVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PropertyParamListVO of this PropertyParamListVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this PropertyParamListVO.

        

        :return: The result of this PropertyParamListVO.
        :rtype: List[PropertyParamSimpleVO]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PropertyParamListVO.

        

        :param result: The result of this PropertyParamListVO.
        :type result: List[PropertyParamSimpleVO]
        """

        self._result = result

    @property
    def status_code(self):
        """Gets the status_code of this PropertyParamListVO.

        

        :return: The status_code of this PropertyParamListVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this PropertyParamListVO.

        

        :param status_code: The status_code of this PropertyParamListVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this PropertyParamListVO.

        

        :return: The status_reason of this PropertyParamListVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this PropertyParamListVO.

        

        :param status_reason: The status_reason of this PropertyParamListVO.
        :type status_reason: str
        """

        self._status_reason = status_reason
