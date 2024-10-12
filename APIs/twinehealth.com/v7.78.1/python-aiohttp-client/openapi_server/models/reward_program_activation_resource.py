# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.reward_program_activation_resource_attributes import RewardProgramActivationResourceAttributes
from openapi_server.models.reward_program_activation_resource_relationships import RewardProgramActivationResourceRelationships
from openapi_server import util


class RewardProgramActivationResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: RewardProgramActivationResourceAttributes=None, id: str=None, relationships: RewardProgramActivationResourceRelationships=None, type: str=None):
        """RewardProgramActivationResource - a model defined in OpenAPI

        :param attributes: The attributes of this RewardProgramActivationResource.
        :param id: The id of this RewardProgramActivationResource.
        :param relationships: The relationships of this RewardProgramActivationResource.
        :param type: The type of this RewardProgramActivationResource.
        """
        self.openapi_types = {
            'attributes': RewardProgramActivationResourceAttributes,
            'id': str,
            'relationships': RewardProgramActivationResourceRelationships,
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
    def from_dict(cls, dikt: dict) -> 'RewardProgramActivationResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RewardProgramActivationResource of this RewardProgramActivationResource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this RewardProgramActivationResource.


        :return: The attributes of this RewardProgramActivationResource.
        :rtype: RewardProgramActivationResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this RewardProgramActivationResource.


        :param attributes: The attributes of this RewardProgramActivationResource.
        :type attributes: RewardProgramActivationResourceAttributes
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this RewardProgramActivationResource.


        :return: The id of this RewardProgramActivationResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RewardProgramActivationResource.


        :param id: The id of this RewardProgramActivationResource.
        :type id: str
        """

        self._id = id

    @property
    def relationships(self):
        """Gets the relationships of this RewardProgramActivationResource.


        :return: The relationships of this RewardProgramActivationResource.
        :rtype: RewardProgramActivationResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this RewardProgramActivationResource.


        :param relationships: The relationships of this RewardProgramActivationResource.
        :type relationships: RewardProgramActivationResourceRelationships
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this RewardProgramActivationResource.


        :return: The type of this RewardProgramActivationResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RewardProgramActivationResource.


        :param type: The type of this RewardProgramActivationResource.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
