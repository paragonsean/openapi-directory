# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.company_price_margins import CompanyPriceMargins
from openapi_server.models.pagination_details import PaginationDetails
from openapi_server import util


class CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[CompanyPriceMargins]=None, pagination: PaginationDetails=None, success: bool=True):
        """CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response - a model defined in OpenAPI

        :param data: The data of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :param pagination: The pagination of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :param success: The success of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        """
        self.openapi_types = {
            'data': List[CompanyPriceMargins],
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
    def from_dict(cls, dikt: dict) -> 'CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _companies__company_id__price_margins__price_margins_id__get_200_response of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :return: The data of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :rtype: List[CompanyPriceMargins]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :param data: The data of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :type data: List[CompanyPriceMargins]
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :return: The pagination of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :rtype: PaginationDetails
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :param pagination: The pagination of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :type pagination: PaginationDetails
        """

        self._pagination = pagination

    @property
    def success(self):
        """Gets the success of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :return: The success of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.


        :param success: The success of this CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.
        :type success: bool
        """

        self._success = success
