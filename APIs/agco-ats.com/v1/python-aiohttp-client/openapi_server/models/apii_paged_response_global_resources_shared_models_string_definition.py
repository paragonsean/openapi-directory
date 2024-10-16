# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.global_resources_shared_models_string_definition import GlobalResourcesSharedModelsStringDefinition
from openapi_server import util


class APIIPagedResponseGlobalResourcesSharedModelsStringDefinition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[GlobalResourcesSharedModelsStringDefinition]=None, metadata: APIPagedResponseMetadata=None):
        """APIIPagedResponseGlobalResourcesSharedModelsStringDefinition - a model defined in OpenAPI

        :param entities: The entities of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        :param metadata: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        """
        self.openapi_types = {
            'entities': List[GlobalResourcesSharedModelsStringDefinition],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIIPagedResponseGlobalResourcesSharedModelsStringDefinition':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.IPagedResponse_GlobalResources.Shared.Models.StringDefinition_ of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.


        :return: The entities of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        :rtype: List[GlobalResourcesSharedModelsStringDefinition]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.


        :param entities: The entities of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        :type entities: List[GlobalResourcesSharedModelsStringDefinition]
        """

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.


        :return: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.


        :param metadata: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.
        :type metadata: APIPagedResponseMetadata
        """

        self._metadata = metadata
