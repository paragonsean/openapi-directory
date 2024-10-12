# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DpmJobTaskDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duration: str=None, end_time: datetime=None, start_time: datetime=None, status: str=None, task_id: str=None):
        """DpmJobTaskDetails - a model defined in OpenAPI

        :param duration: The duration of this DpmJobTaskDetails.
        :param end_time: The end_time of this DpmJobTaskDetails.
        :param start_time: The start_time of this DpmJobTaskDetails.
        :param status: The status of this DpmJobTaskDetails.
        :param task_id: The task_id of this DpmJobTaskDetails.
        """
        self.openapi_types = {
            'duration': str,
            'end_time': datetime,
            'start_time': datetime,
            'status': str,
            'task_id': str
        }

        self.attribute_map = {
            'duration': 'duration',
            'end_time': 'endTime',
            'start_time': 'startTime',
            'status': 'status',
            'task_id': 'taskId'
        }

        self._duration = duration
        self._end_time = end_time
        self._start_time = start_time
        self._status = status
        self._task_id = task_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DpmJobTaskDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DpmJobTaskDetails of this DpmJobTaskDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duration(self):
        """Gets the duration of this DpmJobTaskDetails.

        Time elapsed for task.

        :return: The duration of this DpmJobTaskDetails.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DpmJobTaskDetails.

        Time elapsed for task.

        :param duration: The duration of this DpmJobTaskDetails.
        :type duration: str
        """

        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this DpmJobTaskDetails.

        The end time.

        :return: The end_time of this DpmJobTaskDetails.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DpmJobTaskDetails.

        The end time.

        :param end_time: The end_time of this DpmJobTaskDetails.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this DpmJobTaskDetails.

        The start time.

        :return: The start_time of this DpmJobTaskDetails.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DpmJobTaskDetails.

        The start time.

        :param start_time: The start_time of this DpmJobTaskDetails.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DpmJobTaskDetails.

        The status.

        :return: The status of this DpmJobTaskDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DpmJobTaskDetails.

        The status.

        :param status: The status of this DpmJobTaskDetails.
        :type status: str
        """

        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this DpmJobTaskDetails.

        The task display name.

        :return: The task_id of this DpmJobTaskDetails.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DpmJobTaskDetails.

        The task display name.

        :param task_id: The task_id of this DpmJobTaskDetails.
        :type task_id: str
        """

        self._task_id = task_id
