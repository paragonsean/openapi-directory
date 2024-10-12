# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.global_resources_shared_models_translation_set import GlobalResourcesSharedModelsTranslationSet
from openapi_server import util


class APIIPagedResponseGlobalResourcesSharedModelsTranslationSet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[GlobalResourcesSharedModelsTranslationSet]=None, metadata: APIPagedResponseMetadata=None):
        """APIIPagedResponseGlobalResourcesSharedModelsTranslationSet - a model defined in OpenAPI

        :param entities: The entities of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        :param metadata: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        """
        self.openapi_types = {
            'entities': List[GlobalResourcesSharedModelsTranslationSet],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIIPagedResponseGlobalResourcesSharedModelsTranslationSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.IPagedResponse_GlobalResources.Shared.Models.TranslationSet_ of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.


        :return: The entities of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        :rtype: List[GlobalResourcesSharedModelsTranslationSet]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.


        :param entities: The entities of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        :type entities: List[GlobalResourcesSharedModelsTranslationSet]
        """

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.


        :return: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.


        :param metadata: The metadata of this APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.
        :type metadata: APIPagedResponseMetadata
        """

        self._metadata = metadata
