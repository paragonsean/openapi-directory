# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.table_services_list_metric_definitions200_response_value_inner import TableServicesListMetricDefinitions200ResponseValueInner
from openapi_server import util


class TableServicesListMetricDefinitions200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[TableServicesListMetricDefinitions200ResponseValueInner]=None):
        """TableServicesListMetricDefinitions200Response - a model defined in OpenAPI

        :param next_link: The next_link of this TableServicesListMetricDefinitions200Response.
        :param value: The value of this TableServicesListMetricDefinitions200Response.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[TableServicesListMetricDefinitions200ResponseValueInner]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TableServicesListMetricDefinitions200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TableServices_ListMetricDefinitions_200_response of this TableServicesListMetricDefinitions200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this TableServicesListMetricDefinitions200Response.

        URI to the next page.

        :return: The next_link of this TableServicesListMetricDefinitions200Response.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this TableServicesListMetricDefinitions200Response.

        URI to the next page.

        :param next_link: The next_link of this TableServicesListMetricDefinitions200Response.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this TableServicesListMetricDefinitions200Response.

        List of metric definitions.

        :return: The value of this TableServicesListMetricDefinitions200Response.
        :rtype: List[TableServicesListMetricDefinitions200ResponseValueInner]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TableServicesListMetricDefinitions200Response.

        List of metric definitions.

        :param value: The value of this TableServicesListMetricDefinitions200Response.
        :type value: List[TableServicesListMetricDefinitions200ResponseValueInner]
        """

        self._value = value
