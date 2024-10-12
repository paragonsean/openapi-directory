# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.normalized_rectangle import NormalizedRectangle
from openapi_server.models.recognized_entity import RecognizedEntity
from openapi_server.models.response import Response
from openapi_server import util


class RecognizedEntityRegion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, matching_entities: List[RecognizedEntity]=None, region: NormalizedRectangle=None, read_link: str=None, web_search_url: str=None, id: str=None, type: str=None):
        """RecognizedEntityRegion - a model defined in OpenAPI

        :param matching_entities: The matching_entities of this RecognizedEntityRegion.
        :param region: The region of this RecognizedEntityRegion.
        :param read_link: The read_link of this RecognizedEntityRegion.
        :param web_search_url: The web_search_url of this RecognizedEntityRegion.
        :param id: The id of this RecognizedEntityRegion.
        :param type: The type of this RecognizedEntityRegion.
        """
        self.openapi_types = {
            'matching_entities': List[RecognizedEntity],
            'region': NormalizedRectangle,
            'read_link': str,
            'web_search_url': str,
            'id': str,
            'type': str
        }

        self.attribute_map = {
            'matching_entities': 'matchingEntities',
            'region': 'region',
            'read_link': 'readLink',
            'web_search_url': 'webSearchUrl',
            'id': 'id',
            'type': '_type'
        }

        self._matching_entities = matching_entities
        self._region = region
        self._read_link = read_link
        self._web_search_url = web_search_url
        self._id = id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RecognizedEntityRegion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RecognizedEntityRegion of this RecognizedEntityRegion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def matching_entities(self):
        """Gets the matching_entities of this RecognizedEntityRegion.

        A list of entities that Bing believes match the entity found in the region. The entities are in descending order of confidence (see the matchConfidence field of RecognizedEntity).

        :return: The matching_entities of this RecognizedEntityRegion.
        :rtype: List[RecognizedEntity]
        """
        return self._matching_entities

    @matching_entities.setter
    def matching_entities(self, matching_entities):
        """Sets the matching_entities of this RecognizedEntityRegion.

        A list of entities that Bing believes match the entity found in the region. The entities are in descending order of confidence (see the matchConfidence field of RecognizedEntity).

        :param matching_entities: The matching_entities of this RecognizedEntityRegion.
        :type matching_entities: List[RecognizedEntity]
        """

        self._matching_entities = matching_entities

    @property
    def region(self):
        """Gets the region of this RecognizedEntityRegion.


        :return: The region of this RecognizedEntityRegion.
        :rtype: NormalizedRectangle
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RecognizedEntityRegion.


        :param region: The region of this RecognizedEntityRegion.
        :type region: NormalizedRectangle
        """

        self._region = region

    @property
    def read_link(self):
        """Gets the read_link of this RecognizedEntityRegion.

        The URL that returns this resource.

        :return: The read_link of this RecognizedEntityRegion.
        :rtype: str
        """
        return self._read_link

    @read_link.setter
    def read_link(self, read_link):
        """Sets the read_link of this RecognizedEntityRegion.

        The URL that returns this resource.

        :param read_link: The read_link of this RecognizedEntityRegion.
        :type read_link: str
        """

        self._read_link = read_link

    @property
    def web_search_url(self):
        """Gets the web_search_url of this RecognizedEntityRegion.

        The URL To Bing's search result for this item.

        :return: The web_search_url of this RecognizedEntityRegion.
        :rtype: str
        """
        return self._web_search_url

    @web_search_url.setter
    def web_search_url(self, web_search_url):
        """Sets the web_search_url of this RecognizedEntityRegion.

        The URL To Bing's search result for this item.

        :param web_search_url: The web_search_url of this RecognizedEntityRegion.
        :type web_search_url: str
        """

        self._web_search_url = web_search_url

    @property
    def id(self):
        """Gets the id of this RecognizedEntityRegion.

        A String identifier.

        :return: The id of this RecognizedEntityRegion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecognizedEntityRegion.

        A String identifier.

        :param id: The id of this RecognizedEntityRegion.
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this RecognizedEntityRegion.


        :return: The type of this RecognizedEntityRegion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecognizedEntityRegion.


        :param type: The type of this RecognizedEntityRegion.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
