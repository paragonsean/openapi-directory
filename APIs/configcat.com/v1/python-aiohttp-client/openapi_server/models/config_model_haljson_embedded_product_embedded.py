# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.config_model_haljson_embedded_product_embedded_organization import ConfigModelHaljsonEmbeddedProductEmbeddedOrganization
from openapi_server import util


class ConfigModelHaljsonEmbeddedProductEmbedded(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, organization: ConfigModelHaljsonEmbeddedProductEmbeddedOrganization=None):
        """ConfigModelHaljsonEmbeddedProductEmbedded - a model defined in OpenAPI

        :param organization: The organization of this ConfigModelHaljsonEmbeddedProductEmbedded.
        """
        self.openapi_types = {
            'organization': ConfigModelHaljsonEmbeddedProductEmbeddedOrganization
        }

        self.attribute_map = {
            'organization': 'organization'
        }

        self._organization = organization

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigModelHaljsonEmbeddedProductEmbedded':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConfigModel_haljson__embedded_product__embedded of this ConfigModelHaljsonEmbeddedProductEmbedded.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def organization(self):
        """Gets the organization of this ConfigModelHaljsonEmbeddedProductEmbedded.


        :return: The organization of this ConfigModelHaljsonEmbeddedProductEmbedded.
        :rtype: ConfigModelHaljsonEmbeddedProductEmbeddedOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ConfigModelHaljsonEmbeddedProductEmbedded.


        :param organization: The organization of this ConfigModelHaljsonEmbeddedProductEmbedded.
        :type organization: ConfigModelHaljsonEmbeddedProductEmbeddedOrganization
        """

        self._organization = organization
