# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Schedule3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type: str=None, end_repeat: date=None, name: str=None, recurrence_data: str=None, recurrence_type: str=None, start_repeat: date=None, start_transcoder: datetime=None, stop_transcoder: datetime=None, transcoder_id: str=None):
        """Schedule3 - a model defined in OpenAPI

        :param action_type: The action_type of this Schedule3.
        :param end_repeat: The end_repeat of this Schedule3.
        :param name: The name of this Schedule3.
        :param recurrence_data: The recurrence_data of this Schedule3.
        :param recurrence_type: The recurrence_type of this Schedule3.
        :param start_repeat: The start_repeat of this Schedule3.
        :param start_transcoder: The start_transcoder of this Schedule3.
        :param stop_transcoder: The stop_transcoder of this Schedule3.
        :param transcoder_id: The transcoder_id of this Schedule3.
        """
        self.openapi_types = {
            'action_type': str,
            'end_repeat': date,
            'name': str,
            'recurrence_data': str,
            'recurrence_type': str,
            'start_repeat': date,
            'start_transcoder': datetime,
            'stop_transcoder': datetime,
            'transcoder_id': str
        }

        self.attribute_map = {
            'action_type': 'action_type',
            'end_repeat': 'end_repeat',
            'name': 'name',
            'recurrence_data': 'recurrence_data',
            'recurrence_type': 'recurrence_type',
            'start_repeat': 'start_repeat',
            'start_transcoder': 'start_transcoder',
            'stop_transcoder': 'stop_transcoder',
            'transcoder_id': 'transcoder_id'
        }

        self._action_type = action_type
        self._end_repeat = end_repeat
        self._name = name
        self._recurrence_data = recurrence_data
        self._recurrence_type = recurrence_type
        self._start_repeat = start_repeat
        self._start_transcoder = start_transcoder
        self._stop_transcoder = stop_transcoder
        self._transcoder_id = transcoder_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Schedule3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The schedule_3 of this Schedule3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this Schedule3.

        The type of action that the schedule should trigger on the transcoder. The default is <strong>start</strong>.

        :return: The action_type of this Schedule3.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this Schedule3.

        The type of action that the schedule should trigger on the transcoder. The default is <strong>start</strong>.

        :param action_type: The action_type of this Schedule3.
        :type action_type: str
        """
        allowed_values = ["start", "stop", "start_stop"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def end_repeat(self):
        """Gets the end_repeat of this Schedule3.

        The month, day, and year that a recurring schedule should stop running. Specify <strong>YYYY-MM-DD</strong>.

        :return: The end_repeat of this Schedule3.
        :rtype: date
        """
        return self._end_repeat

    @end_repeat.setter
    def end_repeat(self, end_repeat):
        """Sets the end_repeat of this Schedule3.

        The month, day, and year that a recurring schedule should stop running. Specify <strong>YYYY-MM-DD</strong>.

        :param end_repeat: The end_repeat of this Schedule3.
        :type end_repeat: date
        """

        self._end_repeat = end_repeat

    @property
    def name(self):
        """Gets the name of this Schedule3.

        A descriptive name for the schedule. Maximum 255 characters.

        :return: The name of this Schedule3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Schedule3.

        A descriptive name for the schedule. Maximum 255 characters.

        :param name: The name of this Schedule3.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def recurrence_data(self):
        """Gets the recurrence_data of this Schedule3.

        The day or days of the week that a recurring schedule should run.

        :return: The recurrence_data of this Schedule3.
        :rtype: str
        """
        return self._recurrence_data

    @recurrence_data.setter
    def recurrence_data(self, recurrence_data):
        """Sets the recurrence_data of this Schedule3.

        The day or days of the week that a recurring schedule should run.

        :param recurrence_data: The recurrence_data of this Schedule3.
        :type recurrence_data: str
        """
        allowed_values = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # noqa: E501
        if recurrence_data not in allowed_values:
            raise ValueError(
                "Invalid value for `recurrence_data` ({0}), must be one of {1}"
                .format(recurrence_data, allowed_values)
            )

        self._recurrence_data = recurrence_data

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this Schedule3.

        A schedule can run one time only (<strong>once</strong>) or repeat (<strong>recur</strong>) until a specified <em>end_repeat</em> date. The default is <strong>once</strong>.

        :return: The recurrence_type of this Schedule3.
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this Schedule3.

        A schedule can run one time only (<strong>once</strong>) or repeat (<strong>recur</strong>) until a specified <em>end_repeat</em> date. The default is <strong>once</strong>.

        :param recurrence_type: The recurrence_type of this Schedule3.
        :type recurrence_type: str
        """
        allowed_values = ["once", "recur"]  # noqa: E501
        if recurrence_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recurrence_type` ({0}), must be one of {1}"
                .format(recurrence_type, allowed_values)
            )

        self._recurrence_type = recurrence_type

    @property
    def start_repeat(self):
        """Gets the start_repeat of this Schedule3.

        The month, day, and year that the recurring schedule should go into effect. Specify <strong>YYYY-MM-DD</strong>.

        :return: The start_repeat of this Schedule3.
        :rtype: date
        """
        return self._start_repeat

    @start_repeat.setter
    def start_repeat(self, start_repeat):
        """Sets the start_repeat of this Schedule3.

        The month, day, and year that the recurring schedule should go into effect. Specify <strong>YYYY-MM-DD</strong>.

        :param start_repeat: The start_repeat of this Schedule3.
        :type start_repeat: date
        """

        self._start_repeat = start_repeat

    @property
    def start_transcoder(self):
        """Gets the start_transcoder of this Schedule3.

        The month, day, year, and time of day that the <em>action_type</em> <strong>start</strong> should occur. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC.

        :return: The start_transcoder of this Schedule3.
        :rtype: datetime
        """
        return self._start_transcoder

    @start_transcoder.setter
    def start_transcoder(self, start_transcoder):
        """Sets the start_transcoder of this Schedule3.

        The month, day, year, and time of day that the <em>action_type</em> <strong>start</strong> should occur. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC.

        :param start_transcoder: The start_transcoder of this Schedule3.
        :type start_transcoder: datetime
        """

        self._start_transcoder = start_transcoder

    @property
    def stop_transcoder(self):
        """Gets the stop_transcoder of this Schedule3.

        The month, day, year, and time of day that the <em>action_type</em> <strong>stop</strong> should occur. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC.

        :return: The stop_transcoder of this Schedule3.
        :rtype: datetime
        """
        return self._stop_transcoder

    @stop_transcoder.setter
    def stop_transcoder(self, stop_transcoder):
        """Sets the stop_transcoder of this Schedule3.

        The month, day, year, and time of day that the <em>action_type</em> <strong>stop</strong> should occur. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC.

        :param stop_transcoder: The stop_transcoder of this Schedule3.
        :type stop_transcoder: datetime
        """

        self._stop_transcoder = stop_transcoder

    @property
    def transcoder_id(self):
        """Gets the transcoder_id of this Schedule3.

        The unique alphanumeric string that identifies the transcoder being scheduled.

        :return: The transcoder_id of this Schedule3.
        :rtype: str
        """
        return self._transcoder_id

    @transcoder_id.setter
    def transcoder_id(self, transcoder_id):
        """Sets the transcoder_id of this Schedule3.

        The unique alphanumeric string that identifies the transcoder being scheduled.

        :param transcoder_id: The transcoder_id of this Schedule3.
        :type transcoder_id: str
        """
        if transcoder_id is None:
            raise ValueError("Invalid value for `transcoder_id`, must not be `None`")

        self._transcoder_id = transcoder_id
