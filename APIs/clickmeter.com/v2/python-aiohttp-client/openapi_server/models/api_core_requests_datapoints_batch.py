# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server import util


class ApiCoreRequestsDatapointsBatch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, list: List[ApiCoreDtoDatapointsDatapoint]=None):
        """ApiCoreRequestsDatapointsBatch - a model defined in OpenAPI

        :param list: The list of this ApiCoreRequestsDatapointsBatch.
        """
        self.openapi_types = {
            'list': List[ApiCoreDtoDatapointsDatapoint]
        }

        self.attribute_map = {
            'list': 'List'
        }

        self._list = list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreRequestsDatapointsBatch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Requests.DatapointsBatch of this ApiCoreRequestsDatapointsBatch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def list(self):
        """Gets the list of this ApiCoreRequestsDatapointsBatch.


        :return: The list of this ApiCoreRequestsDatapointsBatch.
        :rtype: List[ApiCoreDtoDatapointsDatapoint]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ApiCoreRequestsDatapointsBatch.


        :param list: The list of this ApiCoreRequestsDatapointsBatch.
        :type list: List[ApiCoreDtoDatapointsDatapoint]
        """

        self._list = list
