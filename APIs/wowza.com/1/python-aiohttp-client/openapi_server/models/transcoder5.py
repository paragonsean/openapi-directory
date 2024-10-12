# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Transcoder5(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, state: str=None, transcoding_uptime_id: str=None):
        """Transcoder5 - a model defined in OpenAPI

        :param state: The state of this Transcoder5.
        :param transcoding_uptime_id: The transcoding_uptime_id of this Transcoder5.
        """
        self.openapi_types = {
            'state': str,
            'transcoding_uptime_id': str
        }

        self.attribute_map = {
            'state': 'state',
            'transcoding_uptime_id': 'transcoding_uptime_id'
        }

        self._state = state
        self._transcoding_uptime_id = transcoding_uptime_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Transcoder5':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The transcoder_5 of this Transcoder5.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self):
        """Gets the state of this Transcoder5.

        The state of the transcoder.

        :return: The state of this Transcoder5.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Transcoder5.

        The state of the transcoder.

        :param state: The state of this Transcoder5.
        :type state: str
        """
        allowed_values = ["starting", "stopping", "started", "stopped", "resetting"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def transcoding_uptime_id(self):
        """Gets the transcoding_uptime_id of this Transcoder5.

        <strong>The <em>transcoding_uptime_id</em> parameter is deprecated and is replaced by <em>uptime_id</em>.</strong> The unique identifier associated with a specific uptime period of a transcoder.

        :return: The transcoding_uptime_id of this Transcoder5.
        :rtype: str
        """
        return self._transcoding_uptime_id

    @transcoding_uptime_id.setter
    def transcoding_uptime_id(self, transcoding_uptime_id):
        """Sets the transcoding_uptime_id of this Transcoder5.

        <strong>The <em>transcoding_uptime_id</em> parameter is deprecated and is replaced by <em>uptime_id</em>.</strong> The unique identifier associated with a specific uptime period of a transcoder.

        :param transcoding_uptime_id: The transcoding_uptime_id of this Transcoder5.
        :type transcoding_uptime_id: str
        """

        self._transcoding_uptime_id = transcoding_uptime_id
