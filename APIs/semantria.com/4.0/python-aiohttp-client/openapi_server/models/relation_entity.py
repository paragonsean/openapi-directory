# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RelationEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_type: str=None, title: str=None):
        """RelationEntity - a model defined in OpenAPI

        :param entity_type: The entity_type of this RelationEntity.
        :param title: The title of this RelationEntity.
        """
        self.openapi_types = {
            'entity_type': str,
            'title': str
        }

        self.attribute_map = {
            'entity_type': 'entity_type',
            'title': 'title'
        }

        self._entity_type = entity_type
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RelationEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RelationEntity of this RelationEntity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_type(self):
        """Gets the entity_type of this RelationEntity.

        Type of the entity (Company, Person, Place, Product, etc.)

        :return: The entity_type of this RelationEntity.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this RelationEntity.

        Type of the entity (Company, Person, Place, Product, etc.)

        :param entity_type: The entity_type of this RelationEntity.
        :type entity_type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def title(self):
        """Gets the title of this RelationEntity.

        Normalized entity title based on existing entity normalization rules

        :return: The title of this RelationEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RelationEntity.

        Normalized entity title based on existing entity normalization rules

        :param title: The title of this RelationEntity.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title
