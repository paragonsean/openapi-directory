# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.trip import Trip
from openapi_server.models.warnings import Warnings
from openapi_server import util


class PostTripParserRequest200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: Trip=None, warnings: List[Warnings]=None):
        """PostTripParserRequest200Response - a model defined in OpenAPI

        :param data: The data of this PostTripParserRequest200Response.
        :param warnings: The warnings of this PostTripParserRequest200Response.
        """
        self.openapi_types = {
            'data': Trip,
            'warnings': List[Warnings]
        }

        self.attribute_map = {
            'data': 'data',
            'warnings': 'warnings'
        }

        self._data = data
        self._warnings = warnings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PostTripParserRequest200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PostTripParserRequest_200_response of this PostTripParserRequest200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this PostTripParserRequest200Response.


        :return: The data of this PostTripParserRequest200Response.
        :rtype: Trip
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PostTripParserRequest200Response.


        :param data: The data of this PostTripParserRequest200Response.
        :type data: Trip
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def warnings(self):
        """Gets the warnings of this PostTripParserRequest200Response.


        :return: The warnings of this PostTripParserRequest200Response.
        :rtype: List[Warnings]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this PostTripParserRequest200Response.


        :param warnings: The warnings of this PostTripParserRequest200Response.
        :type warnings: List[Warnings]
        """

        self._warnings = warnings
