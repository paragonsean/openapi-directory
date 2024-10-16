# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_services_facebook_urls import ConfigurationServicesFacebookUrls
from openapi_server.models.configuration_services_google_types import ConfigurationServicesGoogleTypes
from openapi_server import util


class ConfigurationServicesGoogle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, types: ConfigurationServicesGoogleTypes=None, urls: ConfigurationServicesFacebookUrls=None):
        """ConfigurationServicesGoogle - a model defined in OpenAPI

        :param types: The types of this ConfigurationServicesGoogle.
        :param urls: The urls of this ConfigurationServicesGoogle.
        """
        self.openapi_types = {
            'types': ConfigurationServicesGoogleTypes,
            'urls': ConfigurationServicesFacebookUrls
        }

        self.attribute_map = {
            'types': 'types',
            'urls': 'urls'
        }

        self._types = types
        self._urls = urls

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigurationServicesGoogle':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration_services_google of this ConfigurationServicesGoogle.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def types(self):
        """Gets the types of this ConfigurationServicesGoogle.


        :return: The types of this ConfigurationServicesGoogle.
        :rtype: ConfigurationServicesGoogleTypes
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ConfigurationServicesGoogle.


        :param types: The types of this ConfigurationServicesGoogle.
        :type types: ConfigurationServicesGoogleTypes
        """

        self._types = types

    @property
    def urls(self):
        """Gets the urls of this ConfigurationServicesGoogle.


        :return: The urls of this ConfigurationServicesGoogle.
        :rtype: ConfigurationServicesFacebookUrls
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ConfigurationServicesGoogle.


        :param urls: The urls of this ConfigurationServicesGoogle.
        :type urls: ConfigurationServicesFacebookUrls
        """

        self._urls = urls
