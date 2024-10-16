# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TaskTemplate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, archived: bool=None, created_at: str=None, default_assignee_group: int=None, default_assignee_user: str=None, default_category: int=None, default_due_date_offset: str=None, default_note: str=None, default_priority: str=None, default_status: int=None, default_title: str=None, id: int=None, name: str=None, practice_group: str=None, updated_at: str=None):
        """TaskTemplate - a model defined in OpenAPI

        :param archived: The archived of this TaskTemplate.
        :param created_at: The created_at of this TaskTemplate.
        :param default_assignee_group: The default_assignee_group of this TaskTemplate.
        :param default_assignee_user: The default_assignee_user of this TaskTemplate.
        :param default_category: The default_category of this TaskTemplate.
        :param default_due_date_offset: The default_due_date_offset of this TaskTemplate.
        :param default_note: The default_note of this TaskTemplate.
        :param default_priority: The default_priority of this TaskTemplate.
        :param default_status: The default_status of this TaskTemplate.
        :param default_title: The default_title of this TaskTemplate.
        :param id: The id of this TaskTemplate.
        :param name: The name of this TaskTemplate.
        :param practice_group: The practice_group of this TaskTemplate.
        :param updated_at: The updated_at of this TaskTemplate.
        """
        self.openapi_types = {
            'archived': bool,
            'created_at': str,
            'default_assignee_group': int,
            'default_assignee_user': str,
            'default_category': int,
            'default_due_date_offset': str,
            'default_note': str,
            'default_priority': str,
            'default_status': int,
            'default_title': str,
            'id': int,
            'name': str,
            'practice_group': str,
            'updated_at': str
        }

        self.attribute_map = {
            'archived': 'archived',
            'created_at': 'created_at',
            'default_assignee_group': 'default_assignee_group',
            'default_assignee_user': 'default_assignee_user',
            'default_category': 'default_category',
            'default_due_date_offset': 'default_due_date_offset',
            'default_note': 'default_note',
            'default_priority': 'default_priority',
            'default_status': 'default_status',
            'default_title': 'default_title',
            'id': 'id',
            'name': 'name',
            'practice_group': 'practice_group',
            'updated_at': 'updated_at'
        }

        self._archived = archived
        self._created_at = created_at
        self._default_assignee_group = default_assignee_group
        self._default_assignee_user = default_assignee_user
        self._default_category = default_category
        self._default_due_date_offset = default_due_date_offset
        self._default_note = default_note
        self._default_priority = default_priority
        self._default_status = default_status
        self._default_title = default_title
        self._id = id
        self._name = name
        self._practice_group = practice_group
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaskTemplate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaskTemplate of this TaskTemplate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def archived(self):
        """Gets the archived of this TaskTemplate.

        

        :return: The archived of this TaskTemplate.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this TaskTemplate.

        

        :param archived: The archived of this TaskTemplate.
        :type archived: bool
        """

        self._archived = archived

    @property
    def created_at(self):
        """Gets the created_at of this TaskTemplate.

        

        :return: The created_at of this TaskTemplate.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskTemplate.

        

        :param created_at: The created_at of this TaskTemplate.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def default_assignee_group(self):
        """Gets the default_assignee_group of this TaskTemplate.

        

        :return: The default_assignee_group of this TaskTemplate.
        :rtype: int
        """
        return self._default_assignee_group

    @default_assignee_group.setter
    def default_assignee_group(self, default_assignee_group):
        """Sets the default_assignee_group of this TaskTemplate.

        

        :param default_assignee_group: The default_assignee_group of this TaskTemplate.
        :type default_assignee_group: int
        """

        self._default_assignee_group = default_assignee_group

    @property
    def default_assignee_user(self):
        """Gets the default_assignee_user of this TaskTemplate.

        

        :return: The default_assignee_user of this TaskTemplate.
        :rtype: str
        """
        return self._default_assignee_user

    @default_assignee_user.setter
    def default_assignee_user(self, default_assignee_user):
        """Sets the default_assignee_user of this TaskTemplate.

        

        :param default_assignee_user: The default_assignee_user of this TaskTemplate.
        :type default_assignee_user: str
        """

        self._default_assignee_user = default_assignee_user

    @property
    def default_category(self):
        """Gets the default_category of this TaskTemplate.

        

        :return: The default_category of this TaskTemplate.
        :rtype: int
        """
        return self._default_category

    @default_category.setter
    def default_category(self, default_category):
        """Sets the default_category of this TaskTemplate.

        

        :param default_category: The default_category of this TaskTemplate.
        :type default_category: int
        """

        self._default_category = default_category

    @property
    def default_due_date_offset(self):
        """Gets the default_due_date_offset of this TaskTemplate.

        Offset due date, format should follow `\"[DD] [HH:[MM:]]ss[.uuuuuu]\"`

        :return: The default_due_date_offset of this TaskTemplate.
        :rtype: str
        """
        return self._default_due_date_offset

    @default_due_date_offset.setter
    def default_due_date_offset(self, default_due_date_offset):
        """Sets the default_due_date_offset of this TaskTemplate.

        Offset due date, format should follow `\"[DD] [HH:[MM:]]ss[.uuuuuu]\"`

        :param default_due_date_offset: The default_due_date_offset of this TaskTemplate.
        :type default_due_date_offset: str
        """

        self._default_due_date_offset = default_due_date_offset

    @property
    def default_note(self):
        """Gets the default_note of this TaskTemplate.

        

        :return: The default_note of this TaskTemplate.
        :rtype: str
        """
        return self._default_note

    @default_note.setter
    def default_note(self, default_note):
        """Sets the default_note of this TaskTemplate.

        

        :param default_note: The default_note of this TaskTemplate.
        :type default_note: str
        """

        self._default_note = default_note

    @property
    def default_priority(self):
        """Gets the default_priority of this TaskTemplate.

        Can be one of the following 10(Low), 20(Medium), 30(High), 40(Urgent)

        :return: The default_priority of this TaskTemplate.
        :rtype: str
        """
        return self._default_priority

    @default_priority.setter
    def default_priority(self, default_priority):
        """Sets the default_priority of this TaskTemplate.

        Can be one of the following 10(Low), 20(Medium), 30(High), 40(Urgent)

        :param default_priority: The default_priority of this TaskTemplate.
        :type default_priority: str
        """
        allowed_values = ["10", "20", "30", "40"]  # noqa: E501
        if default_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `default_priority` ({0}), must be one of {1}"
                .format(default_priority, allowed_values)
            )

        self._default_priority = default_priority

    @property
    def default_status(self):
        """Gets the default_status of this TaskTemplate.

        

        :return: The default_status of this TaskTemplate.
        :rtype: int
        """
        return self._default_status

    @default_status.setter
    def default_status(self, default_status):
        """Sets the default_status of this TaskTemplate.

        

        :param default_status: The default_status of this TaskTemplate.
        :type default_status: int
        """

        self._default_status = default_status

    @property
    def default_title(self):
        """Gets the default_title of this TaskTemplate.

        

        :return: The default_title of this TaskTemplate.
        :rtype: str
        """
        return self._default_title

    @default_title.setter
    def default_title(self, default_title):
        """Sets the default_title of this TaskTemplate.

        

        :param default_title: The default_title of this TaskTemplate.
        :type default_title: str
        """

        self._default_title = default_title

    @property
    def id(self):
        """Gets the id of this TaskTemplate.

        

        :return: The id of this TaskTemplate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskTemplate.

        

        :param id: The id of this TaskTemplate.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskTemplate.

        

        :return: The name of this TaskTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskTemplate.

        

        :param name: The name of this TaskTemplate.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def practice_group(self):
        """Gets the practice_group of this TaskTemplate.

        

        :return: The practice_group of this TaskTemplate.
        :rtype: str
        """
        return self._practice_group

    @practice_group.setter
    def practice_group(self, practice_group):
        """Sets the practice_group of this TaskTemplate.

        

        :param practice_group: The practice_group of this TaskTemplate.
        :type practice_group: str
        """

        self._practice_group = practice_group

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskTemplate.

        

        :return: The updated_at of this TaskTemplate.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskTemplate.

        

        :param updated_at: The updated_at of this TaskTemplate.
        :type updated_at: str
        """

        self._updated_at = updated_at
