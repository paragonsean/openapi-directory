# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ChartRowCollections(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, axis_id: str=None, chart_data_id: str=None, id: str=None, name_format_type: int=None):
        """ChartRowCollections - a model defined in OpenAPI

        :param axis_id: The axis_id of this ChartRowCollections.
        :param chart_data_id: The chart_data_id of this ChartRowCollections.
        :param id: The id of this ChartRowCollections.
        :param name_format_type: The name_format_type of this ChartRowCollections.
        """
        self.openapi_types = {
            'axis_id': str,
            'chart_data_id': str,
            'id': str,
            'name_format_type': int
        }

        self.attribute_map = {
            'axis_id': 'axisId',
            'chart_data_id': 'chartDataId',
            'id': 'id',
            'name_format_type': 'nameFormatType'
        }

        self._axis_id = axis_id
        self._chart_data_id = chart_data_id
        self._id = id
        self._name_format_type = name_format_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChartRowCollections':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Chart.RowCollections of this ChartRowCollections.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def axis_id(self):
        """Gets the axis_id of this ChartRowCollections.


        :return: The axis_id of this ChartRowCollections.
        :rtype: str
        """
        return self._axis_id

    @axis_id.setter
    def axis_id(self, axis_id):
        """Sets the axis_id of this ChartRowCollections.


        :param axis_id: The axis_id of this ChartRowCollections.
        :type axis_id: str
        """

        self._axis_id = axis_id

    @property
    def chart_data_id(self):
        """Gets the chart_data_id of this ChartRowCollections.


        :return: The chart_data_id of this ChartRowCollections.
        :rtype: str
        """
        return self._chart_data_id

    @chart_data_id.setter
    def chart_data_id(self, chart_data_id):
        """Sets the chart_data_id of this ChartRowCollections.


        :param chart_data_id: The chart_data_id of this ChartRowCollections.
        :type chart_data_id: str
        """

        self._chart_data_id = chart_data_id

    @property
    def id(self):
        """Gets the id of this ChartRowCollections.


        :return: The id of this ChartRowCollections.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartRowCollections.


        :param id: The id of this ChartRowCollections.
        :type id: str
        """

        self._id = id

    @property
    def name_format_type(self):
        """Gets the name_format_type of this ChartRowCollections.


        :return: The name_format_type of this ChartRowCollections.
        :rtype: int
        """
        return self._name_format_type

    @name_format_type.setter
    def name_format_type(self, name_format_type):
        """Sets the name_format_type of this ChartRowCollections.


        :param name_format_type: The name_format_type of this ChartRowCollections.
        :type name_format_type: int
        """

        self._name_format_type = name_format_type
