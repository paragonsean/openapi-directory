# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.album_for_user_for_api_contract import AlbumForUserForApiContract
from openapi_server import util


class AlbumForUserForApiContractPartialFindResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[AlbumForUserForApiContract]=None, term: str=None, total_count: int=None):
        """AlbumForUserForApiContractPartialFindResult - a model defined in OpenAPI

        :param items: The items of this AlbumForUserForApiContractPartialFindResult.
        :param term: The term of this AlbumForUserForApiContractPartialFindResult.
        :param total_count: The total_count of this AlbumForUserForApiContractPartialFindResult.
        """
        self.openapi_types = {
            'items': List[AlbumForUserForApiContract],
            'term': str,
            'total_count': int
        }

        self.attribute_map = {
            'items': 'items',
            'term': 'term',
            'total_count': 'totalCount'
        }

        self._items = items
        self._term = term
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlbumForUserForApiContractPartialFindResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlbumForUserForApiContractPartialFindResult of this AlbumForUserForApiContractPartialFindResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this AlbumForUserForApiContractPartialFindResult.


        :return: The items of this AlbumForUserForApiContractPartialFindResult.
        :rtype: List[AlbumForUserForApiContract]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AlbumForUserForApiContractPartialFindResult.


        :param items: The items of this AlbumForUserForApiContractPartialFindResult.
        :type items: List[AlbumForUserForApiContract]
        """

        self._items = items

    @property
    def term(self):
        """Gets the term of this AlbumForUserForApiContractPartialFindResult.


        :return: The term of this AlbumForUserForApiContractPartialFindResult.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this AlbumForUserForApiContractPartialFindResult.


        :param term: The term of this AlbumForUserForApiContractPartialFindResult.
        :type term: str
        """

        self._term = term

    @property
    def total_count(self):
        """Gets the total_count of this AlbumForUserForApiContractPartialFindResult.


        :return: The total_count of this AlbumForUserForApiContractPartialFindResult.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this AlbumForUserForApiContractPartialFindResult.


        :param total_count: The total_count of this AlbumForUserForApiContractPartialFindResult.
        :type total_count: int
        """

        self._total_count = total_count
