# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GpuDecoderUsageMetric(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, text: str=None, units: str=None, value: int=None):
        """GpuDecoderUsageMetric - a model defined in OpenAPI

        :param status: The status of this GpuDecoderUsageMetric.
        :param text: The text of this GpuDecoderUsageMetric.
        :param units: The units of this GpuDecoderUsageMetric.
        :param value: The value of this GpuDecoderUsageMetric.
        """
        self.openapi_types = {
            'status': str,
            'text': str,
            'units': str,
            'value': int
        }

        self.attribute_map = {
            'status': 'status',
            'text': 'text',
            'units': 'units',
            'value': 'value'
        }

        self._status = status
        self._text = text
        self._units = units
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GpuDecoderUsageMetric':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The gpu_decoder_usage_metric of this GpuDecoderUsageMetric.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this GpuDecoderUsageMetric.

        The status of the current key. Possible values are <strong>normal</strong> (everything is fine), <strong>warning</strong> (something may be misconfigured), and <strong>no_data</strong> (no data was returned, perhaps because the instance isn't running).

        :return: The status of this GpuDecoderUsageMetric.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GpuDecoderUsageMetric.

        The status of the current key. Possible values are <strong>normal</strong> (everything is fine), <strong>warning</strong> (something may be misconfigured), and <strong>no_data</strong> (no data was returned, perhaps because the instance isn't running).

        :param status: The status of this GpuDecoderUsageMetric.
        :type status: str
        """

        self._status = status

    @property
    def text(self):
        """Gets the text of this GpuDecoderUsageMetric.

        A message related to the value and status of the current key. Usually blank unless there's a warning status.

        :return: The text of this GpuDecoderUsageMetric.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this GpuDecoderUsageMetric.

        A message related to the value and status of the current key. Usually blank unless there's a warning status.

        :param text: The text of this GpuDecoderUsageMetric.
        :type text: str
        """

        self._text = text

    @property
    def units(self):
        """Gets the units of this GpuDecoderUsageMetric.

        The unit of the returned value, such as <strong>Kbps</strong>, <strong>bps</strong>, <strong>%</strong>, <strong>FPS</strong>, or <strong>GOP</strong>.

        :return: The units of this GpuDecoderUsageMetric.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this GpuDecoderUsageMetric.

        The unit of the returned value, such as <strong>Kbps</strong>, <strong>bps</strong>, <strong>%</strong>, <strong>FPS</strong>, or <strong>GOP</strong>.

        :param units: The units of this GpuDecoderUsageMetric.
        :type units: str
        """

        self._units = units

    @property
    def value(self):
        """Gets the value of this GpuDecoderUsageMetric.

        The value of the associated key.

        :return: The value of this GpuDecoderUsageMetric.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GpuDecoderUsageMetric.

        The value of the associated key.

        :param value: The value of this GpuDecoderUsageMetric.
        :type value: int
        """

        self._value = value
