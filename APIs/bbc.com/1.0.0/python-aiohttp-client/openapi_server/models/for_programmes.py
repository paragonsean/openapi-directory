# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.for_programme import ForProgramme
from openapi_server import util


class ForProgrammes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, for_programme: List[ForProgramme]=None):
        """ForProgrammes - a model defined in OpenAPI

        :param for_programme: The for_programme of this ForProgrammes.
        """
        self.openapi_types = {
            'for_programme': List[ForProgramme]
        }

        self.attribute_map = {
            'for_programme': 'for_programme'
        }

        self._for_programme = for_programme

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ForProgrammes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The for_programmes of this ForProgrammes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def for_programme(self):
        """Gets the for_programme of this ForProgrammes.


        :return: The for_programme of this ForProgrammes.
        :rtype: List[ForProgramme]
        """
        return self._for_programme

    @for_programme.setter
    def for_programme(self, for_programme):
        """Sets the for_programme of this ForProgrammes.


        :param for_programme: The for_programme of this ForProgrammes.
        :type for_programme: List[ForProgramme]
        """

        self._for_programme = for_programme
