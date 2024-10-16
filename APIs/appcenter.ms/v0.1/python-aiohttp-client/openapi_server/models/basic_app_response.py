# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.apps_list200_response_inner_all_of_owner import AppsList200ResponseInnerAllOfOwner
from openapi_server import util


class BasicAppResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, display_name: str=None, icon_source: str=None, icon_url: str=None, id: str=None, name: str=None, os: str=None, owner: AppsList200ResponseInnerAllOfOwner=None, release_type: str=None):
        """BasicAppResponse - a model defined in OpenAPI

        :param description: The description of this BasicAppResponse.
        :param display_name: The display_name of this BasicAppResponse.
        :param icon_source: The icon_source of this BasicAppResponse.
        :param icon_url: The icon_url of this BasicAppResponse.
        :param id: The id of this BasicAppResponse.
        :param name: The name of this BasicAppResponse.
        :param os: The os of this BasicAppResponse.
        :param owner: The owner of this BasicAppResponse.
        :param release_type: The release_type of this BasicAppResponse.
        """
        self.openapi_types = {
            'description': str,
            'display_name': str,
            'icon_source': str,
            'icon_url': str,
            'id': str,
            'name': str,
            'os': str,
            'owner': AppsList200ResponseInnerAllOfOwner,
            'release_type': str
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'display_name',
            'icon_source': 'icon_source',
            'icon_url': 'icon_url',
            'id': 'id',
            'name': 'name',
            'os': 'os',
            'owner': 'owner',
            'release_type': 'release_type'
        }

        self._description = description
        self._display_name = display_name
        self._icon_source = icon_source
        self._icon_url = icon_url
        self._id = id
        self._name = name
        self._os = os
        self._owner = owner
        self._release_type = release_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BasicAppResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BasicAppResponse of this BasicAppResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this BasicAppResponse.

        The description of the app

        :return: The description of this BasicAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BasicAppResponse.

        The description of the app

        :param description: The description of this BasicAppResponse.
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this BasicAppResponse.

        The display name of the app

        :return: The display_name of this BasicAppResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BasicAppResponse.

        The display name of the app

        :param display_name: The display_name of this BasicAppResponse.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def icon_source(self):
        """Gets the icon_source of this BasicAppResponse.

        The string representation of the source of the app's icon

        :return: The icon_source of this BasicAppResponse.
        :rtype: str
        """
        return self._icon_source

    @icon_source.setter
    def icon_source(self, icon_source):
        """Sets the icon_source of this BasicAppResponse.

        The string representation of the source of the app's icon

        :param icon_source: The icon_source of this BasicAppResponse.
        :type icon_source: str
        """

        self._icon_source = icon_source

    @property
    def icon_url(self):
        """Gets the icon_url of this BasicAppResponse.

        The string representation of the URL pointing to the app's icon

        :return: The icon_url of this BasicAppResponse.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this BasicAppResponse.

        The string representation of the URL pointing to the app's icon

        :param icon_url: The icon_url of this BasicAppResponse.
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def id(self):
        """Gets the id of this BasicAppResponse.

        The unique ID (UUID) of the app

        :return: The id of this BasicAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicAppResponse.

        The unique ID (UUID) of the app

        :param id: The id of this BasicAppResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this BasicAppResponse.

        The name of the app used in URLs

        :return: The name of this BasicAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicAppResponse.

        The name of the app used in URLs

        :param name: The name of this BasicAppResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def os(self):
        """Gets the os of this BasicAppResponse.

        The OS the app will be running on

        :return: The os of this BasicAppResponse.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this BasicAppResponse.

        The OS the app will be running on

        :param os: The os of this BasicAppResponse.
        :type os: str
        """
        allowed_values = ["Android", "iOS", "macOS", "Tizen", "tvOS", "Windows", "Linux", "Custom"]  # noqa: E501
        if os not in allowed_values:
            raise ValueError(
                "Invalid value for `os` ({0}), must be one of {1}"
                .format(os, allowed_values)
            )

        self._os = os

    @property
    def owner(self):
        """Gets the owner of this BasicAppResponse.


        :return: The owner of this BasicAppResponse.
        :rtype: AppsList200ResponseInnerAllOfOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BasicAppResponse.


        :param owner: The owner of this BasicAppResponse.
        :type owner: AppsList200ResponseInnerAllOfOwner
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def release_type(self):
        """Gets the release_type of this BasicAppResponse.

        A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase

        :return: The release_type of this BasicAppResponse.
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """Sets the release_type of this BasicAppResponse.

        A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase

        :param release_type: The release_type of this BasicAppResponse.
        :type release_type: str
        """

        self._release_type = release_type
