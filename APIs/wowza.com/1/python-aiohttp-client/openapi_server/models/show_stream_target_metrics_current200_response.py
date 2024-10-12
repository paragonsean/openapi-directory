# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.stream_target_metrics import StreamTargetMetrics
from openapi_server import util


class ShowStreamTargetMetricsCurrent200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, metrics: StreamTargetMetrics=None):
        """ShowStreamTargetMetricsCurrent200Response - a model defined in OpenAPI

        :param id: The id of this ShowStreamTargetMetricsCurrent200Response.
        :param metrics: The metrics of this ShowStreamTargetMetricsCurrent200Response.
        """
        self.openapi_types = {
            'id': str,
            'metrics': StreamTargetMetrics
        }

        self.attribute_map = {
            'id': 'id',
            'metrics': 'metrics'
        }

        self._id = id
        self._metrics = metrics

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShowStreamTargetMetricsCurrent200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The showStreamTargetMetricsCurrent_200_response of this ShowStreamTargetMetricsCurrent200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ShowStreamTargetMetricsCurrent200Response.

        The unique alphanumeric string that identifies the stream target.

        :return: The id of this ShowStreamTargetMetricsCurrent200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowStreamTargetMetricsCurrent200Response.

        The unique alphanumeric string that identifies the stream target.

        :param id: The id of this ShowStreamTargetMetricsCurrent200Response.
        :type id: str
        """

        self._id = id

    @property
    def metrics(self):
        """Gets the metrics of this ShowStreamTargetMetricsCurrent200Response.


        :return: The metrics of this ShowStreamTargetMetricsCurrent200Response.
        :rtype: StreamTargetMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowStreamTargetMetricsCurrent200Response.


        :param metrics: The metrics of this ShowStreamTargetMetricsCurrent200Response.
        :type metrics: StreamTargetMetrics
        """

        self._metrics = metrics
