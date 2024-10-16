# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AlertingJiraBugtrackerSettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, jira_project_id: int=None, jira_project_name: str=None, callback_url: str=None, owner_name: str=None, type: str=None):
        """AlertingJiraBugtrackerSettings - a model defined in OpenAPI

        :param jira_project_id: The jira_project_id of this AlertingJiraBugtrackerSettings.
        :param jira_project_name: The jira_project_name of this AlertingJiraBugtrackerSettings.
        :param callback_url: The callback_url of this AlertingJiraBugtrackerSettings.
        :param owner_name: The owner_name of this AlertingJiraBugtrackerSettings.
        :param type: The type of this AlertingJiraBugtrackerSettings.
        """
        self.openapi_types = {
            'jira_project_id': int,
            'jira_project_name': str,
            'callback_url': str,
            'owner_name': str,
            'type': str
        }

        self.attribute_map = {
            'jira_project_id': 'jira_project_id',
            'jira_project_name': 'jira_project_name',
            'callback_url': 'callback_url',
            'owner_name': 'owner_name',
            'type': 'type'
        }

        self._jira_project_id = jira_project_id
        self._jira_project_name = jira_project_name
        self._callback_url = callback_url
        self._owner_name = owner_name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlertingJiraBugtrackerSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlertingJiraBugtrackerSettings of this AlertingJiraBugtrackerSettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def jira_project_id(self):
        """Gets the jira_project_id of this AlertingJiraBugtrackerSettings.


        :return: The jira_project_id of this AlertingJiraBugtrackerSettings.
        :rtype: int
        """
        return self._jira_project_id

    @jira_project_id.setter
    def jira_project_id(self, jira_project_id):
        """Sets the jira_project_id of this AlertingJiraBugtrackerSettings.


        :param jira_project_id: The jira_project_id of this AlertingJiraBugtrackerSettings.
        :type jira_project_id: int
        """
        if jira_project_id is None:
            raise ValueError("Invalid value for `jira_project_id`, must not be `None`")

        self._jira_project_id = jira_project_id

    @property
    def jira_project_name(self):
        """Gets the jira_project_name of this AlertingJiraBugtrackerSettings.


        :return: The jira_project_name of this AlertingJiraBugtrackerSettings.
        :rtype: str
        """
        return self._jira_project_name

    @jira_project_name.setter
    def jira_project_name(self, jira_project_name):
        """Sets the jira_project_name of this AlertingJiraBugtrackerSettings.


        :param jira_project_name: The jira_project_name of this AlertingJiraBugtrackerSettings.
        :type jira_project_name: str
        """
        if jira_project_name is None:
            raise ValueError("Invalid value for `jira_project_name`, must not be `None`")

        self._jira_project_name = jira_project_name

    @property
    def callback_url(self):
        """Gets the callback_url of this AlertingJiraBugtrackerSettings.


        :return: The callback_url of this AlertingJiraBugtrackerSettings.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this AlertingJiraBugtrackerSettings.


        :param callback_url: The callback_url of this AlertingJiraBugtrackerSettings.
        :type callback_url: str
        """

        self._callback_url = callback_url

    @property
    def owner_name(self):
        """Gets the owner_name of this AlertingJiraBugtrackerSettings.


        :return: The owner_name of this AlertingJiraBugtrackerSettings.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this AlertingJiraBugtrackerSettings.


        :param owner_name: The owner_name of this AlertingJiraBugtrackerSettings.
        :type owner_name: str
        """
        if owner_name is None:
            raise ValueError("Invalid value for `owner_name`, must not be `None`")

        self._owner_name = owner_name

    @property
    def type(self):
        """Gets the type of this AlertingJiraBugtrackerSettings.

        type of bugtracker

        :return: The type of this AlertingJiraBugtrackerSettings.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertingJiraBugtrackerSettings.

        type of bugtracker

        :param type: The type of this AlertingJiraBugtrackerSettings.
        :type type: str
        """
        allowed_values = ["github", "vsts", "jira"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
