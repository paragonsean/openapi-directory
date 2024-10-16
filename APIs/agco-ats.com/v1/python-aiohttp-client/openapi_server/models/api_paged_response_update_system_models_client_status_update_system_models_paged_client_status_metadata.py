# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_system_models_client_status import UpdateSystemModelsClientStatus
from openapi_server.models.update_system_models_paged_client_status_metadata import UpdateSystemModelsPagedClientStatusMetadata
from openapi_server import util


class APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[UpdateSystemModelsClientStatus]=None, metadata: UpdateSystemModelsPagedClientStatusMetadata=None):
        """APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        """
        self.openapi_types = {
            'entities': List[UpdateSystemModelsClientStatus],
            'metadata': UpdateSystemModelsPagedClientStatusMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_UpdateSystem.Models.ClientStatus_UpdateSystem.Models.PagedClientStatusMetadata_ of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.


        :return: The entities of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        :rtype: List[UpdateSystemModelsClientStatus]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.


        :param entities: The entities of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        :type entities: List[UpdateSystemModelsClientStatus]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.


        :return: The metadata of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        :rtype: UpdateSystemModelsPagedClientStatusMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.


        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.
        :type metadata: UpdateSystemModelsPagedClientStatusMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
