# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bundle_resource import BundleResource
from openapi_server.models.fetch_meta_response import FetchMetaResponse
from openapi_server import util


class FetchBundleResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: BundleResource=None, meta: FetchMetaResponse=None):
        """FetchBundleResponse - a model defined in OpenAPI

        :param data: The data of this FetchBundleResponse.
        :param meta: The meta of this FetchBundleResponse.
        """
        self.openapi_types = {
            'data': BundleResource,
            'meta': FetchMetaResponse
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FetchBundleResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FetchBundleResponse of this FetchBundleResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this FetchBundleResponse.


        :return: The data of this FetchBundleResponse.
        :rtype: BundleResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FetchBundleResponse.


        :param data: The data of this FetchBundleResponse.
        :type data: BundleResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this FetchBundleResponse.


        :return: The meta of this FetchBundleResponse.
        :rtype: FetchMetaResponse
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FetchBundleResponse.


        :param meta: The meta of this FetchBundleResponse.
        :type meta: FetchMetaResponse
        """

        self._meta = meta
