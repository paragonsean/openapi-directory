# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ThemeThemes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_element_blob_url: str=None, changed_base_element_blob_url: str=None, id: str=None, name: str=None, package_uri: str=None, slide_id: str=None):
        """ThemeThemes - a model defined in OpenAPI

        :param base_element_blob_url: The base_element_blob_url of this ThemeThemes.
        :param changed_base_element_blob_url: The changed_base_element_blob_url of this ThemeThemes.
        :param id: The id of this ThemeThemes.
        :param name: The name of this ThemeThemes.
        :param package_uri: The package_uri of this ThemeThemes.
        :param slide_id: The slide_id of this ThemeThemes.
        """
        self.openapi_types = {
            'base_element_blob_url': str,
            'changed_base_element_blob_url': str,
            'id': str,
            'name': str,
            'package_uri': str,
            'slide_id': str
        }

        self.attribute_map = {
            'base_element_blob_url': 'baseElementBlobUrl',
            'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
            'id': 'id',
            'name': 'name',
            'package_uri': 'packageUri',
            'slide_id': 'slideId'
        }

        self._base_element_blob_url = base_element_blob_url
        self._changed_base_element_blob_url = changed_base_element_blob_url
        self._id = id
        self._name = name
        self._package_uri = package_uri
        self._slide_id = slide_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ThemeThemes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Theme.Themes of this ThemeThemes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this ThemeThemes.


        :return: The base_element_blob_url of this ThemeThemes.
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this ThemeThemes.


        :param base_element_blob_url: The base_element_blob_url of this ThemeThemes.
        :type base_element_blob_url: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this ThemeThemes.


        :return: The changed_base_element_blob_url of this ThemeThemes.
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this ThemeThemes.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this ThemeThemes.
        :type changed_base_element_blob_url: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def id(self):
        """Gets the id of this ThemeThemes.


        :return: The id of this ThemeThemes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThemeThemes.


        :param id: The id of this ThemeThemes.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ThemeThemes.


        :return: The name of this ThemeThemes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThemeThemes.


        :param name: The name of this ThemeThemes.
        :type name: str
        """

        self._name = name

    @property
    def package_uri(self):
        """Gets the package_uri of this ThemeThemes.


        :return: The package_uri of this ThemeThemes.
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this ThemeThemes.


        :param package_uri: The package_uri of this ThemeThemes.
        :type package_uri: str
        """

        self._package_uri = package_uri

    @property
    def slide_id(self):
        """Gets the slide_id of this ThemeThemes.


        :return: The slide_id of this ThemeThemes.
        :rtype: str
        """
        return self._slide_id

    @slide_id.setter
    def slide_id(self, slide_id):
        """Sets the slide_id of this ThemeThemes.


        :param slide_id: The slide_id of this ThemeThemes.
        :type slide_id: str
        """

        self._slide_id = slide_id
