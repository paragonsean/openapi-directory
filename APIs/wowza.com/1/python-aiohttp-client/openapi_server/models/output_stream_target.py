# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.stream_target import StreamTarget
from openapi_server import util


class OutputStreamTarget(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: datetime=None, id: str=None, output_id: str=None, stream_target: StreamTarget=None, stream_target_id: str=None, updated_at: datetime=None, use_stream_target_backup_url: bool=None):
        """OutputStreamTarget - a model defined in OpenAPI

        :param created_at: The created_at of this OutputStreamTarget.
        :param id: The id of this OutputStreamTarget.
        :param output_id: The output_id of this OutputStreamTarget.
        :param stream_target: The stream_target of this OutputStreamTarget.
        :param stream_target_id: The stream_target_id of this OutputStreamTarget.
        :param updated_at: The updated_at of this OutputStreamTarget.
        :param use_stream_target_backup_url: The use_stream_target_backup_url of this OutputStreamTarget.
        """
        self.openapi_types = {
            'created_at': datetime,
            'id': str,
            'output_id': str,
            'stream_target': StreamTarget,
            'stream_target_id': str,
            'updated_at': datetime,
            'use_stream_target_backup_url': bool
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'id': 'id',
            'output_id': 'output_id',
            'stream_target': 'stream_target',
            'stream_target_id': 'stream_target_id',
            'updated_at': 'updated_at',
            'use_stream_target_backup_url': 'use_stream_target_backup_url'
        }

        self._created_at = created_at
        self._id = id
        self._output_id = output_id
        self._stream_target = stream_target
        self._stream_target_id = stream_target_id
        self._updated_at = updated_at
        self._use_stream_target_backup_url = use_stream_target_backup_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputStreamTarget':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The output_stream_target of this OutputStreamTarget.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this OutputStreamTarget.

        The date and time that the output stream target was created.

        :return: The created_at of this OutputStreamTarget.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OutputStreamTarget.

        The date and time that the output stream target was created.

        :param created_at: The created_at of this OutputStreamTarget.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the output stream target.

        :return: The id of this OutputStreamTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the output stream target.

        :param id: The id of this OutputStreamTarget.
        :type id: str
        """

        self._id = id

    @property
    def output_id(self):
        """Gets the output_id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the output rendition.

        :return: The output_id of this OutputStreamTarget.
        :rtype: str
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        """Sets the output_id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the output rendition.

        :param output_id: The output_id of this OutputStreamTarget.
        :type output_id: str
        """

        self._output_id = output_id

    @property
    def stream_target(self):
        """Gets the stream_target of this OutputStreamTarget.


        :return: The stream_target of this OutputStreamTarget.
        :rtype: StreamTarget
        """
        return self._stream_target

    @stream_target.setter
    def stream_target(self, stream_target):
        """Sets the stream_target of this OutputStreamTarget.


        :param stream_target: The stream_target of this OutputStreamTarget.
        :type stream_target: StreamTarget
        """

        self._stream_target = stream_target

    @property
    def stream_target_id(self):
        """Gets the stream_target_id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the stream target.

        :return: The stream_target_id of this OutputStreamTarget.
        :rtype: str
        """
        return self._stream_target_id

    @stream_target_id.setter
    def stream_target_id(self, stream_target_id):
        """Sets the stream_target_id of this OutputStreamTarget.

        The unique alphanumeric string that identifies the stream target.

        :param stream_target_id: The stream_target_id of this OutputStreamTarget.
        :type stream_target_id: str
        """

        self._stream_target_id = stream_target_id

    @property
    def updated_at(self):
        """Gets the updated_at of this OutputStreamTarget.

        The date and time that the output stream target was updated.

        :return: The updated_at of this OutputStreamTarget.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OutputStreamTarget.

        The date and time that the output stream target was updated.

        :param updated_at: The updated_at of this OutputStreamTarget.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def use_stream_target_backup_url(self):
        """Gets the use_stream_target_backup_url of this OutputStreamTarget.

        Specifies whether to use the stream target's primary or backup URL.

        :return: The use_stream_target_backup_url of this OutputStreamTarget.
        :rtype: bool
        """
        return self._use_stream_target_backup_url

    @use_stream_target_backup_url.setter
    def use_stream_target_backup_url(self, use_stream_target_backup_url):
        """Sets the use_stream_target_backup_url of this OutputStreamTarget.

        Specifies whether to use the stream target's primary or backup URL.

        :param use_stream_target_backup_url: The use_stream_target_backup_url of this OutputStreamTarget.
        :type use_stream_target_backup_url: bool
        """

        self._use_stream_target_backup_url = use_stream_target_backup_url
