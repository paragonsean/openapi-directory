# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CompanyMinimal(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_id: int=None, company_name: str=None):
        """CompanyMinimal - a model defined in OpenAPI

        :param company_id: The company_id of this CompanyMinimal.
        :param company_name: The company_name of this CompanyMinimal.
        """
        self.openapi_types = {
            'company_id': int,
            'company_name': str
        }

        self.attribute_map = {
            'company_id': 'CompanyID',
            'company_name': 'CompanyName'
        }

        self._company_id = company_id
        self._company_name = company_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompanyMinimal':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CompanyMinimal of this CompanyMinimal.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_id(self):
        """Gets the company_id of this CompanyMinimal.


        :return: The company_id of this CompanyMinimal.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CompanyMinimal.


        :param company_id: The company_id of this CompanyMinimal.
        :type company_id: int
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this CompanyMinimal.


        :return: The company_name of this CompanyMinimal.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CompanyMinimal.


        :param company_name: The company_name of this CompanyMinimal.
        :type company_name: str
        """

        self._company_name = company_name
