# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_response_links import CollectionResponseLinks
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.health_profile_answer_resource import HealthProfileAnswerResource
from openapi_server.models.resource import Resource
from openapi_server import util


class FetchHealthProfileAnswersResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[HealthProfileAnswerResource]=None, included: List[Resource]=None, links: CollectionResponseLinks=None, meta: FetchMetaResponse=None):
        """FetchHealthProfileAnswersResponse - a model defined in OpenAPI

        :param data: The data of this FetchHealthProfileAnswersResponse.
        :param included: The included of this FetchHealthProfileAnswersResponse.
        :param links: The links of this FetchHealthProfileAnswersResponse.
        :param meta: The meta of this FetchHealthProfileAnswersResponse.
        """
        self.openapi_types = {
            'data': List[HealthProfileAnswerResource],
            'included': List[Resource],
            'links': CollectionResponseLinks,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'included': 'included',
            'links': 'links',
            'meta': 'meta'
        }

        self._data = data
        self._included = included
        self._links = links
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchHealthProfileAnswersResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchHealthProfileAnswersResponse of this FetchHealthProfileAnswersResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchHealthProfileAnswersResponse.


        :return: The data of this FetchHealthProfileAnswersResponse.
        :rtype: List[HealthProfileAnswerResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchHealthProfileAnswersResponse.


        :param data: The data of this FetchHealthProfileAnswersResponse.
        :type data: List[HealthProfileAnswerResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def included(self):
        """Gets the included of this FetchHealthProfileAnswersResponse.

        Related resources which are included in the response based on the `include` param. Attributes of each resource will vary depending on the type. See [patient](#operation/fetchPatient) 

        :return: The included of this FetchHealthProfileAnswersResponse.
        :rtype: List[Resource]
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this FetchHealthProfileAnswersResponse.

        Related resources which are included in the response based on the `include` param. Attributes of each resource will vary depending on the type. See [patient](#operation/fetchPatient) 

        :param included: The included of this FetchHealthProfileAnswersResponse.
        :type included: List[Resource]
        """

        self._included = included

    @property
    def links(self):
        """Gets the links of this FetchHealthProfileAnswersResponse.


        :return: The links of this FetchHealthProfileAnswersResponse.
        :rtype: CollectionResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FetchHealthProfileAnswersResponse.


        :param links: The links of this FetchHealthProfileAnswersResponse.
        :type links: CollectionResponseLinks
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this FetchHealthProfileAnswersResponse.


        :return: The meta of this FetchHealthProfileAnswersResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchHealthProfileAnswersResponse.


        :param meta: The meta of this FetchHealthProfileAnswersResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
