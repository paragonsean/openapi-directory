# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ECTotalsByCandidate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, candidate_id: str=None, cycle: int=None, total: float=None):
        """ECTotalsByCandidate - a model defined in OpenAPI

        :param candidate_id: The candidate_id of this ECTotalsByCandidate.
        :param cycle: The cycle of this ECTotalsByCandidate.
        :param total: The total of this ECTotalsByCandidate.
        """
        self.openapi_types = {
            'candidate_id': str,
            'cycle': int,
            'total': float
        }

        self.attribute_map = {
            'candidate_id': 'candidate_id',
            'cycle': 'cycle',
            'total': 'total'
        }

        self._candidate_id = candidate_id
        self._cycle = cycle
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ECTotalsByCandidate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ECTotalsByCandidate of this ECTotalsByCandidate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def candidate_id(self):
        """Gets the candidate_id of this ECTotalsByCandidate.


        :return: The candidate_id of this ECTotalsByCandidate.
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this ECTotalsByCandidate.


        :param candidate_id: The candidate_id of this ECTotalsByCandidate.
        :type candidate_id: str
        """

        self._candidate_id = candidate_id

    @property
    def cycle(self):
        """Gets the cycle of this ECTotalsByCandidate.


        :return: The cycle of this ECTotalsByCandidate.
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ECTotalsByCandidate.


        :param cycle: The cycle of this ECTotalsByCandidate.
        :type cycle: int
        """

        self._cycle = cycle

    @property
    def total(self):
        """Gets the total of this ECTotalsByCandidate.


        :return: The total of this ECTotalsByCandidate.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ECTotalsByCandidate.


        :param total: The total of this ECTotalsByCandidate.
        :type total: float
        """

        self._total = total
