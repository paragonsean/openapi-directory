# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.collection_links import CollectionLinks
from openapi_server import util


class CollectionMeta(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, links: CollectionLinks=None):
        """CollectionMeta - a model defined in OpenAPI

        :param count: The count of this CollectionMeta.
        :param links: The links of this CollectionMeta.
        """
        self.openapi_types = {
            'count': int,
            'links': CollectionLinks
        }

        self.attribute_map = {
            'count': 'count',
            'links': 'links'
        }

        self._count = count
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionMeta':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Collection_Meta of this CollectionMeta.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this CollectionMeta.


        :return: The count of this CollectionMeta.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CollectionMeta.


        :param count: The count of this CollectionMeta.
        :type count: int
        """

        self._count = count

    @property
    def links(self):
        """Gets the links of this CollectionMeta.


        :return: The links of this CollectionMeta.
        :rtype: CollectionLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionMeta.


        :param links: The links of this CollectionMeta.
        :type links: CollectionLinks
        """

        self._links = links
