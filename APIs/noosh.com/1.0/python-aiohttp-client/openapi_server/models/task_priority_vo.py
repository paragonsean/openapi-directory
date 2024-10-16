# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TaskPriorityVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, task_priority_id: int=None, task_priority_name: str=None):
        """TaskPriorityVO - a model defined in OpenAPI

        :param task_priority_id: The task_priority_id of this TaskPriorityVO.
        :param task_priority_name: The task_priority_name of this TaskPriorityVO.
        """
        self.openapi_types = {
            'task_priority_id': int,
            'task_priority_name': str
        }

        self.attribute_map = {
            'task_priority_id': 'task_priority_id',
            'task_priority_name': 'task_priority_name'
        }

        self._task_priority_id = task_priority_id
        self._task_priority_name = task_priority_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaskPriorityVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaskPriorityVO of this TaskPriorityVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def task_priority_id(self):
        """Gets the task_priority_id of this TaskPriorityVO.

        

        :return: The task_priority_id of this TaskPriorityVO.
        :rtype: int
        """
        return self._task_priority_id

    @task_priority_id.setter
    def task_priority_id(self, task_priority_id):
        """Sets the task_priority_id of this TaskPriorityVO.

        

        :param task_priority_id: The task_priority_id of this TaskPriorityVO.
        :type task_priority_id: int
        """

        self._task_priority_id = task_priority_id

    @property
    def task_priority_name(self):
        """Gets the task_priority_name of this TaskPriorityVO.

        

        :return: The task_priority_name of this TaskPriorityVO.
        :rtype: str
        """
        return self._task_priority_name

    @task_priority_name.setter
    def task_priority_name(self, task_priority_name):
        """Sets the task_priority_name of this TaskPriorityVO.

        

        :param task_priority_name: The task_priority_name of this TaskPriorityVO.
        :type task_priority_name: str
        """

        self._task_priority_name = task_priority_name
