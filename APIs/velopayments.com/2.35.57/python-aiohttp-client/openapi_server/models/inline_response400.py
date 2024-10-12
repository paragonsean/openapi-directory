# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.error import Error
from openapi_server import util


class InlineResponse400(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, correlation_id: str=None, errors: List[Error]=None, http_status_code: int=None):
        """InlineResponse400 - a model defined in OpenAPI

        :param correlation_id: The correlation_id of this InlineResponse400.
        :param errors: The errors of this InlineResponse400.
        :param http_status_code: The http_status_code of this InlineResponse400.
        """
        self.openapi_types = {
            'correlation_id': str,
            'errors': List[Error],
            'http_status_code': int
        }

        self.attribute_map = {
            'correlation_id': 'correlationId',
            'errors': 'errors',
            'http_status_code': 'httpStatusCode'
        }

        self._correlation_id = correlation_id
        self._errors = errors
        self._http_status_code = http_status_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponse400':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_400 of this InlineResponse400.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def correlation_id(self):
        """Gets the correlation_id of this InlineResponse400.

        a unique identifier to track a request or related sequence of requests

        :return: The correlation_id of this InlineResponse400.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this InlineResponse400.

        a unique identifier to track a request or related sequence of requests

        :param correlation_id: The correlation_id of this InlineResponse400.
        :type correlation_id: str
        """

        self._correlation_id = correlation_id

    @property
    def errors(self):
        """Gets the errors of this InlineResponse400.

        one or more errors

        :return: The errors of this InlineResponse400.
        :rtype: List[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse400.

        one or more errors

        :param errors: The errors of this InlineResponse400.
        :type errors: List[Error]
        """
        if errors is not None and len(errors) < 1:
            raise ValueError("Invalid value for `errors`, number of items must be greater than or equal to `1`")

        self._errors = errors

    @property
    def http_status_code(self):
        """Gets the http_status_code of this InlineResponse400.

        this will mirror the Status-Code part of the Status-Line http response header and is included for extra clarity

        :return: The http_status_code of this InlineResponse400.
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this InlineResponse400.

        this will mirror the Status-Code part of the Status-Line http response header and is included for extra clarity

        :param http_status_code: The http_status_code of this InlineResponse400.
        :type http_status_code: int
        """

        self._http_status_code = http_status_code
