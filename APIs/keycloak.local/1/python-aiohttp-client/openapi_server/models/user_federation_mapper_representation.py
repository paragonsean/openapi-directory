# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserFederationMapperRepresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config: Dict[str, object]=None, federation_mapper_type: str=None, federation_provider_display_name: str=None, id: str=None, name: str=None):
        """UserFederationMapperRepresentation - a model defined in OpenAPI

        :param config: The config of this UserFederationMapperRepresentation.
        :param federation_mapper_type: The federation_mapper_type of this UserFederationMapperRepresentation.
        :param federation_provider_display_name: The federation_provider_display_name of this UserFederationMapperRepresentation.
        :param id: The id of this UserFederationMapperRepresentation.
        :param name: The name of this UserFederationMapperRepresentation.
        """
        self.openapi_types = {
            'config': Dict[str, object],
            'federation_mapper_type': str,
            'federation_provider_display_name': str,
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'config': 'config',
            'federation_mapper_type': 'federationMapperType',
            'federation_provider_display_name': 'federationProviderDisplayName',
            'id': 'id',
            'name': 'name'
        }

        self._config = config
        self._federation_mapper_type = federation_mapper_type
        self._federation_provider_display_name = federation_provider_display_name
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserFederationMapperRepresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserFederationMapperRepresentation of this UserFederationMapperRepresentation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config(self):
        """Gets the config of this UserFederationMapperRepresentation.


        :return: The config of this UserFederationMapperRepresentation.
        :rtype: Dict[str, object]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this UserFederationMapperRepresentation.


        :param config: The config of this UserFederationMapperRepresentation.
        :type config: Dict[str, object]
        """

        self._config = config

    @property
    def federation_mapper_type(self):
        """Gets the federation_mapper_type of this UserFederationMapperRepresentation.


        :return: The federation_mapper_type of this UserFederationMapperRepresentation.
        :rtype: str
        """
        return self._federation_mapper_type

    @federation_mapper_type.setter
    def federation_mapper_type(self, federation_mapper_type):
        """Sets the federation_mapper_type of this UserFederationMapperRepresentation.


        :param federation_mapper_type: The federation_mapper_type of this UserFederationMapperRepresentation.
        :type federation_mapper_type: str
        """

        self._federation_mapper_type = federation_mapper_type

    @property
    def federation_provider_display_name(self):
        """Gets the federation_provider_display_name of this UserFederationMapperRepresentation.


        :return: The federation_provider_display_name of this UserFederationMapperRepresentation.
        :rtype: str
        """
        return self._federation_provider_display_name

    @federation_provider_display_name.setter
    def federation_provider_display_name(self, federation_provider_display_name):
        """Sets the federation_provider_display_name of this UserFederationMapperRepresentation.


        :param federation_provider_display_name: The federation_provider_display_name of this UserFederationMapperRepresentation.
        :type federation_provider_display_name: str
        """

        self._federation_provider_display_name = federation_provider_display_name

    @property
    def id(self):
        """Gets the id of this UserFederationMapperRepresentation.


        :return: The id of this UserFederationMapperRepresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserFederationMapperRepresentation.


        :param id: The id of this UserFederationMapperRepresentation.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserFederationMapperRepresentation.


        :return: The name of this UserFederationMapperRepresentation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserFederationMapperRepresentation.


        :param name: The name of this UserFederationMapperRepresentation.
        :type name: str
        """

        self._name = name
