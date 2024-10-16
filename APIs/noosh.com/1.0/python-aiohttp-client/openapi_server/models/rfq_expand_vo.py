# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.rfq_details_vo import RfqDetailsVO
from openapi_server import util


class RfqExpandVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: RfqDetailsVO=None, status_code: int=None, status_reason: str=None):
        """RfqExpandVO - a model defined in OpenAPI

        :param result: The result of this RfqExpandVO.
        :param status_code: The status_code of this RfqExpandVO.
        :param status_reason: The status_reason of this RfqExpandVO.
        """
        self.openapi_types = {
            'result': RfqDetailsVO,
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
    def from_dict(cls, dikt: dict) -> 'RfqExpandVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RfqExpandVO of this RfqExpandVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this RfqExpandVO.


        :return: The result of this RfqExpandVO.
        :rtype: RfqDetailsVO
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RfqExpandVO.


        :param result: The result of this RfqExpandVO.
        :type result: RfqDetailsVO
        """

        self._result = result

    @property
    def status_code(self):
        """Gets the status_code of this RfqExpandVO.

        

        :return: The status_code of this RfqExpandVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RfqExpandVO.

        

        :param status_code: The status_code of this RfqExpandVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this RfqExpandVO.

        

        :return: The status_reason of this RfqExpandVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this RfqExpandVO.

        

        :param status_reason: The status_reason of this RfqExpandVO.
        :type status_reason: str
        """

        self._status_reason = status_reason
