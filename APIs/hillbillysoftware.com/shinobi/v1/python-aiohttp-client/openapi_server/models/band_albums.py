# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BandAlbums(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, album_art: str=None, album_id: str=None, artist_id: str=None, bibliography: str=None, label: str=None, name: str=None, releaseyear: str=None):
        """BandAlbums - a model defined in OpenAPI

        :param album_art: The album_art of this BandAlbums.
        :param album_id: The album_id of this BandAlbums.
        :param artist_id: The artist_id of this BandAlbums.
        :param bibliography: The bibliography of this BandAlbums.
        :param label: The label of this BandAlbums.
        :param name: The name of this BandAlbums.
        :param releaseyear: The releaseyear of this BandAlbums.
        """
        self.openapi_types = {
            'album_art': str,
            'album_id': str,
            'artist_id': str,
            'bibliography': str,
            'label': str,
            'name': str,
            'releaseyear': str
        }

        self.attribute_map = {
            'album_art': 'AlbumArt',
            'album_id': 'AlbumID',
            'artist_id': 'ArtistID',
            'bibliography': 'Bibliography',
            'label': 'Label',
            'name': 'Name',
            'releaseyear': 'Releaseyear'
        }

        self._album_art = album_art
        self._album_id = album_id
        self._artist_id = artist_id
        self._bibliography = bibliography
        self._label = label
        self._name = name
        self._releaseyear = releaseyear

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BandAlbums':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BandAlbums of this BandAlbums.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def album_art(self):
        """Gets the album_art of this BandAlbums.


        :return: The album_art of this BandAlbums.
        :rtype: str
        """
        return self._album_art

    @album_art.setter
    def album_art(self, album_art):
        """Sets the album_art of this BandAlbums.


        :param album_art: The album_art of this BandAlbums.
        :type album_art: str
        """

        self._album_art = album_art

    @property
    def album_id(self):
        """Gets the album_id of this BandAlbums.


        :return: The album_id of this BandAlbums.
        :rtype: str
        """
        return self._album_id

    @album_id.setter
    def album_id(self, album_id):
        """Sets the album_id of this BandAlbums.


        :param album_id: The album_id of this BandAlbums.
        :type album_id: str
        """

        self._album_id = album_id

    @property
    def artist_id(self):
        """Gets the artist_id of this BandAlbums.


        :return: The artist_id of this BandAlbums.
        :rtype: str
        """
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        """Sets the artist_id of this BandAlbums.


        :param artist_id: The artist_id of this BandAlbums.
        :type artist_id: str
        """

        self._artist_id = artist_id

    @property
    def bibliography(self):
        """Gets the bibliography of this BandAlbums.


        :return: The bibliography of this BandAlbums.
        :rtype: str
        """
        return self._bibliography

    @bibliography.setter
    def bibliography(self, bibliography):
        """Sets the bibliography of this BandAlbums.


        :param bibliography: The bibliography of this BandAlbums.
        :type bibliography: str
        """

        self._bibliography = bibliography

    @property
    def label(self):
        """Gets the label of this BandAlbums.


        :return: The label of this BandAlbums.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BandAlbums.


        :param label: The label of this BandAlbums.
        :type label: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this BandAlbums.


        :return: The name of this BandAlbums.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandAlbums.


        :param name: The name of this BandAlbums.
        :type name: str
        """

        self._name = name

    @property
    def releaseyear(self):
        """Gets the releaseyear of this BandAlbums.


        :return: The releaseyear of this BandAlbums.
        :rtype: str
        """
        return self._releaseyear

    @releaseyear.setter
    def releaseyear(self, releaseyear):
        """Sets the releaseyear of this BandAlbums.


        :param releaseyear: The releaseyear of this BandAlbums.
        :type releaseyear: str
        """

        self._releaseyear = releaseyear
