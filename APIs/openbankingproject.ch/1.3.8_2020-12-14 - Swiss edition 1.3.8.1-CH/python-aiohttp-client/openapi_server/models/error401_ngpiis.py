# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.links_all import LinksAll
from openapi_server.models.tpp_message401_piis import TppMessage401PIIS
from openapi_server import util


class Error401NGPIIS(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: LinksAll=None, tpp_messages: List[TppMessage401PIIS]=None):
        """Error401NGPIIS - a model defined in OpenAPI

        :param links: The links of this Error401NGPIIS.
        :param tpp_messages: The tpp_messages of this Error401NGPIIS.
        """
        self.openapi_types = {
            'links': LinksAll,
            'tpp_messages': List[TppMessage401PIIS]
        }

        self.attribute_map = {
            'links': '_links',
            'tpp_messages': 'tppMessages'
        }

        self._links = links
        self._tpp_messages = tpp_messages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error401NGPIIS':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error401_NG_PIIS of this Error401NGPIIS.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Error401NGPIIS.


        :return: The links of this Error401NGPIIS.
        :rtype: LinksAll
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error401NGPIIS.


        :param links: The links of this Error401NGPIIS.
        :type links: LinksAll
        """

        self._links = links

    @property
    def tpp_messages(self):
        """Gets the tpp_messages of this Error401NGPIIS.


        :return: The tpp_messages of this Error401NGPIIS.
        :rtype: List[TppMessage401PIIS]
        """
        return self._tpp_messages

    @tpp_messages.setter
    def tpp_messages(self, tpp_messages):
        """Sets the tpp_messages of this Error401NGPIIS.


        :param tpp_messages: The tpp_messages of this Error401NGPIIS.
        :type tpp_messages: List[TppMessage401PIIS]
        """

        self._tpp_messages = tpp_messages
