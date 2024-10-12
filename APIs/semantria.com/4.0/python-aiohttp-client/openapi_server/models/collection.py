# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Collection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, documents: List[str]=None, id: str=None, job_id: str=None, tag: str=None):
        """Collection - a model defined in OpenAPI

        :param documents: The documents of this Collection.
        :param id: The id of this Collection.
        :param job_id: The job_id of this Collection.
        :param tag: The tag of this Collection.
        """
        self.openapi_types = {
            'documents': List[str],
            'id': str,
            'job_id': str,
            'tag': str
        }

        self.attribute_map = {
            'documents': 'documents',
            'id': 'id',
            'job_id': 'job_id',
            'tag': 'tag'
        }

        self._documents = documents
        self._id = id
        self._job_id = job_id
        self._tag = tag

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Collection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Collection of this Collection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def documents(self):
        """Gets the documents of this Collection.

        List of documents text that need to be analyzed by the service

        :return: The documents of this Collection.
        :rtype: List[str]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Collection.

        List of documents text that need to be analyzed by the service

        :param documents: The documents of this Collection.
        :type documents: List[str]
        """
        if documents is None:
            raise ValueError("Invalid value for `documents`, must not be `None`")

        self._documents = documents

    @property
    def id(self):
        """Gets the id of this Collection.

        Up to 32 symbols unique identifier of document assigned and tracked by client

        :return: The id of this Collection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Collection.

        Up to 32 symbols unique identifier of document assigned and tracked by client

        :param id: The id of this Collection.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this Collection.

        Specific marker of incoming job that can be used then for collections retrieving

        :return: The job_id of this Collection.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Collection.

        Specific marker of incoming job that can be used then for collections retrieving

        :param job_id: The job_id of this Collection.
        :type job_id: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")

        self._job_id = job_id

    @property
    def tag(self):
        """Gets the tag of this Collection.

        Any text of up to 50 characters used like marker

        :return: The tag of this Collection.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Collection.

        Any text of up to 50 characters used like marker

        :param tag: The tag of this Collection.
        :type tag: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")

        self._tag = tag
