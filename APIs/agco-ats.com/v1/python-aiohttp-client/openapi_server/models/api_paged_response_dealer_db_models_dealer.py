# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_paged_response_metadata import APIPagedResponseMetadata
from openapi_server.models.dealer_db_models_dealer import DealerDBModelsDealer
from openapi_server import util


class APIPagedResponseDealerDBModelsDealer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entities: List[DealerDBModelsDealer]=None, metadata: APIPagedResponseMetadata=None):
        """APIPagedResponseDealerDBModelsDealer - a model defined in OpenAPI

        :param entities: The entities of this APIPagedResponseDealerDBModelsDealer.
        :param metadata: The metadata of this APIPagedResponseDealerDBModelsDealer.
        """
        self.openapi_types = {
            'entities': List[DealerDBModelsDealer],
            'metadata': APIPagedResponseMetadata
        }

        self.attribute_map = {
            'entities': 'Entities',
            'metadata': 'Metadata'
        }

        self._entities = entities
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIPagedResponseDealerDBModelsDealer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.PagedResponse_DealerDB.Models.Dealer_ of this APIPagedResponseDealerDBModelsDealer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities(self):
        """Gets the entities of this APIPagedResponseDealerDBModelsDealer.


        :return: The entities of this APIPagedResponseDealerDBModelsDealer.
        :rtype: List[DealerDBModelsDealer]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this APIPagedResponseDealerDBModelsDealer.


        :param entities: The entities of this APIPagedResponseDealerDBModelsDealer.
        :type entities: List[DealerDBModelsDealer]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")

        self._entities = entities

    @property
    def metadata(self):
        """Gets the metadata of this APIPagedResponseDealerDBModelsDealer.


        :return: The metadata of this APIPagedResponseDealerDBModelsDealer.
        :rtype: APIPagedResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this APIPagedResponseDealerDBModelsDealer.


        :param metadata: The metadata of this APIPagedResponseDealerDBModelsDealer.
        :type metadata: APIPagedResponseMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata
