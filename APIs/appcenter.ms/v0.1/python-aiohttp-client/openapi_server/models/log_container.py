# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.log_container_logs_inner import LogContainerLogsInner
from openapi_server import util


class LogContainer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, exceeded_max_limit: bool=None, last_received_log_timestamp: datetime=None, logs: List[LogContainerLogsInner]=None):
        """LogContainer - a model defined in OpenAPI

        :param exceeded_max_limit: The exceeded_max_limit of this LogContainer.
        :param last_received_log_timestamp: The last_received_log_timestamp of this LogContainer.
        :param logs: The logs of this LogContainer.
        """
        self.openapi_types = {
            'exceeded_max_limit': bool,
            'last_received_log_timestamp': datetime,
            'logs': List[LogContainerLogsInner]
        }

        self.attribute_map = {
            'exceeded_max_limit': 'exceeded_max_limit',
            'last_received_log_timestamp': 'last_received_log_timestamp',
            'logs': 'logs'
        }

        self._exceeded_max_limit = exceeded_max_limit
        self._last_received_log_timestamp = last_received_log_timestamp
        self._logs = logs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LogContainer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LogContainer of this LogContainer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def exceeded_max_limit(self):
        """Gets the exceeded_max_limit of this LogContainer.

        indicates if the number of available logs are more than the max allowed return limit(100).

        :return: The exceeded_max_limit of this LogContainer.
        :rtype: bool
        """
        return self._exceeded_max_limit

    @exceeded_max_limit.setter
    def exceeded_max_limit(self, exceeded_max_limit):
        """Sets the exceeded_max_limit of this LogContainer.

        indicates if the number of available logs are more than the max allowed return limit(100).

        :param exceeded_max_limit: The exceeded_max_limit of this LogContainer.
        :type exceeded_max_limit: bool
        """

        self._exceeded_max_limit = exceeded_max_limit

    @property
    def last_received_log_timestamp(self):
        """Gets the last_received_log_timestamp of this LogContainer.

        the timestamp of the last log received. This value can be used as the start time parameter in the consecutive API call.

        :return: The last_received_log_timestamp of this LogContainer.
        :rtype: datetime
        """
        return self._last_received_log_timestamp

    @last_received_log_timestamp.setter
    def last_received_log_timestamp(self, last_received_log_timestamp):
        """Sets the last_received_log_timestamp of this LogContainer.

        the timestamp of the last log received. This value can be used as the start time parameter in the consecutive API call.

        :param last_received_log_timestamp: The last_received_log_timestamp of this LogContainer.
        :type last_received_log_timestamp: datetime
        """

        self._last_received_log_timestamp = last_received_log_timestamp

    @property
    def logs(self):
        """Gets the logs of this LogContainer.

        the list of logs

        :return: The logs of this LogContainer.
        :rtype: List[LogContainerLogsInner]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this LogContainer.

        the list of logs

        :param logs: The logs of this LogContainer.
        :type logs: List[LogContainerLogsInner]
        """
        if logs is None:
            raise ValueError("Invalid value for `logs`, must not be `None`")
        if logs is not None and len(logs) < 0:
            raise ValueError("Invalid value for `logs`, number of items must be greater than or equal to `0`")

        self._logs = logs
