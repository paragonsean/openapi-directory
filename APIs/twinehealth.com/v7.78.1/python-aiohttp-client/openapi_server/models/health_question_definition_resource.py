# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.health_question_definition_resource_attributes import HealthQuestionDefinitionResourceAttributes
from openapi_server.models.health_question_definition_resource_links import HealthQuestionDefinitionResourceLinks
from openapi_server import util


class HealthQuestionDefinitionResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes: HealthQuestionDefinitionResourceAttributes=None, id: str=None, links: HealthQuestionDefinitionResourceLinks=None, relationships: object=None, type: str=None):
        """HealthQuestionDefinitionResource - a model defined in OpenAPI

        :param attributes: The attributes of this HealthQuestionDefinitionResource.
        :param id: The id of this HealthQuestionDefinitionResource.
        :param links: The links of this HealthQuestionDefinitionResource.
        :param relationships: The relationships of this HealthQuestionDefinitionResource.
        :param type: The type of this HealthQuestionDefinitionResource.
        """
        self.openapi_types = {
            'attributes': HealthQuestionDefinitionResourceAttributes,
            'id': str,
            'links': HealthQuestionDefinitionResourceLinks,
            'relationships': object,
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
    def from_dict(cls, dikt: dict) -> 'HealthQuestionDefinitionResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthQuestionDefinitionResource of this HealthQuestionDefinitionResource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this HealthQuestionDefinitionResource.


        :return: The attributes of this HealthQuestionDefinitionResource.
        :rtype: HealthQuestionDefinitionResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this HealthQuestionDefinitionResource.


        :param attributes: The attributes of this HealthQuestionDefinitionResource.
        :type attributes: HealthQuestionDefinitionResourceAttributes
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this HealthQuestionDefinitionResource.


        :return: The id of this HealthQuestionDefinitionResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthQuestionDefinitionResource.


        :param id: The id of this HealthQuestionDefinitionResource.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def links(self):
        """Gets the links of this HealthQuestionDefinitionResource.


        :return: The links of this HealthQuestionDefinitionResource.
        :rtype: HealthQuestionDefinitionResourceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this HealthQuestionDefinitionResource.


        :param links: The links of this HealthQuestionDefinitionResource.
        :type links: HealthQuestionDefinitionResourceLinks
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this HealthQuestionDefinitionResource.


        :return: The relationships of this HealthQuestionDefinitionResource.
        :rtype: object
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this HealthQuestionDefinitionResource.


        :param relationships: The relationships of this HealthQuestionDefinitionResource.
        :type relationships: object
        """

        self._relationships = relationships

    @property
    def type(self):
        """Gets the type of this HealthQuestionDefinitionResource.


        :return: The type of this HealthQuestionDefinitionResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthQuestionDefinitionResource.


        :param type: The type of this HealthQuestionDefinitionResource.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
