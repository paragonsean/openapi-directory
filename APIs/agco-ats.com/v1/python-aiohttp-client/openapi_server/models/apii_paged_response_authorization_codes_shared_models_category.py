# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.authorization_codes_shared_models_category import AuthorizationCodesSharedModelsCategory
from openapi_server import util


class APIIPagedResponseAuthorizationCodesSharedModelsCategory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[AuthorizationCodesSharedModelsCategory]=None, metadata: APIPagedResponseMetadata=None):
        """APIIPagedResponseAuthorizationCodesSharedModelsCategory - a model defined in OpenAPI

        :param entities: The entities of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        :param metadata: The metadata of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        """
        self.openapi_types = {
            'entities': List[AuthorizationCodesSharedModelsCategory],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIIPagedResponseAuthorizationCodesSharedModelsCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.IPagedResponse_AuthorizationCodes.Shared.Models.Category_ of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.


        :return: The entities of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        :rtype: List[AuthorizationCodesSharedModelsCategory]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.


        :param entities: The entities of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        :type entities: List[AuthorizationCodesSharedModelsCategory]
        """

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.


        :return: The metadata of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.


        :param metadata: The metadata of this APIIPagedResponseAuthorizationCodesSharedModelsCategory.
        :type metadata: APIPagedResponseMetadata
        """

        self._metadata = metadata
