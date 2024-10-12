# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NotificationConfigChangeRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, channel_ids: List[int]=None):
        """NotificationConfigChangeRequest - a model defined in OpenAPI

        :param channel_ids: The channel_ids of this NotificationConfigChangeRequest.
        """
        self.openapi_types = {
            'channel_ids': List[int]
        }

        self.attribute_map = {
            'channel_ids': 'channelIds'
        }

        self._channel_ids = channel_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationConfigChangeRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationConfigChangeRequest of this NotificationConfigChangeRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel_ids(self):
        """Gets the channel_ids of this NotificationConfigChangeRequest.

        List of notification channel IDs.  Leave empty to disable notifications.

        :return: The channel_ids of this NotificationConfigChangeRequest.
        :rtype: List[int]
        """
        return self._channel_ids

    @channel_ids.setter
    def channel_ids(self, channel_ids):
        """Sets the channel_ids of this NotificationConfigChangeRequest.

        List of notification channel IDs.  Leave empty to disable notifications.

        :param channel_ids: The channel_ids of this NotificationConfigChangeRequest.
        :type channel_ids: List[int]
        """
        if channel_ids is None:
            raise ValueError("Invalid value for `channel_ids`, must not be `None`")

        self._channel_ids = channel_ids
