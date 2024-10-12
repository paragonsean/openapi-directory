# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.custom_stream_target1 import CustomStreamTarget1
from openapi_server import util


class UllStreamTargetInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, stream_target: CustomStreamTarget1=None):
        """UllStreamTargetInput - a model defined in OpenAPI

        :param stream_target: The stream_target of this UllStreamTargetInput.
        """
        self.openapi_types = {
            'stream_target': CustomStreamTarget1
        }

        self.attribute_map = {
            'stream_target': 'stream_target'
        }

        self._stream_target = stream_target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UllStreamTargetInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ull_stream_target_input of this UllStreamTargetInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def stream_target(self):
        """Gets the stream_target of this UllStreamTargetInput.


        :return: The stream_target of this UllStreamTargetInput.
        :rtype: CustomStreamTarget1
        """
        return self._stream_target

    @stream_target.setter
    def stream_target(self, stream_target):
        """Sets the stream_target of this UllStreamTargetInput.


        :param stream_target: The stream_target of this UllStreamTargetInput.
        :type stream_target: CustomStreamTarget1
        """
        if stream_target is None:
            raise ValueError("Invalid value for `stream_target`, must not be `None`")

        self._stream_target = stream_target
