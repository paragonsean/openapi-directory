# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InstitutionalIdentification2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, clearing_system_id_code: str=None, clearing_system_member_id: str=None):
        """InstitutionalIdentification2 - a model defined in OpenAPI

        :param clearing_system_id_code: The clearing_system_id_code of this InstitutionalIdentification2.
        :param clearing_system_member_id: The clearing_system_member_id of this InstitutionalIdentification2.
        """
        self.openapi_types = {
            'clearing_system_id_code': str,
            'clearing_system_member_id': str
        }

        self.attribute_map = {
            'clearing_system_id_code': 'clearingSystemIdCode',
            'clearing_system_member_id': 'clearingSystemMemberId'
        }

        self._clearing_system_id_code = clearing_system_id_code
        self._clearing_system_member_id = clearing_system_member_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InstitutionalIdentification2':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The institutionalIdentification2 of this InstitutionalIdentification2.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def clearing_system_id_code(self):
        """Gets the clearing_system_id_code of this InstitutionalIdentification2.


        :return: The clearing_system_id_code of this InstitutionalIdentification2.
        :rtype: str
        """
        return self._clearing_system_id_code

    @clearing_system_id_code.setter
    def clearing_system_id_code(self, clearing_system_id_code):
        """Sets the clearing_system_id_code of this InstitutionalIdentification2.


        :param clearing_system_id_code: The clearing_system_id_code of this InstitutionalIdentification2.
        :type clearing_system_id_code: str
        """
        if clearing_system_id_code is None:
            raise ValueError("Invalid value for `clearing_system_id_code`, must not be `None`")
        if clearing_system_id_code is not None and len(clearing_system_id_code) > 5:
            raise ValueError("Invalid value for `clearing_system_id_code`, length must be less than or equal to `5`")
        if clearing_system_id_code is not None and len(clearing_system_id_code) < 1:
            raise ValueError("Invalid value for `clearing_system_id_code`, length must be greater than or equal to `1`")

        self._clearing_system_id_code = clearing_system_id_code

    @property
    def clearing_system_member_id(self):
        """Gets the clearing_system_member_id of this InstitutionalIdentification2.


        :return: The clearing_system_member_id of this InstitutionalIdentification2.
        :rtype: str
        """
        return self._clearing_system_member_id

    @clearing_system_member_id.setter
    def clearing_system_member_id(self, clearing_system_member_id):
        """Sets the clearing_system_member_id of this InstitutionalIdentification2.


        :param clearing_system_member_id: The clearing_system_member_id of this InstitutionalIdentification2.
        :type clearing_system_member_id: str
        """
        if clearing_system_member_id is None:
            raise ValueError("Invalid value for `clearing_system_member_id`, must not be `None`")
        if clearing_system_member_id is not None and len(clearing_system_member_id) > 35:
            raise ValueError("Invalid value for `clearing_system_member_id`, length must be less than or equal to `35`")

        self._clearing_system_member_id = clearing_system_member_id
