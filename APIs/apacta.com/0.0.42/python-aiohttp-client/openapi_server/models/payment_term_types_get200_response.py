# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.pagination_details import PaginationDetails
from openapi_server.models.payment_term_type import PaymentTermType
from openapi_server import util


class PaymentTermTypesGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[PaymentTermType]=None, pagination: PaginationDetails=None, success: bool=True):
        """PaymentTermTypesGet200Response - a model defined in OpenAPI

        :param data: The data of this PaymentTermTypesGet200Response.
        :param pagination: The pagination of this PaymentTermTypesGet200Response.
        :param success: The success of this PaymentTermTypesGet200Response.
        """
        self.openapi_types = {
            'data': List[PaymentTermType],
            'pagination': PaginationDetails,
            'success': bool
        }

        self.attribute_map = {
            'data': 'data',
            'pagination': 'pagination',
            'success': 'success'
        }

        self._data = data
        self._pagination = pagination
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentTermTypesGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _payment_term_types_get_200_response of this PaymentTermTypesGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this PaymentTermTypesGet200Response.


        :return: The data of this PaymentTermTypesGet200Response.
        :rtype: List[PaymentTermType]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PaymentTermTypesGet200Response.


        :param data: The data of this PaymentTermTypesGet200Response.
        :type data: List[PaymentTermType]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this PaymentTermTypesGet200Response.


        :return: The pagination of this PaymentTermTypesGet200Response.
        :rtype: PaginationDetails
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaymentTermTypesGet200Response.


        :param pagination: The pagination of this PaymentTermTypesGet200Response.
        :type pagination: PaginationDetails
        """

        self._pagination = pagination

    @property
    def success(self):
        """Gets the success of this PaymentTermTypesGet200Response.


        :return: The success of this PaymentTermTypesGet200Response.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PaymentTermTypesGet200Response.


        :param success: The success of this PaymentTermTypesGet200Response.
        :type success: bool
        """

        self._success = success
