# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.stream_target_metrics import StreamTargetMetrics
from openapi_server import util


class ShowStreamTargetMetricsHistoric200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, interval: str=None, metrics: List[StreamTargetMetrics]=None):
        """ShowStreamTargetMetricsHistoric200Response - a model defined in OpenAPI

        :param id: The id of this ShowStreamTargetMetricsHistoric200Response.
        :param interval: The interval of this ShowStreamTargetMetricsHistoric200Response.
        :param metrics: The metrics of this ShowStreamTargetMetricsHistoric200Response.
        """
        self.openapi_types = {
            'id': str,
            'interval': str,
            'metrics': List[StreamTargetMetrics]
        }

        self.attribute_map = {
            'id': 'id',
            'interval': 'interval',
            'metrics': 'metrics'
        }

        self._id = id
        self._interval = interval
        self._metrics = metrics

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShowStreamTargetMetricsHistoric200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The showStreamTargetMetricsHistoric_200_response of this ShowStreamTargetMetricsHistoric200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ShowStreamTargetMetricsHistoric200Response.

        The unique alphanumeric string that identifies the stream target.

        :return: The id of this ShowStreamTargetMetricsHistoric200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowStreamTargetMetricsHistoric200Response.

        The unique alphanumeric string that identifies the stream target.

        :param id: The id of this ShowStreamTargetMetricsHistoric200Response.
        :type id: str
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this ShowStreamTargetMetricsHistoric200Response.

        The length of time for a block of metrics. The default is **10m** (10 minutes).

        :return: The interval of this ShowStreamTargetMetricsHistoric200Response.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowStreamTargetMetricsHistoric200Response.

        The length of time for a block of metrics. The default is **10m** (10 minutes).

        :param interval: The interval of this ShowStreamTargetMetricsHistoric200Response.
        :type interval: str
        """

        self._interval = interval

    @property
    def metrics(self):
        """Gets the metrics of this ShowStreamTargetMetricsHistoric200Response.


        :return: The metrics of this ShowStreamTargetMetricsHistoric200Response.
        :rtype: List[StreamTargetMetrics]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowStreamTargetMetricsHistoric200Response.


        :param metrics: The metrics of this ShowStreamTargetMetricsHistoric200Response.
        :type metrics: List[StreamTargetMetrics]
        """

        self._metrics = metrics
