# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.contacts_simple_vo import ContactsSimpleVO
from openapi_server import util


class ContactsListVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, results: List[ContactsSimpleVO]=None, status_code: int=None, status_reason: str=None):
        """ContactsListVO - a model defined in OpenAPI

        :param results: The results of this ContactsListVO.
        :param status_code: The status_code of this ContactsListVO.
        :param status_reason: The status_reason of this ContactsListVO.
        """
        self.openapi_types = {
            'results': List[ContactsSimpleVO],
            'status_code': int,
            'status_reason': str
        }

        self.attribute_map = {
            'results': 'results',
            'status_code': 'status_code',
            'status_reason': 'status_reason'
        }

        self._results = results
        self._status_code = status_code
        self._status_reason = status_reason

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ContactsListVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ContactsListVO of this ContactsListVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def results(self):
        """Gets the results of this ContactsListVO.

        

        :return: The results of this ContactsListVO.
        :rtype: List[ContactsSimpleVO]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ContactsListVO.

        

        :param results: The results of this ContactsListVO.
        :type results: List[ContactsSimpleVO]
        """

        self._results = results

    @property
    def status_code(self):
        """Gets the status_code of this ContactsListVO.

        

        :return: The status_code of this ContactsListVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ContactsListVO.

        

        :param status_code: The status_code of this ContactsListVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this ContactsListVO.

        

        :return: The status_reason of this ContactsListVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ContactsListVO.

        

        :param status_reason: The status_reason of this ContactsListVO.
        :type status_reason: str
        """

        self._status_reason = status_reason
