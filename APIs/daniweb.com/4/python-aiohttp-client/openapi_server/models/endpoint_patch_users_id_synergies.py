# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.endpoint_patch_users_id_synergies_data import EndpointPatchUsersIDSynergiesData
from openapi_server import util


class EndpointPatchUsersIDSynergies(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: EndpointPatchUsersIDSynergiesData=None, success: bool=None):
        """EndpointPatchUsersIDSynergies - a model defined in OpenAPI

        :param data: The data of this EndpointPatchUsersIDSynergies.
        :param success: The success of this EndpointPatchUsersIDSynergies.
        """
        self.openapi_types = {
            'data': EndpointPatchUsersIDSynergiesData,
            'success': bool
        }

        self.attribute_map = {
            'data': 'data',
            'success': 'success'
        }

        self._data = data
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPatchUsersIDSynergies':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint-patch-users-ID-synergies of this EndpointPatchUsersIDSynergies.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EndpointPatchUsersIDSynergies.


        :return: The data of this EndpointPatchUsersIDSynergies.
        :rtype: EndpointPatchUsersIDSynergiesData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EndpointPatchUsersIDSynergies.


        :param data: The data of this EndpointPatchUsersIDSynergies.
        :type data: EndpointPatchUsersIDSynergiesData
        """

        self._data = data

    @property
    def success(self):
        """Gets the success of this EndpointPatchUsersIDSynergies.


        :return: The success of this EndpointPatchUsersIDSynergies.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EndpointPatchUsersIDSynergies.


        :param success: The success of this EndpointPatchUsersIDSynergies.
        :type success: bool
        """

        self._success = success
