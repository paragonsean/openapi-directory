# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.configuration_media import ConfigurationMedia
from openapi_server.models.configuration_services import ConfigurationServices
from openapi_server import util


class Configuration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, media: ConfigurationMedia=None, services: ConfigurationServices=None):
        """Configuration - a model defined in OpenAPI

        :param media: The media of this Configuration.
        :param services: The services of this Configuration.
        """
        self.openapi_types = {
            'media': ConfigurationMedia,
            'services': ConfigurationServices
        }

        self.attribute_map = {
            'media': 'media',
            'services': 'services'
        }

        self._media = media
        self._services = services

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Configuration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The configuration of this Configuration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media(self):
        """Gets the media of this Configuration.


        :return: The media of this Configuration.
        :rtype: ConfigurationMedia
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this Configuration.


        :param media: The media of this Configuration.
        :type media: ConfigurationMedia
        """

        self._media = media

    @property
    def services(self):
        """Gets the services of this Configuration.


        :return: The services of this Configuration.
        :rtype: ConfigurationServices
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Configuration.


        :param services: The services of this Configuration.
        :type services: ConfigurationServices
        """

        self._services = services
