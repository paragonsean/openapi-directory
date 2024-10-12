# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.artist_for_api_contract import ArtistForApiContract
from openapi_server import util


class ArtistForUserForApiContract(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, artist: ArtistForApiContract=None, id: int=None):
        """ArtistForUserForApiContract - a model defined in OpenAPI

        :param artist: The artist of this ArtistForUserForApiContract.
        :param id: The id of this ArtistForUserForApiContract.
        """
        self.openapi_types = {
            'artist': ArtistForApiContract,
            'id': int
        }

        self.attribute_map = {
            'artist': 'artist',
            'id': 'id'
        }

        self._artist = artist
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArtistForUserForApiContract':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArtistForUserForApiContract of this ArtistForUserForApiContract.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def artist(self):
        """Gets the artist of this ArtistForUserForApiContract.


        :return: The artist of this ArtistForUserForApiContract.
        :rtype: ArtistForApiContract
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """Sets the artist of this ArtistForUserForApiContract.


        :param artist: The artist of this ArtistForUserForApiContract.
        :type artist: ArtistForApiContract
        """

        self._artist = artist

    @property
    def id(self):
        """Gets the id of this ArtistForUserForApiContract.


        :return: The id of this ArtistForUserForApiContract.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArtistForUserForApiContract.


        :param id: The id of this ArtistForUserForApiContract.
        :type id: int
        """

        self._id = id
