# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OutputStreamTarget1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, stream_target_id: str=None, use_stream_target_backup_url: bool=None):
        """OutputStreamTarget1 - a model defined in OpenAPI

        :param stream_target_id: The stream_target_id of this OutputStreamTarget1.
        :param use_stream_target_backup_url: The use_stream_target_backup_url of this OutputStreamTarget1.
        """
        self.openapi_types = {
            'stream_target_id': str,
            'use_stream_target_backup_url': bool
        }

        self.attribute_map = {
            'stream_target_id': 'stream_target_id',
            'use_stream_target_backup_url': 'use_stream_target_backup_url'
        }

        self._stream_target_id = stream_target_id
        self._use_stream_target_backup_url = use_stream_target_backup_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputStreamTarget1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The output_stream_target_1 of this OutputStreamTarget1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def stream_target_id(self):
        """Gets the stream_target_id of this OutputStreamTarget1.

        The unique alphanumeric string that identifies the stream target.

        :return: The stream_target_id of this OutputStreamTarget1.
        :rtype: str
        """
        return self._stream_target_id

    @stream_target_id.setter
    def stream_target_id(self, stream_target_id):
        """Sets the stream_target_id of this OutputStreamTarget1.

        The unique alphanumeric string that identifies the stream target.

        :param stream_target_id: The stream_target_id of this OutputStreamTarget1.
        :type stream_target_id: str
        """
        if stream_target_id is None:
            raise ValueError("Invalid value for `stream_target_id`, must not be `None`")

        self._stream_target_id = stream_target_id

    @property
    def use_stream_target_backup_url(self):
        """Gets the use_stream_target_backup_url of this OutputStreamTarget1.

        Use the target's backup URL. Not available for targets whose <em>provider</em> is <strong>akamai_cupertino</strong>. The default is <strong>false</strong>.

        :return: The use_stream_target_backup_url of this OutputStreamTarget1.
        :rtype: bool
        """
        return self._use_stream_target_backup_url

    @use_stream_target_backup_url.setter
    def use_stream_target_backup_url(self, use_stream_target_backup_url):
        """Sets the use_stream_target_backup_url of this OutputStreamTarget1.

        Use the target's backup URL. Not available for targets whose <em>provider</em> is <strong>akamai_cupertino</strong>. The default is <strong>false</strong>.

        :param use_stream_target_backup_url: The use_stream_target_backup_url of this OutputStreamTarget1.
        :type use_stream_target_backup_url: bool
        """

        self._use_stream_target_backup_url = use_stream_target_backup_url
