# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.patient_resource_relationships_coaches import PatientResourceRelationshipsCoaches
from openapi_server.models.patient_resource_relationships_groups import PatientResourceRelationshipsGroups
from openapi_server import util


class PatientResourceRelationships(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coaches: PatientResourceRelationshipsCoaches=None, groups: PatientResourceRelationshipsGroups=None):
        """PatientResourceRelationships - a model defined in OpenAPI

        :param coaches: The coaches of this PatientResourceRelationships.
        :param groups: The groups of this PatientResourceRelationships.
        """
        self.openapi_types = {
            'coaches': PatientResourceRelationshipsCoaches,
            'groups': PatientResourceRelationshipsGroups
        }

        self.attribute_map = {
            'coaches': 'coaches',
            'groups': 'groups'
        }

        self._coaches = coaches
        self._groups = groups

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientResourceRelationships':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientResource_relationships of this PatientResourceRelationships.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coaches(self):
        """Gets the coaches of this PatientResourceRelationships.


        :return: The coaches of this PatientResourceRelationships.
        :rtype: PatientResourceRelationshipsCoaches
        """
        return self._coaches

    @coaches.setter
    def coaches(self, coaches):
        """Sets the coaches of this PatientResourceRelationships.


        :param coaches: The coaches of this PatientResourceRelationships.
        :type coaches: PatientResourceRelationshipsCoaches
        """

        self._coaches = coaches

    @property
    def groups(self):
        """Gets the groups of this PatientResourceRelationships.


        :return: The groups of this PatientResourceRelationships.
        :rtype: PatientResourceRelationshipsGroups
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PatientResourceRelationships.


        :param groups: The groups of this PatientResourceRelationships.
        :type groups: PatientResourceRelationshipsGroups
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")

        self._groups = groups
