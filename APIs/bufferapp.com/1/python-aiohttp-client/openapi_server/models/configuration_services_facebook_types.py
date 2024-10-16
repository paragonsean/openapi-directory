# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_services_facebook_types_group import ConfigurationServicesFacebookTypesGroup
from openapi_server import util


class ConfigurationServicesFacebookTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group: ConfigurationServicesFacebookTypesGroup=None, page: ConfigurationServicesFacebookTypesGroup=None, profile: ConfigurationServicesFacebookTypesGroup=None):
        """ConfigurationServicesFacebookTypes - a model defined in OpenAPI

        :param group: The group of this ConfigurationServicesFacebookTypes.
        :param page: The page of this ConfigurationServicesFacebookTypes.
        :param profile: The profile of this ConfigurationServicesFacebookTypes.
        """
        self.openapi_types = {
            'group': ConfigurationServicesFacebookTypesGroup,
            'page': ConfigurationServicesFacebookTypesGroup,
            'profile': ConfigurationServicesFacebookTypesGroup
        }

        self.attribute_map = {
            'group': 'group',
            'page': 'page',
            'profile': 'profile'
        }

        self._group = group
        self._page = page
        self._profile = profile

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigurationServicesFacebookTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration_services_facebook_types of this ConfigurationServicesFacebookTypes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group(self):
        """Gets the group of this ConfigurationServicesFacebookTypes.


        :return: The group of this ConfigurationServicesFacebookTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ConfigurationServicesFacebookTypes.


        :param group: The group of this ConfigurationServicesFacebookTypes.
        :type group: ConfigurationServicesFacebookTypesGroup
        """

        self._group = group

    @property
    def page(self):
        """Gets the page of this ConfigurationServicesFacebookTypes.


        :return: The page of this ConfigurationServicesFacebookTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ConfigurationServicesFacebookTypes.


        :param page: The page of this ConfigurationServicesFacebookTypes.
        :type page: ConfigurationServicesFacebookTypesGroup
        """

        self._page = page

    @property
    def profile(self):
        """Gets the profile of this ConfigurationServicesFacebookTypes.


        :return: The profile of this ConfigurationServicesFacebookTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ConfigurationServicesFacebookTypes.


        :param profile: The profile of this ConfigurationServicesFacebookTypes.
        :type profile: ConfigurationServicesFacebookTypesGroup
        """

        self._profile = profile
