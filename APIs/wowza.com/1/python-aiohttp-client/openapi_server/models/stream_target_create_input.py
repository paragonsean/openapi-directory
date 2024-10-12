# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.stream_target5 import StreamTarget5
from openapi_server import util


class StreamTargetCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, stream_target: StreamTarget5=None):
        """StreamTargetCreateInput - a model defined in OpenAPI

        :param stream_target: The stream_target of this StreamTargetCreateInput.
        """
        self.openapi_types = {
            'stream_target': StreamTarget5
        }

        self.attribute_map = {
            'stream_target': 'stream_target'
        }

        self._stream_target = stream_target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StreamTargetCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The stream_target_create_input of this StreamTargetCreateInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def stream_target(self):
        """Gets the stream_target of this StreamTargetCreateInput.


        :return: The stream_target of this StreamTargetCreateInput.
        :rtype: StreamTarget5
        """
        return self._stream_target

    @stream_target.setter
    def stream_target(self, stream_target):
        """Sets the stream_target of this StreamTargetCreateInput.


        :param stream_target: The stream_target of this StreamTargetCreateInput.
        :type stream_target: StreamTarget5
        """
        if stream_target is None:
            raise ValueError("Invalid value for `stream_target`, must not be `None`")

        self._stream_target = stream_target
