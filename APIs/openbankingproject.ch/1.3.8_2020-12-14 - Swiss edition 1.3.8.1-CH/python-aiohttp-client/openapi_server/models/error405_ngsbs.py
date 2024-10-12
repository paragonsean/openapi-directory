# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.links_all import LinksAll
from openapi_server.models.tpp_message405_sbs import TppMessage405SBS
from openapi_server import util


class Error405NGSBS(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: LinksAll=None, tpp_messages: List[TppMessage405SBS]=None):
        """Error405NGSBS - a model defined in OpenAPI

        :param links: The links of this Error405NGSBS.
        :param tpp_messages: The tpp_messages of this Error405NGSBS.
        """
        self.openapi_types = {
            'links': LinksAll,
            'tpp_messages': List[TppMessage405SBS]
        }

        self.attribute_map = {
            'links': '_links',
            'tpp_messages': 'tppMessages'
        }

        self._links = links
        self._tpp_messages = tpp_messages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error405NGSBS':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error405_NG_SBS of this Error405NGSBS.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Error405NGSBS.


        :return: The links of this Error405NGSBS.
        :rtype: LinksAll
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error405NGSBS.


        :param links: The links of this Error405NGSBS.
        :type links: LinksAll
        """

        self._links = links

    @property
    def tpp_messages(self):
        """Gets the tpp_messages of this Error405NGSBS.


        :return: The tpp_messages of this Error405NGSBS.
        :rtype: List[TppMessage405SBS]
        """
        return self._tpp_messages

    @tpp_messages.setter
    def tpp_messages(self, tpp_messages):
        """Sets the tpp_messages of this Error405NGSBS.


        :param tpp_messages: The tpp_messages of this Error405NGSBS.
        :type tpp_messages: List[TppMessage405SBS]
        """

        self._tpp_messages = tpp_messages
