# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.grafana_data_source import GrafanaDataSource
from openapi_server import util


class GrafanaTemplateVars(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datasource: GrafanaDataSource=None, hide: int=None, name: str=None, query: str=None, value: object=None):
        """GrafanaTemplateVars - a model defined in OpenAPI

        :param datasource: The datasource of this GrafanaTemplateVars.
        :param hide: The hide of this GrafanaTemplateVars.
        :param name: The name of this GrafanaTemplateVars.
        :param query: The query of this GrafanaTemplateVars.
        :param value: The value of this GrafanaTemplateVars.
        """
        self.openapi_types = {
            'datasource': GrafanaDataSource,
            'hide': int,
            'name': str,
            'query': str,
            'value': object
        }

        self.attribute_map = {
            'datasource': 'datasource',
            'hide': 'hide',
            'name': 'name',
            'query': 'query',
            'value': 'value'
        }

        self._datasource = datasource
        self._hide = hide
        self._name = name
        self._query = query
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GrafanaTemplateVars':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GrafanaTemplateVars of this GrafanaTemplateVars.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datasource(self):
        """Gets the datasource of this GrafanaTemplateVars.


        :return: The datasource of this GrafanaTemplateVars.
        :rtype: GrafanaDataSource
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this GrafanaTemplateVars.


        :param datasource: The datasource of this GrafanaTemplateVars.
        :type datasource: GrafanaDataSource
        """

        self._datasource = datasource

    @property
    def hide(self):
        """Gets the hide of this GrafanaTemplateVars.


        :return: The hide of this GrafanaTemplateVars.
        :rtype: int
        """
        return self._hide

    @hide.setter
    def hide(self, hide):
        """Sets the hide of this GrafanaTemplateVars.


        :param hide: The hide of this GrafanaTemplateVars.
        :type hide: int
        """

        self._hide = hide

    @property
    def name(self):
        """Gets the name of this GrafanaTemplateVars.


        :return: The name of this GrafanaTemplateVars.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrafanaTemplateVars.


        :param name: The name of this GrafanaTemplateVars.
        :type name: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this GrafanaTemplateVars.


        :return: The query of this GrafanaTemplateVars.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this GrafanaTemplateVars.


        :param query: The query of this GrafanaTemplateVars.
        :type query: str
        """

        self._query = query

    @property
    def value(self):
        """Gets the value of this GrafanaTemplateVars.


        :return: The value of this GrafanaTemplateVars.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GrafanaTemplateVars.


        :param value: The value of this GrafanaTemplateVars.
        :type value: object
        """

        self._value = value
