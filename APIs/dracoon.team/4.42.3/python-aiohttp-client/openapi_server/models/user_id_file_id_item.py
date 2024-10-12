# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserIdFileIdItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_id: int=None, user_id: int=None):
        """UserIdFileIdItem - a model defined in OpenAPI

        :param file_id: The file_id of this UserIdFileIdItem.
        :param user_id: The user_id of this UserIdFileIdItem.
        """
        self.openapi_types = {
            'file_id': int,
            'user_id': int
        }

        self.attribute_map = {
            'file_id': 'fileId',
            'user_id': 'userId'
        }

        self._file_id = file_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserIdFileIdItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserIdFileIdItem of this UserIdFileIdItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_id(self):
        """Gets the file_id of this UserIdFileIdItem.

        File ID

        :return: The file_id of this UserIdFileIdItem.
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this UserIdFileIdItem.

        File ID

        :param file_id: The file_id of this UserIdFileIdItem.
        :type file_id: int
        """

        self._file_id = file_id

    @property
    def user_id(self):
        """Gets the user_id of this UserIdFileIdItem.

        Unique identifier for the user

        :return: The user_id of this UserIdFileIdItem.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserIdFileIdItem.

        Unique identifier for the user

        :param user_id: The user_id of this UserIdFileIdItem.
        :type user_id: int
        """

        self._user_id = user_id
