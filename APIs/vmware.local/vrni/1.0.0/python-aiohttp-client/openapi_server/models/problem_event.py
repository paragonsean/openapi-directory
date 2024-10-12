# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_event import BaseEvent
from openapi_server.models.entity_type import EntityType
from openapi_server.models.reference import Reference
from openapi_server import util


class ProblemEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: str=None, entity_type: EntityType=None, name: str=None, admin_state: str=None, anchor_entities: List[Reference]=None, archived: bool=None, event_tags: List[str]=None, event_time_epoch_ms: int=None, message: str=None, related_entities: List[Reference]=None, event_close_time_epoch_ms: int=None, severity: str=None):
        """ProblemEvent - a model defined in OpenAPI

        :param entity_id: The entity_id of this ProblemEvent.
        :param entity_type: The entity_type of this ProblemEvent.
        :param name: The name of this ProblemEvent.
        :param admin_state: The admin_state of this ProblemEvent.
        :param anchor_entities: The anchor_entities of this ProblemEvent.
        :param archived: The archived of this ProblemEvent.
        :param event_tags: The event_tags of this ProblemEvent.
        :param event_time_epoch_ms: The event_time_epoch_ms of this ProblemEvent.
        :param message: The message of this ProblemEvent.
        :param related_entities: The related_entities of this ProblemEvent.
        :param event_close_time_epoch_ms: The event_close_time_epoch_ms of this ProblemEvent.
        :param severity: The severity of this ProblemEvent.
        """
        self.openapi_types = {
            'entity_id': str,
            'entity_type': EntityType,
            'name': str,
            'admin_state': str,
            'anchor_entities': List[Reference],
            'archived': bool,
            'event_tags': List[str],
            'event_time_epoch_ms': int,
            'message': str,
            'related_entities': List[Reference],
            'event_close_time_epoch_ms': int,
            'severity': str
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'name': 'name',
            'admin_state': 'admin_state',
            'anchor_entities': 'anchor_entities',
            'archived': 'archived',
            'event_tags': 'event_tags',
            'event_time_epoch_ms': 'event_time_epoch_ms',
            'message': 'message',
            'related_entities': 'related_entities',
            'event_close_time_epoch_ms': 'event_close_time_epoch_ms',
            'severity': 'severity'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._name = name
        self._admin_state = admin_state
        self._anchor_entities = anchor_entities
        self._archived = archived
        self._event_tags = event_tags
        self._event_time_epoch_ms = event_time_epoch_ms
        self._message = message
        self._related_entities = related_entities
        self._event_close_time_epoch_ms = event_close_time_epoch_ms
        self._severity = severity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProblemEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProblemEvent of this ProblemEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this ProblemEvent.


        :return: The entity_id of this ProblemEvent.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ProblemEvent.


        :param entity_id: The entity_id of this ProblemEvent.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this ProblemEvent.


        :return: The entity_type of this ProblemEvent.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ProblemEvent.


        :param entity_type: The entity_type of this ProblemEvent.
        :type entity_type: EntityType
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this ProblemEvent.


        :return: The name of this ProblemEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProblemEvent.


        :param name: The name of this ProblemEvent.
        :type name: str
        """

        self._name = name

    @property
    def admin_state(self):
        """Gets the admin_state of this ProblemEvent.


        :return: The admin_state of this ProblemEvent.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this ProblemEvent.


        :param admin_state: The admin_state of this ProblemEvent.
        :type admin_state: str
        """
        allowed_values = ["ENABLED", "DISABLED"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def anchor_entities(self):
        """Gets the anchor_entities of this ProblemEvent.


        :return: The anchor_entities of this ProblemEvent.
        :rtype: List[Reference]
        """
        return self._anchor_entities

    @anchor_entities.setter
    def anchor_entities(self, anchor_entities):
        """Sets the anchor_entities of this ProblemEvent.


        :param anchor_entities: The anchor_entities of this ProblemEvent.
        :type anchor_entities: List[Reference]
        """

        self._anchor_entities = anchor_entities

    @property
    def archived(self):
        """Gets the archived of this ProblemEvent.


        :return: The archived of this ProblemEvent.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ProblemEvent.


        :param archived: The archived of this ProblemEvent.
        :type archived: bool
        """

        self._archived = archived

    @property
    def event_tags(self):
        """Gets the event_tags of this ProblemEvent.


        :return: The event_tags of this ProblemEvent.
        :rtype: List[str]
        """
        return self._event_tags

    @event_tags.setter
    def event_tags(self, event_tags):
        """Sets the event_tags of this ProblemEvent.


        :param event_tags: The event_tags of this ProblemEvent.
        :type event_tags: List[str]
        """

        self._event_tags = event_tags

    @property
    def event_time_epoch_ms(self):
        """Gets the event_time_epoch_ms of this ProblemEvent.


        :return: The event_time_epoch_ms of this ProblemEvent.
        :rtype: int
        """
        return self._event_time_epoch_ms

    @event_time_epoch_ms.setter
    def event_time_epoch_ms(self, event_time_epoch_ms):
        """Sets the event_time_epoch_ms of this ProblemEvent.


        :param event_time_epoch_ms: The event_time_epoch_ms of this ProblemEvent.
        :type event_time_epoch_ms: int
        """

        self._event_time_epoch_ms = event_time_epoch_ms

    @property
    def message(self):
        """Gets the message of this ProblemEvent.


        :return: The message of this ProblemEvent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProblemEvent.


        :param message: The message of this ProblemEvent.
        :type message: str
        """

        self._message = message

    @property
    def related_entities(self):
        """Gets the related_entities of this ProblemEvent.


        :return: The related_entities of this ProblemEvent.
        :rtype: List[Reference]
        """
        return self._related_entities

    @related_entities.setter
    def related_entities(self, related_entities):
        """Sets the related_entities of this ProblemEvent.


        :param related_entities: The related_entities of this ProblemEvent.
        :type related_entities: List[Reference]
        """

        self._related_entities = related_entities

    @property
    def event_close_time_epoch_ms(self):
        """Gets the event_close_time_epoch_ms of this ProblemEvent.


        :return: The event_close_time_epoch_ms of this ProblemEvent.
        :rtype: int
        """
        return self._event_close_time_epoch_ms

    @event_close_time_epoch_ms.setter
    def event_close_time_epoch_ms(self, event_close_time_epoch_ms):
        """Sets the event_close_time_epoch_ms of this ProblemEvent.


        :param event_close_time_epoch_ms: The event_close_time_epoch_ms of this ProblemEvent.
        :type event_close_time_epoch_ms: int
        """

        self._event_close_time_epoch_ms = event_close_time_epoch_ms

    @property
    def severity(self):
        """Gets the severity of this ProblemEvent.


        :return: The severity of this ProblemEvent.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ProblemEvent.


        :param severity: The severity of this ProblemEvent.
        :type severity: str
        """
        allowed_values = ["CRITICAL", "MODERATE", "WARNING", "INFO"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity
