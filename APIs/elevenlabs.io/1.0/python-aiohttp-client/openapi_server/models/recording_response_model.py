# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RecordingResponseModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mime_type: str=None, recording_id: str=None, size_bytes: int=None, transcription: str=None, upload_date_unix: int=None):
        """RecordingResponseModel - a model defined in OpenAPI

        :param mime_type: The mime_type of this RecordingResponseModel.
        :param recording_id: The recording_id of this RecordingResponseModel.
        :param size_bytes: The size_bytes of this RecordingResponseModel.
        :param transcription: The transcription of this RecordingResponseModel.
        :param upload_date_unix: The upload_date_unix of this RecordingResponseModel.
        """
        self.openapi_types = {
            'mime_type': str,
            'recording_id': str,
            'size_bytes': int,
            'transcription': str,
            'upload_date_unix': int
        }

        self.attribute_map = {
            'mime_type': 'mime_type',
            'recording_id': 'recording_id',
            'size_bytes': 'size_bytes',
            'transcription': 'transcription',
            'upload_date_unix': 'upload_date_unix'
        }

        self._mime_type = mime_type
        self._recording_id = recording_id
        self._size_bytes = size_bytes
        self._transcription = transcription
        self._upload_date_unix = upload_date_unix

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RecordingResponseModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RecordingResponseModel of this RecordingResponseModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mime_type(self):
        """Gets the mime_type of this RecordingResponseModel.


        :return: The mime_type of this RecordingResponseModel.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this RecordingResponseModel.


        :param mime_type: The mime_type of this RecordingResponseModel.
        :type mime_type: str
        """
        if mime_type is None:
            raise ValueError("Invalid value for `mime_type`, must not be `None`")

        self._mime_type = mime_type

    @property
    def recording_id(self):
        """Gets the recording_id of this RecordingResponseModel.


        :return: The recording_id of this RecordingResponseModel.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id):
        """Sets the recording_id of this RecordingResponseModel.


        :param recording_id: The recording_id of this RecordingResponseModel.
        :type recording_id: str
        """
        if recording_id is None:
            raise ValueError("Invalid value for `recording_id`, must not be `None`")

        self._recording_id = recording_id

    @property
    def size_bytes(self):
        """Gets the size_bytes of this RecordingResponseModel.


        :return: The size_bytes of this RecordingResponseModel.
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this RecordingResponseModel.


        :param size_bytes: The size_bytes of this RecordingResponseModel.
        :type size_bytes: int
        """
        if size_bytes is None:
            raise ValueError("Invalid value for `size_bytes`, must not be `None`")

        self._size_bytes = size_bytes

    @property
    def transcription(self):
        """Gets the transcription of this RecordingResponseModel.


        :return: The transcription of this RecordingResponseModel.
        :rtype: str
        """
        return self._transcription

    @transcription.setter
    def transcription(self, transcription):
        """Sets the transcription of this RecordingResponseModel.


        :param transcription: The transcription of this RecordingResponseModel.
        :type transcription: str
        """
        if transcription is None:
            raise ValueError("Invalid value for `transcription`, must not be `None`")

        self._transcription = transcription

    @property
    def upload_date_unix(self):
        """Gets the upload_date_unix of this RecordingResponseModel.


        :return: The upload_date_unix of this RecordingResponseModel.
        :rtype: int
        """
        return self._upload_date_unix

    @upload_date_unix.setter
    def upload_date_unix(self, upload_date_unix):
        """Sets the upload_date_unix of this RecordingResponseModel.


        :param upload_date_unix: The upload_date_unix of this RecordingResponseModel.
        :type upload_date_unix: int
        """
        if upload_date_unix is None:
            raise ValueError("Invalid value for `upload_date_unix`, must not be `None`")

        self._upload_date_unix = upload_date_unix
