# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.opponent_type_team import OpponentTypeTeam
from openapi_server.models.team import Team
from openapi_server import util


class TournamentTeamRosters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rosters: List[Team]=None, type: OpponentTypeTeam=None):
        """TournamentTeamRosters - a model defined in OpenAPI

        :param rosters: The rosters of this TournamentTeamRosters.
        :param type: The type of this TournamentTeamRosters.
        """
        self.openapi_types = {
            'rosters': List[Team],
            'type': OpponentTypeTeam
        }

        self.attribute_map = {
            'rosters': 'rosters',
            'type': 'type'
        }

        self._rosters = rosters
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TournamentTeamRosters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TournamentTeamRosters of this TournamentTeamRosters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rosters(self):
        """Gets the rosters of this TournamentTeamRosters.

        A list of teams

        :return: The rosters of this TournamentTeamRosters.
        :rtype: List[Team]
        """
        return self._rosters

    @rosters.setter
    def rosters(self, rosters):
        """Sets the rosters of this TournamentTeamRosters.

        A list of teams

        :param rosters: The rosters of this TournamentTeamRosters.
        :type rosters: List[Team]
        """
        if rosters is None:
            raise ValueError("Invalid value for `rosters`, must not be `None`")

        self._rosters = rosters

    @property
    def type(self):
        """Gets the type of this TournamentTeamRosters.


        :return: The type of this TournamentTeamRosters.
        :rtype: OpponentTypeTeam
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TournamentTeamRosters.


        :param type: The type of this TournamentTeamRosters.
        :type type: OpponentTypeTeam
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
