# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


class ApiCoreDtoGrantsGrant(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datapoint_type: str=None, entity: ApiCoreResponsesEntityUriSystemInt64=None, entity_name: str=None, entity_type: str=None, type: str=None):
        """ApiCoreDtoGrantsGrant - a model defined in OpenAPI

        :param datapoint_type: The datapoint_type of this ApiCoreDtoGrantsGrant.
        :param entity: The entity of this ApiCoreDtoGrantsGrant.
        :param entity_name: The entity_name of this ApiCoreDtoGrantsGrant.
        :param entity_type: The entity_type of this ApiCoreDtoGrantsGrant.
        :param type: The type of this ApiCoreDtoGrantsGrant.
        """
        self.openapi_types = {
            'datapoint_type': str,
            'entity': ApiCoreResponsesEntityUriSystemInt64,
            'entity_name': str,
            'entity_type': str,
            'type': str
        }

        self.attribute_map = {
            'datapoint_type': 'DatapointType',
            'entity': 'Entity',
            'entity_name': 'EntityName',
            'entity_type': 'EntityType',
            'type': 'Type'
        }

        self._datapoint_type = datapoint_type
        self._entity = entity
        self._entity_name = entity_name
        self._entity_type = entity_type
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoGrantsGrant':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.Grants.Grant of this ApiCoreDtoGrantsGrant.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datapoint_type(self):
        """Gets the datapoint_type of this ApiCoreDtoGrantsGrant.


        :return: The datapoint_type of this ApiCoreDtoGrantsGrant.
        :rtype: str
        """
        return self._datapoint_type

    @datapoint_type.setter
    def datapoint_type(self, datapoint_type):
        """Sets the datapoint_type of this ApiCoreDtoGrantsGrant.


        :param datapoint_type: The datapoint_type of this ApiCoreDtoGrantsGrant.
        :type datapoint_type: str
        """

        self._datapoint_type = datapoint_type

    @property
    def entity(self):
        """Gets the entity of this ApiCoreDtoGrantsGrant.


        :return: The entity of this ApiCoreDtoGrantsGrant.
        :rtype: ApiCoreResponsesEntityUriSystemInt64
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ApiCoreDtoGrantsGrant.


        :param entity: The entity of this ApiCoreDtoGrantsGrant.
        :type entity: ApiCoreResponsesEntityUriSystemInt64
        """

        self._entity = entity

    @property
    def entity_name(self):
        """Gets the entity_name of this ApiCoreDtoGrantsGrant.


        :return: The entity_name of this ApiCoreDtoGrantsGrant.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this ApiCoreDtoGrantsGrant.


        :param entity_name: The entity_name of this ApiCoreDtoGrantsGrant.
        :type entity_name: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """Gets the entity_type of this ApiCoreDtoGrantsGrant.


        :return: The entity_type of this ApiCoreDtoGrantsGrant.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ApiCoreDtoGrantsGrant.


        :param entity_type: The entity_type of this ApiCoreDtoGrantsGrant.
        :type entity_type: str
        """

        self._entity_type = entity_type

    @property
    def type(self):
        """Gets the type of this ApiCoreDtoGrantsGrant.


        :return: The type of this ApiCoreDtoGrantsGrant.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiCoreDtoGrantsGrant.


        :param type: The type of this ApiCoreDtoGrantsGrant.
        :type type: str
        """

        self._type = type
