# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NotificationChannelActivationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, channel_id: int=None, is_enabled: bool=None):
        """NotificationChannelActivationRequest - a model defined in OpenAPI

        :param channel_id: The channel_id of this NotificationChannelActivationRequest.
        :param is_enabled: The is_enabled of this NotificationChannelActivationRequest.
        """
        self.openapi_types = {
            'channel_id': int,
            'is_enabled': bool
        }

        self.attribute_map = {
            'channel_id': 'channelId',
            'is_enabled': 'isEnabled'
        }

        self._channel_id = channel_id
        self._is_enabled = is_enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationChannelActivationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationChannelActivationRequest of this NotificationChannelActivationRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel_id(self):
        """Gets the channel_id of this NotificationChannelActivationRequest.

        Channel ID

        :return: The channel_id of this NotificationChannelActivationRequest.
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this NotificationChannelActivationRequest.

        Channel ID

        :param channel_id: The channel_id of this NotificationChannelActivationRequest.
        :type channel_id: int
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")

        self._channel_id = channel_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this NotificationChannelActivationRequest.

        Determines whether channel is enabled

        :return: The is_enabled of this NotificationChannelActivationRequest.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this NotificationChannelActivationRequest.

        Determines whether channel is enabled

        :param is_enabled: The is_enabled of this NotificationChannelActivationRequest.
        :type is_enabled: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")

        self._is_enabled = is_enabled
