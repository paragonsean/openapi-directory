# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.releases_update_details200_response_destinations_inner import ReleasesUpdateDetails200ResponseDestinationsInner
from openapi_server import util


class ReleasesUpdateDetails200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, destinations: List[ReleasesUpdateDetails200ResponseDestinationsInner]=None, enabled: bool=None, mandatory_update: bool=None, provisioning_status_url: str=None, release_notes: str=None):
        """ReleasesUpdateDetails200Response - a model defined in OpenAPI

        :param destinations: The destinations of this ReleasesUpdateDetails200Response.
        :param enabled: The enabled of this ReleasesUpdateDetails200Response.
        :param mandatory_update: The mandatory_update of this ReleasesUpdateDetails200Response.
        :param provisioning_status_url: The provisioning_status_url of this ReleasesUpdateDetails200Response.
        :param release_notes: The release_notes of this ReleasesUpdateDetails200Response.
        """
        self.openapi_types = {
            'destinations': List[ReleasesUpdateDetails200ResponseDestinationsInner],
            'enabled': bool,
            'mandatory_update': bool,
            'provisioning_status_url': str,
            'release_notes': str
        }

        self.attribute_map = {
            'destinations': 'destinations',
            'enabled': 'enabled',
            'mandatory_update': 'mandatory_update',
            'provisioning_status_url': 'provisioning_status_url',
            'release_notes': 'release_notes'
        }

        self._destinations = destinations
        self._enabled = enabled
        self._mandatory_update = mandatory_update
        self._provisioning_status_url = provisioning_status_url
        self._release_notes = release_notes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleasesUpdateDetails200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The releases_updateDetails_200_response of this ReleasesUpdateDetails200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destinations(self):
        """Gets the destinations of this ReleasesUpdateDetails200Response.


        :return: The destinations of this ReleasesUpdateDetails200Response.
        :rtype: List[ReleasesUpdateDetails200ResponseDestinationsInner]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ReleasesUpdateDetails200Response.


        :param destinations: The destinations of this ReleasesUpdateDetails200Response.
        :type destinations: List[ReleasesUpdateDetails200ResponseDestinationsInner]
        """

        self._destinations = destinations

    @property
    def enabled(self):
        """Gets the enabled of this ReleasesUpdateDetails200Response.


        :return: The enabled of this ReleasesUpdateDetails200Response.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ReleasesUpdateDetails200Response.


        :param enabled: The enabled of this ReleasesUpdateDetails200Response.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this ReleasesUpdateDetails200Response.


        :return: The mandatory_update of this ReleasesUpdateDetails200Response.
        :rtype: bool
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this ReleasesUpdateDetails200Response.


        :param mandatory_update: The mandatory_update of this ReleasesUpdateDetails200Response.
        :type mandatory_update: bool
        """

        self._mandatory_update = mandatory_update

    @property
    def provisioning_status_url(self):
        """Gets the provisioning_status_url of this ReleasesUpdateDetails200Response.


        :return: The provisioning_status_url of this ReleasesUpdateDetails200Response.
        :rtype: str
        """
        return self._provisioning_status_url

    @provisioning_status_url.setter
    def provisioning_status_url(self, provisioning_status_url):
        """Sets the provisioning_status_url of this ReleasesUpdateDetails200Response.


        :param provisioning_status_url: The provisioning_status_url of this ReleasesUpdateDetails200Response.
        :type provisioning_status_url: str
        """

        self._provisioning_status_url = provisioning_status_url

    @property
    def release_notes(self):
        """Gets the release_notes of this ReleasesUpdateDetails200Response.


        :return: The release_notes of this ReleasesUpdateDetails200Response.
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this ReleasesUpdateDetails200Response.


        :param release_notes: The release_notes of this ReleasesUpdateDetails200Response.
        :type release_notes: str
        """

        self._release_notes = release_notes
