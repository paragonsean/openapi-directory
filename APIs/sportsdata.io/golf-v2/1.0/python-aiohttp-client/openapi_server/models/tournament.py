# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.round import Round
from openapi_server import util


class Tournament(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, canceled: bool=None, city: str=None, country: str=None, covered: bool=None, end_date: str=None, format: str=None, is_in_progress: bool=None, is_over: bool=None, location: str=None, name: str=None, odds_coverage: str=None, par: int=None, purse: float=None, rounds: List[Round]=None, sport_radar_tournament_id: str=None, start_date: str=None, start_date_time: str=None, state: str=None, time_zone: str=None, tournament_id: int=None, venue: str=None, yards: int=None, zip_code: str=None):
        """Tournament - a model defined in OpenAPI

        :param canceled: The canceled of this Tournament.
        :param city: The city of this Tournament.
        :param country: The country of this Tournament.
        :param covered: The covered of this Tournament.
        :param end_date: The end_date of this Tournament.
        :param format: The format of this Tournament.
        :param is_in_progress: The is_in_progress of this Tournament.
        :param is_over: The is_over of this Tournament.
        :param location: The location of this Tournament.
        :param name: The name of this Tournament.
        :param odds_coverage: The odds_coverage of this Tournament.
        :param par: The par of this Tournament.
        :param purse: The purse of this Tournament.
        :param rounds: The rounds of this Tournament.
        :param sport_radar_tournament_id: The sport_radar_tournament_id of this Tournament.
        :param start_date: The start_date of this Tournament.
        :param start_date_time: The start_date_time of this Tournament.
        :param state: The state of this Tournament.
        :param time_zone: The time_zone of this Tournament.
        :param tournament_id: The tournament_id of this Tournament.
        :param venue: The venue of this Tournament.
        :param yards: The yards of this Tournament.
        :param zip_code: The zip_code of this Tournament.
        """
        self.openapi_types = {
            'canceled': bool,
            'city': str,
            'country': str,
            'covered': bool,
            'end_date': str,
            'format': str,
            'is_in_progress': bool,
            'is_over': bool,
            'location': str,
            'name': str,
            'odds_coverage': str,
            'par': int,
            'purse': float,
            'rounds': List[Round],
            'sport_radar_tournament_id': str,
            'start_date': str,
            'start_date_time': str,
            'state': str,
            'time_zone': str,
            'tournament_id': int,
            'venue': str,
            'yards': int,
            'zip_code': str
        }

        self.attribute_map = {
            'canceled': 'Canceled',
            'city': 'City',
            'country': 'Country',
            'covered': 'Covered',
            'end_date': 'EndDate',
            'format': 'Format',
            'is_in_progress': 'IsInProgress',
            'is_over': 'IsOver',
            'location': 'Location',
            'name': 'Name',
            'odds_coverage': 'OddsCoverage',
            'par': 'Par',
            'purse': 'Purse',
            'rounds': 'Rounds',
            'sport_radar_tournament_id': 'SportRadarTournamentID',
            'start_date': 'StartDate',
            'start_date_time': 'StartDateTime',
            'state': 'State',
            'time_zone': 'TimeZone',
            'tournament_id': 'TournamentID',
            'venue': 'Venue',
            'yards': 'Yards',
            'zip_code': 'ZipCode'
        }

        self._canceled = canceled
        self._city = city
        self._country = country
        self._covered = covered
        self._end_date = end_date
        self._format = format
        self._is_in_progress = is_in_progress
        self._is_over = is_over
        self._location = location
        self._name = name
        self._odds_coverage = odds_coverage
        self._par = par
        self._purse = purse
        self._rounds = rounds
        self._sport_radar_tournament_id = sport_radar_tournament_id
        self._start_date = start_date
        self._start_date_time = start_date_time
        self._state = state
        self._time_zone = time_zone
        self._tournament_id = tournament_id
        self._venue = venue
        self._yards = yards
        self._zip_code = zip_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Tournament':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Tournament of this Tournament.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def canceled(self):
        """Gets the canceled of this Tournament.


        :return: The canceled of this Tournament.
        :rtype: bool
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this Tournament.


        :param canceled: The canceled of this Tournament.
        :type canceled: bool
        """

        self._canceled = canceled

    @property
    def city(self):
        """Gets the city of this Tournament.


        :return: The city of this Tournament.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Tournament.


        :param city: The city of this Tournament.
        :type city: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Tournament.


        :return: The country of this Tournament.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Tournament.


        :param country: The country of this Tournament.
        :type country: str
        """

        self._country = country

    @property
    def covered(self):
        """Gets the covered of this Tournament.


        :return: The covered of this Tournament.
        :rtype: bool
        """
        return self._covered

    @covered.setter
    def covered(self, covered):
        """Sets the covered of this Tournament.


        :param covered: The covered of this Tournament.
        :type covered: bool
        """

        self._covered = covered

    @property
    def end_date(self):
        """Gets the end_date of this Tournament.


        :return: The end_date of this Tournament.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Tournament.


        :param end_date: The end_date of this Tournament.
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def format(self):
        """Gets the format of this Tournament.


        :return: The format of this Tournament.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Tournament.


        :param format: The format of this Tournament.
        :type format: str
        """

        self._format = format

    @property
    def is_in_progress(self):
        """Gets the is_in_progress of this Tournament.


        :return: The is_in_progress of this Tournament.
        :rtype: bool
        """
        return self._is_in_progress

    @is_in_progress.setter
    def is_in_progress(self, is_in_progress):
        """Sets the is_in_progress of this Tournament.


        :param is_in_progress: The is_in_progress of this Tournament.
        :type is_in_progress: bool
        """

        self._is_in_progress = is_in_progress

    @property
    def is_over(self):
        """Gets the is_over of this Tournament.


        :return: The is_over of this Tournament.
        :rtype: bool
        """
        return self._is_over

    @is_over.setter
    def is_over(self, is_over):
        """Sets the is_over of this Tournament.


        :param is_over: The is_over of this Tournament.
        :type is_over: bool
        """

        self._is_over = is_over

    @property
    def location(self):
        """Gets the location of this Tournament.


        :return: The location of this Tournament.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Tournament.


        :param location: The location of this Tournament.
        :type location: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this Tournament.


        :return: The name of this Tournament.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tournament.


        :param name: The name of this Tournament.
        :type name: str
        """

        self._name = name

    @property
    def odds_coverage(self):
        """Gets the odds_coverage of this Tournament.


        :return: The odds_coverage of this Tournament.
        :rtype: str
        """
        return self._odds_coverage

    @odds_coverage.setter
    def odds_coverage(self, odds_coverage):
        """Sets the odds_coverage of this Tournament.


        :param odds_coverage: The odds_coverage of this Tournament.
        :type odds_coverage: str
        """

        self._odds_coverage = odds_coverage

    @property
    def par(self):
        """Gets the par of this Tournament.


        :return: The par of this Tournament.
        :rtype: int
        """
        return self._par

    @par.setter
    def par(self, par):
        """Sets the par of this Tournament.


        :param par: The par of this Tournament.
        :type par: int
        """

        self._par = par

    @property
    def purse(self):
        """Gets the purse of this Tournament.


        :return: The purse of this Tournament.
        :rtype: float
        """
        return self._purse

    @purse.setter
    def purse(self, purse):
        """Sets the purse of this Tournament.


        :param purse: The purse of this Tournament.
        :type purse: float
        """

        self._purse = purse

    @property
    def rounds(self):
        """Gets the rounds of this Tournament.


        :return: The rounds of this Tournament.
        :rtype: List[Round]
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        """Sets the rounds of this Tournament.


        :param rounds: The rounds of this Tournament.
        :type rounds: List[Round]
        """

        self._rounds = rounds

    @property
    def sport_radar_tournament_id(self):
        """Gets the sport_radar_tournament_id of this Tournament.


        :return: The sport_radar_tournament_id of this Tournament.
        :rtype: str
        """
        return self._sport_radar_tournament_id

    @sport_radar_tournament_id.setter
    def sport_radar_tournament_id(self, sport_radar_tournament_id):
        """Sets the sport_radar_tournament_id of this Tournament.


        :param sport_radar_tournament_id: The sport_radar_tournament_id of this Tournament.
        :type sport_radar_tournament_id: str
        """

        self._sport_radar_tournament_id = sport_radar_tournament_id

    @property
    def start_date(self):
        """Gets the start_date of this Tournament.


        :return: The start_date of this Tournament.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Tournament.


        :param start_date: The start_date of this Tournament.
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def start_date_time(self):
        """Gets the start_date_time of this Tournament.


        :return: The start_date_time of this Tournament.
        :rtype: str
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this Tournament.


        :param start_date_time: The start_date_time of this Tournament.
        :type start_date_time: str
        """

        self._start_date_time = start_date_time

    @property
    def state(self):
        """Gets the state of this Tournament.


        :return: The state of this Tournament.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Tournament.


        :param state: The state of this Tournament.
        :type state: str
        """

        self._state = state

    @property
    def time_zone(self):
        """Gets the time_zone of this Tournament.


        :return: The time_zone of this Tournament.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Tournament.


        :param time_zone: The time_zone of this Tournament.
        :type time_zone: str
        """

        self._time_zone = time_zone

    @property
    def tournament_id(self):
        """Gets the tournament_id of this Tournament.


        :return: The tournament_id of this Tournament.
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this Tournament.


        :param tournament_id: The tournament_id of this Tournament.
        :type tournament_id: int
        """

        self._tournament_id = tournament_id

    @property
    def venue(self):
        """Gets the venue of this Tournament.


        :return: The venue of this Tournament.
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this Tournament.


        :param venue: The venue of this Tournament.
        :type venue: str
        """

        self._venue = venue

    @property
    def yards(self):
        """Gets the yards of this Tournament.


        :return: The yards of this Tournament.
        :rtype: int
        """
        return self._yards

    @yards.setter
    def yards(self, yards):
        """Sets the yards of this Tournament.


        :param yards: The yards of this Tournament.
        :type yards: int
        """

        self._yards = yards

    @property
    def zip_code(self):
        """Gets the zip_code of this Tournament.


        :return: The zip_code of this Tournament.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Tournament.


        :param zip_code: The zip_code of this Tournament.
        :type zip_code: str
        """

        self._zip_code = zip_code
