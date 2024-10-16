# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.update_system_models_update_group_subscription import UpdateSystemModelsUpdateGroupSubscription
from openapi_server import util


class APIPagedResponseUpdateSystemModelsUpdateGroupSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[UpdateSystemModelsUpdateGroupSubscription]=None, metadata: APIPagedResponseMetadata=None):
        """APIPagedResponseUpdateSystemModelsUpdateGroupSubscription - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        """
        self.openapi_types = {
            'entities': List[UpdateSystemModelsUpdateGroupSubscription],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseUpdateSystemModelsUpdateGroupSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_UpdateSystem.Models.UpdateGroupSubscription_ of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.


        :return: The entities of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        :rtype: List[UpdateSystemModelsUpdateGroupSubscription]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.


        :param entities: The entities of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        :type entities: List[UpdateSystemModelsUpdateGroupSubscription]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.


        :return: The metadata of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.


        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.
        :type metadata: APIPagedResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
