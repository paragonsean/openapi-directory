# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_services_twitter_types import ConfigurationServicesTwitterTypes
from openapi_server.models.configuration_services_twitter_urls import ConfigurationServicesTwitterUrls
from openapi_server import util


class ConfigurationServicesTwitter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, types: ConfigurationServicesTwitterTypes=None, urls: ConfigurationServicesTwitterUrls=None):
        """ConfigurationServicesTwitter - a model defined in OpenAPI

        :param types: The types of this ConfigurationServicesTwitter.
        :param urls: The urls of this ConfigurationServicesTwitter.
        """
        self.openapi_types = {
            'types': ConfigurationServicesTwitterTypes,
            'urls': ConfigurationServicesTwitterUrls
        }

        self.attribute_map = {
            'types': 'types',
            'urls': 'urls'
        }

        self._types = types
        self._urls = urls

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigurationServicesTwitter':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration_services_twitter of this ConfigurationServicesTwitter.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def types(self):
        """Gets the types of this ConfigurationServicesTwitter.


        :return: The types of this ConfigurationServicesTwitter.
        :rtype: ConfigurationServicesTwitterTypes
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ConfigurationServicesTwitter.


        :param types: The types of this ConfigurationServicesTwitter.
        :type types: ConfigurationServicesTwitterTypes
        """

        self._types = types

    @property
    def urls(self):
        """Gets the urls of this ConfigurationServicesTwitter.


        :return: The urls of this ConfigurationServicesTwitter.
        :rtype: ConfigurationServicesTwitterUrls
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ConfigurationServicesTwitter.


        :param urls: The urls of this ConfigurationServicesTwitter.
        :type urls: ConfigurationServicesTwitterUrls
        """

        self._urls = urls
