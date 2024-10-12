# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ScoutingObservationSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_time: datetime=None, id: str=None, start_time: datetime=None, updated_at: datetime=None):
        """ScoutingObservationSummary - a model defined in OpenAPI

        :param end_time: The end_time of this ScoutingObservationSummary.
        :param id: The id of this ScoutingObservationSummary.
        :param start_time: The start_time of this ScoutingObservationSummary.
        :param updated_at: The updated_at of this ScoutingObservationSummary.
        """
        self.openapi_types = {
            'end_time': datetime,
            'id': str,
            'start_time': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'end_time': 'endTime',
            'id': 'id',
            'start_time': 'startTime',
            'updated_at': 'updatedAt'
        }

        self._end_time = end_time
        self._id = id
        self._start_time = start_time
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ScoutingObservationSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ScoutingObservationSummary of this ScoutingObservationSummary.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_time(self):
        """Gets the end_time of this ScoutingObservationSummary.

        The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).

        :return: The end_time of this ScoutingObservationSummary.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScoutingObservationSummary.

        The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).

        :param end_time: The end_time of this ScoutingObservationSummary.
        :type end_time: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")

        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this ScoutingObservationSummary.

        The id of a scouting observation.

        :return: The id of this ScoutingObservationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScoutingObservationSummary.

        The id of a scouting observation.

        :param id: The id of this ScoutingObservationSummary.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this ScoutingObservationSummary.

        The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).

        :return: The start_time of this ScoutingObservationSummary.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScoutingObservationSummary.

        The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).

        :param start_time: The start_time of this ScoutingObservationSummary.
        :type start_time: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")

        self._start_time = start_time

    @property
    def updated_at(self):
        """Gets the updated_at of this ScoutingObservationSummary.

        The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).

        :return: The updated_at of this ScoutingObservationSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ScoutingObservationSummary.

        The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).

        :param updated_at: The updated_at of this ScoutingObservationSummary.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at
