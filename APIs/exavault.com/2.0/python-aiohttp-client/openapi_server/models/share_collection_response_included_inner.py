# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification import Notification
from openapi_server.models.resource import Resource
from openapi_server.models.resource_attributes import ResourceAttributes
from openapi_server.models.resource_relationships import ResourceRelationships
from openapi_server.models.user import User
from openapi_server import util


class ShareCollectionResponseIncludedInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: ResourceAttributes=None, id: int=None, relationships: ResourceRelationships=None, type: str=None):
        """ShareCollectionResponseIncludedInner - a model defined in OpenAPI

        :param attributes: The attributes of this ShareCollectionResponseIncludedInner.
        :param id: The id of this ShareCollectionResponseIncludedInner.
        :param relationships: The relationships of this ShareCollectionResponseIncludedInner.
        :param type: The type of this ShareCollectionResponseIncludedInner.
        """
        self.openapi_types = {
            'attributes': ResourceAttributes,
            'id': int,
            'relationships': ResourceRelationships,
            'type': str
        }

        self.attribute_map = {
            'attributes': 'attributes',
            'id': 'id',
            'relationships': 'relationships',
            'type': 'type'
        }

        self._attributes = attributes
        self._id = id
        self._relationships = relationships
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShareCollectionResponseIncludedInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ShareCollectionResponse_included_inner of this ShareCollectionResponseIncludedInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ShareCollectionResponseIncludedInner.


        :return: The attributes of this ShareCollectionResponseIncludedInner.
        :rtype: ResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ShareCollectionResponseIncludedInner.


        :param attributes: The attributes of this ShareCollectionResponseIncludedInner.
        :type attributes: ResourceAttributes
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this ShareCollectionResponseIncludedInner.


        :return: The id of this ShareCollectionResponseIncludedInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShareCollectionResponseIncludedInner.


        :param id: The id of this ShareCollectionResponseIncludedInner.
        :type id: int
        """

        self._id = id

    @property
    def relationships(self):
        """Gets the relationships of this ShareCollectionResponseIncludedInner.


        :return: The relationships of this ShareCollectionResponseIncludedInner.
        :rtype: ResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this ShareCollectionResponseIncludedInner.


        :param relationships: The relationships of this ShareCollectionResponseIncludedInner.
        :type relationships: ResourceRelationships
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this ShareCollectionResponseIncludedInner.


        :return: The type of this ShareCollectionResponseIncludedInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShareCollectionResponseIncludedInner.


        :param type: The type of this ShareCollectionResponseIncludedInner.
        :type type: str
        """

        self._type = type
