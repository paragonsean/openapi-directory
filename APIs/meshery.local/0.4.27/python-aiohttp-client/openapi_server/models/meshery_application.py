# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MesheryApplication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application_file: str=None, created_at: datetime=None, id: List[int]=None, location: Dict[str, object]=None, name: str=None, updated_at: datetime=None, user_id: str=None):
        """MesheryApplication - a model defined in OpenAPI

        :param application_file: The application_file of this MesheryApplication.
        :param created_at: The created_at of this MesheryApplication.
        :param id: The id of this MesheryApplication.
        :param location: The location of this MesheryApplication.
        :param name: The name of this MesheryApplication.
        :param updated_at: The updated_at of this MesheryApplication.
        :param user_id: The user_id of this MesheryApplication.
        """
        self.openapi_types = {
            'application_file': str,
            'created_at': datetime,
            'id': List[int],
            'location': Dict[str, object],
            'name': str,
            'updated_at': datetime,
            'user_id': str
        }

        self.attribute_map = {
            'application_file': 'application_file',
            'created_at': 'created_at',
            'id': 'id',
            'location': 'location',
            'name': 'name',
            'updated_at': 'updated_at',
            'user_id': 'user_id'
        }

        self._application_file = application_file
        self._created_at = created_at
        self._id = id
        self._location = location
        self._name = name
        self._updated_at = updated_at
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MesheryApplication':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MesheryApplication of this MesheryApplication.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application_file(self):
        """Gets the application_file of this MesheryApplication.


        :return: The application_file of this MesheryApplication.
        :rtype: str
        """
        return self._application_file

    @application_file.setter
    def application_file(self, application_file):
        """Sets the application_file of this MesheryApplication.


        :param application_file: The application_file of this MesheryApplication.
        :type application_file: str
        """

        self._application_file = application_file

    @property
    def created_at(self):
        """Gets the created_at of this MesheryApplication.


        :return: The created_at of this MesheryApplication.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MesheryApplication.


        :param created_at: The created_at of this MesheryApplication.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this MesheryApplication.


        :return: The id of this MesheryApplication.
        :rtype: List[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MesheryApplication.


        :param id: The id of this MesheryApplication.
        :type id: List[int]
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this MesheryApplication.

        It implements native SQL driver interfaces and hence can be used for SQL json or jsonb types as a drop in replacement of golang native maps

        :return: The location of this MesheryApplication.
        :rtype: Dict[str, object]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MesheryApplication.

        It implements native SQL driver interfaces and hence can be used for SQL json or jsonb types as a drop in replacement of golang native maps

        :param location: The location of this MesheryApplication.
        :type location: Dict[str, object]
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this MesheryApplication.


        :return: The name of this MesheryApplication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MesheryApplication.


        :param name: The name of this MesheryApplication.
        :type name: str
        """

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this MesheryApplication.


        :return: The updated_at of this MesheryApplication.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MesheryApplication.


        :param updated_at: The updated_at of this MesheryApplication.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this MesheryApplication.

        Meshery doesn't have the user id fields but the remote provider is allowed to provide one

        :return: The user_id of this MesheryApplication.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MesheryApplication.

        Meshery doesn't have the user id fields but the remote provider is allowed to provide one

        :param user_id: The user_id of this MesheryApplication.
        :type user_id: str
        """

        self._user_id = user_id
