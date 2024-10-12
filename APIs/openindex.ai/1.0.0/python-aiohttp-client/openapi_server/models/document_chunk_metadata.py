# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.source import Source
from openapi_server import util


class DocumentChunkMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, author: str=None, collection_id: str=None, created_at: str=None, document_id: str=None, keywords: List[str]=None, language: str=None, source: Source=None, source_id: str=None, time_period: str=None, updated_at: str=None, url: str=None, user_id: str=None):
        """DocumentChunkMetadata - a model defined in OpenAPI

        :param author: The author of this DocumentChunkMetadata.
        :param collection_id: The collection_id of this DocumentChunkMetadata.
        :param created_at: The created_at of this DocumentChunkMetadata.
        :param document_id: The document_id of this DocumentChunkMetadata.
        :param keywords: The keywords of this DocumentChunkMetadata.
        :param language: The language of this DocumentChunkMetadata.
        :param source: The source of this DocumentChunkMetadata.
        :param source_id: The source_id of this DocumentChunkMetadata.
        :param time_period: The time_period of this DocumentChunkMetadata.
        :param updated_at: The updated_at of this DocumentChunkMetadata.
        :param url: The url of this DocumentChunkMetadata.
        :param user_id: The user_id of this DocumentChunkMetadata.
        """
        self.openapi_types = {
            'author': str,
            'collection_id': str,
            'created_at': str,
            'document_id': str,
            'keywords': List[str],
            'language': str,
            'source': Source,
            'source_id': str,
            'time_period': str,
            'updated_at': str,
            'url': str,
            'user_id': str
        }

        self.attribute_map = {
            'author': 'author',
            'collection_id': 'collection_id',
            'created_at': 'created_at',
            'document_id': 'document_id',
            'keywords': 'keywords',
            'language': 'language',
            'source': 'source',
            'source_id': 'source_id',
            'time_period': 'time_period',
            'updated_at': 'updated_at',
            'url': 'url',
            'user_id': 'user_id'
        }

        self._author = author
        self._collection_id = collection_id
        self._created_at = created_at
        self._document_id = document_id
        self._keywords = keywords
        self._language = language
        self._source = source
        self._source_id = source_id
        self._time_period = time_period
        self._updated_at = updated_at
        self._url = url
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DocumentChunkMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DocumentChunkMetadata of this DocumentChunkMetadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def author(self):
        """Gets the author of this DocumentChunkMetadata.


        :return: The author of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DocumentChunkMetadata.


        :param author: The author of this DocumentChunkMetadata.
        :type author: str
        """

        self._author = author

    @property
    def collection_id(self):
        """Gets the collection_id of this DocumentChunkMetadata.


        :return: The collection_id of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this DocumentChunkMetadata.


        :param collection_id: The collection_id of this DocumentChunkMetadata.
        :type collection_id: str
        """

        self._collection_id = collection_id

    @property
    def created_at(self):
        """Gets the created_at of this DocumentChunkMetadata.


        :return: The created_at of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentChunkMetadata.


        :param created_at: The created_at of this DocumentChunkMetadata.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def document_id(self):
        """Gets the document_id of this DocumentChunkMetadata.


        :return: The document_id of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentChunkMetadata.


        :param document_id: The document_id of this DocumentChunkMetadata.
        :type document_id: str
        """

        self._document_id = document_id

    @property
    def keywords(self):
        """Gets the keywords of this DocumentChunkMetadata.


        :return: The keywords of this DocumentChunkMetadata.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this DocumentChunkMetadata.


        :param keywords: The keywords of this DocumentChunkMetadata.
        :type keywords: List[str]
        """

        self._keywords = keywords

    @property
    def language(self):
        """Gets the language of this DocumentChunkMetadata.


        :return: The language of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DocumentChunkMetadata.


        :param language: The language of this DocumentChunkMetadata.
        :type language: str
        """

        self._language = language

    @property
    def source(self):
        """Gets the source of this DocumentChunkMetadata.


        :return: The source of this DocumentChunkMetadata.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DocumentChunkMetadata.


        :param source: The source of this DocumentChunkMetadata.
        :type source: Source
        """

        self._source = source

    @property
    def source_id(self):
        """Gets the source_id of this DocumentChunkMetadata.


        :return: The source_id of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this DocumentChunkMetadata.


        :param source_id: The source_id of this DocumentChunkMetadata.
        :type source_id: str
        """

        self._source_id = source_id

    @property
    def time_period(self):
        """Gets the time_period of this DocumentChunkMetadata.


        :return: The time_period of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this DocumentChunkMetadata.


        :param time_period: The time_period of this DocumentChunkMetadata.
        :type time_period: str
        """

        self._time_period = time_period

    @property
    def updated_at(self):
        """Gets the updated_at of this DocumentChunkMetadata.


        :return: The updated_at of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DocumentChunkMetadata.


        :param updated_at: The updated_at of this DocumentChunkMetadata.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this DocumentChunkMetadata.


        :return: The url of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DocumentChunkMetadata.


        :param url: The url of this DocumentChunkMetadata.
        :type url: str
        """

        self._url = url

    @property
    def user_id(self):
        """Gets the user_id of this DocumentChunkMetadata.


        :return: The user_id of this DocumentChunkMetadata.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DocumentChunkMetadata.


        :param user_id: The user_id of this DocumentChunkMetadata.
        :type user_id: str
        """

        self._user_id = user_id
