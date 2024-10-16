# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Player(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_city: str=None, birth_country: str=None, birth_date: str=None, common_name: str=None, draft_kings_position: str=None, first_name: str=None, foot: str=None, gender: str=None, height: int=None, injury_body_part: str=None, injury_notes: str=None, injury_start_date: str=None, injury_status: str=None, jersey: int=None, last_name: str=None, nationality: str=None, photo_url: str=None, player_id: int=None, position: str=None, position_category: str=None, roto_wire_player_id: int=None, short_name: str=None, updated: str=None, usa_today_headshot_no_background_updated: str=None, usa_today_headshot_no_background_url: str=None, usa_today_headshot_updated: str=None, usa_today_headshot_url: str=None, usa_today_player_id: int=None, weight: int=None):
        """Player - a model defined in OpenAPI

        :param birth_city: The birth_city of this Player.
        :param birth_country: The birth_country of this Player.
        :param birth_date: The birth_date of this Player.
        :param common_name: The common_name of this Player.
        :param draft_kings_position: The draft_kings_position of this Player.
        :param first_name: The first_name of this Player.
        :param foot: The foot of this Player.
        :param gender: The gender of this Player.
        :param height: The height of this Player.
        :param injury_body_part: The injury_body_part of this Player.
        :param injury_notes: The injury_notes of this Player.
        :param injury_start_date: The injury_start_date of this Player.
        :param injury_status: The injury_status of this Player.
        :param jersey: The jersey of this Player.
        :param last_name: The last_name of this Player.
        :param nationality: The nationality of this Player.
        :param photo_url: The photo_url of this Player.
        :param player_id: The player_id of this Player.
        :param position: The position of this Player.
        :param position_category: The position_category of this Player.
        :param roto_wire_player_id: The roto_wire_player_id of this Player.
        :param short_name: The short_name of this Player.
        :param updated: The updated of this Player.
        :param usa_today_headshot_no_background_updated: The usa_today_headshot_no_background_updated of this Player.
        :param usa_today_headshot_no_background_url: The usa_today_headshot_no_background_url of this Player.
        :param usa_today_headshot_updated: The usa_today_headshot_updated of this Player.
        :param usa_today_headshot_url: The usa_today_headshot_url of this Player.
        :param usa_today_player_id: The usa_today_player_id of this Player.
        :param weight: The weight of this Player.
        """
        self.openapi_types = {
            'birth_city': str,
            'birth_country': str,
            'birth_date': str,
            'common_name': str,
            'draft_kings_position': str,
            'first_name': str,
            'foot': str,
            'gender': str,
            'height': int,
            'injury_body_part': str,
            'injury_notes': str,
            'injury_start_date': str,
            'injury_status': str,
            'jersey': int,
            'last_name': str,
            'nationality': str,
            'photo_url': str,
            'player_id': int,
            'position': str,
            'position_category': str,
            'roto_wire_player_id': int,
            'short_name': str,
            'updated': str,
            'usa_today_headshot_no_background_updated': str,
            'usa_today_headshot_no_background_url': str,
            'usa_today_headshot_updated': str,
            'usa_today_headshot_url': str,
            'usa_today_player_id': int,
            'weight': int
        }

        self.attribute_map = {
            'birth_city': 'BirthCity',
            'birth_country': 'BirthCountry',
            'birth_date': 'BirthDate',
            'common_name': 'CommonName',
            'draft_kings_position': 'DraftKingsPosition',
            'first_name': 'FirstName',
            'foot': 'Foot',
            'gender': 'Gender',
            'height': 'Height',
            'injury_body_part': 'InjuryBodyPart',
            'injury_notes': 'InjuryNotes',
            'injury_start_date': 'InjuryStartDate',
            'injury_status': 'InjuryStatus',
            'jersey': 'Jersey',
            'last_name': 'LastName',
            'nationality': 'Nationality',
            'photo_url': 'PhotoUrl',
            'player_id': 'PlayerId',
            'position': 'Position',
            'position_category': 'PositionCategory',
            'roto_wire_player_id': 'RotoWirePlayerID',
            'short_name': 'ShortName',
            'updated': 'Updated',
            'usa_today_headshot_no_background_updated': 'UsaTodayHeadshotNoBackgroundUpdated',
            'usa_today_headshot_no_background_url': 'UsaTodayHeadshotNoBackgroundUrl',
            'usa_today_headshot_updated': 'UsaTodayHeadshotUpdated',
            'usa_today_headshot_url': 'UsaTodayHeadshotUrl',
            'usa_today_player_id': 'UsaTodayPlayerID',
            'weight': 'Weight'
        }

        self._birth_city = birth_city
        self._birth_country = birth_country
        self._birth_date = birth_date
        self._common_name = common_name
        self._draft_kings_position = draft_kings_position
        self._first_name = first_name
        self._foot = foot
        self._gender = gender
        self._height = height
        self._injury_body_part = injury_body_part
        self._injury_notes = injury_notes
        self._injury_start_date = injury_start_date
        self._injury_status = injury_status
        self._jersey = jersey
        self._last_name = last_name
        self._nationality = nationality
        self._photo_url = photo_url
        self._player_id = player_id
        self._position = position
        self._position_category = position_category
        self._roto_wire_player_id = roto_wire_player_id
        self._short_name = short_name
        self._updated = updated
        self._usa_today_headshot_no_background_updated = usa_today_headshot_no_background_updated
        self._usa_today_headshot_no_background_url = usa_today_headshot_no_background_url
        self._usa_today_headshot_updated = usa_today_headshot_updated
        self._usa_today_headshot_url = usa_today_headshot_url
        self._usa_today_player_id = usa_today_player_id
        self._weight = weight

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
    def birth_country(self):
        """Gets the birth_country of this Player.


        :return: The birth_country of this Player.
        :rtype: str
        """
        return self._birth_country

    @birth_country.setter
    def birth_country(self, birth_country):
        """Sets the birth_country of this Player.


        :param birth_country: The birth_country of this Player.
        :type birth_country: str
        """

        self._birth_country = birth_country

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
    def common_name(self):
        """Gets the common_name of this Player.


        :return: The common_name of this Player.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this Player.


        :param common_name: The common_name of this Player.
        :type common_name: str
        """

        self._common_name = common_name

    @property
    def draft_kings_position(self):
        """Gets the draft_kings_position of this Player.


        :return: The draft_kings_position of this Player.
        :rtype: str
        """
        return self._draft_kings_position

    @draft_kings_position.setter
    def draft_kings_position(self, draft_kings_position):
        """Sets the draft_kings_position of this Player.


        :param draft_kings_position: The draft_kings_position of this Player.
        :type draft_kings_position: str
        """

        self._draft_kings_position = draft_kings_position

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
    def foot(self):
        """Gets the foot of this Player.


        :return: The foot of this Player.
        :rtype: str
        """
        return self._foot

    @foot.setter
    def foot(self, foot):
        """Sets the foot of this Player.


        :param foot: The foot of this Player.
        :type foot: str
        """

        self._foot = foot

    @property
    def gender(self):
        """Gets the gender of this Player.


        :return: The gender of this Player.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Player.


        :param gender: The gender of this Player.
        :type gender: str
        """

        self._gender = gender

    @property
    def height(self):
        """Gets the height of this Player.


        :return: The height of this Player.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Player.


        :param height: The height of this Player.
        :type height: int
        """

        self._height = height

    @property
    def injury_body_part(self):
        """Gets the injury_body_part of this Player.


        :return: The injury_body_part of this Player.
        :rtype: str
        """
        return self._injury_body_part

    @injury_body_part.setter
    def injury_body_part(self, injury_body_part):
        """Sets the injury_body_part of this Player.


        :param injury_body_part: The injury_body_part of this Player.
        :type injury_body_part: str
        """

        self._injury_body_part = injury_body_part

    @property
    def injury_notes(self):
        """Gets the injury_notes of this Player.


        :return: The injury_notes of this Player.
        :rtype: str
        """
        return self._injury_notes

    @injury_notes.setter
    def injury_notes(self, injury_notes):
        """Sets the injury_notes of this Player.


        :param injury_notes: The injury_notes of this Player.
        :type injury_notes: str
        """

        self._injury_notes = injury_notes

    @property
    def injury_start_date(self):
        """Gets the injury_start_date of this Player.


        :return: The injury_start_date of this Player.
        :rtype: str
        """
        return self._injury_start_date

    @injury_start_date.setter
    def injury_start_date(self, injury_start_date):
        """Sets the injury_start_date of this Player.


        :param injury_start_date: The injury_start_date of this Player.
        :type injury_start_date: str
        """

        self._injury_start_date = injury_start_date

    @property
    def injury_status(self):
        """Gets the injury_status of this Player.


        :return: The injury_status of this Player.
        :rtype: str
        """
        return self._injury_status

    @injury_status.setter
    def injury_status(self, injury_status):
        """Sets the injury_status of this Player.


        :param injury_status: The injury_status of this Player.
        :type injury_status: str
        """

        self._injury_status = injury_status

    @property
    def jersey(self):
        """Gets the jersey of this Player.


        :return: The jersey of this Player.
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this Player.


        :param jersey: The jersey of this Player.
        :type jersey: int
        """

        self._jersey = jersey

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
    def nationality(self):
        """Gets the nationality of this Player.


        :return: The nationality of this Player.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this Player.


        :param nationality: The nationality of this Player.
        :type nationality: str
        """

        self._nationality = nationality

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
    def position(self):
        """Gets the position of this Player.


        :return: The position of this Player.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Player.


        :param position: The position of this Player.
        :type position: str
        """

        self._position = position

    @property
    def position_category(self):
        """Gets the position_category of this Player.


        :return: The position_category of this Player.
        :rtype: str
        """
        return self._position_category

    @position_category.setter
    def position_category(self, position_category):
        """Sets the position_category of this Player.


        :param position_category: The position_category of this Player.
        :type position_category: str
        """

        self._position_category = position_category

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
    def short_name(self):
        """Gets the short_name of this Player.


        :return: The short_name of this Player.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Player.


        :param short_name: The short_name of this Player.
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def updated(self):
        """Gets the updated of this Player.


        :return: The updated of this Player.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Player.


        :param updated: The updated of this Player.
        :type updated: str
        """

        self._updated = updated

    @property
    def usa_today_headshot_no_background_updated(self):
        """Gets the usa_today_headshot_no_background_updated of this Player.


        :return: The usa_today_headshot_no_background_updated of this Player.
        :rtype: str
        """
        return self._usa_today_headshot_no_background_updated

    @usa_today_headshot_no_background_updated.setter
    def usa_today_headshot_no_background_updated(self, usa_today_headshot_no_background_updated):
        """Sets the usa_today_headshot_no_background_updated of this Player.


        :param usa_today_headshot_no_background_updated: The usa_today_headshot_no_background_updated of this Player.
        :type usa_today_headshot_no_background_updated: str
        """

        self._usa_today_headshot_no_background_updated = usa_today_headshot_no_background_updated

    @property
    def usa_today_headshot_no_background_url(self):
        """Gets the usa_today_headshot_no_background_url of this Player.


        :return: The usa_today_headshot_no_background_url of this Player.
        :rtype: str
        """
        return self._usa_today_headshot_no_background_url

    @usa_today_headshot_no_background_url.setter
    def usa_today_headshot_no_background_url(self, usa_today_headshot_no_background_url):
        """Sets the usa_today_headshot_no_background_url of this Player.


        :param usa_today_headshot_no_background_url: The usa_today_headshot_no_background_url of this Player.
        :type usa_today_headshot_no_background_url: str
        """

        self._usa_today_headshot_no_background_url = usa_today_headshot_no_background_url

    @property
    def usa_today_headshot_updated(self):
        """Gets the usa_today_headshot_updated of this Player.


        :return: The usa_today_headshot_updated of this Player.
        :rtype: str
        """
        return self._usa_today_headshot_updated

    @usa_today_headshot_updated.setter
    def usa_today_headshot_updated(self, usa_today_headshot_updated):
        """Sets the usa_today_headshot_updated of this Player.


        :param usa_today_headshot_updated: The usa_today_headshot_updated of this Player.
        :type usa_today_headshot_updated: str
        """

        self._usa_today_headshot_updated = usa_today_headshot_updated

    @property
    def usa_today_headshot_url(self):
        """Gets the usa_today_headshot_url of this Player.


        :return: The usa_today_headshot_url of this Player.
        :rtype: str
        """
        return self._usa_today_headshot_url

    @usa_today_headshot_url.setter
    def usa_today_headshot_url(self, usa_today_headshot_url):
        """Sets the usa_today_headshot_url of this Player.


        :param usa_today_headshot_url: The usa_today_headshot_url of this Player.
        :type usa_today_headshot_url: str
        """

        self._usa_today_headshot_url = usa_today_headshot_url

    @property
    def usa_today_player_id(self):
        """Gets the usa_today_player_id of this Player.


        :return: The usa_today_player_id of this Player.
        :rtype: int
        """
        return self._usa_today_player_id

    @usa_today_player_id.setter
    def usa_today_player_id(self, usa_today_player_id):
        """Sets the usa_today_player_id of this Player.


        :param usa_today_player_id: The usa_today_player_id of this Player.
        :type usa_today_player_id: int
        """

        self._usa_today_player_id = usa_today_player_id

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
