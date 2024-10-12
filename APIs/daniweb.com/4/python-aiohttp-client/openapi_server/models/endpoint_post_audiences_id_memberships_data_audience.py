# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EndpointPostAudiencesIDMembershipsDataAudience(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: float=None):
        """EndpointPostAudiencesIDMembershipsDataAudience - a model defined in OpenAPI

        :param id: The id of this EndpointPostAudiencesIDMembershipsDataAudience.
        """
        self.openapi_types = {
            'id': float
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPostAudiencesIDMembershipsDataAudience':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint_post_audiences_ID_memberships_data_audience of this EndpointPostAudiencesIDMembershipsDataAudience.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EndpointPostAudiencesIDMembershipsDataAudience.


        :return: The id of this EndpointPostAudiencesIDMembershipsDataAudience.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointPostAudiencesIDMembershipsDataAudience.


        :param id: The id of this EndpointPostAudiencesIDMembershipsDataAudience.
        :type id: float
        """

        self._id = id
