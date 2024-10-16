# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Team(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active: bool=None, ap_rank: int=None, coaches_rank: int=None, conference: str=None, conference_id: int=None, conference_losses: int=None, conference_wins: int=None, global_team_id: int=None, key: str=None, losses: int=None, name: str=None, playoff_rank: int=None, rank_season: int=None, rank_season_type: int=None, rank_week: int=None, school: str=None, short_display_name: str=None, stadium_id: int=None, team_id: int=None, team_logo_url: str=None, wins: int=None):
        """Team - a model defined in OpenAPI

        :param active: The active of this Team.
        :param ap_rank: The ap_rank of this Team.
        :param coaches_rank: The coaches_rank of this Team.
        :param conference: The conference of this Team.
        :param conference_id: The conference_id of this Team.
        :param conference_losses: The conference_losses of this Team.
        :param conference_wins: The conference_wins of this Team.
        :param global_team_id: The global_team_id of this Team.
        :param key: The key of this Team.
        :param losses: The losses of this Team.
        :param name: The name of this Team.
        :param playoff_rank: The playoff_rank of this Team.
        :param rank_season: The rank_season of this Team.
        :param rank_season_type: The rank_season_type of this Team.
        :param rank_week: The rank_week of this Team.
        :param school: The school of this Team.
        :param short_display_name: The short_display_name of this Team.
        :param stadium_id: The stadium_id of this Team.
        :param team_id: The team_id of this Team.
        :param team_logo_url: The team_logo_url of this Team.
        :param wins: The wins of this Team.
        """
        self.openapi_types = {
            'active': bool,
            'ap_rank': int,
            'coaches_rank': int,
            'conference': str,
            'conference_id': int,
            'conference_losses': int,
            'conference_wins': int,
            'global_team_id': int,
            'key': str,
            'losses': int,
            'name': str,
            'playoff_rank': int,
            'rank_season': int,
            'rank_season_type': int,
            'rank_week': int,
            'school': str,
            'short_display_name': str,
            'stadium_id': int,
            'team_id': int,
            'team_logo_url': str,
            'wins': int
        }

        self.attribute_map = {
            'active': 'Active',
            'ap_rank': 'ApRank',
            'coaches_rank': 'CoachesRank',
            'conference': 'Conference',
            'conference_id': 'ConferenceID',
            'conference_losses': 'ConferenceLosses',
            'conference_wins': 'ConferenceWins',
            'global_team_id': 'GlobalTeamID',
            'key': 'Key',
            'losses': 'Losses',
            'name': 'Name',
            'playoff_rank': 'PlayoffRank',
            'rank_season': 'RankSeason',
            'rank_season_type': 'RankSeasonType',
            'rank_week': 'RankWeek',
            'school': 'School',
            'short_display_name': 'ShortDisplayName',
            'stadium_id': 'StadiumID',
            'team_id': 'TeamID',
            'team_logo_url': 'TeamLogoUrl',
            'wins': 'Wins'
        }

        self._active = active
        self._ap_rank = ap_rank
        self._coaches_rank = coaches_rank
        self._conference = conference
        self._conference_id = conference_id
        self._conference_losses = conference_losses
        self._conference_wins = conference_wins
        self._global_team_id = global_team_id
        self._key = key
        self._losses = losses
        self._name = name
        self._playoff_rank = playoff_rank
        self._rank_season = rank_season
        self._rank_season_type = rank_season_type
        self._rank_week = rank_week
        self._school = school
        self._short_display_name = short_display_name
        self._stadium_id = stadium_id
        self._team_id = team_id
        self._team_logo_url = team_logo_url
        self._wins = wins

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Team':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Team of this Team.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self):
        """Gets the active of this Team.


        :return: The active of this Team.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Team.


        :param active: The active of this Team.
        :type active: bool
        """

        self._active = active

    @property
    def ap_rank(self):
        """Gets the ap_rank of this Team.


        :return: The ap_rank of this Team.
        :rtype: int
        """
        return self._ap_rank

    @ap_rank.setter
    def ap_rank(self, ap_rank):
        """Sets the ap_rank of this Team.


        :param ap_rank: The ap_rank of this Team.
        :type ap_rank: int
        """

        self._ap_rank = ap_rank

    @property
    def coaches_rank(self):
        """Gets the coaches_rank of this Team.


        :return: The coaches_rank of this Team.
        :rtype: int
        """
        return self._coaches_rank

    @coaches_rank.setter
    def coaches_rank(self, coaches_rank):
        """Sets the coaches_rank of this Team.


        :param coaches_rank: The coaches_rank of this Team.
        :type coaches_rank: int
        """

        self._coaches_rank = coaches_rank

    @property
    def conference(self):
        """Gets the conference of this Team.


        :return: The conference of this Team.
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this Team.


        :param conference: The conference of this Team.
        :type conference: str
        """

        self._conference = conference

    @property
    def conference_id(self):
        """Gets the conference_id of this Team.


        :return: The conference_id of this Team.
        :rtype: int
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this Team.


        :param conference_id: The conference_id of this Team.
        :type conference_id: int
        """

        self._conference_id = conference_id

    @property
    def conference_losses(self):
        """Gets the conference_losses of this Team.


        :return: The conference_losses of this Team.
        :rtype: int
        """
        return self._conference_losses

    @conference_losses.setter
    def conference_losses(self, conference_losses):
        """Sets the conference_losses of this Team.


        :param conference_losses: The conference_losses of this Team.
        :type conference_losses: int
        """

        self._conference_losses = conference_losses

    @property
    def conference_wins(self):
        """Gets the conference_wins of this Team.


        :return: The conference_wins of this Team.
        :rtype: int
        """
        return self._conference_wins

    @conference_wins.setter
    def conference_wins(self, conference_wins):
        """Sets the conference_wins of this Team.


        :param conference_wins: The conference_wins of this Team.
        :type conference_wins: int
        """

        self._conference_wins = conference_wins

    @property
    def global_team_id(self):
        """Gets the global_team_id of this Team.


        :return: The global_team_id of this Team.
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this Team.


        :param global_team_id: The global_team_id of this Team.
        :type global_team_id: int
        """

        self._global_team_id = global_team_id

    @property
    def key(self):
        """Gets the key of this Team.


        :return: The key of this Team.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Team.


        :param key: The key of this Team.
        :type key: str
        """

        self._key = key

    @property
    def losses(self):
        """Gets the losses of this Team.


        :return: The losses of this Team.
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this Team.


        :param losses: The losses of this Team.
        :type losses: int
        """

        self._losses = losses

    @property
    def name(self):
        """Gets the name of this Team.


        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.
        :type name: str
        """

        self._name = name

    @property
    def playoff_rank(self):
        """Gets the playoff_rank of this Team.


        :return: The playoff_rank of this Team.
        :rtype: int
        """
        return self._playoff_rank

    @playoff_rank.setter
    def playoff_rank(self, playoff_rank):
        """Sets the playoff_rank of this Team.


        :param playoff_rank: The playoff_rank of this Team.
        :type playoff_rank: int
        """

        self._playoff_rank = playoff_rank

    @property
    def rank_season(self):
        """Gets the rank_season of this Team.


        :return: The rank_season of this Team.
        :rtype: int
        """
        return self._rank_season

    @rank_season.setter
    def rank_season(self, rank_season):
        """Sets the rank_season of this Team.


        :param rank_season: The rank_season of this Team.
        :type rank_season: int
        """

        self._rank_season = rank_season

    @property
    def rank_season_type(self):
        """Gets the rank_season_type of this Team.


        :return: The rank_season_type of this Team.
        :rtype: int
        """
        return self._rank_season_type

    @rank_season_type.setter
    def rank_season_type(self, rank_season_type):
        """Sets the rank_season_type of this Team.


        :param rank_season_type: The rank_season_type of this Team.
        :type rank_season_type: int
        """

        self._rank_season_type = rank_season_type

    @property
    def rank_week(self):
        """Gets the rank_week of this Team.


        :return: The rank_week of this Team.
        :rtype: int
        """
        return self._rank_week

    @rank_week.setter
    def rank_week(self, rank_week):
        """Sets the rank_week of this Team.


        :param rank_week: The rank_week of this Team.
        :type rank_week: int
        """

        self._rank_week = rank_week

    @property
    def school(self):
        """Gets the school of this Team.


        :return: The school of this Team.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this Team.


        :param school: The school of this Team.
        :type school: str
        """

        self._school = school

    @property
    def short_display_name(self):
        """Gets the short_display_name of this Team.


        :return: The short_display_name of this Team.
        :rtype: str
        """
        return self._short_display_name

    @short_display_name.setter
    def short_display_name(self, short_display_name):
        """Sets the short_display_name of this Team.


        :param short_display_name: The short_display_name of this Team.
        :type short_display_name: str
        """

        self._short_display_name = short_display_name

    @property
    def stadium_id(self):
        """Gets the stadium_id of this Team.


        :return: The stadium_id of this Team.
        :rtype: int
        """
        return self._stadium_id

    @stadium_id.setter
    def stadium_id(self, stadium_id):
        """Sets the stadium_id of this Team.


        :param stadium_id: The stadium_id of this Team.
        :type stadium_id: int
        """

        self._stadium_id = stadium_id

    @property
    def team_id(self):
        """Gets the team_id of this Team.


        :return: The team_id of this Team.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Team.


        :param team_id: The team_id of this Team.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def team_logo_url(self):
        """Gets the team_logo_url of this Team.


        :return: The team_logo_url of this Team.
        :rtype: str
        """
        return self._team_logo_url

    @team_logo_url.setter
    def team_logo_url(self, team_logo_url):
        """Sets the team_logo_url of this Team.


        :param team_logo_url: The team_logo_url of this Team.
        :type team_logo_url: str
        """

        self._team_logo_url = team_logo_url

    @property
    def wins(self):
        """Gets the wins of this Team.


        :return: The wins of this Team.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this Team.


        :param wins: The wins of this Team.
        :type wins: int
        """

        self._wins = wins
