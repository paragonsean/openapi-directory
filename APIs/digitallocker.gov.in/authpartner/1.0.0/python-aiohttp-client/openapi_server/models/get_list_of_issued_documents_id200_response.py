# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_list_of_issued_documents_id200_response_items_inner import GetListOfIssuedDocumentsId200ResponseItemsInner
from openapi_server import util


class GetListOfIssuedDocumentsId200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: list[GetListOfIssuedDocumentsId200ResponseItemsInner]=None, resource: str=None):
        """GetListOfIssuedDocumentsId200Response - a model defined in OpenAPI

        :param items: The items of this GetListOfIssuedDocumentsId200Response.
        :param resource: The resource of this GetListOfIssuedDocumentsId200Response.
        """
        self.openapi_types = {
            'items': list[GetListOfIssuedDocumentsId200ResponseItemsInner],
            'resource': str
        }

        self.attribute_map = {
            'items': 'items',
            'resource': 'resource'
        }

        self._items = items
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetListOfIssuedDocumentsId200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Get_List_of_issued_Documents_id_200_response of this GetListOfIssuedDocumentsId200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this GetListOfIssuedDocumentsId200Response.


        :return: The items of this GetListOfIssuedDocumentsId200Response.
        :rtype: list[GetListOfIssuedDocumentsId200ResponseItemsInner]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GetListOfIssuedDocumentsId200Response.


        :param items: The items of this GetListOfIssuedDocumentsId200Response.
        :type items: list[GetListOfIssuedDocumentsId200ResponseItemsInner]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")
        if items is not None and len(items) < 1:
            raise ValueError("Invalid value for `items`, number of items must be greater than or equal to `1`")

        self._items = items

    @property
    def resource(self):
        """Gets the resource of this GetListOfIssuedDocumentsId200Response.


        :return: The resource of this GetListOfIssuedDocumentsId200Response.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this GetListOfIssuedDocumentsId200Response.


        :param resource: The resource of this GetListOfIssuedDocumentsId200Response.
        :type resource: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")
        if resource is not None and len(resource) < 1:
            raise ValueError("Invalid value for `resource`, length must be greater than or equal to `1`")

        self._resource = resource
