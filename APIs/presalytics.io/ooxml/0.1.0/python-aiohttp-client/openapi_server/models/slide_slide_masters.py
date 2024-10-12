# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SlideSlideMasters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, slide_id: str=None):
        """SlideSlideMasters - a model defined in OpenAPI

        :param id: The id of this SlideSlideMasters.
        :param slide_id: The slide_id of this SlideSlideMasters.
        """
        self.openapi_types = {
            'id': str,
            'slide_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'slide_id': 'slideId'
        }

        self._id = id
        self._slide_id = slide_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideSlideMasters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.SlideMasters of this SlideSlideMasters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SlideSlideMasters.


        :return: The id of this SlideSlideMasters.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideSlideMasters.


        :param id: The id of this SlideSlideMasters.
        :type id: str
        """

        self._id = id

    @property
    def slide_id(self):
        """Gets the slide_id of this SlideSlideMasters.


        :return: The slide_id of this SlideSlideMasters.
        :rtype: str
        """
        return self._slide_id

    @slide_id.setter
    def slide_id(self, slide_id):
        """Sets the slide_id of this SlideSlideMasters.


        :param slide_id: The slide_id of this SlideSlideMasters.
        :type slide_id: str
        """

        self._slide_id = slide_id
