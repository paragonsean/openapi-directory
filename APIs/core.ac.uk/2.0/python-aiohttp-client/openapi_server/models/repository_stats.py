# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RepositoryStats(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count_fulltext: int=None, count_metadata: int=None, date_last_processed: str=None):
        """RepositoryStats - a model defined in OpenAPI

        :param count_fulltext: The count_fulltext of this RepositoryStats.
        :param count_metadata: The count_metadata of this RepositoryStats.
        :param date_last_processed: The date_last_processed of this RepositoryStats.
        """
        self.openapi_types = {
            'count_fulltext': int,
            'count_metadata': int,
            'date_last_processed': str
        }

        self.attribute_map = {
            'count_fulltext': 'countFulltext',
            'count_metadata': 'countMetadata',
            'date_last_processed': 'dateLastProcessed'
        }

        self._count_fulltext = count_fulltext
        self._count_metadata = count_metadata
        self._date_last_processed = date_last_processed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RepositoryStats':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RepositoryStats of this RepositoryStats.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count_fulltext(self):
        """Gets the count_fulltext of this RepositoryStats.

        Repository fulltext count

        :return: The count_fulltext of this RepositoryStats.
        :rtype: int
        """
        return self._count_fulltext

    @count_fulltext.setter
    def count_fulltext(self, count_fulltext):
        """Sets the count_fulltext of this RepositoryStats.

        Repository fulltext count

        :param count_fulltext: The count_fulltext of this RepositoryStats.
        :type count_fulltext: int
        """

        self._count_fulltext = count_fulltext

    @property
    def count_metadata(self):
        """Gets the count_metadata of this RepositoryStats.

        Repository metadata count

        :return: The count_metadata of this RepositoryStats.
        :rtype: int
        """
        return self._count_metadata

    @count_metadata.setter
    def count_metadata(self, count_metadata):
        """Sets the count_metadata of this RepositoryStats.

        Repository metadata count

        :param count_metadata: The count_metadata of this RepositoryStats.
        :type count_metadata: int
        """

        self._count_metadata = count_metadata

    @property
    def date_last_processed(self):
        """Gets the date_last_processed of this RepositoryStats.

        Last repository processing date

        :return: The date_last_processed of this RepositoryStats.
        :rtype: str
        """
        return self._date_last_processed

    @date_last_processed.setter
    def date_last_processed(self, date_last_processed):
        """Sets the date_last_processed of this RepositoryStats.

        Last repository processing date

        :param date_last_processed: The date_last_processed of this RepositoryStats.
        :type date_last_processed: str
        """

        self._date_last_processed = date_last_processed
