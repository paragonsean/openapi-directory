# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.resource_relationships_share_data import ResourceRelationshipsShareData
from openapi_server import util


class ResourceRelationshipsShare(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: ResourceRelationshipsShareData=None):
        """ResourceRelationshipsShare - a model defined in OpenAPI

        :param data: The data of this ResourceRelationshipsShare.
        """
        self.openapi_types = {
            'data': ResourceRelationshipsShareData
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceRelationshipsShare':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Resource_relationships_share of this ResourceRelationshipsShare.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ResourceRelationshipsShare.


        :return: The data of this ResourceRelationshipsShare.
        :rtype: ResourceRelationshipsShareData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResourceRelationshipsShare.


        :param data: The data of this ResourceRelationshipsShare.
        :type data: ResourceRelationshipsShareData
        """

        self._data = data
