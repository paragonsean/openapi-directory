# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.patient_create_resource_all_of_relationships_groups_meta import PatientCreateResourceAllOfRelationshipsGroupsMeta
from openapi_server import util


class PatientCreateResourceAllOfRelationshipsGroupsData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, meta: PatientCreateResourceAllOfRelationshipsGroupsMeta=None, type: str=None):
        """PatientCreateResourceAllOfRelationshipsGroupsData - a model defined in OpenAPI

        :param id: The id of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :param meta: The meta of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :param type: The type of this PatientCreateResourceAllOfRelationshipsGroupsData.
        """
        self.openapi_types = {
            'id': str,
            'meta': PatientCreateResourceAllOfRelationshipsGroupsMeta,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'meta': 'meta',
            'type': 'type'
        }

        self._id = id
        self._meta = meta
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientCreateResourceAllOfRelationshipsGroupsData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientCreateResource_allOf_relationships_groups_data of this PatientCreateResourceAllOfRelationshipsGroupsData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PatientCreateResourceAllOfRelationshipsGroupsData.

        Required if the `meta.query` is not defined.

        :return: The id of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatientCreateResourceAllOfRelationshipsGroupsData.

        Required if the `meta.query` is not defined.

        :param id: The id of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :type id: str
        """

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this PatientCreateResourceAllOfRelationshipsGroupsData.


        :return: The meta of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :rtype: PatientCreateResourceAllOfRelationshipsGroupsMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PatientCreateResourceAllOfRelationshipsGroupsData.


        :param meta: The meta of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :type meta: PatientCreateResourceAllOfRelationshipsGroupsMeta
        """

        self._meta = meta

    @property
    def type(self):
        """Gets the type of this PatientCreateResourceAllOfRelationshipsGroupsData.


        :return: The type of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatientCreateResourceAllOfRelationshipsGroupsData.


        :param type: The type of this PatientCreateResourceAllOfRelationshipsGroupsData.
        :type type: str
        """
        allowed_values = ["group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
