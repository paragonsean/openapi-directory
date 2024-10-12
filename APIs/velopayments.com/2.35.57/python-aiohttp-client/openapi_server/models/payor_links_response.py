# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.payor_links_response_links import PayorLinksResponseLinks
from openapi_server.models.payor_links_response_payors import PayorLinksResponsePayors
from openapi_server import util


class PayorLinksResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: List[PayorLinksResponseLinks]=None, payors: List[PayorLinksResponsePayors]=None):
        """PayorLinksResponse - a model defined in OpenAPI

        :param links: The links of this PayorLinksResponse.
        :param payors: The payors of this PayorLinksResponse.
        """
        self.openapi_types = {
            'links': List[PayorLinksResponseLinks],
            'payors': List[PayorLinksResponsePayors]
        }

        self.attribute_map = {
            'links': 'links',
            'payors': 'payors'
        }

        self._links = links
        self._payors = payors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayorLinksResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayorLinksResponse of this PayorLinksResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this PayorLinksResponse.


        :return: The links of this PayorLinksResponse.
        :rtype: List[PayorLinksResponseLinks]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PayorLinksResponse.


        :param links: The links of this PayorLinksResponse.
        :type links: List[PayorLinksResponseLinks]
        """

        self._links = links

    @property
    def payors(self):
        """Gets the payors of this PayorLinksResponse.


        :return: The payors of this PayorLinksResponse.
        :rtype: List[PayorLinksResponsePayors]
        """
        return self._payors

    @payors.setter
    def payors(self, payors):
        """Sets the payors of this PayorLinksResponse.


        :param payors: The payors of this PayorLinksResponse.
        :type payors: List[PayorLinksResponsePayors]
        """

        self._payors = payors
