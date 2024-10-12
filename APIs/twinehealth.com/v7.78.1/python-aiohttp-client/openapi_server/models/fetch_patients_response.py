# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_response_links import CollectionResponseLinks
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.patient_resource import PatientResource
from openapi_server import util


class FetchPatientsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[PatientResource]=None, links: CollectionResponseLinks=None, meta: FetchMetaResponse=None):
        """FetchPatientsResponse - a model defined in OpenAPI

        :param data: The data of this FetchPatientsResponse.
        :param links: The links of this FetchPatientsResponse.
        :param meta: The meta of this FetchPatientsResponse.
        """
        self.openapi_types = {
            'data': List[PatientResource],
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
    def from_dict(cls, dikt: dict) -> 'FetchPatientsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchPatientsResponse of this FetchPatientsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchPatientsResponse.


        :return: The data of this FetchPatientsResponse.
        :rtype: List[PatientResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchPatientsResponse.


        :param data: The data of this FetchPatientsResponse.
        :type data: List[PatientResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def links(self):
        """Gets the links of this FetchPatientsResponse.


        :return: The links of this FetchPatientsResponse.
        :rtype: CollectionResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FetchPatientsResponse.


        :param links: The links of this FetchPatientsResponse.
        :type links: CollectionResponseLinks
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this FetchPatientsResponse.


        :return: The meta of this FetchPatientsResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchPatientsResponse.


        :param meta: The meta of this FetchPatientsResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
