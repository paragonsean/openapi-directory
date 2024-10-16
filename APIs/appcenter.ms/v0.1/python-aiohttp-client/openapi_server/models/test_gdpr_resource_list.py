# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.test_gdpr_export_accounts200_response_resources_inner import TestGdprExportAccounts200ResponseResourcesInner
from openapi_server import util


class TestGDPRResourceList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resources: List[TestGdprExportAccounts200ResponseResourcesInner]=None):
        """TestGDPRResourceList - a model defined in OpenAPI

        :param resources: The resources of this TestGDPRResourceList.
        """
        self.openapi_types = {
            'resources': List[TestGdprExportAccounts200ResponseResourcesInner]
        }

        self.attribute_map = {
            'resources': 'resources'
        }

        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestGDPRResourceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TestGDPRResourceList of this TestGDPRResourceList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resources(self):
        """Gets the resources of this TestGDPRResourceList.


        :return: The resources of this TestGDPRResourceList.
        :rtype: List[TestGdprExportAccounts200ResponseResourcesInner]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this TestGDPRResourceList.


        :param resources: The resources of this TestGDPRResourceList.
        :type resources: List[TestGdprExportAccounts200ResponseResourcesInner]
        """

        self._resources = resources
