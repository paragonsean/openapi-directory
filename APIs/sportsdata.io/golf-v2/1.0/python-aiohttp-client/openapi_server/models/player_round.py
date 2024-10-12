# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.player_hole import PlayerHole
from openapi_server import util


class PlayerRound(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, back_nine_start: bool=None, birdies: int=None, bogey_free: bool=None, bogeys: int=None, bounce_back_count: float=None, consecutive_birdie_or_better_count: float=None, day: str=None, double_bogeys: int=None, double_eagles: int=None, eagles: int=None, hole_in_ones: int=None, holes: List[PlayerHole]=None, includes_five_or_more_birdies_or_better: bool=None, includes_streak_of_five_birdies_or_better: bool=None, includes_streak_of_four_birdies_or_better: bool=None, includes_streak_of_six_birdies_or_better: bool=None, includes_streak_of_three_birdies_or_better: bool=None, longest_birdie_or_better_streak: float=None, number: int=None, par: int=None, pars: int=None, player_round_id: int=None, player_tournament_id: int=None, score: int=None, tee_time: str=None, triple_bogeys: int=None, worse_than_double_bogey: int=None, worse_than_triple_bogey: int=None):
        """PlayerRound - a model defined in OpenAPI

        :param back_nine_start: The back_nine_start of this PlayerRound.
        :param birdies: The birdies of this PlayerRound.
        :param bogey_free: The bogey_free of this PlayerRound.
        :param bogeys: The bogeys of this PlayerRound.
        :param bounce_back_count: The bounce_back_count of this PlayerRound.
        :param consecutive_birdie_or_better_count: The consecutive_birdie_or_better_count of this PlayerRound.
        :param day: The day of this PlayerRound.
        :param double_bogeys: The double_bogeys of this PlayerRound.
        :param double_eagles: The double_eagles of this PlayerRound.
        :param eagles: The eagles of this PlayerRound.
        :param hole_in_ones: The hole_in_ones of this PlayerRound.
        :param holes: The holes of this PlayerRound.
        :param includes_five_or_more_birdies_or_better: The includes_five_or_more_birdies_or_better of this PlayerRound.
        :param includes_streak_of_five_birdies_or_better: The includes_streak_of_five_birdies_or_better of this PlayerRound.
        :param includes_streak_of_four_birdies_or_better: The includes_streak_of_four_birdies_or_better of this PlayerRound.
        :param includes_streak_of_six_birdies_or_better: The includes_streak_of_six_birdies_or_better of this PlayerRound.
        :param includes_streak_of_three_birdies_or_better: The includes_streak_of_three_birdies_or_better of this PlayerRound.
        :param longest_birdie_or_better_streak: The longest_birdie_or_better_streak of this PlayerRound.
        :param number: The number of this PlayerRound.
        :param par: The par of this PlayerRound.
        :param pars: The pars of this PlayerRound.
        :param player_round_id: The player_round_id of this PlayerRound.
        :param player_tournament_id: The player_tournament_id of this PlayerRound.
        :param score: The score of this PlayerRound.
        :param tee_time: The tee_time of this PlayerRound.
        :param triple_bogeys: The triple_bogeys of this PlayerRound.
        :param worse_than_double_bogey: The worse_than_double_bogey of this PlayerRound.
        :param worse_than_triple_bogey: The worse_than_triple_bogey of this PlayerRound.
        """
        self.openapi_types = {
            'back_nine_start': bool,
            'birdies': int,
            'bogey_free': bool,
            'bogeys': int,
            'bounce_back_count': float,
            'consecutive_birdie_or_better_count': float,
            'day': str,
            'double_bogeys': int,
            'double_eagles': int,
            'eagles': int,
            'hole_in_ones': int,
            'holes': List[PlayerHole],
            'includes_five_or_more_birdies_or_better': bool,
            'includes_streak_of_five_birdies_or_better': bool,
            'includes_streak_of_four_birdies_or_better': bool,
            'includes_streak_of_six_birdies_or_better': bool,
            'includes_streak_of_three_birdies_or_better': bool,
            'longest_birdie_or_better_streak': float,
            'number': int,
            'par': int,
            'pars': int,
            'player_round_id': int,
            'player_tournament_id': int,
            'score': int,
            'tee_time': str,
            'triple_bogeys': int,
            'worse_than_double_bogey': int,
            'worse_than_triple_bogey': int
        }

        self.attribute_map = {
            'back_nine_start': 'BackNineStart',
            'birdies': 'Birdies',
            'bogey_free': 'BogeyFree',
            'bogeys': 'Bogeys',
            'bounce_back_count': 'BounceBackCount',
            'consecutive_birdie_or_better_count': 'ConsecutiveBirdieOrBetterCount',
            'day': 'Day',
            'double_bogeys': 'DoubleBogeys',
            'double_eagles': 'DoubleEagles',
            'eagles': 'Eagles',
            'hole_in_ones': 'HoleInOnes',
            'holes': 'Holes',
            'includes_five_or_more_birdies_or_better': 'IncludesFiveOrMoreBirdiesOrBetter',
            'includes_streak_of_five_birdies_or_better': 'IncludesStreakOfFiveBirdiesOrBetter',
            'includes_streak_of_four_birdies_or_better': 'IncludesStreakOfFourBirdiesOrBetter',
            'includes_streak_of_six_birdies_or_better': 'IncludesStreakOfSixBirdiesOrBetter',
            'includes_streak_of_three_birdies_or_better': 'IncludesStreakOfThreeBirdiesOrBetter',
            'longest_birdie_or_better_streak': 'LongestBirdieOrBetterStreak',
            'number': 'Number',
            'par': 'Par',
            'pars': 'Pars',
            'player_round_id': 'PlayerRoundID',
            'player_tournament_id': 'PlayerTournamentID',
            'score': 'Score',
            'tee_time': 'TeeTime',
            'triple_bogeys': 'TripleBogeys',
            'worse_than_double_bogey': 'WorseThanDoubleBogey',
            'worse_than_triple_bogey': 'WorseThanTripleBogey'
        }

        self._back_nine_start = back_nine_start
        self._birdies = birdies
        self._bogey_free = bogey_free
        self._bogeys = bogeys
        self._bounce_back_count = bounce_back_count
        self._consecutive_birdie_or_better_count = consecutive_birdie_or_better_count
        self._day = day
        self._double_bogeys = double_bogeys
        self._double_eagles = double_eagles
        self._eagles = eagles
        self._hole_in_ones = hole_in_ones
        self._holes = holes
        self._includes_five_or_more_birdies_or_better = includes_five_or_more_birdies_or_better
        self._includes_streak_of_five_birdies_or_better = includes_streak_of_five_birdies_or_better
        self._includes_streak_of_four_birdies_or_better = includes_streak_of_four_birdies_or_better
        self._includes_streak_of_six_birdies_or_better = includes_streak_of_six_birdies_or_better
        self._includes_streak_of_three_birdies_or_better = includes_streak_of_three_birdies_or_better
        self._longest_birdie_or_better_streak = longest_birdie_or_better_streak
        self._number = number
        self._par = par
        self._pars = pars
        self._player_round_id = player_round_id
        self._player_tournament_id = player_tournament_id
        self._score = score
        self._tee_time = tee_time
        self._triple_bogeys = triple_bogeys
        self._worse_than_double_bogey = worse_than_double_bogey
        self._worse_than_triple_bogey = worse_than_triple_bogey

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PlayerRound':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PlayerRound of this PlayerRound.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def back_nine_start(self):
        """Gets the back_nine_start of this PlayerRound.


        :return: The back_nine_start of this PlayerRound.
        :rtype: bool
        """
        return self._back_nine_start

    @back_nine_start.setter
    def back_nine_start(self, back_nine_start):
        """Sets the back_nine_start of this PlayerRound.


        :param back_nine_start: The back_nine_start of this PlayerRound.
        :type back_nine_start: bool
        """

        self._back_nine_start = back_nine_start

    @property
    def birdies(self):
        """Gets the birdies of this PlayerRound.


        :return: The birdies of this PlayerRound.
        :rtype: int
        """
        return self._birdies

    @birdies.setter
    def birdies(self, birdies):
        """Sets the birdies of this PlayerRound.


        :param birdies: The birdies of this PlayerRound.
        :type birdies: int
        """

        self._birdies = birdies

    @property
    def bogey_free(self):
        """Gets the bogey_free of this PlayerRound.


        :return: The bogey_free of this PlayerRound.
        :rtype: bool
        """
        return self._bogey_free

    @bogey_free.setter
    def bogey_free(self, bogey_free):
        """Sets the bogey_free of this PlayerRound.


        :param bogey_free: The bogey_free of this PlayerRound.
        :type bogey_free: bool
        """

        self._bogey_free = bogey_free

    @property
    def bogeys(self):
        """Gets the bogeys of this PlayerRound.


        :return: The bogeys of this PlayerRound.
        :rtype: int
        """
        return self._bogeys

    @bogeys.setter
    def bogeys(self, bogeys):
        """Sets the bogeys of this PlayerRound.


        :param bogeys: The bogeys of this PlayerRound.
        :type bogeys: int
        """

        self._bogeys = bogeys

    @property
    def bounce_back_count(self):
        """Gets the bounce_back_count of this PlayerRound.


        :return: The bounce_back_count of this PlayerRound.
        :rtype: float
        """
        return self._bounce_back_count

    @bounce_back_count.setter
    def bounce_back_count(self, bounce_back_count):
        """Sets the bounce_back_count of this PlayerRound.


        :param bounce_back_count: The bounce_back_count of this PlayerRound.
        :type bounce_back_count: float
        """

        self._bounce_back_count = bounce_back_count

    @property
    def consecutive_birdie_or_better_count(self):
        """Gets the consecutive_birdie_or_better_count of this PlayerRound.


        :return: The consecutive_birdie_or_better_count of this PlayerRound.
        :rtype: float
        """
        return self._consecutive_birdie_or_better_count

    @consecutive_birdie_or_better_count.setter
    def consecutive_birdie_or_better_count(self, consecutive_birdie_or_better_count):
        """Sets the consecutive_birdie_or_better_count of this PlayerRound.


        :param consecutive_birdie_or_better_count: The consecutive_birdie_or_better_count of this PlayerRound.
        :type consecutive_birdie_or_better_count: float
        """

        self._consecutive_birdie_or_better_count = consecutive_birdie_or_better_count

    @property
    def day(self):
        """Gets the day of this PlayerRound.


        :return: The day of this PlayerRound.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this PlayerRound.


        :param day: The day of this PlayerRound.
        :type day: str
        """

        self._day = day

    @property
    def double_bogeys(self):
        """Gets the double_bogeys of this PlayerRound.


        :return: The double_bogeys of this PlayerRound.
        :rtype: int
        """
        return self._double_bogeys

    @double_bogeys.setter
    def double_bogeys(self, double_bogeys):
        """Sets the double_bogeys of this PlayerRound.


        :param double_bogeys: The double_bogeys of this PlayerRound.
        :type double_bogeys: int
        """

        self._double_bogeys = double_bogeys

    @property
    def double_eagles(self):
        """Gets the double_eagles of this PlayerRound.


        :return: The double_eagles of this PlayerRound.
        :rtype: int
        """
        return self._double_eagles

    @double_eagles.setter
    def double_eagles(self, double_eagles):
        """Sets the double_eagles of this PlayerRound.


        :param double_eagles: The double_eagles of this PlayerRound.
        :type double_eagles: int
        """

        self._double_eagles = double_eagles

    @property
    def eagles(self):
        """Gets the eagles of this PlayerRound.


        :return: The eagles of this PlayerRound.
        :rtype: int
        """
        return self._eagles

    @eagles.setter
    def eagles(self, eagles):
        """Sets the eagles of this PlayerRound.


        :param eagles: The eagles of this PlayerRound.
        :type eagles: int
        """

        self._eagles = eagles

    @property
    def hole_in_ones(self):
        """Gets the hole_in_ones of this PlayerRound.


        :return: The hole_in_ones of this PlayerRound.
        :rtype: int
        """
        return self._hole_in_ones

    @hole_in_ones.setter
    def hole_in_ones(self, hole_in_ones):
        """Sets the hole_in_ones of this PlayerRound.


        :param hole_in_ones: The hole_in_ones of this PlayerRound.
        :type hole_in_ones: int
        """

        self._hole_in_ones = hole_in_ones

    @property
    def holes(self):
        """Gets the holes of this PlayerRound.


        :return: The holes of this PlayerRound.
        :rtype: List[PlayerHole]
        """
        return self._holes

    @holes.setter
    def holes(self, holes):
        """Sets the holes of this PlayerRound.


        :param holes: The holes of this PlayerRound.
        :type holes: List[PlayerHole]
        """

        self._holes = holes

    @property
    def includes_five_or_more_birdies_or_better(self):
        """Gets the includes_five_or_more_birdies_or_better of this PlayerRound.


        :return: The includes_five_or_more_birdies_or_better of this PlayerRound.
        :rtype: bool
        """
        return self._includes_five_or_more_birdies_or_better

    @includes_five_or_more_birdies_or_better.setter
    def includes_five_or_more_birdies_or_better(self, includes_five_or_more_birdies_or_better):
        """Sets the includes_five_or_more_birdies_or_better of this PlayerRound.


        :param includes_five_or_more_birdies_or_better: The includes_five_or_more_birdies_or_better of this PlayerRound.
        :type includes_five_or_more_birdies_or_better: bool
        """

        self._includes_five_or_more_birdies_or_better = includes_five_or_more_birdies_or_better

    @property
    def includes_streak_of_five_birdies_or_better(self):
        """Gets the includes_streak_of_five_birdies_or_better of this PlayerRound.


        :return: The includes_streak_of_five_birdies_or_better of this PlayerRound.
        :rtype: bool
        """
        return self._includes_streak_of_five_birdies_or_better

    @includes_streak_of_five_birdies_or_better.setter
    def includes_streak_of_five_birdies_or_better(self, includes_streak_of_five_birdies_or_better):
        """Sets the includes_streak_of_five_birdies_or_better of this PlayerRound.


        :param includes_streak_of_five_birdies_or_better: The includes_streak_of_five_birdies_or_better of this PlayerRound.
        :type includes_streak_of_five_birdies_or_better: bool
        """

        self._includes_streak_of_five_birdies_or_better = includes_streak_of_five_birdies_or_better

    @property
    def includes_streak_of_four_birdies_or_better(self):
        """Gets the includes_streak_of_four_birdies_or_better of this PlayerRound.


        :return: The includes_streak_of_four_birdies_or_better of this PlayerRound.
        :rtype: bool
        """
        return self._includes_streak_of_four_birdies_or_better

    @includes_streak_of_four_birdies_or_better.setter
    def includes_streak_of_four_birdies_or_better(self, includes_streak_of_four_birdies_or_better):
        """Sets the includes_streak_of_four_birdies_or_better of this PlayerRound.


        :param includes_streak_of_four_birdies_or_better: The includes_streak_of_four_birdies_or_better of this PlayerRound.
        :type includes_streak_of_four_birdies_or_better: bool
        """

        self._includes_streak_of_four_birdies_or_better = includes_streak_of_four_birdies_or_better

    @property
    def includes_streak_of_six_birdies_or_better(self):
        """Gets the includes_streak_of_six_birdies_or_better of this PlayerRound.


        :return: The includes_streak_of_six_birdies_or_better of this PlayerRound.
        :rtype: bool
        """
        return self._includes_streak_of_six_birdies_or_better

    @includes_streak_of_six_birdies_or_better.setter
    def includes_streak_of_six_birdies_or_better(self, includes_streak_of_six_birdies_or_better):
        """Sets the includes_streak_of_six_birdies_or_better of this PlayerRound.


        :param includes_streak_of_six_birdies_or_better: The includes_streak_of_six_birdies_or_better of this PlayerRound.
        :type includes_streak_of_six_birdies_or_better: bool
        """

        self._includes_streak_of_six_birdies_or_better = includes_streak_of_six_birdies_or_better

    @property
    def includes_streak_of_three_birdies_or_better(self):
        """Gets the includes_streak_of_three_birdies_or_better of this PlayerRound.


        :return: The includes_streak_of_three_birdies_or_better of this PlayerRound.
        :rtype: bool
        """
        return self._includes_streak_of_three_birdies_or_better

    @includes_streak_of_three_birdies_or_better.setter
    def includes_streak_of_three_birdies_or_better(self, includes_streak_of_three_birdies_or_better):
        """Sets the includes_streak_of_three_birdies_or_better of this PlayerRound.


        :param includes_streak_of_three_birdies_or_better: The includes_streak_of_three_birdies_or_better of this PlayerRound.
        :type includes_streak_of_three_birdies_or_better: bool
        """

        self._includes_streak_of_three_birdies_or_better = includes_streak_of_three_birdies_or_better

    @property
    def longest_birdie_or_better_streak(self):
        """Gets the longest_birdie_or_better_streak of this PlayerRound.


        :return: The longest_birdie_or_better_streak of this PlayerRound.
        :rtype: float
        """
        return self._longest_birdie_or_better_streak

    @longest_birdie_or_better_streak.setter
    def longest_birdie_or_better_streak(self, longest_birdie_or_better_streak):
        """Sets the longest_birdie_or_better_streak of this PlayerRound.


        :param longest_birdie_or_better_streak: The longest_birdie_or_better_streak of this PlayerRound.
        :type longest_birdie_or_better_streak: float
        """

        self._longest_birdie_or_better_streak = longest_birdie_or_better_streak

    @property
    def number(self):
        """Gets the number of this PlayerRound.


        :return: The number of this PlayerRound.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PlayerRound.


        :param number: The number of this PlayerRound.
        :type number: int
        """

        self._number = number

    @property
    def par(self):
        """Gets the par of this PlayerRound.


        :return: The par of this PlayerRound.
        :rtype: int
        """
        return self._par

    @par.setter
    def par(self, par):
        """Sets the par of this PlayerRound.


        :param par: The par of this PlayerRound.
        :type par: int
        """

        self._par = par

    @property
    def pars(self):
        """Gets the pars of this PlayerRound.


        :return: The pars of this PlayerRound.
        :rtype: int
        """
        return self._pars

    @pars.setter
    def pars(self, pars):
        """Sets the pars of this PlayerRound.


        :param pars: The pars of this PlayerRound.
        :type pars: int
        """

        self._pars = pars

    @property
    def player_round_id(self):
        """Gets the player_round_id of this PlayerRound.


        :return: The player_round_id of this PlayerRound.
        :rtype: int
        """
        return self._player_round_id

    @player_round_id.setter
    def player_round_id(self, player_round_id):
        """Sets the player_round_id of this PlayerRound.


        :param player_round_id: The player_round_id of this PlayerRound.
        :type player_round_id: int
        """

        self._player_round_id = player_round_id

    @property
    def player_tournament_id(self):
        """Gets the player_tournament_id of this PlayerRound.


        :return: The player_tournament_id of this PlayerRound.
        :rtype: int
        """
        return self._player_tournament_id

    @player_tournament_id.setter
    def player_tournament_id(self, player_tournament_id):
        """Sets the player_tournament_id of this PlayerRound.


        :param player_tournament_id: The player_tournament_id of this PlayerRound.
        :type player_tournament_id: int
        """

        self._player_tournament_id = player_tournament_id

    @property
    def score(self):
        """Gets the score of this PlayerRound.


        :return: The score of this PlayerRound.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PlayerRound.


        :param score: The score of this PlayerRound.
        :type score: int
        """

        self._score = score

    @property
    def tee_time(self):
        """Gets the tee_time of this PlayerRound.


        :return: The tee_time of this PlayerRound.
        :rtype: str
        """
        return self._tee_time

    @tee_time.setter
    def tee_time(self, tee_time):
        """Sets the tee_time of this PlayerRound.


        :param tee_time: The tee_time of this PlayerRound.
        :type tee_time: str
        """

        self._tee_time = tee_time

    @property
    def triple_bogeys(self):
        """Gets the triple_bogeys of this PlayerRound.


        :return: The triple_bogeys of this PlayerRound.
        :rtype: int
        """
        return self._triple_bogeys

    @triple_bogeys.setter
    def triple_bogeys(self, triple_bogeys):
        """Sets the triple_bogeys of this PlayerRound.


        :param triple_bogeys: The triple_bogeys of this PlayerRound.
        :type triple_bogeys: int
        """

        self._triple_bogeys = triple_bogeys

    @property
    def worse_than_double_bogey(self):
        """Gets the worse_than_double_bogey of this PlayerRound.


        :return: The worse_than_double_bogey of this PlayerRound.
        :rtype: int
        """
        return self._worse_than_double_bogey

    @worse_than_double_bogey.setter
    def worse_than_double_bogey(self, worse_than_double_bogey):
        """Sets the worse_than_double_bogey of this PlayerRound.


        :param worse_than_double_bogey: The worse_than_double_bogey of this PlayerRound.
        :type worse_than_double_bogey: int
        """

        self._worse_than_double_bogey = worse_than_double_bogey

    @property
    def worse_than_triple_bogey(self):
        """Gets the worse_than_triple_bogey of this PlayerRound.


        :return: The worse_than_triple_bogey of this PlayerRound.
        :rtype: int
        """
        return self._worse_than_triple_bogey

    @worse_than_triple_bogey.setter
    def worse_than_triple_bogey(self, worse_than_triple_bogey):
        """Sets the worse_than_triple_bogey of this PlayerRound.


        :param worse_than_triple_bogey: The worse_than_triple_bogey of this PlayerRound.
        :type worse_than_triple_bogey: int
        """

        self._worse_than_triple_bogey = worse_than_triple_bogey
