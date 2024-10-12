# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EndpointDeleteGroupsIDMemberships(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, success: bool=None):
        """EndpointDeleteGroupsIDMemberships - a model defined in OpenAPI

        :param success: The success of this EndpointDeleteGroupsIDMemberships.
        """
        self.openapi_types = {
            'success': bool
        }

        self.attribute_map = {
            'success': 'success'
        }

        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointDeleteGroupsIDMemberships':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-delete-groups-ID-memberships of this EndpointDeleteGroupsIDMemberships.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def success(self):
        """Gets the success of this EndpointDeleteGroupsIDMemberships.


        :return: The success of this EndpointDeleteGroupsIDMemberships.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EndpointDeleteGroupsIDMemberships.


        :param success: The success of this EndpointDeleteGroupsIDMemberships.
        :type success: bool
        """

        self._success = success
