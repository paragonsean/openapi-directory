# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.test_created_by import TestCreatedBy
from openapi_server import util


class Test(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: int=None, created_by: TestCreatedBy=None, default_environment_id: str=None, description: str=None, id: str=None, last_run: object=None, name: str=None, trigger_url: str=None):
        """Test - a model defined in OpenAPI

        :param created_at: The created_at of this Test.
        :param created_by: The created_by of this Test.
        :param default_environment_id: The default_environment_id of this Test.
        :param description: The description of this Test.
        :param id: The id of this Test.
        :param last_run: The last_run of this Test.
        :param name: The name of this Test.
        :param trigger_url: The trigger_url of this Test.
        """
        self.openapi_types = {
            'created_at': int,
            'created_by': TestCreatedBy,
            'default_environment_id': str,
            'description': str,
            'id': str,
            'last_run': object,
            'name': str,
            'trigger_url': str
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'created_by': 'created_by',
            'default_environment_id': 'default_environment_id',
            'description': 'description',
            'id': 'id',
            'last_run': 'last_run',
            'name': 'name',
            'trigger_url': 'trigger_url'
        }

        self._created_at = created_at
        self._created_by = created_by
        self._default_environment_id = default_environment_id
        self._description = description
        self._id = id
        self._last_run = last_run
        self._name = name
        self._trigger_url = trigger_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Test':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Test of this Test.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this Test.

        The date the test was created in seconds (Unix time stamp format).

        :return: The created_at of this Test.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Test.

        The date the test was created in seconds (Unix time stamp format).

        :param created_at: The created_at of this Test.
        :type created_at: int
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Test.


        :return: The created_by of this Test.
        :rtype: TestCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Test.


        :param created_by: The created_by of this Test.
        :type created_by: TestCreatedBy
        """

        self._created_by = created_by

    @property
    def default_environment_id(self):
        """Gets the default_environment_id of this Test.


        :return: The default_environment_id of this Test.
        :rtype: str
        """
        return self._default_environment_id

    @default_environment_id.setter
    def default_environment_id(self, default_environment_id):
        """Sets the default_environment_id of this Test.


        :param default_environment_id: The default_environment_id of this Test.
        :type default_environment_id: str
        """

        self._default_environment_id = default_environment_id

    @property
    def description(self):
        """Gets the description of this Test.

        The description for the test.

        :return: The description of this Test.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Test.

        The description for the test.

        :param description: The description of this Test.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Test.


        :return: The id of this Test.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Test.


        :param id: The id of this Test.
        :type id: str
        """

        self._id = id

    @property
    def last_run(self):
        """Gets the last_run of this Test.


        :return: The last_run of this Test.
        :rtype: object
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this Test.


        :param last_run: The last_run of this Test.
        :type last_run: object
        """

        self._last_run = last_run

    @property
    def name(self):
        """Gets the name of this Test.

        The name for the test.

        :return: The name of this Test.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Test.

        The name for the test.

        :param name: The name of this Test.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def trigger_url(self):
        """Gets the trigger_url of this Test.


        :return: The trigger_url of this Test.
        :rtype: str
        """
        return self._trigger_url

    @trigger_url.setter
    def trigger_url(self, trigger_url):
        """Sets the trigger_url of this Test.


        :param trigger_url: The trigger_url of this Test.
        :type trigger_url: str
        """

        self._trigger_url = trigger_url
