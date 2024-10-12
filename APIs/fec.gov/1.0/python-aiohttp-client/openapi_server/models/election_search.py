# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ElectionSearch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, candidate_status: str=None, cycle: int=None, district: str=None, incumbent_id: str=None, incumbent_name: str=None, office: str=None, state: str=None):
        """ElectionSearch - a model defined in OpenAPI

        :param candidate_status: The candidate_status of this ElectionSearch.
        :param cycle: The cycle of this ElectionSearch.
        :param district: The district of this ElectionSearch.
        :param incumbent_id: The incumbent_id of this ElectionSearch.
        :param incumbent_name: The incumbent_name of this ElectionSearch.
        :param office: The office of this ElectionSearch.
        :param state: The state of this ElectionSearch.
        """
        self.openapi_types = {
            'candidate_status': str,
            'cycle': int,
            'district': str,
            'incumbent_id': str,
            'incumbent_name': str,
            'office': str,
            'state': str
        }

        self.attribute_map = {
            'candidate_status': 'candidate_status',
            'cycle': 'cycle',
            'district': 'district',
            'incumbent_id': 'incumbent_id',
            'incumbent_name': 'incumbent_name',
            'office': 'office',
            'state': 'state'
        }

        self._candidate_status = candidate_status
        self._cycle = cycle
        self._district = district
        self._incumbent_id = incumbent_id
        self._incumbent_name = incumbent_name
        self._office = office
        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ElectionSearch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ElectionSearch of this ElectionSearch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def candidate_status(self):
        """Gets the candidate_status of this ElectionSearch.


        :return: The candidate_status of this ElectionSearch.
        :rtype: str
        """
        return self._candidate_status

    @candidate_status.setter
    def candidate_status(self, candidate_status):
        """Sets the candidate_status of this ElectionSearch.


        :param candidate_status: The candidate_status of this ElectionSearch.
        :type candidate_status: str
        """

        self._candidate_status = candidate_status

    @property
    def cycle(self):
        """Gets the cycle of this ElectionSearch.


        :return: The cycle of this ElectionSearch.
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ElectionSearch.


        :param cycle: The cycle of this ElectionSearch.
        :type cycle: int
        """

        self._cycle = cycle

    @property
    def district(self):
        """Gets the district of this ElectionSearch.


        :return: The district of this ElectionSearch.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this ElectionSearch.


        :param district: The district of this ElectionSearch.
        :type district: str
        """

        self._district = district

    @property
    def incumbent_id(self):
        """Gets the incumbent_id of this ElectionSearch.


        :return: The incumbent_id of this ElectionSearch.
        :rtype: str
        """
        return self._incumbent_id

    @incumbent_id.setter
    def incumbent_id(self, incumbent_id):
        """Sets the incumbent_id of this ElectionSearch.


        :param incumbent_id: The incumbent_id of this ElectionSearch.
        :type incumbent_id: str
        """

        self._incumbent_id = incumbent_id

    @property
    def incumbent_name(self):
        """Gets the incumbent_name of this ElectionSearch.


        :return: The incumbent_name of this ElectionSearch.
        :rtype: str
        """
        return self._incumbent_name

    @incumbent_name.setter
    def incumbent_name(self, incumbent_name):
        """Sets the incumbent_name of this ElectionSearch.


        :param incumbent_name: The incumbent_name of this ElectionSearch.
        :type incumbent_name: str
        """

        self._incumbent_name = incumbent_name

    @property
    def office(self):
        """Gets the office of this ElectionSearch.


        :return: The office of this ElectionSearch.
        :rtype: str
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this ElectionSearch.


        :param office: The office of this ElectionSearch.
        :type office: str
        """

        self._office = office

    @property
    def state(self):
        """Gets the state of this ElectionSearch.


        :return: The state of this ElectionSearch.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ElectionSearch.


        :param state: The state of this ElectionSearch.
        :type state: str
        """

        self._state = state
