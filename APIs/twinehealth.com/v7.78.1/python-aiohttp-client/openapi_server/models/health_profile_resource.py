# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.health_profile_resource_attributes import HealthProfileResourceAttributes
from openapi_server.models.health_profile_resource_links import HealthProfileResourceLinks
from openapi_server.models.health_profile_resource_relationships import HealthProfileResourceRelationships
from openapi_server import util


class HealthProfileResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: HealthProfileResourceAttributes=None, id: str=None, links: HealthProfileResourceLinks=None, relationships: HealthProfileResourceRelationships=None, type: str=None):
        """HealthProfileResource - a model defined in OpenAPI

        :param attributes: The attributes of this HealthProfileResource.
        :param id: The id of this HealthProfileResource.
        :param links: The links of this HealthProfileResource.
        :param relationships: The relationships of this HealthProfileResource.
        :param type: The type of this HealthProfileResource.
        """
        self.openapi_types = {
            'attributes': HealthProfileResourceAttributes,
            'id': str,
            'links': HealthProfileResourceLinks,
            'relationships': HealthProfileResourceRelationships,
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
    def from_dict(cls, dikt: dict) -> 'HealthProfileResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthProfileResource of this HealthProfileResource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this HealthProfileResource.


        :return: The attributes of this HealthProfileResource.
        :rtype: HealthProfileResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this HealthProfileResource.


        :param attributes: The attributes of this HealthProfileResource.
        :type attributes: HealthProfileResourceAttributes
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this HealthProfileResource.


        :return: The id of this HealthProfileResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthProfileResource.


        :param id: The id of this HealthProfileResource.
        :type id: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this HealthProfileResource.


        :return: The links of this HealthProfileResource.
        :rtype: HealthProfileResourceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this HealthProfileResource.


        :param links: The links of this HealthProfileResource.
        :type links: HealthProfileResourceLinks
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this HealthProfileResource.


        :return: The relationships of this HealthProfileResource.
        :rtype: HealthProfileResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this HealthProfileResource.


        :param relationships: The relationships of this HealthProfileResource.
        :type relationships: HealthProfileResourceRelationships
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this HealthProfileResource.


        :return: The type of this HealthProfileResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthProfileResource.


        :param type: The type of this HealthProfileResource.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
