# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetLicenseByID200ResponseLicensesLicenseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, url: str=None):
        """GetLicenseByID200ResponseLicensesLicenseInner - a model defined in OpenAPI

        :param id: The id of this GetLicenseByID200ResponseLicensesLicenseInner.
        :param name: The name of this GetLicenseByID200ResponseLicensesLicenseInner.
        :param url: The url of this GetLicenseByID200ResponseLicensesLicenseInner.
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'url': 'url'
        }

        self._id = id
        self._name = name
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetLicenseByID200ResponseLicensesLicenseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getLicenseByID_200_response_licenses_license_inner of this GetLicenseByID200ResponseLicensesLicenseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetLicenseByID200ResponseLicensesLicenseInner.


        :return: The id of this GetLicenseByID200ResponseLicensesLicenseInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetLicenseByID200ResponseLicensesLicenseInner.


        :param id: The id of this GetLicenseByID200ResponseLicensesLicenseInner.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetLicenseByID200ResponseLicensesLicenseInner.


        :return: The name of this GetLicenseByID200ResponseLicensesLicenseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetLicenseByID200ResponseLicensesLicenseInner.


        :param name: The name of this GetLicenseByID200ResponseLicensesLicenseInner.
        :type name: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this GetLicenseByID200ResponseLicensesLicenseInner.


        :return: The url of this GetLicenseByID200ResponseLicensesLicenseInner.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetLicenseByID200ResponseLicensesLicenseInner.


        :param url: The url of this GetLicenseByID200ResponseLicensesLicenseInner.
        :type url: str
        """

        self._url = url
