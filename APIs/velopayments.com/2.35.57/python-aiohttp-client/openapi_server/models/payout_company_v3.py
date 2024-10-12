# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PayoutCompanyV3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_name: str=None):
        """PayoutCompanyV3 - a model defined in OpenAPI

        :param company_name: The company_name of this PayoutCompanyV3.
        """
        self.openapi_types = {
            'company_name': str
        }

        self.attribute_map = {
            'company_name': 'companyName'
        }

        self._company_name = company_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayoutCompanyV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayoutCompanyV3 of this PayoutCompanyV3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_name(self):
        """Gets the company_name of this PayoutCompanyV3.


        :return: The company_name of this PayoutCompanyV3.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this PayoutCompanyV3.


        :param company_name: The company_name of this PayoutCompanyV3.
        :type company_name: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")

        self._company_name = company_name
