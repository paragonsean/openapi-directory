# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_services_facebook_types_group import ConfigurationServicesFacebookTypesGroup
from openapi_server import util


class ConfigurationServicesTwitterTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, profile: ConfigurationServicesFacebookTypesGroup=None):
        """ConfigurationServicesTwitterTypes - a model defined in OpenAPI

        :param profile: The profile of this ConfigurationServicesTwitterTypes.
        """
        self.openapi_types = {
            'profile': ConfigurationServicesFacebookTypesGroup
        }

        self.attribute_map = {
            'profile': 'profile'
        }

        self._profile = profile

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigurationServicesTwitterTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration_services_twitter_types of this ConfigurationServicesTwitterTypes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def profile(self):
        """Gets the profile of this ConfigurationServicesTwitterTypes.


        :return: The profile of this ConfigurationServicesTwitterTypes.
        :rtype: ConfigurationServicesFacebookTypesGroup
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ConfigurationServicesTwitterTypes.


        :param profile: The profile of this ConfigurationServicesTwitterTypes.
        :type profile: ConfigurationServicesFacebookTypesGroup
        """

        self._profile = profile
