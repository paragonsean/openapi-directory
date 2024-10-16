# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_services_facebook_types_group import ConfigurationServicesFacebookTypesGroup
from openapi_server import util


class ConfigurationServicesGoogleTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, page: ConfigurationServicesFacebookTypesGroup=None, profile: ConfigurationServicesFacebookTypesGroup=None):
        """ConfigurationServicesGoogleTypes - a model defined in OpenAPI

        :param page: The page of this ConfigurationServicesGoogleTypes.
        :param profile: The profile of this ConfigurationServicesGoogleTypes.
        """
        self.openapi_types = {
            'page': ConfigurationServicesFacebookTypesGroup,
            'profile': ConfigurationServicesFacebookTypesGroup
        }

        self.attribute_map = {
            'page': 'page',
            'profile': 'profile'
        }

        self._page = page
        self._profile = profile

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigurationServicesGoogleTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration_services_google_types of this ConfigurationServicesGoogleTypes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def page(self):
        """Gets the page of this ConfigurationServicesGoogleTypes.


        :return: The page of this ConfigurationServicesGoogleTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ConfigurationServicesGoogleTypes.


        :param page: The page of this ConfigurationServicesGoogleTypes.
        :type page: ConfigurationServicesFacebookTypesGroup
        """

        self._page = page

    @property
    def profile(self):
        """Gets the profile of this ConfigurationServicesGoogleTypes.


        :return: The profile of this ConfigurationServicesGoogleTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ConfigurationServicesGoogleTypes.


        :param profile: The profile of this ConfigurationServicesGoogleTypes.
        :type profile: ConfigurationServicesFacebookTypesGroup
        """

        self._profile = profile
