# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TeamMemberBaseInfVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status_code: int=None, status_reason: str=None, teammember_id: int=None):
        """TeamMemberBaseInfVO - a model defined in OpenAPI

        :param status_code: The status_code of this TeamMemberBaseInfVO.
        :param status_reason: The status_reason of this TeamMemberBaseInfVO.
        :param teammember_id: The teammember_id of this TeamMemberBaseInfVO.
        """
        self.openapi_types = {
            'status_code': int,
            'status_reason': str,
            'teammember_id': int
        }

        self.attribute_map = {
            'status_code': 'status_code',
            'status_reason': 'status_reason',
            'teammember_id': 'teammember_id'
        }

        self._status_code = status_code
        self._status_reason = status_reason
        self._teammember_id = teammember_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamMemberBaseInfVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TeamMemberBaseInfVO of this TeamMemberBaseInfVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status_code(self):
        """Gets the status_code of this TeamMemberBaseInfVO.

        

        :return: The status_code of this TeamMemberBaseInfVO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this TeamMemberBaseInfVO.

        

        :param status_code: The status_code of this TeamMemberBaseInfVO.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def status_reason(self):
        """Gets the status_reason of this TeamMemberBaseInfVO.

        

        :return: The status_reason of this TeamMemberBaseInfVO.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this TeamMemberBaseInfVO.

        

        :param status_reason: The status_reason of this TeamMemberBaseInfVO.
        :type status_reason: str
        """

        self._status_reason = status_reason

    @property
    def teammember_id(self):
        """Gets the teammember_id of this TeamMemberBaseInfVO.

        

        :return: The teammember_id of this TeamMemberBaseInfVO.
        :rtype: int
        """
        return self._teammember_id

    @teammember_id.setter
    def teammember_id(self, teammember_id):
        """Sets the teammember_id of this TeamMemberBaseInfVO.

        

        :param teammember_id: The teammember_id of this TeamMemberBaseInfVO.
        :type teammember_id: int
        """

        self._teammember_id = teammember_id
