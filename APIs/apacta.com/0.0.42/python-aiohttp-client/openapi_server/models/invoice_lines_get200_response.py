# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.invoice_line import InvoiceLine
from openapi_server.models.pagination_details import PaginationDetails
from openapi_server import util


class InvoiceLinesGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[InvoiceLine]=None, pagination: PaginationDetails=None, success: bool=None):
        """InvoiceLinesGet200Response - a model defined in OpenAPI

        :param data: The data of this InvoiceLinesGet200Response.
        :param pagination: The pagination of this InvoiceLinesGet200Response.
        :param success: The success of this InvoiceLinesGet200Response.
        """
        self.openapi_types = {
            'data': List[InvoiceLine],
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
    def from_dict(cls, dikt: dict) -> 'InvoiceLinesGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _invoice_lines_get_200_response of this InvoiceLinesGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this InvoiceLinesGet200Response.


        :return: The data of this InvoiceLinesGet200Response.
        :rtype: List[InvoiceLine]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InvoiceLinesGet200Response.


        :param data: The data of this InvoiceLinesGet200Response.
        :type data: List[InvoiceLine]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this InvoiceLinesGet200Response.


        :return: The pagination of this InvoiceLinesGet200Response.
        :rtype: PaginationDetails
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this InvoiceLinesGet200Response.


        :param pagination: The pagination of this InvoiceLinesGet200Response.
        :type pagination: PaginationDetails
        """

        self._pagination = pagination

    @property
    def success(self):
        """Gets the success of this InvoiceLinesGet200Response.


        :return: The success of this InvoiceLinesGet200Response.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InvoiceLinesGet200Response.


        :param success: The success of this InvoiceLinesGet200Response.
        :type success: bool
        """

        self._success = success
