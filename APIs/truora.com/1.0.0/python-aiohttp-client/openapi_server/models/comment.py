# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Comment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, check_id: str=None, content: str=None, creation_date: str=None, id: str=None, parent_id: str=None, update_date: str=None, username: str=None):
        """Comment - a model defined in OpenAPI

        :param check_id: The check_id of this Comment.
        :param content: The content of this Comment.
        :param creation_date: The creation_date of this Comment.
        :param id: The id of this Comment.
        :param parent_id: The parent_id of this Comment.
        :param update_date: The update_date of this Comment.
        :param username: The username of this Comment.
        """
        self.openapi_types = {
            'check_id': str,
            'content': str,
            'creation_date': str,
            'id': str,
            'parent_id': str,
            'update_date': str,
            'username': str
        }

        self.attribute_map = {
            'check_id': 'check_id',
            'content': 'content',
            'creation_date': 'creation_date',
            'id': 'id',
            'parent_id': 'parent_id',
            'update_date': 'update_date',
            'username': 'username'
        }

        self._check_id = check_id
        self._content = content
        self._creation_date = creation_date
        self._id = id
        self._parent_id = parent_id
        self._update_date = update_date
        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Comment of this Comment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def check_id(self):
        """Gets the check_id of this Comment.

        Background check ID

        :return: The check_id of this Comment.
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this Comment.

        Background check ID

        :param check_id: The check_id of this Comment.
        :type check_id: str
        """
        if check_id is None:
            raise ValueError("Invalid value for `check_id`, must not be `None`")

        self._check_id = check_id

    @property
    def content(self):
        """Gets the content of this Comment.

        Comment content

        :return: The content of this Comment.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Comment.

        Comment content

        :param content: The content of this Comment.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

        self._content = content

    @property
    def creation_date(self):
        """Gets the creation_date of this Comment.

        Comment creation date

        :return: The creation_date of this Comment.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Comment.

        Comment creation date

        :param creation_date: The creation_date of this Comment.
        :type creation_date: str
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")

        self._creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this Comment.

        Comment ID

        :return: The id of this Comment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.

        Comment ID

        :param id: The id of this Comment.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this Comment.

        Comment parent ID

        :return: The parent_id of this Comment.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Comment.

        Comment parent ID

        :param parent_id: The parent_id of this Comment.
        :type parent_id: str
        """

        self._parent_id = parent_id

    @property
    def update_date(self):
        """Gets the update_date of this Comment.

        Comment update date

        :return: The update_date of this Comment.
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this Comment.

        Comment update date

        :param update_date: The update_date of this Comment.
        :type update_date: str
        """
        if update_date is None:
            raise ValueError("Invalid value for `update_date`, must not be `None`")

        self._update_date = update_date

    @property
    def username(self):
        """Gets the username of this Comment.

        Comment creator username

        :return: The username of this Comment.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Comment.

        Comment creator username

        :param username: The username of this Comment.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username
