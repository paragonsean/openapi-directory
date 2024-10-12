# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.output_stream_target3 import OutputStreamTarget3
from openapi_server import util


class OutputStreamTargetCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output_stream_target: OutputStreamTarget3=None):
        """OutputStreamTargetCreateInput - a model defined in OpenAPI

        :param output_stream_target: The output_stream_target of this OutputStreamTargetCreateInput.
        """
        self.openapi_types = {
            'output_stream_target': OutputStreamTarget3
        }

        self.attribute_map = {
            'output_stream_target': 'output_stream_target'
        }

        self._output_stream_target = output_stream_target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputStreamTargetCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The output_stream_target_create_input of this OutputStreamTargetCreateInput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output_stream_target(self):
        """Gets the output_stream_target of this OutputStreamTargetCreateInput.


        :return: The output_stream_target of this OutputStreamTargetCreateInput.
        :rtype: OutputStreamTarget3
        """
        return self._output_stream_target

    @output_stream_target.setter
    def output_stream_target(self, output_stream_target):
        """Sets the output_stream_target of this OutputStreamTargetCreateInput.


        :param output_stream_target: The output_stream_target of this OutputStreamTargetCreateInput.
        :type output_stream_target: OutputStreamTarget3
        """
        if output_stream_target is None:
            raise ValueError("Invalid value for `output_stream_target`, must not be `None`")

        self._output_stream_target = output_stream_target
