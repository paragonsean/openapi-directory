# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Player(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_city: str=None, birth_date: str=None, birth_state: str=None, college: str=None, country: str=None, draft_kings_name: str=None, draft_kings_player_id: int=None, fan_duel_name: str=None, fan_duel_player_id: int=None, fantasy_alarm_player_id: int=None, fantasy_draft_name: str=None, fantasy_draft_player_id: int=None, first_name: str=None, last_name: str=None, pga_debut: int=None, pga_tour_player_id: int=None, photo_url: str=None, player_id: int=None, roto_wire_player_id: int=None, rotoworld_player_id: int=None, sport_radar_player_id: str=None, swings: str=None, weight: int=None, yahoo_player_id: int=None):
        """Player - a model defined in OpenAPI

        :param birth_city: The birth_city of this Player.
        :param birth_date: The birth_date of this Player.
        :param birth_state: The birth_state of this Player.
        :param college: The college of this Player.
        :param country: The country of this Player.
        :param draft_kings_name: The draft_kings_name of this Player.
        :param draft_kings_player_id: The draft_kings_player_id of this Player.
        :param fan_duel_name: The fan_duel_name of this Player.
        :param fan_duel_player_id: The fan_duel_player_id of this Player.
        :param fantasy_alarm_player_id: The fantasy_alarm_player_id of this Player.
        :param fantasy_draft_name: The fantasy_draft_name of this Player.
        :param fantasy_draft_player_id: The fantasy_draft_player_id of this Player.
        :param first_name: The first_name of this Player.
        :param last_name: The last_name of this Player.
        :param pga_debut: The pga_debut of this Player.
        :param pga_tour_player_id: The pga_tour_player_id of this Player.
        :param photo_url: The photo_url of this Player.
        :param player_id: The player_id of this Player.
        :param roto_wire_player_id: The roto_wire_player_id of this Player.
        :param rotoworld_player_id: The rotoworld_player_id of this Player.
        :param sport_radar_player_id: The sport_radar_player_id of this Player.
        :param swings: The swings of this Player.
        :param weight: The weight of this Player.
        :param yahoo_player_id: The yahoo_player_id of this Player.
        """
        self.openapi_types = {
            'birth_city': str,
            'birth_date': str,
            'birth_state': str,
            'college': str,
            'country': str,
            'draft_kings_name': str,
            'draft_kings_player_id': int,
            'fan_duel_name': str,
            'fan_duel_player_id': int,
            'fantasy_alarm_player_id': int,
            'fantasy_draft_name': str,
            'fantasy_draft_player_id': int,
            'first_name': str,
            'last_name': str,
            'pga_debut': int,
            'pga_tour_player_id': int,
            'photo_url': str,
            'player_id': int,
            'roto_wire_player_id': int,
            'rotoworld_player_id': int,
            'sport_radar_player_id': str,
            'swings': str,
            'weight': int,
            'yahoo_player_id': int
        }

        self.attribute_map = {
            'birth_city': 'BirthCity',
            'birth_date': 'BirthDate',
            'birth_state': 'BirthState',
            'college': 'College',
            'country': 'Country',
            'draft_kings_name': 'DraftKingsName',
            'draft_kings_player_id': 'DraftKingsPlayerID',
            'fan_duel_name': 'FanDuelName',
            'fan_duel_player_id': 'FanDuelPlayerID',
            'fantasy_alarm_player_id': 'FantasyAlarmPlayerID',
            'fantasy_draft_name': 'FantasyDraftName',
            'fantasy_draft_player_id': 'FantasyDraftPlayerID',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'pga_debut': 'PgaDebut',
            'pga_tour_player_id': 'PgaTourPlayerID',
            'photo_url': 'PhotoUrl',
            'player_id': 'PlayerID',
            'roto_wire_player_id': 'RotoWirePlayerID',
            'rotoworld_player_id': 'RotoworldPlayerID',
            'sport_radar_player_id': 'SportRadarPlayerID',
            'swings': 'Swings',
            'weight': 'Weight',
            'yahoo_player_id': 'YahooPlayerID'
        }

        self._birth_city = birth_city
        self._birth_date = birth_date
        self._birth_state = birth_state
        self._college = college
        self._country = country
        self._draft_kings_name = draft_kings_name
        self._draft_kings_player_id = draft_kings_player_id
        self._fan_duel_name = fan_duel_name
        self._fan_duel_player_id = fan_duel_player_id
        self._fantasy_alarm_player_id = fantasy_alarm_player_id
        self._fantasy_draft_name = fantasy_draft_name
        self._fantasy_draft_player_id = fantasy_draft_player_id
        self._first_name = first_name
        self._last_name = last_name
        self._pga_debut = pga_debut
        self._pga_tour_player_id = pga_tour_player_id
        self._photo_url = photo_url
        self._player_id = player_id
        self._roto_wire_player_id = roto_wire_player_id
        self._rotoworld_player_id = rotoworld_player_id
        self._sport_radar_player_id = sport_radar_player_id
        self._swings = swings
        self._weight = weight
        self._yahoo_player_id = yahoo_player_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Player':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Player of this Player.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_city(self):
        """Gets the birth_city of this Player.


        :return: The birth_city of this Player.
        :rtype: str
        """
        return self._birth_city

    @birth_city.setter
    def birth_city(self, birth_city):
        """Sets the birth_city of this Player.


        :param birth_city: The birth_city of this Player.
        :type birth_city: str
        """

        self._birth_city = birth_city

    @property
    def birth_date(self):
        """Gets the birth_date of this Player.


        :return: The birth_date of this Player.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this Player.


        :param birth_date: The birth_date of this Player.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def birth_state(self):
        """Gets the birth_state of this Player.


        :return: The birth_state of this Player.
        :rtype: str
        """
        return self._birth_state

    @birth_state.setter
    def birth_state(self, birth_state):
        """Sets the birth_state of this Player.


        :param birth_state: The birth_state of this Player.
        :type birth_state: str
        """

        self._birth_state = birth_state

    @property
    def college(self):
        """Gets the college of this Player.


        :return: The college of this Player.
        :rtype: str
        """
        return self._college

    @college.setter
    def college(self, college):
        """Sets the college of this Player.


        :param college: The college of this Player.
        :type college: str
        """

        self._college = college

    @property
    def country(self):
        """Gets the country of this Player.


        :return: The country of this Player.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Player.


        :param country: The country of this Player.
        :type country: str
        """

        self._country = country

    @property
    def draft_kings_name(self):
        """Gets the draft_kings_name of this Player.


        :return: The draft_kings_name of this Player.
        :rtype: str
        """
        return self._draft_kings_name

    @draft_kings_name.setter
    def draft_kings_name(self, draft_kings_name):
        """Sets the draft_kings_name of this Player.


        :param draft_kings_name: The draft_kings_name of this Player.
        :type draft_kings_name: str
        """

        self._draft_kings_name = draft_kings_name

    @property
    def draft_kings_player_id(self):
        """Gets the draft_kings_player_id of this Player.


        :return: The draft_kings_player_id of this Player.
        :rtype: int
        """
        return self._draft_kings_player_id

    @draft_kings_player_id.setter
    def draft_kings_player_id(self, draft_kings_player_id):
        """Sets the draft_kings_player_id of this Player.


        :param draft_kings_player_id: The draft_kings_player_id of this Player.
        :type draft_kings_player_id: int
        """

        self._draft_kings_player_id = draft_kings_player_id

    @property
    def fan_duel_name(self):
        """Gets the fan_duel_name of this Player.


        :return: The fan_duel_name of this Player.
        :rtype: str
        """
        return self._fan_duel_name

    @fan_duel_name.setter
    def fan_duel_name(self, fan_duel_name):
        """Sets the fan_duel_name of this Player.


        :param fan_duel_name: The fan_duel_name of this Player.
        :type fan_duel_name: str
        """

        self._fan_duel_name = fan_duel_name

    @property
    def fan_duel_player_id(self):
        """Gets the fan_duel_player_id of this Player.


        :return: The fan_duel_player_id of this Player.
        :rtype: int
        """
        return self._fan_duel_player_id

    @fan_duel_player_id.setter
    def fan_duel_player_id(self, fan_duel_player_id):
        """Sets the fan_duel_player_id of this Player.


        :param fan_duel_player_id: The fan_duel_player_id of this Player.
        :type fan_duel_player_id: int
        """

        self._fan_duel_player_id = fan_duel_player_id

    @property
    def fantasy_alarm_player_id(self):
        """Gets the fantasy_alarm_player_id of this Player.


        :return: The fantasy_alarm_player_id of this Player.
        :rtype: int
        """
        return self._fantasy_alarm_player_id

    @fantasy_alarm_player_id.setter
    def fantasy_alarm_player_id(self, fantasy_alarm_player_id):
        """Sets the fantasy_alarm_player_id of this Player.


        :param fantasy_alarm_player_id: The fantasy_alarm_player_id of this Player.
        :type fantasy_alarm_player_id: int
        """

        self._fantasy_alarm_player_id = fantasy_alarm_player_id

    @property
    def fantasy_draft_name(self):
        """Gets the fantasy_draft_name of this Player.


        :return: The fantasy_draft_name of this Player.
        :rtype: str
        """
        return self._fantasy_draft_name

    @fantasy_draft_name.setter
    def fantasy_draft_name(self, fantasy_draft_name):
        """Sets the fantasy_draft_name of this Player.


        :param fantasy_draft_name: The fantasy_draft_name of this Player.
        :type fantasy_draft_name: str
        """

        self._fantasy_draft_name = fantasy_draft_name

    @property
    def fantasy_draft_player_id(self):
        """Gets the fantasy_draft_player_id of this Player.


        :return: The fantasy_draft_player_id of this Player.
        :rtype: int
        """
        return self._fantasy_draft_player_id

    @fantasy_draft_player_id.setter
    def fantasy_draft_player_id(self, fantasy_draft_player_id):
        """Sets the fantasy_draft_player_id of this Player.


        :param fantasy_draft_player_id: The fantasy_draft_player_id of this Player.
        :type fantasy_draft_player_id: int
        """

        self._fantasy_draft_player_id = fantasy_draft_player_id

    @property
    def first_name(self):
        """Gets the first_name of this Player.


        :return: The first_name of this Player.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Player.


        :param first_name: The first_name of this Player.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Player.


        :return: The last_name of this Player.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Player.


        :param last_name: The last_name of this Player.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def pga_debut(self):
        """Gets the pga_debut of this Player.


        :return: The pga_debut of this Player.
        :rtype: int
        """
        return self._pga_debut

    @pga_debut.setter
    def pga_debut(self, pga_debut):
        """Sets the pga_debut of this Player.


        :param pga_debut: The pga_debut of this Player.
        :type pga_debut: int
        """

        self._pga_debut = pga_debut

    @property
    def pga_tour_player_id(self):
        """Gets the pga_tour_player_id of this Player.


        :return: The pga_tour_player_id of this Player.
        :rtype: int
        """
        return self._pga_tour_player_id

    @pga_tour_player_id.setter
    def pga_tour_player_id(self, pga_tour_player_id):
        """Sets the pga_tour_player_id of this Player.


        :param pga_tour_player_id: The pga_tour_player_id of this Player.
        :type pga_tour_player_id: int
        """

        self._pga_tour_player_id = pga_tour_player_id

    @property
    def photo_url(self):
        """Gets the photo_url of this Player.


        :return: The photo_url of this Player.
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this Player.


        :param photo_url: The photo_url of this Player.
        :type photo_url: str
        """

        self._photo_url = photo_url

    @property
    def player_id(self):
        """Gets the player_id of this Player.


        :return: The player_id of this Player.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this Player.


        :param player_id: The player_id of this Player.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def roto_wire_player_id(self):
        """Gets the roto_wire_player_id of this Player.


        :return: The roto_wire_player_id of this Player.
        :rtype: int
        """
        return self._roto_wire_player_id

    @roto_wire_player_id.setter
    def roto_wire_player_id(self, roto_wire_player_id):
        """Sets the roto_wire_player_id of this Player.


        :param roto_wire_player_id: The roto_wire_player_id of this Player.
        :type roto_wire_player_id: int
        """

        self._roto_wire_player_id = roto_wire_player_id

    @property
    def rotoworld_player_id(self):
        """Gets the rotoworld_player_id of this Player.


        :return: The rotoworld_player_id of this Player.
        :rtype: int
        """
        return self._rotoworld_player_id

    @rotoworld_player_id.setter
    def rotoworld_player_id(self, rotoworld_player_id):
        """Sets the rotoworld_player_id of this Player.


        :param rotoworld_player_id: The rotoworld_player_id of this Player.
        :type rotoworld_player_id: int
        """

        self._rotoworld_player_id = rotoworld_player_id

    @property
    def sport_radar_player_id(self):
        """Gets the sport_radar_player_id of this Player.


        :return: The sport_radar_player_id of this Player.
        :rtype: str
        """
        return self._sport_radar_player_id

    @sport_radar_player_id.setter
    def sport_radar_player_id(self, sport_radar_player_id):
        """Sets the sport_radar_player_id of this Player.


        :param sport_radar_player_id: The sport_radar_player_id of this Player.
        :type sport_radar_player_id: str
        """

        self._sport_radar_player_id = sport_radar_player_id

    @property
    def swings(self):
        """Gets the swings of this Player.


        :return: The swings of this Player.
        :rtype: str
        """
        return self._swings

    @swings.setter
    def swings(self, swings):
        """Sets the swings of this Player.


        :param swings: The swings of this Player.
        :type swings: str
        """

        self._swings = swings

    @property
    def weight(self):
        """Gets the weight of this Player.


        :return: The weight of this Player.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Player.


        :param weight: The weight of this Player.
        :type weight: int
        """

        self._weight = weight

    @property
    def yahoo_player_id(self):
        """Gets the yahoo_player_id of this Player.


        :return: The yahoo_player_id of this Player.
        :rtype: int
        """
        return self._yahoo_player_id

    @yahoo_player_id.setter
    def yahoo_player_id(self, yahoo_player_id):
        """Sets the yahoo_player_id of this Player.


        :param yahoo_player_id: The yahoo_player_id of this Player.
        :type yahoo_player_id: int
        """

        self._yahoo_player_id = yahoo_player_id
