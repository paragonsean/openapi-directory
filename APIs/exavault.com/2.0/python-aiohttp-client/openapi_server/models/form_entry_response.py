# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.form_entry import FormEntry
from openapi_server import util


class FormEntryResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[FormEntry]=None, response_status: int=None, returned_results: int=None, total_results: int=None):
        """FormEntryResponse - a model defined in OpenAPI

        :param data: The data of this FormEntryResponse.
        :param response_status: The response_status of this FormEntryResponse.
        :param returned_results: The returned_results of this FormEntryResponse.
        :param total_results: The total_results of this FormEntryResponse.
        """
        self.openapi_types = {
            'data': List[FormEntry],
            'response_status': int,
            'returned_results': int,
            'total_results': int
        }

        self.attribute_map = {
            'data': 'data',
            'response_status': 'responseStatus',
            'returned_results': 'returnedResults',
            'total_results': 'totalResults'
        }

        self._data = data
        self._response_status = response_status
        self._returned_results = returned_results
        self._total_results = total_results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FormEntryResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FormEntryResponse of this FormEntryResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FormEntryResponse.

        Object submissions data for form.

        :return: The data of this FormEntryResponse.
        :rtype: List[FormEntry]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FormEntryResponse.

        Object submissions data for form.

        :param data: The data of this FormEntryResponse.
        :type data: List[FormEntry]
        """

        self._data = data

    @property
    def response_status(self):
        """Gets the response_status of this FormEntryResponse.

        Http status code of the response. 

        :return: The response_status of this FormEntryResponse.
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this FormEntryResponse.

        Http status code of the response. 

        :param response_status: The response_status of this FormEntryResponse.
        :type response_status: int
        """

        self._response_status = response_status

    @property
    def returned_results(self):
        """Gets the returned_results of this FormEntryResponse.

        Number of returned results. 

        :return: The returned_results of this FormEntryResponse.
        :rtype: int
        """
        return self._returned_results

    @returned_results.setter
    def returned_results(self, returned_results):
        """Sets the returned_results of this FormEntryResponse.

        Number of returned results. 

        :param returned_results: The returned_results of this FormEntryResponse.
        :type returned_results: int
        """

        self._returned_results = returned_results

    @property
    def total_results(self):
        """Gets the total_results of this FormEntryResponse.

        Total results found. 

        :return: The total_results of this FormEntryResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this FormEntryResponse.

        Total results found. 

        :param total_results: The total_results of this FormEntryResponse.
        :type total_results: int
        """

        self._total_results = total_results
