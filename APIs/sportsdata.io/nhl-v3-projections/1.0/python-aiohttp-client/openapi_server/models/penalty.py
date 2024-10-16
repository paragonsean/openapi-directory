# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Penalty(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bench_penalty_served_by_player_id: int=None, description: str=None, drawn_by_player_id: int=None, drawn_by_team_id: int=None, is_bench_penalty: bool=None, penalized_player_id: int=None, penalized_team_id: int=None, penalty_id: int=None, penalty_minutes: int=None, period_id: int=None, sequence: int=None, time_remaining_minutes: int=None, time_remaining_seconds: int=None):
        """Penalty - a model defined in OpenAPI

        :param bench_penalty_served_by_player_id: The bench_penalty_served_by_player_id of this Penalty.
        :param description: The description of this Penalty.
        :param drawn_by_player_id: The drawn_by_player_id of this Penalty.
        :param drawn_by_team_id: The drawn_by_team_id of this Penalty.
        :param is_bench_penalty: The is_bench_penalty of this Penalty.
        :param penalized_player_id: The penalized_player_id of this Penalty.
        :param penalized_team_id: The penalized_team_id of this Penalty.
        :param penalty_id: The penalty_id of this Penalty.
        :param penalty_minutes: The penalty_minutes of this Penalty.
        :param period_id: The period_id of this Penalty.
        :param sequence: The sequence of this Penalty.
        :param time_remaining_minutes: The time_remaining_minutes of this Penalty.
        :param time_remaining_seconds: The time_remaining_seconds of this Penalty.
        """
        self.openapi_types = {
            'bench_penalty_served_by_player_id': int,
            'description': str,
            'drawn_by_player_id': int,
            'drawn_by_team_id': int,
            'is_bench_penalty': bool,
            'penalized_player_id': int,
            'penalized_team_id': int,
            'penalty_id': int,
            'penalty_minutes': int,
            'period_id': int,
            'sequence': int,
            'time_remaining_minutes': int,
            'time_remaining_seconds': int
        }

        self.attribute_map = {
            'bench_penalty_served_by_player_id': 'BenchPenaltyServedByPlayerID',
            'description': 'Description',
            'drawn_by_player_id': 'DrawnByPlayerID',
            'drawn_by_team_id': 'DrawnByTeamID',
            'is_bench_penalty': 'IsBenchPenalty',
            'penalized_player_id': 'PenalizedPlayerID',
            'penalized_team_id': 'PenalizedTeamID',
            'penalty_id': 'PenaltyID',
            'penalty_minutes': 'PenaltyMinutes',
            'period_id': 'PeriodID',
            'sequence': 'Sequence',
            'time_remaining_minutes': 'TimeRemainingMinutes',
            'time_remaining_seconds': 'TimeRemainingSeconds'
        }

        self._bench_penalty_served_by_player_id = bench_penalty_served_by_player_id
        self._description = description
        self._drawn_by_player_id = drawn_by_player_id
        self._drawn_by_team_id = drawn_by_team_id
        self._is_bench_penalty = is_bench_penalty
        self._penalized_player_id = penalized_player_id
        self._penalized_team_id = penalized_team_id
        self._penalty_id = penalty_id
        self._penalty_minutes = penalty_minutes
        self._period_id = period_id
        self._sequence = sequence
        self._time_remaining_minutes = time_remaining_minutes
        self._time_remaining_seconds = time_remaining_seconds

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Penalty':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Penalty of this Penalty.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bench_penalty_served_by_player_id(self):
        """Gets the bench_penalty_served_by_player_id of this Penalty.


        :return: The bench_penalty_served_by_player_id of this Penalty.
        :rtype: int
        """
        return self._bench_penalty_served_by_player_id

    @bench_penalty_served_by_player_id.setter
    def bench_penalty_served_by_player_id(self, bench_penalty_served_by_player_id):
        """Sets the bench_penalty_served_by_player_id of this Penalty.


        :param bench_penalty_served_by_player_id: The bench_penalty_served_by_player_id of this Penalty.
        :type bench_penalty_served_by_player_id: int
        """

        self._bench_penalty_served_by_player_id = bench_penalty_served_by_player_id

    @property
    def description(self):
        """Gets the description of this Penalty.


        :return: The description of this Penalty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Penalty.


        :param description: The description of this Penalty.
        :type description: str
        """

        self._description = description

    @property
    def drawn_by_player_id(self):
        """Gets the drawn_by_player_id of this Penalty.


        :return: The drawn_by_player_id of this Penalty.
        :rtype: int
        """
        return self._drawn_by_player_id

    @drawn_by_player_id.setter
    def drawn_by_player_id(self, drawn_by_player_id):
        """Sets the drawn_by_player_id of this Penalty.


        :param drawn_by_player_id: The drawn_by_player_id of this Penalty.
        :type drawn_by_player_id: int
        """

        self._drawn_by_player_id = drawn_by_player_id

    @property
    def drawn_by_team_id(self):
        """Gets the drawn_by_team_id of this Penalty.


        :return: The drawn_by_team_id of this Penalty.
        :rtype: int
        """
        return self._drawn_by_team_id

    @drawn_by_team_id.setter
    def drawn_by_team_id(self, drawn_by_team_id):
        """Sets the drawn_by_team_id of this Penalty.


        :param drawn_by_team_id: The drawn_by_team_id of this Penalty.
        :type drawn_by_team_id: int
        """

        self._drawn_by_team_id = drawn_by_team_id

    @property
    def is_bench_penalty(self):
        """Gets the is_bench_penalty of this Penalty.


        :return: The is_bench_penalty of this Penalty.
        :rtype: bool
        """
        return self._is_bench_penalty

    @is_bench_penalty.setter
    def is_bench_penalty(self, is_bench_penalty):
        """Sets the is_bench_penalty of this Penalty.


        :param is_bench_penalty: The is_bench_penalty of this Penalty.
        :type is_bench_penalty: bool
        """

        self._is_bench_penalty = is_bench_penalty

    @property
    def penalized_player_id(self):
        """Gets the penalized_player_id of this Penalty.


        :return: The penalized_player_id of this Penalty.
        :rtype: int
        """
        return self._penalized_player_id

    @penalized_player_id.setter
    def penalized_player_id(self, penalized_player_id):
        """Sets the penalized_player_id of this Penalty.


        :param penalized_player_id: The penalized_player_id of this Penalty.
        :type penalized_player_id: int
        """

        self._penalized_player_id = penalized_player_id

    @property
    def penalized_team_id(self):
        """Gets the penalized_team_id of this Penalty.


        :return: The penalized_team_id of this Penalty.
        :rtype: int
        """
        return self._penalized_team_id

    @penalized_team_id.setter
    def penalized_team_id(self, penalized_team_id):
        """Sets the penalized_team_id of this Penalty.


        :param penalized_team_id: The penalized_team_id of this Penalty.
        :type penalized_team_id: int
        """

        self._penalized_team_id = penalized_team_id

    @property
    def penalty_id(self):
        """Gets the penalty_id of this Penalty.


        :return: The penalty_id of this Penalty.
        :rtype: int
        """
        return self._penalty_id

    @penalty_id.setter
    def penalty_id(self, penalty_id):
        """Sets the penalty_id of this Penalty.


        :param penalty_id: The penalty_id of this Penalty.
        :type penalty_id: int
        """

        self._penalty_id = penalty_id

    @property
    def penalty_minutes(self):
        """Gets the penalty_minutes of this Penalty.


        :return: The penalty_minutes of this Penalty.
        :rtype: int
        """
        return self._penalty_minutes

    @penalty_minutes.setter
    def penalty_minutes(self, penalty_minutes):
        """Sets the penalty_minutes of this Penalty.


        :param penalty_minutes: The penalty_minutes of this Penalty.
        :type penalty_minutes: int
        """

        self._penalty_minutes = penalty_minutes

    @property
    def period_id(self):
        """Gets the period_id of this Penalty.


        :return: The period_id of this Penalty.
        :rtype: int
        """
        return self._period_id

    @period_id.setter
    def period_id(self, period_id):
        """Sets the period_id of this Penalty.


        :param period_id: The period_id of this Penalty.
        :type period_id: int
        """

        self._period_id = period_id

    @property
    def sequence(self):
        """Gets the sequence of this Penalty.


        :return: The sequence of this Penalty.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this Penalty.


        :param sequence: The sequence of this Penalty.
        :type sequence: int
        """

        self._sequence = sequence

    @property
    def time_remaining_minutes(self):
        """Gets the time_remaining_minutes of this Penalty.


        :return: The time_remaining_minutes of this Penalty.
        :rtype: int
        """
        return self._time_remaining_minutes

    @time_remaining_minutes.setter
    def time_remaining_minutes(self, time_remaining_minutes):
        """Sets the time_remaining_minutes of this Penalty.


        :param time_remaining_minutes: The time_remaining_minutes of this Penalty.
        :type time_remaining_minutes: int
        """

        self._time_remaining_minutes = time_remaining_minutes

    @property
    def time_remaining_seconds(self):
        """Gets the time_remaining_seconds of this Penalty.


        :return: The time_remaining_seconds of this Penalty.
        :rtype: int
        """
        return self._time_remaining_seconds

    @time_remaining_seconds.setter
    def time_remaining_seconds(self, time_remaining_seconds):
        """Sets the time_remaining_seconds of this Penalty.


        :param time_remaining_seconds: The time_remaining_seconds of this Penalty.
        :type time_remaining_seconds: int
        """

        self._time_remaining_seconds = time_remaining_seconds
