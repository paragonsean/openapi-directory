# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DimensionFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, values: str=None):
        """DimensionFilter - a model defined in OpenAPI

        :param name: The name of this DimensionFilter.
        :param values: The values of this DimensionFilter.
        """
        self.openapi_types = {
            'name': str,
            'values': str
        }

        self.attribute_map = {
            'name': 'name',
            'values': 'values'
        }

        self._name = name
        self._values = values

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DimensionFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DimensionFilter of this DimensionFilter.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this DimensionFilter.

        Specifies the dimension name. E.g., NetworkInterface. Valid values are the ones specified in the field \"dimensions\" in the ListMetricDefinitions call. Only 'Equality' operator is supported for this property.

        :return: The name of this DimensionFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DimensionFilter.

        Specifies the dimension name. E.g., NetworkInterface. Valid values are the ones specified in the field \"dimensions\" in the ListMetricDefinitions call. Only 'Equality' operator is supported for this property.

        :param name: The name of this DimensionFilter.
        :type name: str
        """

        self._name = name

    @property
    def values(self):
        """Gets the values of this DimensionFilter.

        Specifies the dimension value. E.g., Data0. Valid values are the ones returned in the field \"dimensions\" in the ListMetricDefinitions call. Only 'Equality' operator is supported for this property.

        :return: The values of this DimensionFilter.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DimensionFilter.

        Specifies the dimension value. E.g., Data0. Valid values are the ones returned in the field \"dimensions\" in the ListMetricDefinitions call. Only 'Equality' operator is supported for this property.

        :param values: The values of this DimensionFilter.
        :type values: str
        """

        self._values = values
