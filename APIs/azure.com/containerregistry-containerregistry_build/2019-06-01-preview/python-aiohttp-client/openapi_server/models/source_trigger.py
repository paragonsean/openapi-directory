# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.source_properties import SourceProperties
from openapi_server import util


class SourceTrigger(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, source_repository: SourceProperties=None, source_trigger_events: List[str]=None, status: str='Enabled'):
        """SourceTrigger - a model defined in OpenAPI

        :param name: The name of this SourceTrigger.
        :param source_repository: The source_repository of this SourceTrigger.
        :param source_trigger_events: The source_trigger_events of this SourceTrigger.
        :param status: The status of this SourceTrigger.
        """
        self.openapi_types = {
            'name': str,
            'source_repository': SourceProperties,
            'source_trigger_events': List[str],
            'status': str
        }

        self.attribute_map = {
            'name': 'name',
            'source_repository': 'sourceRepository',
            'source_trigger_events': 'sourceTriggerEvents',
            'status': 'status'
        }

        self._name = name
        self._source_repository = source_repository
        self._source_trigger_events = source_trigger_events
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SourceTrigger':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SourceTrigger of this SourceTrigger.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this SourceTrigger.

        The name of the trigger.

        :return: The name of this SourceTrigger.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceTrigger.

        The name of the trigger.

        :param name: The name of this SourceTrigger.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def source_repository(self):
        """Gets the source_repository of this SourceTrigger.


        :return: The source_repository of this SourceTrigger.
        :rtype: SourceProperties
        """
        return self._source_repository

    @source_repository.setter
    def source_repository(self, source_repository):
        """Sets the source_repository of this SourceTrigger.


        :param source_repository: The source_repository of this SourceTrigger.
        :type source_repository: SourceProperties
        """
        if source_repository is None:
            raise ValueError("Invalid value for `source_repository`, must not be `None`")

        self._source_repository = source_repository

    @property
    def source_trigger_events(self):
        """Gets the source_trigger_events of this SourceTrigger.

        The source event corresponding to the trigger.

        :return: The source_trigger_events of this SourceTrigger.
        :rtype: List[str]
        """
        return self._source_trigger_events

    @source_trigger_events.setter
    def source_trigger_events(self, source_trigger_events):
        """Sets the source_trigger_events of this SourceTrigger.

        The source event corresponding to the trigger.

        :param source_trigger_events: The source_trigger_events of this SourceTrigger.
        :type source_trigger_events: List[str]
        """
        allowed_values = ["commit", "pullrequest"]  # noqa: E501
        if not set(source_trigger_events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `source_trigger_events` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(source_trigger_events) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._source_trigger_events = source_trigger_events

    @property
    def status(self):
        """Gets the status of this SourceTrigger.

        The current status of trigger.

        :return: The status of this SourceTrigger.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SourceTrigger.

        The current status of trigger.

        :param status: The status of this SourceTrigger.
        :type status: str
        """
        allowed_values = ["Disabled", "Enabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
