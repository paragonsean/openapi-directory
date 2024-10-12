# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tournament import Tournament
from openapi_server import util


class DfsSlateTournament(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operator_tournament_id: int=None, removed_by_operator: bool=None, slate_id: int=None, slate_tournament_id: int=None, tournament: Tournament=None, tournament_id: int=None):
        """DfsSlateTournament - a model defined in OpenAPI

        :param operator_tournament_id: The operator_tournament_id of this DfsSlateTournament.
        :param removed_by_operator: The removed_by_operator of this DfsSlateTournament.
        :param slate_id: The slate_id of this DfsSlateTournament.
        :param slate_tournament_id: The slate_tournament_id of this DfsSlateTournament.
        :param tournament: The tournament of this DfsSlateTournament.
        :param tournament_id: The tournament_id of this DfsSlateTournament.
        """
        self.openapi_types = {
            'operator_tournament_id': int,
            'removed_by_operator': bool,
            'slate_id': int,
            'slate_tournament_id': int,
            'tournament': Tournament,
            'tournament_id': int
        }

        self.attribute_map = {
            'operator_tournament_id': 'OperatorTournamentID',
            'removed_by_operator': 'RemovedByOperator',
            'slate_id': 'SlateID',
            'slate_tournament_id': 'SlateTournamentID',
            'tournament': 'Tournament',
            'tournament_id': 'TournamentID'
        }

        self._operator_tournament_id = operator_tournament_id
        self._removed_by_operator = removed_by_operator
        self._slate_id = slate_id
        self._slate_tournament_id = slate_tournament_id
        self._tournament = tournament
        self._tournament_id = tournament_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DfsSlateTournament':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DfsSlateTournament of this DfsSlateTournament.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operator_tournament_id(self):
        """Gets the operator_tournament_id of this DfsSlateTournament.


        :return: The operator_tournament_id of this DfsSlateTournament.
        :rtype: int
        """
        return self._operator_tournament_id

    @operator_tournament_id.setter
    def operator_tournament_id(self, operator_tournament_id):
        """Sets the operator_tournament_id of this DfsSlateTournament.


        :param operator_tournament_id: The operator_tournament_id of this DfsSlateTournament.
        :type operator_tournament_id: int
        """

        self._operator_tournament_id = operator_tournament_id

    @property
    def removed_by_operator(self):
        """Gets the removed_by_operator of this DfsSlateTournament.


        :return: The removed_by_operator of this DfsSlateTournament.
        :rtype: bool
        """
        return self._removed_by_operator

    @removed_by_operator.setter
    def removed_by_operator(self, removed_by_operator):
        """Sets the removed_by_operator of this DfsSlateTournament.


        :param removed_by_operator: The removed_by_operator of this DfsSlateTournament.
        :type removed_by_operator: bool
        """

        self._removed_by_operator = removed_by_operator

    @property
    def slate_id(self):
        """Gets the slate_id of this DfsSlateTournament.


        :return: The slate_id of this DfsSlateTournament.
        :rtype: int
        """
        return self._slate_id

    @slate_id.setter
    def slate_id(self, slate_id):
        """Sets the slate_id of this DfsSlateTournament.


        :param slate_id: The slate_id of this DfsSlateTournament.
        :type slate_id: int
        """

        self._slate_id = slate_id

    @property
    def slate_tournament_id(self):
        """Gets the slate_tournament_id of this DfsSlateTournament.


        :return: The slate_tournament_id of this DfsSlateTournament.
        :rtype: int
        """
        return self._slate_tournament_id

    @slate_tournament_id.setter
    def slate_tournament_id(self, slate_tournament_id):
        """Sets the slate_tournament_id of this DfsSlateTournament.


        :param slate_tournament_id: The slate_tournament_id of this DfsSlateTournament.
        :type slate_tournament_id: int
        """

        self._slate_tournament_id = slate_tournament_id

    @property
    def tournament(self):
        """Gets the tournament of this DfsSlateTournament.


        :return: The tournament of this DfsSlateTournament.
        :rtype: Tournament
        """
        return self._tournament

    @tournament.setter
    def tournament(self, tournament):
        """Sets the tournament of this DfsSlateTournament.


        :param tournament: The tournament of this DfsSlateTournament.
        :type tournament: Tournament
        """

        self._tournament = tournament

    @property
    def tournament_id(self):
        """Gets the tournament_id of this DfsSlateTournament.


        :return: The tournament_id of this DfsSlateTournament.
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this DfsSlateTournament.


        :param tournament_id: The tournament_id of this DfsSlateTournament.
        :type tournament_id: int
        """

        self._tournament_id = tournament_id
