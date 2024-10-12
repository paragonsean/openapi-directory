# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.transaction_resource_relationships_tags_data_inner import TransactionResourceRelationshipsTagsDataInner
from openapi_server.models.transaction_resource_relationships_tags_links import TransactionResourceRelationshipsTagsLinks
from openapi_server import util


class TransactionResourceRelationshipsTags(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[TransactionResourceRelationshipsTagsDataInner]=None, links: TransactionResourceRelationshipsTagsLinks=None):
        """TransactionResourceRelationshipsTags - a model defined in OpenAPI

        :param data: The data of this TransactionResourceRelationshipsTags.
        :param links: The links of this TransactionResourceRelationshipsTags.
        """
        self.openapi_types = {
            'data': List[TransactionResourceRelationshipsTagsDataInner],
            'links': TransactionResourceRelationshipsTagsLinks
        }

        self.attribute_map = {
            'data': 'data',
            'links': 'links'
        }

        self._data = data
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionResourceRelationshipsTags':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TransactionResource_relationships_tags of this TransactionResourceRelationshipsTags.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this TransactionResourceRelationshipsTags.


        :return: The data of this TransactionResourceRelationshipsTags.
        :rtype: List[TransactionResourceRelationshipsTagsDataInner]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TransactionResourceRelationshipsTags.


        :param data: The data of this TransactionResourceRelationshipsTags.
        :type data: List[TransactionResourceRelationshipsTagsDataInner]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def links(self):
        """Gets the links of this TransactionResourceRelationshipsTags.


        :return: The links of this TransactionResourceRelationshipsTags.
        :rtype: TransactionResourceRelationshipsTagsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionResourceRelationshipsTags.


        :param links: The links of this TransactionResourceRelationshipsTags.
        :type links: TransactionResourceRelationshipsTagsLinks
        """

        self._links = links
