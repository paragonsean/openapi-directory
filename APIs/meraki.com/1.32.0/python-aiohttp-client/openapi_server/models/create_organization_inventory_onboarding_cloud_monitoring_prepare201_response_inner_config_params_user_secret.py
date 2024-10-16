# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hash: str=None):
        """CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret - a model defined in OpenAPI

        :param hash: The hash of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.
        """
        self.openapi_types = {
            'hash': str
        }

        self.attribute_map = {
            'hash': 'hash'
        }

        self._hash = hash

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_user_secret of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hash(self):
        """Gets the hash of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.

        The hashed secret

        :return: The hash of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.

        The hashed secret

        :param hash: The hash of this CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInnerConfigParamsUserSecret.
        :type hash: str
        """

        self._hash = hash
