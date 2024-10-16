# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.crash_group_places_places_inner import CrashGroupPlacesPlacesInner
from openapi_server import util


class CrashGroupPlaces(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, crash_count: int=None, places: List[CrashGroupPlacesPlacesInner]=None):
        """CrashGroupPlaces - a model defined in OpenAPI

        :param crash_count: The crash_count of this CrashGroupPlaces.
        :param places: The places of this CrashGroupPlaces.
        """
        self.openapi_types = {
            'crash_count': int,
            'places': List[CrashGroupPlacesPlacesInner]
        }

        self.attribute_map = {
            'crash_count': 'crash_count',
            'places': 'places'
        }

        self._crash_count = crash_count
        self._places = places

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashGroupPlaces':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CrashGroupPlaces of this CrashGroupPlaces.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def crash_count(self):
        """Gets the crash_count of this CrashGroupPlaces.


        :return: The crash_count of this CrashGroupPlaces.
        :rtype: int
        """
        return self._crash_count

    @crash_count.setter
    def crash_count(self, crash_count):
        """Sets the crash_count of this CrashGroupPlaces.


        :param crash_count: The crash_count of this CrashGroupPlaces.
        :type crash_count: int
        """

        self._crash_count = crash_count

    @property
    def places(self):
        """Gets the places of this CrashGroupPlaces.


        :return: The places of this CrashGroupPlaces.
        :rtype: List[CrashGroupPlacesPlacesInner]
        """
        return self._places

    @places.setter
    def places(self, places):
        """Sets the places of this CrashGroupPlaces.


        :param places: The places of this CrashGroupPlaces.
        :type places: List[CrashGroupPlacesPlacesInner]
        """

        self._places = places
