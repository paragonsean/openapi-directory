# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.ancestor_summary import AncestorSummary
from openapi_server.models.available_versions import AvailableVersions
from openapi_server.models.image import Image
from openapi_server.models.network_summary import NetworkSummary
from openapi_server.models.programme_titles import ProgrammeTitles
from openapi_server import util


class ClipSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ancestors: List[AncestorSummary]=None, available_versions: List[AvailableVersions]=None, images: List[Image]=None, media_type: str=None, network_summary: NetworkSummary=None, pid: str=None, release_date: str=None, short_synopsis: str=None, titles: ProgrammeTitles=None, type: str=None):
        """ClipSummary - a model defined in OpenAPI

        :param ancestors: The ancestors of this ClipSummary.
        :param available_versions: The available_versions of this ClipSummary.
        :param images: The images of this ClipSummary.
        :param media_type: The media_type of this ClipSummary.
        :param network_summary: The network_summary of this ClipSummary.
        :param pid: The pid of this ClipSummary.
        :param release_date: The release_date of this ClipSummary.
        :param short_synopsis: The short_synopsis of this ClipSummary.
        :param titles: The titles of this ClipSummary.
        :param type: The type of this ClipSummary.
        """
        self.openapi_types = {
            'ancestors': List[AncestorSummary],
            'available_versions': List[AvailableVersions],
            'images': List[Image],
            'media_type': str,
            'network_summary': NetworkSummary,
            'pid': str,
            'release_date': str,
            'short_synopsis': str,
            'titles': ProgrammeTitles,
            'type': str
        }

        self.attribute_map = {
            'ancestors': 'ancestors',
            'available_versions': 'available_versions',
            'images': 'images',
            'media_type': 'media_type',
            'network_summary': 'network_summary',
            'pid': 'pid',
            'release_date': 'release_date',
            'short_synopsis': 'short_synopsis',
            'titles': 'titles',
            'type': 'type'
        }

        self._ancestors = ancestors
        self._available_versions = available_versions
        self._images = images
        self._media_type = media_type
        self._network_summary = network_summary
        self._pid = pid
        self._release_date = release_date
        self._short_synopsis = short_synopsis
        self._titles = titles
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ClipSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ClipSummary of this ClipSummary.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ancestors(self):
        """Gets the ancestors of this ClipSummary.


        :return: The ancestors of this ClipSummary.
        :rtype: List[AncestorSummary]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """Sets the ancestors of this ClipSummary.


        :param ancestors: The ancestors of this ClipSummary.
        :type ancestors: List[AncestorSummary]
        """
        if ancestors is None:
            raise ValueError("Invalid value for `ancestors`, must not be `None`")

        self._ancestors = ancestors

    @property
    def available_versions(self):
        """Gets the available_versions of this ClipSummary.


        :return: The available_versions of this ClipSummary.
        :rtype: List[AvailableVersions]
        """
        return self._available_versions

    @available_versions.setter
    def available_versions(self, available_versions):
        """Sets the available_versions of this ClipSummary.


        :param available_versions: The available_versions of this ClipSummary.
        :type available_versions: List[AvailableVersions]
        """
        if available_versions is None:
            raise ValueError("Invalid value for `available_versions`, must not be `None`")

        self._available_versions = available_versions

    @property
    def images(self):
        """Gets the images of this ClipSummary.


        :return: The images of this ClipSummary.
        :rtype: List[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ClipSummary.


        :param images: The images of this ClipSummary.
        :type images: List[Image]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")

        self._images = images

    @property
    def media_type(self):
        """Gets the media_type of this ClipSummary.


        :return: The media_type of this ClipSummary.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ClipSummary.


        :param media_type: The media_type of this ClipSummary.
        :type media_type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")

        self._media_type = media_type

    @property
    def network_summary(self):
        """Gets the network_summary of this ClipSummary.


        :return: The network_summary of this ClipSummary.
        :rtype: NetworkSummary
        """
        return self._network_summary

    @network_summary.setter
    def network_summary(self, network_summary):
        """Sets the network_summary of this ClipSummary.


        :param network_summary: The network_summary of this ClipSummary.
        :type network_summary: NetworkSummary
        """
        if network_summary is None:
            raise ValueError("Invalid value for `network_summary`, must not be `None`")

        self._network_summary = network_summary

    @property
    def pid(self):
        """Gets the pid of this ClipSummary.


        :return: The pid of this ClipSummary.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this ClipSummary.


        :param pid: The pid of this ClipSummary.
        :type pid: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")

        self._pid = pid

    @property
    def release_date(self):
        """Gets the release_date of this ClipSummary.


        :return: The release_date of this ClipSummary.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ClipSummary.


        :param release_date: The release_date of this ClipSummary.
        :type release_date: str
        """
        if release_date is None:
            raise ValueError("Invalid value for `release_date`, must not be `None`")

        self._release_date = release_date

    @property
    def short_synopsis(self):
        """Gets the short_synopsis of this ClipSummary.


        :return: The short_synopsis of this ClipSummary.
        :rtype: str
        """
        return self._short_synopsis

    @short_synopsis.setter
    def short_synopsis(self, short_synopsis):
        """Sets the short_synopsis of this ClipSummary.


        :param short_synopsis: The short_synopsis of this ClipSummary.
        :type short_synopsis: str
        """
        if short_synopsis is None:
            raise ValueError("Invalid value for `short_synopsis`, must not be `None`")

        self._short_synopsis = short_synopsis

    @property
    def titles(self):
        """Gets the titles of this ClipSummary.


        :return: The titles of this ClipSummary.
        :rtype: ProgrammeTitles
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this ClipSummary.


        :param titles: The titles of this ClipSummary.
        :type titles: ProgrammeTitles
        """
        if titles is None:
            raise ValueError("Invalid value for `titles`, must not be `None`")

        self._titles = titles

    @property
    def type(self):
        """Gets the type of this ClipSummary.


        :return: The type of this ClipSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClipSummary.


        :param type: The type of this ClipSummary.
        :type type: str
        """
        allowed_values = ["clip_summary"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
