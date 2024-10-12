# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.output_stream_target import OutputStreamTarget
from openapi_server import util


class OutputStreamTargets(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output_stream_targets: List[OutputStreamTarget]=None):
        """OutputStreamTargets - a model defined in OpenAPI

        :param output_stream_targets: The output_stream_targets of this OutputStreamTargets.
        """
        self.openapi_types = {
            'output_stream_targets': List[OutputStreamTarget]
        }

        self.attribute_map = {
            'output_stream_targets': 'output_stream_targets'
        }

        self._output_stream_targets = output_stream_targets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputStreamTargets':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The output_stream_targets of this OutputStreamTargets.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output_stream_targets(self):
        """Gets the output_stream_targets of this OutputStreamTargets.


        :return: The output_stream_targets of this OutputStreamTargets.
        :rtype: List[OutputStreamTarget]
        """
        return self._output_stream_targets

    @output_stream_targets.setter
    def output_stream_targets(self, output_stream_targets):
        """Sets the output_stream_targets of this OutputStreamTargets.


        :param output_stream_targets: The output_stream_targets of this OutputStreamTargets.
        :type output_stream_targets: List[OutputStreamTarget]
        """
        if output_stream_targets is None:
            raise ValueError("Invalid value for `output_stream_targets`, must not be `None`")

        self._output_stream_targets = output_stream_targets
