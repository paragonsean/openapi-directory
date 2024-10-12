# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.solr_response_response import SolrResponseResponse
from openapi_server.models.solr_response_response_header import SolrResponseResponseHeader
from openapi_server import util


class SolrResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, response: SolrResponseResponse=None, response_header: SolrResponseResponseHeader=None):
        """SolrResponse - a model defined in OpenAPI

        :param response: The response of this SolrResponse.
        :param response_header: The response_header of this SolrResponse.
        """
        self.openapi_types = {
            'response': SolrResponseResponse,
            'response_header': SolrResponseResponseHeader
        }

        self.attribute_map = {
            'response': 'response',
            'response_header': 'responseHeader'
        }

        self._response = response
        self._response_header = response_header

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SolrResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SolrResponse of this SolrResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def response(self):
        """Gets the response of this SolrResponse.


        :return: The response of this SolrResponse.
        :rtype: SolrResponseResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this SolrResponse.


        :param response: The response of this SolrResponse.
        :type response: SolrResponseResponse
        """

        self._response = response

    @property
    def response_header(self):
        """Gets the response_header of this SolrResponse.


        :return: The response_header of this SolrResponse.
        :rtype: SolrResponseResponseHeader
        """
        return self._response_header

    @response_header.setter
    def response_header(self, response_header):
        """Sets the response_header of this SolrResponse.


        :param response_header: The response_header of this SolrResponse.
        :type response_header: SolrResponseResponseHeader
        """

        self._response_header = response_header
