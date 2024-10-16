# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organizations200_response_inner_management_details_inner import GetOrganizations200ResponseInnerManagementDetailsInner
from openapi_server import util


class GetOrganizations200ResponseInnerManagement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, details: List[GetOrganizations200ResponseInnerManagementDetailsInner]=None):
        """GetOrganizations200ResponseInnerManagement - a model defined in OpenAPI

        :param details: The details of this GetOrganizations200ResponseInnerManagement.
        """
        self.openapi_types = {
            'details': List[GetOrganizations200ResponseInnerManagementDetailsInner]
        }

        self.attribute_map = {
            'details': 'details'
        }

        self._details = details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizations200ResponseInnerManagement':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizations_200_response_inner_management of this GetOrganizations200ResponseInnerManagement.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def details(self):
        """Gets the details of this GetOrganizations200ResponseInnerManagement.

        Details related to organization management, possibly empty

        :return: The details of this GetOrganizations200ResponseInnerManagement.
        :rtype: List[GetOrganizations200ResponseInnerManagementDetailsInner]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this GetOrganizations200ResponseInnerManagement.

        Details related to organization management, possibly empty

        :param details: The details of this GetOrganizations200ResponseInnerManagement.
        :type details: List[GetOrganizations200ResponseInnerManagementDetailsInner]
        """

        self._details = details
