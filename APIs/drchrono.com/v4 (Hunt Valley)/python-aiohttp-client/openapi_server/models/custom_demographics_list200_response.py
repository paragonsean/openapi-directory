# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.custom_patient_field_type import CustomPatientFieldType
from openapi_server import util


class CustomDemographicsList200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[CustomPatientFieldType]=None, next: str=None, previous: str=None):
        """CustomDemographicsList200Response - a model defined in OpenAPI

        :param data: The data of this CustomDemographicsList200Response.
        :param next: The next of this CustomDemographicsList200Response.
        :param previous: The previous of this CustomDemographicsList200Response.
        """
        self.openapi_types = {
            'data': List[CustomPatientFieldType],
            'next': str,
            'previous': str
        }

        self.attribute_map = {
            'data': 'data',
            'next': 'next',
            'previous': 'previous'
        }

        self._data = data
        self._next = next
        self._previous = previous

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CustomDemographicsList200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The custom_demographics_list_200_response of this CustomDemographicsList200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CustomDemographicsList200Response.

        result data

        :return: The data of this CustomDemographicsList200Response.
        :rtype: List[CustomPatientFieldType]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CustomDemographicsList200Response.

        result data

        :param data: The data of this CustomDemographicsList200Response.
        :type data: List[CustomPatientFieldType]
        """

        self._data = data

    @property
    def next(self):
        """Gets the next of this CustomDemographicsList200Response.

        Next Paginated page

        :return: The next of this CustomDemographicsList200Response.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this CustomDemographicsList200Response.

        Next Paginated page

        :param next: The next of this CustomDemographicsList200Response.
        :type next: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this CustomDemographicsList200Response.

        Previous paginated page

        :return: The previous of this CustomDemographicsList200Response.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this CustomDemographicsList200Response.

        Previous paginated page

        :param previous: The previous of this CustomDemographicsList200Response.
        :type previous: str
        """

        self._previous = previous
