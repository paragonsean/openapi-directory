# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.list_accounts_response_links import ListAccountsResponseLinks
from openapi_server.models.webhook_resource import WebhookResource
from openapi_server import util


class ListWebhooksResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[WebhookResource]=None, links: ListAccountsResponseLinks=None):
        """ListWebhooksResponse - a model defined in OpenAPI

        :param data: The data of this ListWebhooksResponse.
        :param links: The links of this ListWebhooksResponse.
        """
        self.openapi_types = {
            'data': List[WebhookResource],
            'links': ListAccountsResponseLinks
        }

        self.attribute_map = {
            'data': 'data',
            'links': 'links'
        }

        self._data = data
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListWebhooksResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListWebhooksResponse of this ListWebhooksResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListWebhooksResponse.

        The list of webhooks returned in this response. 

        :return: The data of this ListWebhooksResponse.
        :rtype: List[WebhookResource]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListWebhooksResponse.

        The list of webhooks returned in this response. 

        :param data: The data of this ListWebhooksResponse.
        :type data: List[WebhookResource]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def links(self):
        """Gets the links of this ListWebhooksResponse.


        :return: The links of this ListWebhooksResponse.
        :rtype: ListAccountsResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListWebhooksResponse.


        :param links: The links of this ListWebhooksResponse.
        :type links: ListAccountsResponseLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")

        self._links = links
