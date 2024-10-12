# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ModelProperty(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, section: str=None, value: str=None):
        """ModelProperty - a model defined in OpenAPI

        :param key: The key of this ModelProperty.
        :param section: The section of this ModelProperty.
        :param value: The value of this ModelProperty.
        """
        self.openapi_types = {
            'key': str,
            'section': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'section': 'section',
            'value': 'value'
        }

        self._key = key
        self._section = section
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelProperty':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _property of this ModelProperty.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this ModelProperty.

        <strong>chunkSize</strong> defines the duration of the time-based audio and video chunks that Wowza Streaming Cloud delivers to the target. <strong>playSSL</strong> determines whether Wowza Streaming Cloud sends the stream from the target to the player by using SSL (HTTPS). <strong>relativePlaylists</strong> allows the viewer to watch the stream over HTTP and HTTPS, whichever protocol their browser calls. <strong>sendSSL</strong> determines whether Wowza Streaming Cloud sends the stream from the transcoder to the target by using SSL (HTTPS).

        :return: The key of this ModelProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ModelProperty.

        <strong>chunkSize</strong> defines the duration of the time-based audio and video chunks that Wowza Streaming Cloud delivers to the target. <strong>playSSL</strong> determines whether Wowza Streaming Cloud sends the stream from the target to the player by using SSL (HTTPS). <strong>relativePlaylists</strong> allows the viewer to watch the stream over HTTP and HTTPS, whichever protocol their browser calls. <strong>sendSSL</strong> determines whether Wowza Streaming Cloud sends the stream from the transcoder to the target by using SSL (HTTPS).

        :param key: The key of this ModelProperty.
        :type key: str
        """
        allowed_values = ["chunkSize", "playSSL", "relativePlaylists", "sendSSL"]  # noqa: E501
        if key not in allowed_values:
            raise ValueError(
                "Invalid value for `key` ({0}), must be one of {1}"
                .format(key, allowed_values)
            )

        self._key = key

    @property
    def section(self):
        """Gets the section of this ModelProperty.

        The section of the stream target configuration table that contains the property. For <strong>chunkSize</strong> and <strong>sendSSL</strong>, use <strong>hls</strong>. For <strong>playSSL</strong> and <strong>relativePlaylists</strong>, use <strong>playlist</strong>.

        :return: The section of this ModelProperty.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this ModelProperty.

        The section of the stream target configuration table that contains the property. For <strong>chunkSize</strong> and <strong>sendSSL</strong>, use <strong>hls</strong>. For <strong>playSSL</strong> and <strong>relativePlaylists</strong>, use <strong>playlist</strong>.

        :param section: The section of this ModelProperty.
        :type section: str
        """
        allowed_values = ["hls", "playlist"]  # noqa: E501
        if section not in allowed_values:
            raise ValueError(
                "Invalid value for `section` ({0}), must be one of {1}"
                .format(section, allowed_values)
            )

        self._section = section

    @property
    def value(self):
        """Gets the value of this ModelProperty.

        For <strong>chunkSize</strong> use <strong>2</strong>, <strong>4</strong>, <strong>6</strong>, <strong>8</strong>, or <strong>10</strong>. For <strong>playSSL</strong>, <strong>relativePlaylists</strong>, and <strong>sendSSL</strong> use <strong>true</strong> or <strong>false</strong>.

        :return: The value of this ModelProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelProperty.

        For <strong>chunkSize</strong> use <strong>2</strong>, <strong>4</strong>, <strong>6</strong>, <strong>8</strong>, or <strong>10</strong>. For <strong>playSSL</strong>, <strong>relativePlaylists</strong>, and <strong>sendSSL</strong> use <strong>true</strong> or <strong>false</strong>.

        :param value: The value of this ModelProperty.
        :type value: str
        """
        allowed_values = ["2", "4", "6", "8", "10", "true", "false"]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"
                .format(value, allowed_values)
            )

        self._value = value
