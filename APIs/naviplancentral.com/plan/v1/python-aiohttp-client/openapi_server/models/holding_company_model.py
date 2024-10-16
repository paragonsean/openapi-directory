# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_holding_company import IHoldingCompany
from openapi_server.models.object_link import ObjectLink
from openapi_server import util


class HoldingCompanyModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, holding_company: IHoldingCompany=None, links: List[ObjectLink]=None):
        """HoldingCompanyModel - a model defined in OpenAPI

        :param holding_company: The holding_company of this HoldingCompanyModel.
        :param links: The links of this HoldingCompanyModel.
        """
        self.openapi_types = {
            'holding_company': IHoldingCompany,
            'links': List[ObjectLink]
        }

        self.attribute_map = {
            'holding_company': 'holdingCompany',
            'links': 'links'
        }

        self._holding_company = holding_company
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HoldingCompanyModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HoldingCompanyModel of this HoldingCompanyModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def holding_company(self):
        """Gets the holding_company of this HoldingCompanyModel.


        :return: The holding_company of this HoldingCompanyModel.
        :rtype: IHoldingCompany
        """
        return self._holding_company

    @holding_company.setter
    def holding_company(self, holding_company):
        """Sets the holding_company of this HoldingCompanyModel.


        :param holding_company: The holding_company of this HoldingCompanyModel.
        :type holding_company: IHoldingCompany
        """

        self._holding_company = holding_company

    @property
    def links(self):
        """Gets the links of this HoldingCompanyModel.


        :return: The links of this HoldingCompanyModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this HoldingCompanyModel.


        :param links: The links of this HoldingCompanyModel.
        :type links: List[ObjectLink]
        """

        self._links = links
