# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.endpoint_patch_users_id_synergies_data_relationship import EndpointPatchUsersIDSynergiesDataRelationship
from openapi_server import util


class EndpointPatchUsersIDSynergiesData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, relationship: EndpointPatchUsersIDSynergiesDataRelationship=None):
        """EndpointPatchUsersIDSynergiesData - a model defined in OpenAPI

        :param relationship: The relationship of this EndpointPatchUsersIDSynergiesData.
        """
        self.openapi_types = {
            'relationship': EndpointPatchUsersIDSynergiesDataRelationship
        }

        self.attribute_map = {
            'relationship': 'relationship'
        }

        self._relationship = relationship

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointPatchUsersIDSynergiesData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint_patch_users_ID_synergies_data of this EndpointPatchUsersIDSynergiesData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def relationship(self):
        """Gets the relationship of this EndpointPatchUsersIDSynergiesData.


        :return: The relationship of this EndpointPatchUsersIDSynergiesData.
        :rtype: EndpointPatchUsersIDSynergiesDataRelationship
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this EndpointPatchUsersIDSynergiesData.


        :param relationship: The relationship of this EndpointPatchUsersIDSynergiesData.
        :type relationship: EndpointPatchUsersIDSynergiesDataRelationship
        """

        self._relationship = relationship
