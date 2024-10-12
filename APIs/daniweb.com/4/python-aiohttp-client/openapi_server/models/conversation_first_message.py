# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user import User
from openapi_server import util


class ConversationFirstMessage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, author: User=None, timestamp: datetime=None):
        """ConversationFirstMessage - a model defined in OpenAPI

        :param author: The author of this ConversationFirstMessage.
        :param timestamp: The timestamp of this ConversationFirstMessage.
        """
        self.openapi_types = {
            'author': User,
            'timestamp': datetime
        }

        self.attribute_map = {
            'author': 'author',
            'timestamp': 'timestamp'
        }

        self._author = author
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConversationFirstMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Conversation_first_message of this ConversationFirstMessage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def author(self):
        """Gets the author of this ConversationFirstMessage.


        :return: The author of this ConversationFirstMessage.
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ConversationFirstMessage.


        :param author: The author of this ConversationFirstMessage.
        :type author: User
        """

        self._author = author

    @property
    def timestamp(self):
        """Gets the timestamp of this ConversationFirstMessage.


        :return: The timestamp of this ConversationFirstMessage.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ConversationFirstMessage.


        :param timestamp: The timestamp of this ConversationFirstMessage.
        :type timestamp: datetime
        """

        self._timestamp = timestamp
