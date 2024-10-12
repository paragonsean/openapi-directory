# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CandidateSearch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, office_sought: str=None):
        """CandidateSearch - a model defined in OpenAPI

        :param id: The id of this CandidateSearch.
        :param name: The name of this CandidateSearch.
        :param office_sought: The office_sought of this CandidateSearch.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'office_sought': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'office_sought': 'office_sought'
        }

        self._id = id
        self._name = name
        self._office_sought = office_sought

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CandidateSearch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CandidateSearch of this CandidateSearch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CandidateSearch.


        :return: The id of this CandidateSearch.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CandidateSearch.


        :param id: The id of this CandidateSearch.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CandidateSearch.


        :return: The name of this CandidateSearch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CandidateSearch.


        :param name: The name of this CandidateSearch.
        :type name: str
        """

        self._name = name

    @property
    def office_sought(self):
        """Gets the office_sought of this CandidateSearch.


        :return: The office_sought of this CandidateSearch.
        :rtype: str
        """
        return self._office_sought

    @office_sought.setter
    def office_sought(self, office_sought):
        """Sets the office_sought of this CandidateSearch.


        :param office_sought: The office_sought of this CandidateSearch.
        :type office_sought: str
        """

        self._office_sought = office_sought
