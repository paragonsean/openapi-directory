# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.podcast_minimum import PodcastMinimum
from openapi_server import util


class SubmitPodcastResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, podcast: PodcastMinimum=None, status: str=None):
        """SubmitPodcastResponse - a model defined in OpenAPI

        :param podcast: The podcast of this SubmitPodcastResponse.
        :param status: The status of this SubmitPodcastResponse.
        """
        self.openapi_types = {
            'podcast': PodcastMinimum,
            'status': str
        }

        self.attribute_map = {
            'podcast': 'podcast',
            'status': 'status'
        }

        self._podcast = podcast
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SubmitPodcastResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SubmitPodcastResponse of this SubmitPodcastResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def podcast(self):
        """Gets the podcast of this SubmitPodcastResponse.


        :return: The podcast of this SubmitPodcastResponse.
        :rtype: PodcastMinimum
        """
        return self._podcast

    @podcast.setter
    def podcast(self, podcast):
        """Sets the podcast of this SubmitPodcastResponse.


        :param podcast: The podcast of this SubmitPodcastResponse.
        :type podcast: PodcastMinimum
        """
        if podcast is None:
            raise ValueError("Invalid value for `podcast`, must not be `None`")

        self._podcast = podcast

    @property
    def status(self):
        """Gets the status of this SubmitPodcastResponse.

        The status of this submission.

        :return: The status of this SubmitPodcastResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubmitPodcastResponse.

        The status of this submission.

        :param status: The status of this SubmitPodcastResponse.
        :type status: str
        """
        allowed_values = ["found", "in review", "rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
