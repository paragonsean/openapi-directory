# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.dealer_db_models_license import DealerDBModelsLicense
from openapi_server import util


class APIPagedResponseDealerDBModelsLicense(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[DealerDBModelsLicense]=None, metadata: APIPagedResponseMetadata=None):
        """APIPagedResponseDealerDBModelsLicense - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseDealerDBModelsLicense.
        :param metadata: The metadata of this APIPagedResponseDealerDBModelsLicense.
        """
        self.openapi_types = {
            'entities': List[DealerDBModelsLicense],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseDealerDBModelsLicense':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_DealerDB.Models.License_ of this APIPagedResponseDealerDBModelsLicense.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseDealerDBModelsLicense.


        :return: The entities of this APIPagedResponseDealerDBModelsLicense.
        :rtype: List[DealerDBModelsLicense]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseDealerDBModelsLicense.


        :param entities: The entities of this APIPagedResponseDealerDBModelsLicense.
        :type entities: List[DealerDBModelsLicense]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseDealerDBModelsLicense.


        :return: The metadata of this APIPagedResponseDealerDBModelsLicense.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseDealerDBModelsLicense.


        :param metadata: The metadata of this APIPagedResponseDealerDBModelsLicense.
        :type metadata: APIPagedResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
