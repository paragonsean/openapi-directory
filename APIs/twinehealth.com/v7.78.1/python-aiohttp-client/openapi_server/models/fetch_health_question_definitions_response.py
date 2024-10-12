# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_response_links import CollectionResponseLinks
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.health_question_definition_resource import HealthQuestionDefinitionResource
from openapi_server import util


class FetchHealthQuestionDefinitionsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[HealthQuestionDefinitionResource]=None, links: CollectionResponseLinks=None, meta: FetchMetaResponse=None):
        """FetchHealthQuestionDefinitionsResponse - a model defined in OpenAPI

        :param data: The data of this FetchHealthQuestionDefinitionsResponse.
        :param links: The links of this FetchHealthQuestionDefinitionsResponse.
        :param meta: The meta of this FetchHealthQuestionDefinitionsResponse.
        """
        self.openapi_types = {
            'data': List[HealthQuestionDefinitionResource],
            'links': CollectionResponseLinks,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'links': 'links',
            'meta': 'meta'
        }

        self._data = data
        self._links = links
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchHealthQuestionDefinitionsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchHealthQuestionDefinitionsResponse of this FetchHealthQuestionDefinitionsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchHealthQuestionDefinitionsResponse.


        :return: The data of this FetchHealthQuestionDefinitionsResponse.
        :rtype: List[HealthQuestionDefinitionResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchHealthQuestionDefinitionsResponse.


        :param data: The data of this FetchHealthQuestionDefinitionsResponse.
        :type data: List[HealthQuestionDefinitionResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def links(self):
        """Gets the links of this FetchHealthQuestionDefinitionsResponse.


        :return: The links of this FetchHealthQuestionDefinitionsResponse.
        :rtype: CollectionResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FetchHealthQuestionDefinitionsResponse.


        :param links: The links of this FetchHealthQuestionDefinitionsResponse.
        :type links: CollectionResponseLinks
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this FetchHealthQuestionDefinitionsResponse.


        :return: The meta of this FetchHealthQuestionDefinitionsResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchHealthQuestionDefinitionsResponse.


        :param meta: The meta of this FetchHealthQuestionDefinitionsResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
