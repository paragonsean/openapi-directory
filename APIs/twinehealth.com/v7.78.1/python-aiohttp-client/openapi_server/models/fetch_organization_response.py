# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server.models.organization_resource import OrganizationResource
from openapi_server import util


class FetchOrganizationResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: OrganizationResource=None, meta: FetchMetaResponse=None):
        """FetchOrganizationResponse - a model defined in OpenAPI

        :param data: The data of this FetchOrganizationResponse.
        :param meta: The meta of this FetchOrganizationResponse.
        """
        self.openapi_types = {
            'data': OrganizationResource,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchOrganizationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchOrganizationResponse of this FetchOrganizationResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchOrganizationResponse.


        :return: The data of this FetchOrganizationResponse.
        :rtype: OrganizationResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchOrganizationResponse.


        :param data: The data of this FetchOrganizationResponse.
        :type data: OrganizationResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this FetchOrganizationResponse.


        :return: The meta of this FetchOrganizationResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchOrganizationResponse.


        :param meta: The meta of this FetchOrganizationResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
