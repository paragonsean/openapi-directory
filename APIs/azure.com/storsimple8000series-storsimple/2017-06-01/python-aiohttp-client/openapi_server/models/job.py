# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.job_error_details import JobErrorDetails
from openapi_server.models.job_properties import JobProperties
from openapi_server import util


class Job(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_time: datetime=None, error: JobErrorDetails=None, percent_complete: int=None, properties: JobProperties=None, start_time: datetime=None, status: str=None, id: str=None, kind: str=None, name: str=None, type: str=None):
        """Job - a model defined in OpenAPI

        :param end_time: The end_time of this Job.
        :param error: The error of this Job.
        :param percent_complete: The percent_complete of this Job.
        :param properties: The properties of this Job.
        :param start_time: The start_time of this Job.
        :param status: The status of this Job.
        :param id: The id of this Job.
        :param kind: The kind of this Job.
        :param name: The name of this Job.
        :param type: The type of this Job.
        """
        self.openapi_types = {
            'end_time': datetime,
            'error': JobErrorDetails,
            'percent_complete': int,
            'properties': JobProperties,
            'start_time': datetime,
            'status': str,
            'id': str,
            'kind': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'end_time': 'endTime',
            'error': 'error',
            'percent_complete': 'percentComplete',
            'properties': 'properties',
            'start_time': 'startTime',
            'status': 'status',
            'id': 'id',
            'kind': 'kind',
            'name': 'name',
            'type': 'type'
        }

        self._end_time = end_time
        self._error = error
        self._percent_complete = percent_complete
        self._properties = properties
        self._start_time = start_time
        self._status = status
        self._id = id
        self._kind = kind
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Job':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Job of this Job.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_time(self):
        """Gets the end_time of this Job.

        The UTC time at which the job completed.

        :return: The end_time of this Job.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Job.

        The UTC time at which the job completed.

        :param end_time: The end_time of this Job.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def error(self):
        """Gets the error of this Job.


        :return: The error of this Job.
        :rtype: JobErrorDetails
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Job.


        :param error: The error of this Job.
        :type error: JobErrorDetails
        """

        self._error = error

    @property
    def percent_complete(self):
        """Gets the percent_complete of this Job.

        The percentage of the job that is already complete.

        :return: The percent_complete of this Job.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this Job.

        The percentage of the job that is already complete.

        :param percent_complete: The percent_complete of this Job.
        :type percent_complete: int
        """
        if percent_complete is None:
            raise ValueError("Invalid value for `percent_complete`, must not be `None`")

        self._percent_complete = percent_complete

    @property
    def properties(self):
        """Gets the properties of this Job.


        :return: The properties of this Job.
        :rtype: JobProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Job.


        :param properties: The properties of this Job.
        :type properties: JobProperties
        """

        self._properties = properties

    @property
    def start_time(self):
        """Gets the start_time of this Job.

        The UTC time at which the job was started.

        :return: The start_time of this Job.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Job.

        The UTC time at which the job was started.

        :param start_time: The start_time of this Job.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this Job.

        The current status of the job.

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        The current status of the job.

        :param status: The status of this Job.
        :type status: str
        """
        allowed_values = ["Running", "Succeeded", "Failed", "Canceled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def id(self):
        """Gets the id of this Job.

        The path ID that uniquely identifies the object.

        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        The path ID that uniquely identifies the object.

        :param id: The id of this Job.
        :type id: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this Job.

        The Kind of the object. Currently only Series8000 is supported

        :return: The kind of this Job.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Job.

        The Kind of the object. Currently only Series8000 is supported

        :param kind: The kind of this Job.
        :type kind: str
        """
        allowed_values = ["Series8000"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this Job.

        The name of the object.

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        The name of the object.

        :param name: The name of this Job.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Job.

        The hierarchical type of the object.

        :return: The type of this Job.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.

        The hierarchical type of the object.

        :param type: The type of this Job.
        :type type: str
        """

        self._type = type
