# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.anonymization_profile import AnonymizationProfile
from openapi_server import util


class RemoteBox(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_url: str=None, default_profile: AnonymizationProfile=None, name: str=None):
        """RemoteBox - a model defined in OpenAPI

        :param base_url: The base_url of this RemoteBox.
        :param default_profile: The default_profile of this RemoteBox.
        :param name: The name of this RemoteBox.
        """
        self.openapi_types = {
            'base_url': str,
            'default_profile': AnonymizationProfile,
            'name': str
        }

        self.attribute_map = {
            'base_url': 'baseUrl',
            'default_profile': 'defaultProfile',
            'name': 'name'
        }

        self._base_url = base_url
        self._default_profile = default_profile
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RemoteBox':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The remoteBox of this RemoteBox.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_url(self):
        """Gets the base_url of this RemoteBox.


        :return: The base_url of this RemoteBox.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this RemoteBox.


        :param base_url: The base_url of this RemoteBox.
        :type base_url: str
        """

        self._base_url = base_url

    @property
    def default_profile(self):
        """Gets the default_profile of this RemoteBox.


        :return: The default_profile of this RemoteBox.
        :rtype: AnonymizationProfile
        """
        return self._default_profile

    @default_profile.setter
    def default_profile(self, default_profile):
        """Sets the default_profile of this RemoteBox.


        :param default_profile: The default_profile of this RemoteBox.
        :type default_profile: AnonymizationProfile
        """

        self._default_profile = default_profile

    @property
    def name(self):
        """Gets the name of this RemoteBox.


        :return: The name of this RemoteBox.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RemoteBox.


        :param name: The name of this RemoteBox.
        :type name: str
        """

        self._name = name
