# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Emoji(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category: str=None, shortcode: str=None, static_url: str=None, url: str=None, visible_in_picker: bool=None):
        """Emoji - a model defined in OpenAPI

        :param category: The category of this Emoji.
        :param shortcode: The shortcode of this Emoji.
        :param static_url: The static_url of this Emoji.
        :param url: The url of this Emoji.
        :param visible_in_picker: The visible_in_picker of this Emoji.
        """
        self.openapi_types = {
            'category': str,
            'shortcode': str,
            'static_url': str,
            'url': str,
            'visible_in_picker': bool
        }

        self.attribute_map = {
            'category': 'category',
            'shortcode': 'shortcode',
            'static_url': 'static_url',
            'url': 'url',
            'visible_in_picker': 'visible_in_picker'
        }

        self._category = category
        self._shortcode = shortcode
        self._static_url = static_url
        self._url = url
        self._visible_in_picker = visible_in_picker

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Emoji':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Emoji of this Emoji.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self):
        """Gets the category of this Emoji.

        Used for sorting custom emoji in the picker.

        :return: The category of this Emoji.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Emoji.

        Used for sorting custom emoji in the picker.

        :param category: The category of this Emoji.
        :type category: str
        """

        self._category = category

    @property
    def shortcode(self):
        """Gets the shortcode of this Emoji.

        The name of the custom emoji.

        :return: The shortcode of this Emoji.
        :rtype: str
        """
        return self._shortcode

    @shortcode.setter
    def shortcode(self, shortcode):
        """Sets the shortcode of this Emoji.

        The name of the custom emoji.

        :param shortcode: The shortcode of this Emoji.
        :type shortcode: str
        """
        if shortcode is None:
            raise ValueError("Invalid value for `shortcode`, must not be `None`")

        self._shortcode = shortcode

    @property
    def static_url(self):
        """Gets the static_url of this Emoji.

        A link to a static copy of the custom emoji. The format is URL.

        :return: The static_url of this Emoji.
        :rtype: str
        """
        return self._static_url

    @static_url.setter
    def static_url(self, static_url):
        """Sets the static_url of this Emoji.

        A link to a static copy of the custom emoji. The format is URL.

        :param static_url: The static_url of this Emoji.
        :type static_url: str
        """
        if static_url is None:
            raise ValueError("Invalid value for `static_url`, must not be `None`")

        self._static_url = static_url

    @property
    def url(self):
        """Gets the url of this Emoji.

        A link to the custom emoji. The format is URL.

        :return: The url of this Emoji.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Emoji.

        A link to the custom emoji. The format is URL.

        :param url: The url of this Emoji.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def visible_in_picker(self):
        """Gets the visible_in_picker of this Emoji.

        Whether this Emoji should be visible in the picker or unlisted.

        :return: The visible_in_picker of this Emoji.
        :rtype: bool
        """
        return self._visible_in_picker

    @visible_in_picker.setter
    def visible_in_picker(self, visible_in_picker):
        """Sets the visible_in_picker of this Emoji.

        Whether this Emoji should be visible in the picker or unlisted.

        :param visible_in_picker: The visible_in_picker of this Emoji.
        :type visible_in_picker: bool
        """
        if visible_in_picker is None:
            raise ValueError("Invalid value for `visible_in_picker`, must not be `None`")

        self._visible_in_picker = visible_in_picker
