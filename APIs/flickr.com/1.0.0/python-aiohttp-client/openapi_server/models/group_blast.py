# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GroupBlast(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content: str=None, date_blast_added: str=None, user_id: str=None):
        """GroupBlast - a model defined in OpenAPI

        :param content: The content of this GroupBlast.
        :param date_blast_added: The date_blast_added of this GroupBlast.
        :param user_id: The user_id of this GroupBlast.
        """
        self.openapi_types = {
            'content': str,
            'date_blast_added': str,
            'user_id': str
        }

        self.attribute_map = {
            'content': '_content',
            'date_blast_added': 'date_blast_added',
            'user_id': 'user_id'
        }

        self._content = content
        self._date_blast_added = date_blast_added
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GroupBlast':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Group_blast of this GroupBlast.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self):
        """Gets the content of this GroupBlast.


        :return: The content of this GroupBlast.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GroupBlast.


        :param content: The content of this GroupBlast.
        :type content: str
        """

        self._content = content

    @property
    def date_blast_added(self):
        """Gets the date_blast_added of this GroupBlast.


        :return: The date_blast_added of this GroupBlast.
        :rtype: str
        """
        return self._date_blast_added

    @date_blast_added.setter
    def date_blast_added(self, date_blast_added):
        """Sets the date_blast_added of this GroupBlast.


        :param date_blast_added: The date_blast_added of this GroupBlast.
        :type date_blast_added: str
        """

        self._date_blast_added = date_blast_added

    @property
    def user_id(self):
        """Gets the user_id of this GroupBlast.


        :return: The user_id of this GroupBlast.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupBlast.


        :param user_id: The user_id of this GroupBlast.
        :type user_id: str
        """

        self._user_id = user_id
