# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.dsc_compilation_job_stream_list_by_job200_response_value_inner_properties import DscCompilationJobStreamListByJob200ResponseValueInnerProperties
from openapi_server import util


class DscCompilationJobStreamListByJob200ResponseValueInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, properties: DscCompilationJobStreamListByJob200ResponseValueInnerProperties=None):
        """DscCompilationJobStreamListByJob200ResponseValueInner - a model defined in OpenAPI

        :param id: The id of this DscCompilationJobStreamListByJob200ResponseValueInner.
        :param properties: The properties of this DscCompilationJobStreamListByJob200ResponseValueInner.
        """
        self.openapi_types = {
            'id': str,
            'properties': DscCompilationJobStreamListByJob200ResponseValueInnerProperties
        }

        self.attribute_map = {
            'id': 'id',
            'properties': 'properties'
        }

        self._id = id
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DscCompilationJobStreamListByJob200ResponseValueInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DscCompilationJobStream_ListByJob_200_response_value_inner of this DscCompilationJobStreamListByJob200ResponseValueInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DscCompilationJobStreamListByJob200ResponseValueInner.

        Gets or sets the id of the resource.

        :return: The id of this DscCompilationJobStreamListByJob200ResponseValueInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DscCompilationJobStreamListByJob200ResponseValueInner.

        Gets or sets the id of the resource.

        :param id: The id of this DscCompilationJobStreamListByJob200ResponseValueInner.
        :type id: str
        """

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this DscCompilationJobStreamListByJob200ResponseValueInner.


        :return: The properties of this DscCompilationJobStreamListByJob200ResponseValueInner.
        :rtype: DscCompilationJobStreamListByJob200ResponseValueInnerProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DscCompilationJobStreamListByJob200ResponseValueInner.


        :param properties: The properties of this DscCompilationJobStreamListByJob200ResponseValueInner.
        :type properties: DscCompilationJobStreamListByJob200ResponseValueInnerProperties
        """

        self._properties = properties
