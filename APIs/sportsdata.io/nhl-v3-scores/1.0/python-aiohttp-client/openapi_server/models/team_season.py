# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.opponent_season import OpponentSeason
from openapi_server import util


class TeamSeason(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assists: float=None, bench_penalty_minutes: float=None, blocks: float=None, empty_net_goals: float=None, faceoffs_lost: float=None, faceoffs_won: float=None, fantasy_points: float=None, fantasy_points_draft_kings: float=None, fantasy_points_fan_duel: float=None, fantasy_points_fantasy_draft: float=None, fantasy_points_yahoo: float=None, games: int=None, giveaways: float=None, global_team_id: int=None, goals: float=None, goaltending_goals_against: float=None, goaltending_losses: float=None, goaltending_minutes: int=None, goaltending_overtime_losses: float=None, goaltending_saves: float=None, goaltending_seconds: int=None, goaltending_shots_against: float=None, goaltending_shutouts: float=None, goaltending_wins: float=None, hat_tricks: float=None, hits: float=None, losses: int=None, minutes: int=None, name: str=None, opponent_position: str=None, opponent_stat: OpponentSeason=None, overtime_losses: int=None, penalty_minutes: float=None, plus_minus: float=None, power_play_assists: float=None, power_play_goals: float=None, season: int=None, season_type: int=None, seconds: int=None, shifts: float=None, shootout_goals: float=None, short_handed_assists: float=None, short_handed_goals: float=None, shots_on_goal: float=None, started: int=None, stat_id: int=None, takeaways: float=None, team: str=None, team_id: int=None, updated: str=None, wins: int=None):
        """TeamSeason - a model defined in OpenAPI

        :param assists: The assists of this TeamSeason.
        :param bench_penalty_minutes: The bench_penalty_minutes of this TeamSeason.
        :param blocks: The blocks of this TeamSeason.
        :param empty_net_goals: The empty_net_goals of this TeamSeason.
        :param faceoffs_lost: The faceoffs_lost of this TeamSeason.
        :param faceoffs_won: The faceoffs_won of this TeamSeason.
        :param fantasy_points: The fantasy_points of this TeamSeason.
        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this TeamSeason.
        :param fantasy_points_fan_duel: The fantasy_points_fan_duel of this TeamSeason.
        :param fantasy_points_fantasy_draft: The fantasy_points_fantasy_draft of this TeamSeason.
        :param fantasy_points_yahoo: The fantasy_points_yahoo of this TeamSeason.
        :param games: The games of this TeamSeason.
        :param giveaways: The giveaways of this TeamSeason.
        :param global_team_id: The global_team_id of this TeamSeason.
        :param goals: The goals of this TeamSeason.
        :param goaltending_goals_against: The goaltending_goals_against of this TeamSeason.
        :param goaltending_losses: The goaltending_losses of this TeamSeason.
        :param goaltending_minutes: The goaltending_minutes of this TeamSeason.
        :param goaltending_overtime_losses: The goaltending_overtime_losses of this TeamSeason.
        :param goaltending_saves: The goaltending_saves of this TeamSeason.
        :param goaltending_seconds: The goaltending_seconds of this TeamSeason.
        :param goaltending_shots_against: The goaltending_shots_against of this TeamSeason.
        :param goaltending_shutouts: The goaltending_shutouts of this TeamSeason.
        :param goaltending_wins: The goaltending_wins of this TeamSeason.
        :param hat_tricks: The hat_tricks of this TeamSeason.
        :param hits: The hits of this TeamSeason.
        :param losses: The losses of this TeamSeason.
        :param minutes: The minutes of this TeamSeason.
        :param name: The name of this TeamSeason.
        :param opponent_position: The opponent_position of this TeamSeason.
        :param opponent_stat: The opponent_stat of this TeamSeason.
        :param overtime_losses: The overtime_losses of this TeamSeason.
        :param penalty_minutes: The penalty_minutes of this TeamSeason.
        :param plus_minus: The plus_minus of this TeamSeason.
        :param power_play_assists: The power_play_assists of this TeamSeason.
        :param power_play_goals: The power_play_goals of this TeamSeason.
        :param season: The season of this TeamSeason.
        :param season_type: The season_type of this TeamSeason.
        :param seconds: The seconds of this TeamSeason.
        :param shifts: The shifts of this TeamSeason.
        :param shootout_goals: The shootout_goals of this TeamSeason.
        :param short_handed_assists: The short_handed_assists of this TeamSeason.
        :param short_handed_goals: The short_handed_goals of this TeamSeason.
        :param shots_on_goal: The shots_on_goal of this TeamSeason.
        :param started: The started of this TeamSeason.
        :param stat_id: The stat_id of this TeamSeason.
        :param takeaways: The takeaways of this TeamSeason.
        :param team: The team of this TeamSeason.
        :param team_id: The team_id of this TeamSeason.
        :param updated: The updated of this TeamSeason.
        :param wins: The wins of this TeamSeason.
        """
        self.openapi_types = {
            'assists': float,
            'bench_penalty_minutes': float,
            'blocks': float,
            'empty_net_goals': float,
            'faceoffs_lost': float,
            'faceoffs_won': float,
            'fantasy_points': float,
            'fantasy_points_draft_kings': float,
            'fantasy_points_fan_duel': float,
            'fantasy_points_fantasy_draft': float,
            'fantasy_points_yahoo': float,
            'games': int,
            'giveaways': float,
            'global_team_id': int,
            'goals': float,
            'goaltending_goals_against': float,
            'goaltending_losses': float,
            'goaltending_minutes': int,
            'goaltending_overtime_losses': float,
            'goaltending_saves': float,
            'goaltending_seconds': int,
            'goaltending_shots_against': float,
            'goaltending_shutouts': float,
            'goaltending_wins': float,
            'hat_tricks': float,
            'hits': float,
            'losses': int,
            'minutes': int,
            'name': str,
            'opponent_position': str,
            'opponent_stat': OpponentSeason,
            'overtime_losses': int,
            'penalty_minutes': float,
            'plus_minus': float,
            'power_play_assists': float,
            'power_play_goals': float,
            'season': int,
            'season_type': int,
            'seconds': int,
            'shifts': float,
            'shootout_goals': float,
            'short_handed_assists': float,
            'short_handed_goals': float,
            'shots_on_goal': float,
            'started': int,
            'stat_id': int,
            'takeaways': float,
            'team': str,
            'team_id': int,
            'updated': str,
            'wins': int
        }

        self.attribute_map = {
            'assists': 'Assists',
            'bench_penalty_minutes': 'BenchPenaltyMinutes',
            'blocks': 'Blocks',
            'empty_net_goals': 'EmptyNetGoals',
            'faceoffs_lost': 'FaceoffsLost',
            'faceoffs_won': 'FaceoffsWon',
            'fantasy_points': 'FantasyPoints',
            'fantasy_points_draft_kings': 'FantasyPointsDraftKings',
            'fantasy_points_fan_duel': 'FantasyPointsFanDuel',
            'fantasy_points_fantasy_draft': 'FantasyPointsFantasyDraft',
            'fantasy_points_yahoo': 'FantasyPointsYahoo',
            'games': 'Games',
            'giveaways': 'Giveaways',
            'global_team_id': 'GlobalTeamID',
            'goals': 'Goals',
            'goaltending_goals_against': 'GoaltendingGoalsAgainst',
            'goaltending_losses': 'GoaltendingLosses',
            'goaltending_minutes': 'GoaltendingMinutes',
            'goaltending_overtime_losses': 'GoaltendingOvertimeLosses',
            'goaltending_saves': 'GoaltendingSaves',
            'goaltending_seconds': 'GoaltendingSeconds',
            'goaltending_shots_against': 'GoaltendingShotsAgainst',
            'goaltending_shutouts': 'GoaltendingShutouts',
            'goaltending_wins': 'GoaltendingWins',
            'hat_tricks': 'HatTricks',
            'hits': 'Hits',
            'losses': 'Losses',
            'minutes': 'Minutes',
            'name': 'Name',
            'opponent_position': 'OpponentPosition',
            'opponent_stat': 'OpponentStat',
            'overtime_losses': 'OvertimeLosses',
            'penalty_minutes': 'PenaltyMinutes',
            'plus_minus': 'PlusMinus',
            'power_play_assists': 'PowerPlayAssists',
            'power_play_goals': 'PowerPlayGoals',
            'season': 'Season',
            'season_type': 'SeasonType',
            'seconds': 'Seconds',
            'shifts': 'Shifts',
            'shootout_goals': 'ShootoutGoals',
            'short_handed_assists': 'ShortHandedAssists',
            'short_handed_goals': 'ShortHandedGoals',
            'shots_on_goal': 'ShotsOnGoal',
            'started': 'Started',
            'stat_id': 'StatID',
            'takeaways': 'Takeaways',
            'team': 'Team',
            'team_id': 'TeamID',
            'updated': 'Updated',
            'wins': 'Wins'
        }

        self._assists = assists
        self._bench_penalty_minutes = bench_penalty_minutes
        self._blocks = blocks
        self._empty_net_goals = empty_net_goals
        self._faceoffs_lost = faceoffs_lost
        self._faceoffs_won = faceoffs_won
        self._fantasy_points = fantasy_points
        self._fantasy_points_draft_kings = fantasy_points_draft_kings
        self._fantasy_points_fan_duel = fantasy_points_fan_duel
        self._fantasy_points_fantasy_draft = fantasy_points_fantasy_draft
        self._fantasy_points_yahoo = fantasy_points_yahoo
        self._games = games
        self._giveaways = giveaways
        self._global_team_id = global_team_id
        self._goals = goals
        self._goaltending_goals_against = goaltending_goals_against
        self._goaltending_losses = goaltending_losses
        self._goaltending_minutes = goaltending_minutes
        self._goaltending_overtime_losses = goaltending_overtime_losses
        self._goaltending_saves = goaltending_saves
        self._goaltending_seconds = goaltending_seconds
        self._goaltending_shots_against = goaltending_shots_against
        self._goaltending_shutouts = goaltending_shutouts
        self._goaltending_wins = goaltending_wins
        self._hat_tricks = hat_tricks
        self._hits = hits
        self._losses = losses
        self._minutes = minutes
        self._name = name
        self._opponent_position = opponent_position
        self._opponent_stat = opponent_stat
        self._overtime_losses = overtime_losses
        self._penalty_minutes = penalty_minutes
        self._plus_minus = plus_minus
        self._power_play_assists = power_play_assists
        self._power_play_goals = power_play_goals
        self._season = season
        self._season_type = season_type
        self._seconds = seconds
        self._shifts = shifts
        self._shootout_goals = shootout_goals
        self._short_handed_assists = short_handed_assists
        self._short_handed_goals = short_handed_goals
        self._shots_on_goal = shots_on_goal
        self._started = started
        self._stat_id = stat_id
        self._takeaways = takeaways
        self._team = team
        self._team_id = team_id
        self._updated = updated
        self._wins = wins

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamSeason':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TeamSeason of this TeamSeason.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assists(self):
        """Gets the assists of this TeamSeason.


        :return: The assists of this TeamSeason.
        :rtype: float
        """
        return self._assists

    @assists.setter
    def assists(self, assists):
        """Sets the assists of this TeamSeason.


        :param assists: The assists of this TeamSeason.
        :type assists: float
        """

        self._assists = assists

    @property
    def bench_penalty_minutes(self):
        """Gets the bench_penalty_minutes of this TeamSeason.


        :return: The bench_penalty_minutes of this TeamSeason.
        :rtype: float
        """
        return self._bench_penalty_minutes

    @bench_penalty_minutes.setter
    def bench_penalty_minutes(self, bench_penalty_minutes):
        """Sets the bench_penalty_minutes of this TeamSeason.


        :param bench_penalty_minutes: The bench_penalty_minutes of this TeamSeason.
        :type bench_penalty_minutes: float
        """

        self._bench_penalty_minutes = bench_penalty_minutes

    @property
    def blocks(self):
        """Gets the blocks of this TeamSeason.


        :return: The blocks of this TeamSeason.
        :rtype: float
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this TeamSeason.


        :param blocks: The blocks of this TeamSeason.
        :type blocks: float
        """

        self._blocks = blocks

    @property
    def empty_net_goals(self):
        """Gets the empty_net_goals of this TeamSeason.


        :return: The empty_net_goals of this TeamSeason.
        :rtype: float
        """
        return self._empty_net_goals

    @empty_net_goals.setter
    def empty_net_goals(self, empty_net_goals):
        """Sets the empty_net_goals of this TeamSeason.


        :param empty_net_goals: The empty_net_goals of this TeamSeason.
        :type empty_net_goals: float
        """

        self._empty_net_goals = empty_net_goals

    @property
    def faceoffs_lost(self):
        """Gets the faceoffs_lost of this TeamSeason.


        :return: The faceoffs_lost of this TeamSeason.
        :rtype: float
        """
        return self._faceoffs_lost

    @faceoffs_lost.setter
    def faceoffs_lost(self, faceoffs_lost):
        """Sets the faceoffs_lost of this TeamSeason.


        :param faceoffs_lost: The faceoffs_lost of this TeamSeason.
        :type faceoffs_lost: float
        """

        self._faceoffs_lost = faceoffs_lost

    @property
    def faceoffs_won(self):
        """Gets the faceoffs_won of this TeamSeason.


        :return: The faceoffs_won of this TeamSeason.
        :rtype: float
        """
        return self._faceoffs_won

    @faceoffs_won.setter
    def faceoffs_won(self, faceoffs_won):
        """Sets the faceoffs_won of this TeamSeason.


        :param faceoffs_won: The faceoffs_won of this TeamSeason.
        :type faceoffs_won: float
        """

        self._faceoffs_won = faceoffs_won

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this TeamSeason.


        :return: The fantasy_points of this TeamSeason.
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this TeamSeason.


        :param fantasy_points: The fantasy_points of this TeamSeason.
        :type fantasy_points: float
        """

        self._fantasy_points = fantasy_points

    @property
    def fantasy_points_draft_kings(self):
        """Gets the fantasy_points_draft_kings of this TeamSeason.


        :return: The fantasy_points_draft_kings of this TeamSeason.
        :rtype: float
        """
        return self._fantasy_points_draft_kings

    @fantasy_points_draft_kings.setter
    def fantasy_points_draft_kings(self, fantasy_points_draft_kings):
        """Sets the fantasy_points_draft_kings of this TeamSeason.


        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this TeamSeason.
        :type fantasy_points_draft_kings: float
        """

        self._fantasy_points_draft_kings = fantasy_points_draft_kings

    @property
    def fantasy_points_fan_duel(self):
        """Gets the fantasy_points_fan_duel of this TeamSeason.


        :return: The fantasy_points_fan_duel of this TeamSeason.
        :rtype: float
        """
        return self._fantasy_points_fan_duel

    @fantasy_points_fan_duel.setter
    def fantasy_points_fan_duel(self, fantasy_points_fan_duel):
        """Sets the fantasy_points_fan_duel of this TeamSeason.


        :param fantasy_points_fan_duel: The fantasy_points_fan_duel of this TeamSeason.
        :type fantasy_points_fan_duel: float
        """

        self._fantasy_points_fan_duel = fantasy_points_fan_duel

    @property
    def fantasy_points_fantasy_draft(self):
        """Gets the fantasy_points_fantasy_draft of this TeamSeason.


        :return: The fantasy_points_fantasy_draft of this TeamSeason.
        :rtype: float
        """
        return self._fantasy_points_fantasy_draft

    @fantasy_points_fantasy_draft.setter
    def fantasy_points_fantasy_draft(self, fantasy_points_fantasy_draft):
        """Sets the fantasy_points_fantasy_draft of this TeamSeason.


        :param fantasy_points_fantasy_draft: The fantasy_points_fantasy_draft of this TeamSeason.
        :type fantasy_points_fantasy_draft: float
        """

        self._fantasy_points_fantasy_draft = fantasy_points_fantasy_draft

    @property
    def fantasy_points_yahoo(self):
        """Gets the fantasy_points_yahoo of this TeamSeason.


        :return: The fantasy_points_yahoo of this TeamSeason.
        :rtype: float
        """
        return self._fantasy_points_yahoo

    @fantasy_points_yahoo.setter
    def fantasy_points_yahoo(self, fantasy_points_yahoo):
        """Sets the fantasy_points_yahoo of this TeamSeason.


        :param fantasy_points_yahoo: The fantasy_points_yahoo of this TeamSeason.
        :type fantasy_points_yahoo: float
        """

        self._fantasy_points_yahoo = fantasy_points_yahoo

    @property
    def games(self):
        """Gets the games of this TeamSeason.


        :return: The games of this TeamSeason.
        :rtype: int
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this TeamSeason.


        :param games: The games of this TeamSeason.
        :type games: int
        """

        self._games = games

    @property
    def giveaways(self):
        """Gets the giveaways of this TeamSeason.


        :return: The giveaways of this TeamSeason.
        :rtype: float
        """
        return self._giveaways

    @giveaways.setter
    def giveaways(self, giveaways):
        """Sets the giveaways of this TeamSeason.


        :param giveaways: The giveaways of this TeamSeason.
        :type giveaways: float
        """

        self._giveaways = giveaways

    @property
    def global_team_id(self):
        """Gets the global_team_id of this TeamSeason.


        :return: The global_team_id of this TeamSeason.
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this TeamSeason.


        :param global_team_id: The global_team_id of this TeamSeason.
        :type global_team_id: int
        """

        self._global_team_id = global_team_id

    @property
    def goals(self):
        """Gets the goals of this TeamSeason.


        :return: The goals of this TeamSeason.
        :rtype: float
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """Sets the goals of this TeamSeason.


        :param goals: The goals of this TeamSeason.
        :type goals: float
        """

        self._goals = goals

    @property
    def goaltending_goals_against(self):
        """Gets the goaltending_goals_against of this TeamSeason.


        :return: The goaltending_goals_against of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_goals_against

    @goaltending_goals_against.setter
    def goaltending_goals_against(self, goaltending_goals_against):
        """Sets the goaltending_goals_against of this TeamSeason.


        :param goaltending_goals_against: The goaltending_goals_against of this TeamSeason.
        :type goaltending_goals_against: float
        """

        self._goaltending_goals_against = goaltending_goals_against

    @property
    def goaltending_losses(self):
        """Gets the goaltending_losses of this TeamSeason.


        :return: The goaltending_losses of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_losses

    @goaltending_losses.setter
    def goaltending_losses(self, goaltending_losses):
        """Sets the goaltending_losses of this TeamSeason.


        :param goaltending_losses: The goaltending_losses of this TeamSeason.
        :type goaltending_losses: float
        """

        self._goaltending_losses = goaltending_losses

    @property
    def goaltending_minutes(self):
        """Gets the goaltending_minutes of this TeamSeason.


        :return: The goaltending_minutes of this TeamSeason.
        :rtype: int
        """
        return self._goaltending_minutes

    @goaltending_minutes.setter
    def goaltending_minutes(self, goaltending_minutes):
        """Sets the goaltending_minutes of this TeamSeason.


        :param goaltending_minutes: The goaltending_minutes of this TeamSeason.
        :type goaltending_minutes: int
        """

        self._goaltending_minutes = goaltending_minutes

    @property
    def goaltending_overtime_losses(self):
        """Gets the goaltending_overtime_losses of this TeamSeason.


        :return: The goaltending_overtime_losses of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_overtime_losses

    @goaltending_overtime_losses.setter
    def goaltending_overtime_losses(self, goaltending_overtime_losses):
        """Sets the goaltending_overtime_losses of this TeamSeason.


        :param goaltending_overtime_losses: The goaltending_overtime_losses of this TeamSeason.
        :type goaltending_overtime_losses: float
        """

        self._goaltending_overtime_losses = goaltending_overtime_losses

    @property
    def goaltending_saves(self):
        """Gets the goaltending_saves of this TeamSeason.


        :return: The goaltending_saves of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_saves

    @goaltending_saves.setter
    def goaltending_saves(self, goaltending_saves):
        """Sets the goaltending_saves of this TeamSeason.


        :param goaltending_saves: The goaltending_saves of this TeamSeason.
        :type goaltending_saves: float
        """

        self._goaltending_saves = goaltending_saves

    @property
    def goaltending_seconds(self):
        """Gets the goaltending_seconds of this TeamSeason.


        :return: The goaltending_seconds of this TeamSeason.
        :rtype: int
        """
        return self._goaltending_seconds

    @goaltending_seconds.setter
    def goaltending_seconds(self, goaltending_seconds):
        """Sets the goaltending_seconds of this TeamSeason.


        :param goaltending_seconds: The goaltending_seconds of this TeamSeason.
        :type goaltending_seconds: int
        """

        self._goaltending_seconds = goaltending_seconds

    @property
    def goaltending_shots_against(self):
        """Gets the goaltending_shots_against of this TeamSeason.


        :return: The goaltending_shots_against of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_shots_against

    @goaltending_shots_against.setter
    def goaltending_shots_against(self, goaltending_shots_against):
        """Sets the goaltending_shots_against of this TeamSeason.


        :param goaltending_shots_against: The goaltending_shots_against of this TeamSeason.
        :type goaltending_shots_against: float
        """

        self._goaltending_shots_against = goaltending_shots_against

    @property
    def goaltending_shutouts(self):
        """Gets the goaltending_shutouts of this TeamSeason.


        :return: The goaltending_shutouts of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_shutouts

    @goaltending_shutouts.setter
    def goaltending_shutouts(self, goaltending_shutouts):
        """Sets the goaltending_shutouts of this TeamSeason.


        :param goaltending_shutouts: The goaltending_shutouts of this TeamSeason.
        :type goaltending_shutouts: float
        """

        self._goaltending_shutouts = goaltending_shutouts

    @property
    def goaltending_wins(self):
        """Gets the goaltending_wins of this TeamSeason.


        :return: The goaltending_wins of this TeamSeason.
        :rtype: float
        """
        return self._goaltending_wins

    @goaltending_wins.setter
    def goaltending_wins(self, goaltending_wins):
        """Sets the goaltending_wins of this TeamSeason.


        :param goaltending_wins: The goaltending_wins of this TeamSeason.
        :type goaltending_wins: float
        """

        self._goaltending_wins = goaltending_wins

    @property
    def hat_tricks(self):
        """Gets the hat_tricks of this TeamSeason.


        :return: The hat_tricks of this TeamSeason.
        :rtype: float
        """
        return self._hat_tricks

    @hat_tricks.setter
    def hat_tricks(self, hat_tricks):
        """Sets the hat_tricks of this TeamSeason.


        :param hat_tricks: The hat_tricks of this TeamSeason.
        :type hat_tricks: float
        """

        self._hat_tricks = hat_tricks

    @property
    def hits(self):
        """Gets the hits of this TeamSeason.


        :return: The hits of this TeamSeason.
        :rtype: float
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this TeamSeason.


        :param hits: The hits of this TeamSeason.
        :type hits: float
        """

        self._hits = hits

    @property
    def losses(self):
        """Gets the losses of this TeamSeason.


        :return: The losses of this TeamSeason.
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this TeamSeason.


        :param losses: The losses of this TeamSeason.
        :type losses: int
        """

        self._losses = losses

    @property
    def minutes(self):
        """Gets the minutes of this TeamSeason.


        :return: The minutes of this TeamSeason.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this TeamSeason.


        :param minutes: The minutes of this TeamSeason.
        :type minutes: int
        """

        self._minutes = minutes

    @property
    def name(self):
        """Gets the name of this TeamSeason.


        :return: The name of this TeamSeason.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamSeason.


        :param name: The name of this TeamSeason.
        :type name: str
        """

        self._name = name

    @property
    def opponent_position(self):
        """Gets the opponent_position of this TeamSeason.


        :return: The opponent_position of this TeamSeason.
        :rtype: str
        """
        return self._opponent_position

    @opponent_position.setter
    def opponent_position(self, opponent_position):
        """Sets the opponent_position of this TeamSeason.


        :param opponent_position: The opponent_position of this TeamSeason.
        :type opponent_position: str
        """

        self._opponent_position = opponent_position

    @property
    def opponent_stat(self):
        """Gets the opponent_stat of this TeamSeason.


        :return: The opponent_stat of this TeamSeason.
        :rtype: OpponentSeason
        """
        return self._opponent_stat

    @opponent_stat.setter
    def opponent_stat(self, opponent_stat):
        """Sets the opponent_stat of this TeamSeason.


        :param opponent_stat: The opponent_stat of this TeamSeason.
        :type opponent_stat: OpponentSeason
        """

        self._opponent_stat = opponent_stat

    @property
    def overtime_losses(self):
        """Gets the overtime_losses of this TeamSeason.


        :return: The overtime_losses of this TeamSeason.
        :rtype: int
        """
        return self._overtime_losses

    @overtime_losses.setter
    def overtime_losses(self, overtime_losses):
        """Sets the overtime_losses of this TeamSeason.


        :param overtime_losses: The overtime_losses of this TeamSeason.
        :type overtime_losses: int
        """

        self._overtime_losses = overtime_losses

    @property
    def penalty_minutes(self):
        """Gets the penalty_minutes of this TeamSeason.


        :return: The penalty_minutes of this TeamSeason.
        :rtype: float
        """
        return self._penalty_minutes

    @penalty_minutes.setter
    def penalty_minutes(self, penalty_minutes):
        """Sets the penalty_minutes of this TeamSeason.


        :param penalty_minutes: The penalty_minutes of this TeamSeason.
        :type penalty_minutes: float
        """

        self._penalty_minutes = penalty_minutes

    @property
    def plus_minus(self):
        """Gets the plus_minus of this TeamSeason.


        :return: The plus_minus of this TeamSeason.
        :rtype: float
        """
        return self._plus_minus

    @plus_minus.setter
    def plus_minus(self, plus_minus):
        """Sets the plus_minus of this TeamSeason.


        :param plus_minus: The plus_minus of this TeamSeason.
        :type plus_minus: float
        """

        self._plus_minus = plus_minus

    @property
    def power_play_assists(self):
        """Gets the power_play_assists of this TeamSeason.


        :return: The power_play_assists of this TeamSeason.
        :rtype: float
        """
        return self._power_play_assists

    @power_play_assists.setter
    def power_play_assists(self, power_play_assists):
        """Sets the power_play_assists of this TeamSeason.


        :param power_play_assists: The power_play_assists of this TeamSeason.
        :type power_play_assists: float
        """

        self._power_play_assists = power_play_assists

    @property
    def power_play_goals(self):
        """Gets the power_play_goals of this TeamSeason.


        :return: The power_play_goals of this TeamSeason.
        :rtype: float
        """
        return self._power_play_goals

    @power_play_goals.setter
    def power_play_goals(self, power_play_goals):
        """Sets the power_play_goals of this TeamSeason.


        :param power_play_goals: The power_play_goals of this TeamSeason.
        :type power_play_goals: float
        """

        self._power_play_goals = power_play_goals

    @property
    def season(self):
        """Gets the season of this TeamSeason.


        :return: The season of this TeamSeason.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this TeamSeason.


        :param season: The season of this TeamSeason.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this TeamSeason.


        :return: The season_type of this TeamSeason.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this TeamSeason.


        :param season_type: The season_type of this TeamSeason.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def seconds(self):
        """Gets the seconds of this TeamSeason.


        :return: The seconds of this TeamSeason.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this TeamSeason.


        :param seconds: The seconds of this TeamSeason.
        :type seconds: int
        """

        self._seconds = seconds

    @property
    def shifts(self):
        """Gets the shifts of this TeamSeason.


        :return: The shifts of this TeamSeason.
        :rtype: float
        """
        return self._shifts

    @shifts.setter
    def shifts(self, shifts):
        """Sets the shifts of this TeamSeason.


        :param shifts: The shifts of this TeamSeason.
        :type shifts: float
        """

        self._shifts = shifts

    @property
    def shootout_goals(self):
        """Gets the shootout_goals of this TeamSeason.


        :return: The shootout_goals of this TeamSeason.
        :rtype: float
        """
        return self._shootout_goals

    @shootout_goals.setter
    def shootout_goals(self, shootout_goals):
        """Sets the shootout_goals of this TeamSeason.


        :param shootout_goals: The shootout_goals of this TeamSeason.
        :type shootout_goals: float
        """

        self._shootout_goals = shootout_goals

    @property
    def short_handed_assists(self):
        """Gets the short_handed_assists of this TeamSeason.


        :return: The short_handed_assists of this TeamSeason.
        :rtype: float
        """
        return self._short_handed_assists

    @short_handed_assists.setter
    def short_handed_assists(self, short_handed_assists):
        """Sets the short_handed_assists of this TeamSeason.


        :param short_handed_assists: The short_handed_assists of this TeamSeason.
        :type short_handed_assists: float
        """

        self._short_handed_assists = short_handed_assists

    @property
    def short_handed_goals(self):
        """Gets the short_handed_goals of this TeamSeason.


        :return: The short_handed_goals of this TeamSeason.
        :rtype: float
        """
        return self._short_handed_goals

    @short_handed_goals.setter
    def short_handed_goals(self, short_handed_goals):
        """Sets the short_handed_goals of this TeamSeason.


        :param short_handed_goals: The short_handed_goals of this TeamSeason.
        :type short_handed_goals: float
        """

        self._short_handed_goals = short_handed_goals

    @property
    def shots_on_goal(self):
        """Gets the shots_on_goal of this TeamSeason.


        :return: The shots_on_goal of this TeamSeason.
        :rtype: float
        """
        return self._shots_on_goal

    @shots_on_goal.setter
    def shots_on_goal(self, shots_on_goal):
        """Sets the shots_on_goal of this TeamSeason.


        :param shots_on_goal: The shots_on_goal of this TeamSeason.
        :type shots_on_goal: float
        """

        self._shots_on_goal = shots_on_goal

    @property
    def started(self):
        """Gets the started of this TeamSeason.


        :return: The started of this TeamSeason.
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this TeamSeason.


        :param started: The started of this TeamSeason.
        :type started: int
        """

        self._started = started

    @property
    def stat_id(self):
        """Gets the stat_id of this TeamSeason.


        :return: The stat_id of this TeamSeason.
        :rtype: int
        """
        return self._stat_id

    @stat_id.setter
    def stat_id(self, stat_id):
        """Sets the stat_id of this TeamSeason.


        :param stat_id: The stat_id of this TeamSeason.
        :type stat_id: int
        """

        self._stat_id = stat_id

    @property
    def takeaways(self):
        """Gets the takeaways of this TeamSeason.


        :return: The takeaways of this TeamSeason.
        :rtype: float
        """
        return self._takeaways

    @takeaways.setter
    def takeaways(self, takeaways):
        """Sets the takeaways of this TeamSeason.


        :param takeaways: The takeaways of this TeamSeason.
        :type takeaways: float
        """

        self._takeaways = takeaways

    @property
    def team(self):
        """Gets the team of this TeamSeason.


        :return: The team of this TeamSeason.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamSeason.


        :param team: The team of this TeamSeason.
        :type team: str
        """

        self._team = team

    @property
    def team_id(self):
        """Gets the team_id of this TeamSeason.


        :return: The team_id of this TeamSeason.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamSeason.


        :param team_id: The team_id of this TeamSeason.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def updated(self):
        """Gets the updated of this TeamSeason.


        :return: The updated of this TeamSeason.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TeamSeason.


        :param updated: The updated of this TeamSeason.
        :type updated: str
        """

        self._updated = updated

    @property
    def wins(self):
        """Gets the wins of this TeamSeason.


        :return: The wins of this TeamSeason.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this TeamSeason.


        :param wins: The wins of this TeamSeason.
        :type wins: int
        """

        self._wins = wins
