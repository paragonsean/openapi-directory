# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_pagination import ApiPagination
from openapi_server.models.endpoint_post_conversations_id_schedules_data_inner import EndpointPostConversationsIDSchedulesDataInner
from openapi_server import util


class EndpointPostConversationsIDSchedules(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[EndpointPostConversationsIDSchedulesDataInner]=None, pagination: ApiPagination=None):
        """EndpointPostConversationsIDSchedules - a model defined in OpenAPI

        :param data: The data of this EndpointPostConversationsIDSchedules.
        :param pagination: The pagination of this EndpointPostConversationsIDSchedules.
        """
        self.openapi_types = {
            'data': List[EndpointPostConversationsIDSchedulesDataInner],
            'pagination': ApiPagination
        }

        self.attribute_map = {
            'data': 'data',
            'pagination': 'pagination'
        }

        self._data = data
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPostConversationsIDSchedules':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-post-conversations-ID-schedules of this EndpointPostConversationsIDSchedules.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EndpointPostConversationsIDSchedules.


        :return: The data of this EndpointPostConversationsIDSchedules.
        :rtype: List[EndpointPostConversationsIDSchedulesDataInner]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EndpointPostConversationsIDSchedules.


        :param data: The data of this EndpointPostConversationsIDSchedules.
        :type data: List[EndpointPostConversationsIDSchedulesDataInner]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this EndpointPostConversationsIDSchedules.


        :return: The pagination of this EndpointPostConversationsIDSchedules.
        :rtype: ApiPagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EndpointPostConversationsIDSchedules.


        :param pagination: The pagination of this EndpointPostConversationsIDSchedules.
        :type pagination: ApiPagination
        """

        self._pagination = pagination
