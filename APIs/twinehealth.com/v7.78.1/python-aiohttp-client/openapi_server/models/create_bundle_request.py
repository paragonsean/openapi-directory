# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bundle_resource import BundleResource
from openapi_server import util


class CreateBundleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: BundleResource=None):
        """CreateBundleRequest - a model defined in OpenAPI

        :param data: The data of this CreateBundleRequest.
        """
        self.openapi_types = {
            'data': BundleResource
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateBundleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateBundleRequest of this CreateBundleRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CreateBundleRequest.


        :return: The data of this CreateBundleRequest.
        :rtype: BundleResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateBundleRequest.


        :param data: The data of this CreateBundleRequest.
        :type data: BundleResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data
