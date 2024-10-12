# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user import User
from openapi_server import util


class EndpointPostUsersInvitesDataExisting(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, conversations: List[User]=None):
        """EndpointPostUsersInvitesDataExisting - a model defined in OpenAPI

        :param conversations: The conversations of this EndpointPostUsersInvitesDataExisting.
        """
        self.openapi_types = {
            'conversations': List[User]
        }

        self.attribute_map = {
            'conversations': 'conversations'
        }

        self._conversations = conversations

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPostUsersInvitesDataExisting':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint_post_users_invites_data_existing of this EndpointPostUsersInvitesDataExisting.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def conversations(self):
        """Gets the conversations of this EndpointPostUsersInvitesDataExisting.


        :return: The conversations of this EndpointPostUsersInvitesDataExisting.
        :rtype: List[User]
        """
        return self._conversations

    @conversations.setter
    def conversations(self, conversations):
        """Sets the conversations of this EndpointPostUsersInvitesDataExisting.


        :param conversations: The conversations of this EndpointPostUsersInvitesDataExisting.
        :type conversations: List[User]
        """

        self._conversations = conversations
