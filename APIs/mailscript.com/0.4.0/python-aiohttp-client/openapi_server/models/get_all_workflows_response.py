# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_all_workflows_response_list_inner import GetAllWorkflowsResponseListInner
from openapi_server import util


class GetAllWorkflowsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, list: List[GetAllWorkflowsResponseListInner]=None):
        """GetAllWorkflowsResponse - a model defined in OpenAPI

        :param list: The list of this GetAllWorkflowsResponse.
        """
        self.openapi_types = {
            'list': List[GetAllWorkflowsResponseListInner]
        }

        self.attribute_map = {
            'list': 'list'
        }

        self._list = list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetAllWorkflowsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetAllWorkflowsResponse of this GetAllWorkflowsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def list(self):
        """Gets the list of this GetAllWorkflowsResponse.


        :return: The list of this GetAllWorkflowsResponse.
        :rtype: List[GetAllWorkflowsResponseListInner]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this GetAllWorkflowsResponse.


        :param list: The list of this GetAllWorkflowsResponse.
        :type list: List[GetAllWorkflowsResponseListInner]
        """
        if list is None:
            raise ValueError("Invalid value for `list`, must not be `None`")

        self._list = list
