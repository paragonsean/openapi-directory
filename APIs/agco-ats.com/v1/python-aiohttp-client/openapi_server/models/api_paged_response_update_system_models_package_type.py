# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.update_system_models_package_type import UpdateSystemModelsPackageType
from openapi_server import util


class APIPagedResponseUpdateSystemModelsPackageType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[UpdateSystemModelsPackageType]=None, metadata: APIPagedResponseMetadata=None):
        """APIPagedResponseUpdateSystemModelsPackageType - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseUpdateSystemModelsPackageType.
        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsPackageType.
        """
        self.openapi_types = {
            'entities': List[UpdateSystemModelsPackageType],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseUpdateSystemModelsPackageType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_UpdateSystem.Models.PackageType_ of this APIPagedResponseUpdateSystemModelsPackageType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseUpdateSystemModelsPackageType.


        :return: The entities of this APIPagedResponseUpdateSystemModelsPackageType.
        :rtype: List[UpdateSystemModelsPackageType]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseUpdateSystemModelsPackageType.


        :param entities: The entities of this APIPagedResponseUpdateSystemModelsPackageType.
        :type entities: List[UpdateSystemModelsPackageType]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseUpdateSystemModelsPackageType.


        :return: The metadata of this APIPagedResponseUpdateSystemModelsPackageType.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseUpdateSystemModelsPackageType.


        :param metadata: The metadata of this APIPagedResponseUpdateSystemModelsPackageType.
        :type metadata: APIPagedResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
