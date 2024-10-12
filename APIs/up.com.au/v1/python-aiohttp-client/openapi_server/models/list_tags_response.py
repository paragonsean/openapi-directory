# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.list_accounts_response_links import ListAccountsResponseLinks
from openapi_server.models.tag_resource import TagResource
from openapi_server import util


class ListTagsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[TagResource]=None, links: ListAccountsResponseLinks=None):
        """ListTagsResponse - a model defined in OpenAPI

        :param data: The data of this ListTagsResponse.
        :param links: The links of this ListTagsResponse.
        """
        self.openapi_types = {
            'data': List[TagResource],
            'links': ListAccountsResponseLinks
        }

        self.attribute_map = {
            'data': 'data',
            'links': 'links'
        }

        self._data = data
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListTagsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListTagsResponse of this ListTagsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListTagsResponse.

        The list of tags returned in this response. 

        :return: The data of this ListTagsResponse.
        :rtype: List[TagResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListTagsResponse.

        The list of tags returned in this response. 

        :param data: The data of this ListTagsResponse.
        :type data: List[TagResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def links(self):
        """Gets the links of this ListTagsResponse.


        :return: The links of this ListTagsResponse.
        :rtype: ListAccountsResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListTagsResponse.


        :param links: The links of this ListTagsResponse.
        :type links: ListAccountsResponseLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")

        self._links = links
