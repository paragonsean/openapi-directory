# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OperationStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_time: datetime=None, last_action_time: datetime=None, message: str=None, resource_location: str=None, status: str=None):
        """OperationStatus - a model defined in OpenAPI

        :param created_time: The created_time of this OperationStatus.
        :param last_action_time: The last_action_time of this OperationStatus.
        :param message: The message of this OperationStatus.
        :param resource_location: The resource_location of this OperationStatus.
        :param status: The status of this OperationStatus.
        """
        self.openapi_types = {
            'created_time': datetime,
            'last_action_time': datetime,
            'message': str,
            'resource_location': str,
            'status': str
        }

        self.attribute_map = {
            'created_time': 'createdTime',
            'last_action_time': 'lastActionTime',
            'message': 'message',
            'resource_location': 'resourceLocation',
            'status': 'status'
        }

        self._created_time = created_time
        self._last_action_time = last_action_time
        self._message = message
        self._resource_location = resource_location
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationStatus of this OperationStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_time(self):
        """Gets the created_time of this OperationStatus.

        A combined UTC date and time string that describes the time when the operation (take or apply a snapshot) is requested. E.g. 2018-12-25T11:41:02.2331413Z.

        :return: The created_time of this OperationStatus.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OperationStatus.

        A combined UTC date and time string that describes the time when the operation (take or apply a snapshot) is requested. E.g. 2018-12-25T11:41:02.2331413Z.

        :param created_time: The created_time of this OperationStatus.
        :type created_time: datetime
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")

        self._created_time = created_time

    @property
    def last_action_time(self):
        """Gets the last_action_time of this OperationStatus.

        A combined UTC date and time string that describes the last time the operation (take or apply a snapshot) is actively migrating data. The lastActionTime will keep increasing until the operation finishes. E.g. 2018-12-25T11:51:27.8705696Z.

        :return: The last_action_time of this OperationStatus.
        :rtype: datetime
        """
        return self._last_action_time

    @last_action_time.setter
    def last_action_time(self, last_action_time):
        """Sets the last_action_time of this OperationStatus.

        A combined UTC date and time string that describes the last time the operation (take or apply a snapshot) is actively migrating data. The lastActionTime will keep increasing until the operation finishes. E.g. 2018-12-25T11:51:27.8705696Z.

        :param last_action_time: The last_action_time of this OperationStatus.
        :type last_action_time: datetime
        """

        self._last_action_time = last_action_time

    @property
    def message(self):
        """Gets the message of this OperationStatus.

        Show failure message when operation fails (omitted when operation succeeds).

        :return: The message of this OperationStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OperationStatus.

        Show failure message when operation fails (omitted when operation succeeds).

        :param message: The message of this OperationStatus.
        :type message: str
        """

        self._message = message

    @property
    def resource_location(self):
        """Gets the resource_location of this OperationStatus.

        When the operation succeeds successfully, for snapshot taking operation the snapshot id will be included in this field, and for snapshot applying operation, the path to get the target object will be returned in this field.

        :return: The resource_location of this OperationStatus.
        :rtype: str
        """
        return self._resource_location

    @resource_location.setter
    def resource_location(self, resource_location):
        """Sets the resource_location of this OperationStatus.

        When the operation succeeds successfully, for snapshot taking operation the snapshot id will be included in this field, and for snapshot applying operation, the path to get the target object will be returned in this field.

        :param resource_location: The resource_location of this OperationStatus.
        :type resource_location: str
        """

        self._resource_location = resource_location

    @property
    def status(self):
        """Gets the status of this OperationStatus.

        Operation status: notstarted, running, succeeded, failed. If the operation is requested and waiting to perform, the status is notstarted. If the operation is ongoing in backend, the status is running. Status succeeded means the operation is completed successfully, specifically for snapshot taking operation, it illustrates the snapshot is well taken and ready to apply, and for snapshot applying operation, it presents the target object has finished creating by the snapshot and ready to be used. Status failed is often caused by editing the source object while taking the snapshot or editing the target object while applying the snapshot before completion, see the field \"message\" to check the failure reason.

        :return: The status of this OperationStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OperationStatus.

        Operation status: notstarted, running, succeeded, failed. If the operation is requested and waiting to perform, the status is notstarted. If the operation is ongoing in backend, the status is running. Status succeeded means the operation is completed successfully, specifically for snapshot taking operation, it illustrates the snapshot is well taken and ready to apply, and for snapshot applying operation, it presents the target object has finished creating by the snapshot and ready to be used. Status failed is often caused by editing the source object while taking the snapshot or editing the target object while applying the snapshot before completion, see the field \"message\" to check the failure reason.

        :param status: The status of this OperationStatus.
        :type status: str
        """
        allowed_values = ["notstarted", "running", "succeeded", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
