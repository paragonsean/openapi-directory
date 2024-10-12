# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.metric_data import MetricData
from openapi_server.models.metric_dimension import MetricDimension
from openapi_server.models.metric_name import MetricName
from openapi_server import util


class Metrics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dimensions: List[MetricDimension]=None, end_time: datetime=None, name: MetricName=None, primary_aggregation: str=None, resource_id: str=None, start_time: datetime=None, time_grain: str=None, type: str=None, unit: str=None, values: List[MetricData]=None):
        """Metrics - a model defined in OpenAPI

        :param dimensions: The dimensions of this Metrics.
        :param end_time: The end_time of this Metrics.
        :param name: The name of this Metrics.
        :param primary_aggregation: The primary_aggregation of this Metrics.
        :param resource_id: The resource_id of this Metrics.
        :param start_time: The start_time of this Metrics.
        :param time_grain: The time_grain of this Metrics.
        :param type: The type of this Metrics.
        :param unit: The unit of this Metrics.
        :param values: The values of this Metrics.
        """
        self.openapi_types = {
            'dimensions': List[MetricDimension],
            'end_time': datetime,
            'name': MetricName,
            'primary_aggregation': str,
            'resource_id': str,
            'start_time': datetime,
            'time_grain': str,
            'type': str,
            'unit': str,
            'values': List[MetricData]
        }

        self.attribute_map = {
            'dimensions': 'dimensions',
            'end_time': 'endTime',
            'name': 'name',
            'primary_aggregation': 'primaryAggregation',
            'resource_id': 'resourceId',
            'start_time': 'startTime',
            'time_grain': 'timeGrain',
            'type': 'type',
            'unit': 'unit',
            'values': 'values'
        }

        self._dimensions = dimensions
        self._end_time = end_time
        self._name = name
        self._primary_aggregation = primary_aggregation
        self._resource_id = resource_id
        self._start_time = start_time
        self._time_grain = time_grain
        self._type = type
        self._unit = unit
        self._values = values

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Metrics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Metrics of this Metrics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dimensions(self):
        """Gets the dimensions of this Metrics.

        The metric dimensions.

        :return: The dimensions of this Metrics.
        :rtype: List[MetricDimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Metrics.

        The metric dimensions.

        :param dimensions: The dimensions of this Metrics.
        :type dimensions: List[MetricDimension]
        """

        self._dimensions = dimensions

    @property
    def end_time(self):
        """Gets the end_time of this Metrics.

        The end time of the metric data.

        :return: The end_time of this Metrics.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Metrics.

        The end time of the metric data.

        :param end_time: The end_time of this Metrics.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def name(self):
        """Gets the name of this Metrics.


        :return: The name of this Metrics.
        :rtype: MetricName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metrics.


        :param name: The name of this Metrics.
        :type name: MetricName
        """

        self._name = name

    @property
    def primary_aggregation(self):
        """Gets the primary_aggregation of this Metrics.

        The metric aggregation type.

        :return: The primary_aggregation of this Metrics.
        :rtype: str
        """
        return self._primary_aggregation

    @primary_aggregation.setter
    def primary_aggregation(self, primary_aggregation):
        """Sets the primary_aggregation of this Metrics.

        The metric aggregation type.

        :param primary_aggregation: The primary_aggregation of this Metrics.
        :type primary_aggregation: str
        """
        allowed_values = ["Average", "Last", "Maximum", "Minimum", "None", "Total"]  # noqa: E501
        if primary_aggregation not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_aggregation` ({0}), must be one of {1}"
                .format(primary_aggregation, allowed_values)
            )

        self._primary_aggregation = primary_aggregation

    @property
    def resource_id(self):
        """Gets the resource_id of this Metrics.

        The ID of metric source.

        :return: The resource_id of this Metrics.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Metrics.

        The ID of metric source.

        :param resource_id: The resource_id of this Metrics.
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def start_time(self):
        """Gets the start_time of this Metrics.

        The start time of the metric data.

        :return: The start_time of this Metrics.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Metrics.

        The start time of the metric data.

        :param start_time: The start_time of this Metrics.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def time_grain(self):
        """Gets the time_grain of this Metrics.

        The time granularity of the metric data.

        :return: The time_grain of this Metrics.
        :rtype: str
        """
        return self._time_grain

    @time_grain.setter
    def time_grain(self, time_grain):
        """Sets the time_grain of this Metrics.

        The time granularity of the metric data.

        :param time_grain: The time_grain of this Metrics.
        :type time_grain: str
        """

        self._time_grain = time_grain

    @property
    def type(self):
        """Gets the type of this Metrics.

        The type of the metric data.

        :return: The type of this Metrics.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Metrics.

        The type of the metric data.

        :param type: The type of this Metrics.
        :type type: str
        """

        self._type = type

    @property
    def unit(self):
        """Gets the unit of this Metrics.

        The unit of the metric data.

        :return: The unit of this Metrics.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Metrics.

        The unit of the metric data.

        :param unit: The unit of this Metrics.
        :type unit: str
        """
        allowed_values = ["Bytes", "BytesPerSecond", "Count", "CountPerSecond", "Percent", "Seconds"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def values(self):
        """Gets the values of this Metrics.

        The list of the metric data.

        :return: The values of this Metrics.
        :rtype: List[MetricData]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Metrics.

        The list of the metric data.

        :param values: The values of this Metrics.
        :type values: List[MetricData]
        """

        self._values = values
