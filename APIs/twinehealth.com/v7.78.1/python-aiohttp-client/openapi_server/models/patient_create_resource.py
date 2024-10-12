# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.patient_create_resource_all_of_relationships import PatientCreateResourceAllOfRelationships
from openapi_server.models.patient_resource_attributes import PatientResourceAttributes
from openapi_server.models.patient_resource_links import PatientResourceLinks
from openapi_server import util


class PatientCreateResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: PatientResourceAttributes=None, id: str=None, links: PatientResourceLinks=None, relationships: PatientCreateResourceAllOfRelationships=None, type: str=None):
        """PatientCreateResource - a model defined in OpenAPI

        :param attributes: The attributes of this PatientCreateResource.
        :param id: The id of this PatientCreateResource.
        :param links: The links of this PatientCreateResource.
        :param relationships: The relationships of this PatientCreateResource.
        :param type: The type of this PatientCreateResource.
        """
        self.openapi_types = {
            'attributes': PatientResourceAttributes,
            'id': str,
            'links': PatientResourceLinks,
            'relationships': PatientCreateResourceAllOfRelationships,
            'type': str
        }

        self.attribute_map = {
            'attributes': 'attributes',
            'id': 'id',
            'links': 'links',
            'relationships': 'relationships',
            'type': 'type'
        }

        self._attributes = attributes
        self._id = id
        self._links = links
        self._relationships = relationships
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatientCreateResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatientCreateResource of this PatientCreateResource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this PatientCreateResource.


        :return: The attributes of this PatientCreateResource.
        :rtype: PatientResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PatientCreateResource.


        :param attributes: The attributes of this PatientCreateResource.
        :type attributes: PatientResourceAttributes
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this PatientCreateResource.


        :return: The id of this PatientCreateResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatientCreateResource.


        :param id: The id of this PatientCreateResource.
        :type id: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this PatientCreateResource.


        :return: The links of this PatientCreateResource.
        :rtype: PatientResourceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PatientCreateResource.


        :param links: The links of this PatientCreateResource.
        :type links: PatientResourceLinks
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this PatientCreateResource.


        :return: The relationships of this PatientCreateResource.
        :rtype: PatientCreateResourceAllOfRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this PatientCreateResource.


        :param relationships: The relationships of this PatientCreateResource.
        :type relationships: PatientCreateResourceAllOfRelationships
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this PatientCreateResource.


        :return: The type of this PatientCreateResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatientCreateResource.


        :param type: The type of this PatientCreateResource.
        :type type: str
        """
        allowed_values = ["patient"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
