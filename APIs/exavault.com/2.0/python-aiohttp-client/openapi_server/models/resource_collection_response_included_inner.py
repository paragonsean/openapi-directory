# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account import Account
from openapi_server.models.notification import Notification
from openapi_server.models.resource import Resource
from openapi_server.models.share import Share
from openapi_server.models.share_attributes import ShareAttributes
from openapi_server.models.share_relationships import ShareRelationships
from openapi_server.models.user import User
from openapi_server import util


class ResourceCollectionResponseIncludedInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: ShareAttributes=None, id: int=None, relationships: ShareRelationships=None, type: str=None):
        """ResourceCollectionResponseIncludedInner - a model defined in OpenAPI

        :param attributes: The attributes of this ResourceCollectionResponseIncludedInner.
        :param id: The id of this ResourceCollectionResponseIncludedInner.
        :param relationships: The relationships of this ResourceCollectionResponseIncludedInner.
        :param type: The type of this ResourceCollectionResponseIncludedInner.
        """
        self.openapi_types = {
            'attributes': ShareAttributes,
            'id': int,
            'relationships': ShareRelationships,
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
    def from_dict(cls, dikt: dict) -> 'ResourceCollectionResponseIncludedInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceCollectionResponse_included_inner of this ResourceCollectionResponseIncludedInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ResourceCollectionResponseIncludedInner.


        :return: The attributes of this ResourceCollectionResponseIncludedInner.
        :rtype: ShareAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ResourceCollectionResponseIncludedInner.


        :param attributes: The attributes of this ResourceCollectionResponseIncludedInner.
        :type attributes: ShareAttributes
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this ResourceCollectionResponseIncludedInner.

        ID of the share.

        :return: The id of this ResourceCollectionResponseIncludedInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceCollectionResponseIncludedInner.

        ID of the share.

        :param id: The id of this ResourceCollectionResponseIncludedInner.
        :type id: int
        """

        self._id = id

    @property
    def relationships(self):
        """Gets the relationships of this ResourceCollectionResponseIncludedInner.


        :return: The relationships of this ResourceCollectionResponseIncludedInner.
        :rtype: ShareRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this ResourceCollectionResponseIncludedInner.


        :param relationships: The relationships of this ResourceCollectionResponseIncludedInner.
        :type relationships: ShareRelationships
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this ResourceCollectionResponseIncludedInner.


        :return: The type of this ResourceCollectionResponseIncludedInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceCollectionResponseIncludedInner.


        :param type: The type of this ResourceCollectionResponseIncludedInner.
        :type type: str
        """

        self._type = type
