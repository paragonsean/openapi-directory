# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class TokenResourceRelationshipsGroupsLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, related: str=None):
        """TokenResourceRelationshipsGroupsLinks - a model defined in OpenAPI

        :param related: The related of this TokenResourceRelationshipsGroupsLinks.
        """
        self.openapi_types = {
            'related': str
        }

        self.attribute_map = {
            'related': 'related'
        }

        self._related = related

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TokenResourceRelationshipsGroupsLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TokenResource_relationships_groups_links of this TokenResourceRelationshipsGroupsLinks.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def related(self):
        """Gets the related of this TokenResourceRelationshipsGroupsLinks.


        :return: The related of this TokenResourceRelationshipsGroupsLinks.
        :rtype: str
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this TokenResourceRelationshipsGroupsLinks.


        :param related: The related of this TokenResourceRelationshipsGroupsLinks.
        :type related: str
        """
        if related is None:
            raise ValueError("Invalid value for `related`, must not be `None`")
        if related is not None and not re.search(r'oauth/token/[0-9a-z]+', related, flags=re.UNICODE | re.DOTALL):
            raise ValueError("Invalid value for `related`, must be a follow pattern or equal to `/oauth/token/[0-9a-z]+/groups`")

        self._related = related
