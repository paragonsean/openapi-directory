# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.links import Links
from openapi_server import util


class Meta(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: Links=None):
        """Meta - a model defined in OpenAPI

        :param links: The links of this Meta.
        """
        self.openapi_types = {
            'links': Links
        }

        self.attribute_map = {
            'links': 'links'
        }

        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Meta':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Meta of this Meta.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Meta.


        :return: The links of this Meta.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Meta.


        :param links: The links of this Meta.
        :type links: Links
        """

        self._links = links
