# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.test_gdpr_export_accounts200_response_resources_inner import TestGdprExportAccounts200ResponseResourcesInner
from openapi_server import util


class TestGdprExportAccounts200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resources: List[TestGdprExportAccounts200ResponseResourcesInner]=None):
        """TestGdprExportAccounts200Response - a model defined in OpenAPI

        :param resources: The resources of this TestGdprExportAccounts200Response.
        """
        self.openapi_types = {
            'resources': List[TestGdprExportAccounts200ResponseResourcesInner]
        }

        self.attribute_map = {
            'resources': 'resources'
        }

        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestGdprExportAccounts200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The test_gdprExportAccounts_200_response of this TestGdprExportAccounts200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resources(self):
        """Gets the resources of this TestGdprExportAccounts200Response.


        :return: The resources of this TestGdprExportAccounts200Response.
        :rtype: List[TestGdprExportAccounts200ResponseResourcesInner]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this TestGdprExportAccounts200Response.


        :param resources: The resources of this TestGdprExportAccounts200Response.
        :type resources: List[TestGdprExportAccounts200ResponseResourcesInner]
        """

        self._resources = resources
