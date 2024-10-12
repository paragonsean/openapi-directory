# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.child import Child
from openapi_server import util


class ResponseProductChildItemListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_fields: object=None, children: List[Child]=None, custom_fields: object=None, total_count: int=None):
        """ResponseProductChildItemListResult - a model defined in OpenAPI

        :param additional_fields: The additional_fields of this ResponseProductChildItemListResult.
        :param children: The children of this ResponseProductChildItemListResult.
        :param custom_fields: The custom_fields of this ResponseProductChildItemListResult.
        :param total_count: The total_count of this ResponseProductChildItemListResult.
        """
        self.openapi_types = {
            'additional_fields': object,
            'children': List[Child],
            'custom_fields': object,
            'total_count': int
        }

        self.attribute_map = {
            'additional_fields': 'additional_fields',
            'children': 'children',
            'custom_fields': 'custom_fields',
            'total_count': 'total_count'
        }

        self._additional_fields = additional_fields
        self._children = children
        self._custom_fields = custom_fields
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResponseProductChildItemListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Response_Product_ChildItem_List_Result of this ResponseProductChildItemListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ResponseProductChildItemListResult.


        :return: The additional_fields of this ResponseProductChildItemListResult.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ResponseProductChildItemListResult.


        :param additional_fields: The additional_fields of this ResponseProductChildItemListResult.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def children(self):
        """Gets the children of this ResponseProductChildItemListResult.


        :return: The children of this ResponseProductChildItemListResult.
        :rtype: List[Child]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ResponseProductChildItemListResult.


        :param children: The children of this ResponseProductChildItemListResult.
        :type children: List[Child]
        """

        self._children = children

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResponseProductChildItemListResult.


        :return: The custom_fields of this ResponseProductChildItemListResult.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResponseProductChildItemListResult.


        :param custom_fields: The custom_fields of this ResponseProductChildItemListResult.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def total_count(self):
        """Gets the total_count of this ResponseProductChildItemListResult.


        :return: The total_count of this ResponseProductChildItemListResult.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ResponseProductChildItemListResult.


        :param total_count: The total_count of this ResponseProductChildItemListResult.
        :type total_count: int
        """

        self._total_count = total_count
