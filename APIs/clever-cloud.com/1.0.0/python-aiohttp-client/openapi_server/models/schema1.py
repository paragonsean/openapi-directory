# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.schema1_member import Schema1Member
from openapi_server import util


class Schema1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job: str=None, member: Schema1Member=None, role: str=None):
        """Schema1 - a model defined in OpenAPI

        :param job: The job of this Schema1.
        :param member: The member of this Schema1.
        :param role: The role of this Schema1.
        """
        self.openapi_types = {
            'job': str,
            'member': Schema1Member,
            'role': str
        }

        self.attribute_map = {
            'job': 'job',
            'member': 'member',
            'role': 'role'
        }

        self._job = job
        self._member = member
        self._role = role

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Schema1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The schema1 of this Schema1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job(self):
        """Gets the job of this Schema1.


        :return: The job of this Schema1.
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this Schema1.


        :param job: The job of this Schema1.
        :type job: str
        """
        if job is None:
            raise ValueError("Invalid value for `job`, must not be `None`")

        self._job = job

    @property
    def member(self):
        """Gets the member of this Schema1.


        :return: The member of this Schema1.
        :rtype: Schema1Member
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Schema1.


        :param member: The member of this Schema1.
        :type member: Schema1Member
        """
        if member is None:
            raise ValueError("Invalid value for `member`, must not be `None`")

        self._member = member

    @property
    def role(self):
        """Gets the role of this Schema1.


        :return: The role of this Schema1.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Schema1.


        :param role: The role of this Schema1.
        :type role: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role
