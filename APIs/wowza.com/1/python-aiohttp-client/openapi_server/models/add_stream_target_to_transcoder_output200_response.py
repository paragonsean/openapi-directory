# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.output_stream_target import OutputStreamTarget
from openapi_server import util


class AddStreamTargetToTranscoderOutput200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output_stream_target: OutputStreamTarget=None):
        """AddStreamTargetToTranscoderOutput200Response - a model defined in OpenAPI

        :param output_stream_target: The output_stream_target of this AddStreamTargetToTranscoderOutput200Response.
        """
        self.openapi_types = {
            'output_stream_target': OutputStreamTarget
        }

        self.attribute_map = {
            'output_stream_target': 'output_stream_target'
        }

        self._output_stream_target = output_stream_target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddStreamTargetToTranscoderOutput200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The addStreamTargetToTranscoderOutput_200_response of this AddStreamTargetToTranscoderOutput200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output_stream_target(self):
        """Gets the output_stream_target of this AddStreamTargetToTranscoderOutput200Response.


        :return: The output_stream_target of this AddStreamTargetToTranscoderOutput200Response.
        :rtype: OutputStreamTarget
        """
        return self._output_stream_target

    @output_stream_target.setter
    def output_stream_target(self, output_stream_target):
        """Sets the output_stream_target of this AddStreamTargetToTranscoderOutput200Response.


        :param output_stream_target: The output_stream_target of this AddStreamTargetToTranscoderOutput200Response.
        :type output_stream_target: OutputStreamTarget
        """
        if output_stream_target is None:
            raise ValueError("Invalid value for `output_stream_target`, must not be `None`")

        self._output_stream_target = output_stream_target
