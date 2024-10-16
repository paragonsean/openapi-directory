# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RfqVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rfq_id: int=None, status_code: int=None, status_reason: str=None):
        """RfqVO - a model defined in OpenAPI

        :param rfq_id: The rfq_id of this RfqVO.
        :param status_code: The status_code of this RfqVO.
        :param status_reason: The status_reason of this RfqVO.
        """
        self.openapi_types = {
            'rfq_id': int,
            'status_code': int,
            'status_reason': str
        }

        self.attribute_map = {
            'rfq_id': 'rfq_id',
            'status_code': 'status_code',
            'status_reason': 'status_reason'
        }

        self._rfq_id = rfq_id
        self._status_code = status_code
        self._status_reason = status_reason

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RfqVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RfqVO of this RfqVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rfq_id(self):
        """Gets the rfq_id of this RfqVO.

        

        :return: The rfq_id of this RfqVO.
        :rtype: int
        """
        return self._rfq_id

    @rfq_id.setter
    def rfq_id(self, rfq_id):
        """Sets the rfq_id of this RfqVO.

        

        :param rfq_id: The rfq_id of this RfqVO.
        :type rfq_id: int
        """

        self._rfq_id = rfq_id

    @property
    def status_code(self):
        """Gets the status_code of this RfqVO.

        

        :return: The status_code of this RfqVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RfqVO.

        

        :param status_code: The status_code of this RfqVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this RfqVO.

        

        :return: The status_reason of this RfqVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this RfqVO.

        

        :param status_reason: The status_reason of this RfqVO.
        :type status_reason: str
        """

        self._status_reason = status_reason
