# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.transcoder import Transcoder
from openapi_server import util


class CreateTranscoder200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transcoder: Transcoder=None):
        """CreateTranscoder200Response - a model defined in OpenAPI

        :param transcoder: The transcoder of this CreateTranscoder200Response.
        """
        self.openapi_types = {
            'transcoder': Transcoder
        }

        self.attribute_map = {
            'transcoder': 'transcoder'
        }

        self._transcoder = transcoder

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateTranscoder200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createTranscoder_200_response of this CreateTranscoder200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transcoder(self):
        """Gets the transcoder of this CreateTranscoder200Response.


        :return: The transcoder of this CreateTranscoder200Response.
        :rtype: Transcoder
        """
        return self._transcoder

    @transcoder.setter
    def transcoder(self, transcoder):
        """Sets the transcoder of this CreateTranscoder200Response.


        :param transcoder: The transcoder of this CreateTranscoder200Response.
        :type transcoder: Transcoder
        """
        if transcoder is None:
            raise ValueError("Invalid value for `transcoder`, must not be `None`")

        self._transcoder = transcoder
