# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_resource_links import AccountResourceLinks
from openapi_server.models.category_resource_attributes import CategoryResourceAttributes
from openapi_server.models.category_resource_relationships import CategoryResourceRelationships
from openapi_server import util


class CategoryResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: CategoryResourceAttributes=None, id: str=None, links: AccountResourceLinks=None, relationships: CategoryResourceRelationships=None, type: str=None):
        """CategoryResource - a model defined in OpenAPI

        :param attributes: The attributes of this CategoryResource.
        :param id: The id of this CategoryResource.
        :param links: The links of this CategoryResource.
        :param relationships: The relationships of this CategoryResource.
        :param type: The type of this CategoryResource.
        """
        self.openapi_types = {
            'attributes': CategoryResourceAttributes,
            'id': str,
            'links': AccountResourceLinks,
            'relationships': CategoryResourceRelationships,
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
    def from_dict(cls, dikt: dict) -> 'CategoryResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CategoryResource of this CategoryResource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this CategoryResource.


        :return: The attributes of this CategoryResource.
        :rtype: CategoryResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CategoryResource.


        :param attributes: The attributes of this CategoryResource.
        :type attributes: CategoryResourceAttributes
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this CategoryResource.

        The unique identifier for this category. This is a human-readable but URL-safe value. 

        :return: The id of this CategoryResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryResource.

        The unique identifier for this category. This is a human-readable but URL-safe value. 

        :param id: The id of this CategoryResource.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def links(self):
        """Gets the links of this CategoryResource.


        :return: The links of this CategoryResource.
        :rtype: AccountResourceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CategoryResource.


        :param links: The links of this CategoryResource.
        :type links: AccountResourceLinks
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this CategoryResource.


        :return: The relationships of this CategoryResource.
        :rtype: CategoryResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this CategoryResource.


        :param relationships: The relationships of this CategoryResource.
        :type relationships: CategoryResourceRelationships
        """
        if relationships is None:
            raise ValueError("Invalid value for `relationships`, must not be `None`")

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this CategoryResource.

        The type of this resource: `categories`

        :return: The type of this CategoryResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CategoryResource.

        The type of this resource: `categories`

        :param type: The type of this CategoryResource.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
