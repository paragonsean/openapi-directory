# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.recording_response_model import RecordingResponseModel
from openapi_server import util


class VerificationAttemptResponseModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accepted: bool=None, date_unix: int=None, levenshtein_distance: float=None, recording: RecordingResponseModel=None, similarity: float=None, text: str=None):
        """VerificationAttemptResponseModel - a model defined in OpenAPI

        :param accepted: The accepted of this VerificationAttemptResponseModel.
        :param date_unix: The date_unix of this VerificationAttemptResponseModel.
        :param levenshtein_distance: The levenshtein_distance of this VerificationAttemptResponseModel.
        :param recording: The recording of this VerificationAttemptResponseModel.
        :param similarity: The similarity of this VerificationAttemptResponseModel.
        :param text: The text of this VerificationAttemptResponseModel.
        """
        self.openapi_types = {
            'accepted': bool,
            'date_unix': int,
            'levenshtein_distance': float,
            'recording': RecordingResponseModel,
            'similarity': float,
            'text': str
        }

        self.attribute_map = {
            'accepted': 'accepted',
            'date_unix': 'date_unix',
            'levenshtein_distance': 'levenshtein_distance',
            'recording': 'recording',
            'similarity': 'similarity',
            'text': 'text'
        }

        self._accepted = accepted
        self._date_unix = date_unix
        self._levenshtein_distance = levenshtein_distance
        self._recording = recording
        self._similarity = similarity
        self._text = text

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VerificationAttemptResponseModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VerificationAttemptResponseModel of this VerificationAttemptResponseModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accepted(self):
        """Gets the accepted of this VerificationAttemptResponseModel.


        :return: The accepted of this VerificationAttemptResponseModel.
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this VerificationAttemptResponseModel.


        :param accepted: The accepted of this VerificationAttemptResponseModel.
        :type accepted: bool
        """
        if accepted is None:
            raise ValueError("Invalid value for `accepted`, must not be `None`")

        self._accepted = accepted

    @property
    def date_unix(self):
        """Gets the date_unix of this VerificationAttemptResponseModel.


        :return: The date_unix of this VerificationAttemptResponseModel.
        :rtype: int
        """
        return self._date_unix

    @date_unix.setter
    def date_unix(self, date_unix):
        """Sets the date_unix of this VerificationAttemptResponseModel.


        :param date_unix: The date_unix of this VerificationAttemptResponseModel.
        :type date_unix: int
        """
        if date_unix is None:
            raise ValueError("Invalid value for `date_unix`, must not be `None`")

        self._date_unix = date_unix

    @property
    def levenshtein_distance(self):
        """Gets the levenshtein_distance of this VerificationAttemptResponseModel.


        :return: The levenshtein_distance of this VerificationAttemptResponseModel.
        :rtype: float
        """
        return self._levenshtein_distance

    @levenshtein_distance.setter
    def levenshtein_distance(self, levenshtein_distance):
        """Sets the levenshtein_distance of this VerificationAttemptResponseModel.


        :param levenshtein_distance: The levenshtein_distance of this VerificationAttemptResponseModel.
        :type levenshtein_distance: float
        """
        if levenshtein_distance is None:
            raise ValueError("Invalid value for `levenshtein_distance`, must not be `None`")

        self._levenshtein_distance = levenshtein_distance

    @property
    def recording(self):
        """Gets the recording of this VerificationAttemptResponseModel.


        :return: The recording of this VerificationAttemptResponseModel.
        :rtype: RecordingResponseModel
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        """Sets the recording of this VerificationAttemptResponseModel.


        :param recording: The recording of this VerificationAttemptResponseModel.
        :type recording: RecordingResponseModel
        """
        if recording is None:
            raise ValueError("Invalid value for `recording`, must not be `None`")

        self._recording = recording

    @property
    def similarity(self):
        """Gets the similarity of this VerificationAttemptResponseModel.


        :return: The similarity of this VerificationAttemptResponseModel.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this VerificationAttemptResponseModel.


        :param similarity: The similarity of this VerificationAttemptResponseModel.
        :type similarity: float
        """
        if similarity is None:
            raise ValueError("Invalid value for `similarity`, must not be `None`")

        self._similarity = similarity

    @property
    def text(self):
        """Gets the text of this VerificationAttemptResponseModel.


        :return: The text of this VerificationAttemptResponseModel.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this VerificationAttemptResponseModel.


        :param text: The text of this VerificationAttemptResponseModel.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text
