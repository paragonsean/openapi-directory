# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.root200_response_links import Root200ResponseLinks
from openapi_server import util


class Root200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: Root200ResponseLinks=None, message: str=None):
        """Root200Response - a model defined in OpenAPI

        :param links: The links of this Root200Response.
        :param message: The message of this Root200Response.
        """
        self.openapi_types = {
            'links': Root200ResponseLinks,
            'message': str
        }

        self.attribute_map = {
            'links': '_links',
            'message': 'message'
        }

        self._links = links
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Root200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The root_200_response of this Root200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Root200Response.


        :return: The links of this Root200Response.
        :rtype: Root200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Root200Response.


        :param links: The links of this Root200Response.
        :type links: Root200ResponseLinks
        """

        self._links = links

    @property
    def message(self):
        """Gets the message of this Root200Response.


        :return: The message of this Root200Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Root200Response.


        :param message: The message of this Root200Response.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
