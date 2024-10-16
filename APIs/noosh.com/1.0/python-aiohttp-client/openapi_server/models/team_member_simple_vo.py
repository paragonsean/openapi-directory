# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TeamMemberSimpleVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_name: str=None, name: str=None, phone: str=None, role: str=None, teammember_id: int=None, user_id: int=None, workgroup_name: str=None):
        """TeamMemberSimpleVO - a model defined in OpenAPI

        :param company_name: The company_name of this TeamMemberSimpleVO.
        :param name: The name of this TeamMemberSimpleVO.
        :param phone: The phone of this TeamMemberSimpleVO.
        :param role: The role of this TeamMemberSimpleVO.
        :param teammember_id: The teammember_id of this TeamMemberSimpleVO.
        :param user_id: The user_id of this TeamMemberSimpleVO.
        :param workgroup_name: The workgroup_name of this TeamMemberSimpleVO.
        """
        self.openapi_types = {
            'company_name': str,
            'name': str,
            'phone': str,
            'role': str,
            'teammember_id': int,
            'user_id': int,
            'workgroup_name': str
        }

        self.attribute_map = {
            'company_name': 'company_name',
            'name': 'name',
            'phone': 'phone',
            'role': 'role',
            'teammember_id': 'teammember_id',
            'user_id': 'user_id',
            'workgroup_name': 'workgroup_name'
        }

        self._company_name = company_name
        self._name = name
        self._phone = phone
        self._role = role
        self._teammember_id = teammember_id
        self._user_id = user_id
        self._workgroup_name = workgroup_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamMemberSimpleVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TeamMemberSimpleVO of this TeamMemberSimpleVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_name(self):
        """Gets the company_name of this TeamMemberSimpleVO.

        

        :return: The company_name of this TeamMemberSimpleVO.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this TeamMemberSimpleVO.

        

        :param company_name: The company_name of this TeamMemberSimpleVO.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def name(self):
        """Gets the name of this TeamMemberSimpleVO.

        

        :return: The name of this TeamMemberSimpleVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamMemberSimpleVO.

        

        :param name: The name of this TeamMemberSimpleVO.
        :type name: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this TeamMemberSimpleVO.

        

        :return: The phone of this TeamMemberSimpleVO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this TeamMemberSimpleVO.

        

        :param phone: The phone of this TeamMemberSimpleVO.
        :type phone: str
        """

        self._phone = phone

    @property
    def role(self):
        """Gets the role of this TeamMemberSimpleVO.

        

        :return: The role of this TeamMemberSimpleVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeamMemberSimpleVO.

        

        :param role: The role of this TeamMemberSimpleVO.
        :type role: str
        """

        self._role = role

    @property
    def teammember_id(self):
        """Gets the teammember_id of this TeamMemberSimpleVO.

        

        :return: The teammember_id of this TeamMemberSimpleVO.
        :rtype: int
        """
        return self._teammember_id

    @teammember_id.setter
    def teammember_id(self, teammember_id):
        """Sets the teammember_id of this TeamMemberSimpleVO.

        

        :param teammember_id: The teammember_id of this TeamMemberSimpleVO.
        :type teammember_id: int
        """

        self._teammember_id = teammember_id

    @property
    def user_id(self):
        """Gets the user_id of this TeamMemberSimpleVO.

        

        :return: The user_id of this TeamMemberSimpleVO.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TeamMemberSimpleVO.

        

        :param user_id: The user_id of this TeamMemberSimpleVO.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def workgroup_name(self):
        """Gets the workgroup_name of this TeamMemberSimpleVO.

        

        :return: The workgroup_name of this TeamMemberSimpleVO.
        :rtype: str
        """
        return self._workgroup_name

    @workgroup_name.setter
    def workgroup_name(self, workgroup_name):
        """Sets the workgroup_name of this TeamMemberSimpleVO.

        

        :param workgroup_name: The workgroup_name of this TeamMemberSimpleVO.
        :type workgroup_name: str
        """

        self._workgroup_name = workgroup_name
