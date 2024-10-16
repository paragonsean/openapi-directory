# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TestGdprExportAccounts200ResponseResourcesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path: str=None, rel: str=None):
        """TestGdprExportAccounts200ResponseResourcesInner - a model defined in OpenAPI

        :param path: The path of this TestGdprExportAccounts200ResponseResourcesInner.
        :param rel: The rel of this TestGdprExportAccounts200ResponseResourcesInner.
        """
        self.openapi_types = {
            'path': str,
            'rel': str
        }

        self.attribute_map = {
            'path': 'path',
            'rel': 'rel'
        }

        self._path = path
        self._rel = rel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestGdprExportAccounts200ResponseResourcesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The test_gdprExportAccounts_200_response_resources_inner of this TestGdprExportAccounts200ResponseResourcesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path(self):
        """Gets the path of this TestGdprExportAccounts200ResponseResourcesInner.


        :return: The path of this TestGdprExportAccounts200ResponseResourcesInner.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TestGdprExportAccounts200ResponseResourcesInner.


        :param path: The path of this TestGdprExportAccounts200ResponseResourcesInner.
        :type path: str
        """

        self._path = path

    @property
    def rel(self):
        """Gets the rel of this TestGdprExportAccounts200ResponseResourcesInner.


        :return: The rel of this TestGdprExportAccounts200ResponseResourcesInner.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this TestGdprExportAccounts200ResponseResourcesInner.


        :param rel: The rel of this TestGdprExportAccounts200ResponseResourcesInner.
        :type rel: str
        """

        self._rel = rel
