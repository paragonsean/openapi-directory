# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Segment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, channels: int=None, created_date: datetime=None, episode_id: int=None, file_name: str=None, file_size: int=None, id: int=None, in_cue: str=None, last_modified_date: datetime=None, length: int=None, original_file_name: str=None, out_cue: str=None, segment_number: int=None):
        """Segment - a model defined in OpenAPI

        :param channels: The channels of this Segment.
        :param created_date: The created_date of this Segment.
        :param episode_id: The episode_id of this Segment.
        :param file_name: The file_name of this Segment.
        :param file_size: The file_size of this Segment.
        :param id: The id of this Segment.
        :param in_cue: The in_cue of this Segment.
        :param last_modified_date: The last_modified_date of this Segment.
        :param length: The length of this Segment.
        :param original_file_name: The original_file_name of this Segment.
        :param out_cue: The out_cue of this Segment.
        :param segment_number: The segment_number of this Segment.
        """
        self.openapi_types = {
            'channels': int,
            'created_date': datetime,
            'episode_id': int,
            'file_name': str,
            'file_size': int,
            'id': int,
            'in_cue': str,
            'last_modified_date': datetime,
            'length': int,
            'original_file_name': str,
            'out_cue': str,
            'segment_number': int
        }

        self.attribute_map = {
            'channels': 'channels',
            'created_date': 'createdDate',
            'episode_id': 'episodeId',
            'file_name': 'fileName',
            'file_size': 'fileSize',
            'id': 'id',
            'in_cue': 'inCue',
            'last_modified_date': 'lastModifiedDate',
            'length': 'length',
            'original_file_name': 'originalFileName',
            'out_cue': 'outCue',
            'segment_number': 'segmentNumber'
        }

        self._channels = channels
        self._created_date = created_date
        self._episode_id = episode_id
        self._file_name = file_name
        self._file_size = file_size
        self._id = id
        self._in_cue = in_cue
        self._last_modified_date = last_modified_date
        self._length = length
        self._original_file_name = original_file_name
        self._out_cue = out_cue
        self._segment_number = segment_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Segment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Segment of this Segment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channels(self):
        """Gets the channels of this Segment.

        The number of audio channels in the segment. Generated at creation.

        :return: The channels of this Segment.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this Segment.

        The number of audio channels in the segment. Generated at creation.

        :param channels: The channels of this Segment.
        :type channels: int
        """

        self._channels = channels

    @property
    def created_date(self):
        """Gets the created_date of this Segment.

        The date the segment was created. Generated at creation.

        :return: The created_date of this Segment.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Segment.

        The date the segment was created. Generated at creation.

        :param created_date: The created_date of this Segment.
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def episode_id(self):
        """Gets the episode_id of this Segment.

        The ID of the episode that owns the segment.

        :return: The episode_id of this Segment.
        :rtype: int
        """
        return self._episode_id

    @episode_id.setter
    def episode_id(self, episode_id):
        """Sets the episode_id of this Segment.

        The ID of the episode that owns the segment.

        :param episode_id: The episode_id of this Segment.
        :type episode_id: int
        """
        if episode_id is None:
            raise ValueError("Invalid value for `episode_id`, must not be `None`")
        if episode_id is not None and episode_id < 0:
            raise ValueError("Invalid value for `episode_id`, must be a value greater than or equal to `0`")

        self._episode_id = episode_id

    @property
    def file_name(self):
        """Gets the file_name of this Segment.

        The name of the audio content file. Generated at creation.

        :return: The file_name of this Segment.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Segment.

        The name of the audio content file. Generated at creation.

        :param file_name: The file_name of this Segment.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this Segment.

        The size of the audio content file in bytes. Generated at creation.

        :return: The file_size of this Segment.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this Segment.

        The size of the audio content file in bytes. Generated at creation.

        :param file_size: The file_size of this Segment.
        :type file_size: int
        """

        self._file_size = file_size

    @property
    def id(self):
        """Gets the id of this Segment.

        The unique ID of the segment. Generated at creation.

        :return: The id of this Segment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Segment.

        The unique ID of the segment. Generated at creation.

        :param id: The id of this Segment.
        :type id: int
        """
        if id is not None and id < 0:
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")

        self._id = id

    @property
    def in_cue(self):
        """Gets the in_cue of this Segment.

        The in-cue copy that signals the start of the segment to a board operator.

        :return: The in_cue of this Segment.
        :rtype: str
        """
        return self._in_cue

    @in_cue.setter
    def in_cue(self, in_cue):
        """Sets the in_cue of this Segment.

        The in-cue copy that signals the start of the segment to a board operator.

        :param in_cue: The in_cue of this Segment.
        :type in_cue: str
        """

        self._in_cue = in_cue

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Segment.

        The date the segment was last modified/updated. Automatically updated on any write operation.

        :return: The last_modified_date of this Segment.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Segment.

        The date the segment was last modified/updated. Automatically updated on any write operation.

        :param last_modified_date: The last_modified_date of this Segment.
        :type last_modified_date: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def length(self):
        """Gets the length of this Segment.

        The length (duration) of the segment in seconds.

        :return: The length of this Segment.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Segment.

        The length (duration) of the segment in seconds.

        :param length: The length of this Segment.
        :type length: int
        """

        self._length = length

    @property
    def original_file_name(self):
        """Gets the original_file_name of this Segment.

        The original name of the audio content file.

        :return: The original_file_name of this Segment.
        :rtype: str
        """
        return self._original_file_name

    @original_file_name.setter
    def original_file_name(self, original_file_name):
        """Sets the original_file_name of this Segment.

        The original name of the audio content file.

        :param original_file_name: The original_file_name of this Segment.
        :type original_file_name: str
        """

        self._original_file_name = original_file_name

    @property
    def out_cue(self):
        """Gets the out_cue of this Segment.

        The out-cue copy that signals the end of the segment to a board operator.

        :return: The out_cue of this Segment.
        :rtype: str
        """
        return self._out_cue

    @out_cue.setter
    def out_cue(self, out_cue):
        """Sets the out_cue of this Segment.

        The out-cue copy that signals the end of the segment to a board operator.

        :param out_cue: The out_cue of this Segment.
        :type out_cue: str
        """

        self._out_cue = out_cue

    @property
    def segment_number(self):
        """Gets the segment_number of this Segment.

        The number of the segment in the episode, starting with 1.

        :return: The segment_number of this Segment.
        :rtype: int
        """
        return self._segment_number

    @segment_number.setter
    def segment_number(self, segment_number):
        """Sets the segment_number of this Segment.

        The number of the segment in the episode, starting with 1.

        :param segment_number: The segment_number of this Segment.
        :type segment_number: int
        """
        if segment_number is None:
            raise ValueError("Invalid value for `segment_number`, must not be `None`")
        if segment_number is not None and segment_number < 1:
            raise ValueError("Invalid value for `segment_number`, must be a value greater than or equal to `1`")

        self._segment_number = segment_number
