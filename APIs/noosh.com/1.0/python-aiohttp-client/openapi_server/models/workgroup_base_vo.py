# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WorkgroupBaseVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, workgroup_id: int=None, workgroup_name: str=None):
        """WorkgroupBaseVO - a model defined in OpenAPI

        :param workgroup_id: The workgroup_id of this WorkgroupBaseVO.
        :param workgroup_name: The workgroup_name of this WorkgroupBaseVO.
        """
        self.openapi_types = {
            'workgroup_id': int,
            'workgroup_name': str
        }

        self.attribute_map = {
            'workgroup_id': 'workgroup_id',
            'workgroup_name': 'workgroup_name'
        }

        self._workgroup_id = workgroup_id
        self._workgroup_name = workgroup_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WorkgroupBaseVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WorkgroupBaseVO of this WorkgroupBaseVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def workgroup_id(self):
        """Gets the workgroup_id of this WorkgroupBaseVO.

        

        :return: The workgroup_id of this WorkgroupBaseVO.
        :rtype: int
        """
        return self._workgroup_id

    @workgroup_id.setter
    def workgroup_id(self, workgroup_id):
        """Sets the workgroup_id of this WorkgroupBaseVO.

        

        :param workgroup_id: The workgroup_id of this WorkgroupBaseVO.
        :type workgroup_id: int
        """

        self._workgroup_id = workgroup_id

    @property
    def workgroup_name(self):
        """Gets the workgroup_name of this WorkgroupBaseVO.

        

        :return: The workgroup_name of this WorkgroupBaseVO.
        :rtype: str
        """
        return self._workgroup_name

    @workgroup_name.setter
    def workgroup_name(self, workgroup_name):
        """Sets the workgroup_name of this WorkgroupBaseVO.

        

        :param workgroup_name: The workgroup_name of this WorkgroupBaseVO.
        :type workgroup_name: str
        """

        self._workgroup_name = workgroup_name
