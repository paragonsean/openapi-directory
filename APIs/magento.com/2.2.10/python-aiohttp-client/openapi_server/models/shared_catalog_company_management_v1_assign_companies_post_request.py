# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.company_data_company_interface import CompanyDataCompanyInterface
from openapi_server import util


class SharedCatalogCompanyManagementV1AssignCompaniesPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, companies: List[CompanyDataCompanyInterface]=None):
        """SharedCatalogCompanyManagementV1AssignCompaniesPostRequest - a model defined in OpenAPI

        :param companies: The companies of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.
        """
        self.openapi_types = {
            'companies': List[CompanyDataCompanyInterface]
        }

        self.attribute_map = {
            'companies': 'companies'
        }

        self._companies = companies

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SharedCatalogCompanyManagementV1AssignCompaniesPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sharedCatalogCompanyManagementV1AssignCompaniesPost_request of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def companies(self):
        """Gets the companies of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.


        :return: The companies of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.
        :rtype: List[CompanyDataCompanyInterface]
        """
        return self._companies

    @companies.setter
    def companies(self, companies):
        """Sets the companies of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.


        :param companies: The companies of this SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.
        :type companies: List[CompanyDataCompanyInterface]
        """
        if companies is None:
            raise ValueError("Invalid value for `companies`, must not be `None`")

        self._companies = companies
