# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.update_system_models_client import UpdateSystemModelsClient
from openapi_server import util


class APIPagedResponseUpdateSystemModelsClient(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[UpdateSystemModelsClient]=None, metadata: APIPagedResponseMetadata=None):
        """APIPagedResponseUpdateSystemModelsClient - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseUpdateSystemModelsClient.
        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsClient.
        """
        self.openapi_types = {
            'entities': List[UpdateSystemModelsClient],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseUpdateSystemModelsClient':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_UpdateSystem.Models.Client_ of this APIPagedResponseUpdateSystemModelsClient.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseUpdateSystemModelsClient.


        :return: The entities of this APIPagedResponseUpdateSystemModelsClient.
        :rtype: List[UpdateSystemModelsClient]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseUpdateSystemModelsClient.


        :param entities: The entities of this APIPagedResponseUpdateSystemModelsClient.
        :type entities: List[UpdateSystemModelsClient]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseUpdateSystemModelsClient.


        :return: The metadata of this APIPagedResponseUpdateSystemModelsClient.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseUpdateSystemModelsClient.


        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsClient.
        :type metadata: APIPagedResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
