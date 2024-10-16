# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.videogame_id import VideogameID
from openapi_server import util


class FilterOverPlayers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_year: List[float]=None, birthday: List[str]=None, first_name: List[str]=None, hometown: List[str]=None, id: List[int]=None, last_name: List[str]=None, name: List[str]=None, nationality: List[str]=None, role: List[str]=None, slug: List[str]=None, team_id: List[int]=None, videogame_id: List[VideogameID]=None):
        """FilterOverPlayers - a model defined in OpenAPI

        :param birth_year: The birth_year of this FilterOverPlayers.
        :param birthday: The birthday of this FilterOverPlayers.
        :param first_name: The first_name of this FilterOverPlayers.
        :param hometown: The hometown of this FilterOverPlayers.
        :param id: The id of this FilterOverPlayers.
        :param last_name: The last_name of this FilterOverPlayers.
        :param name: The name of this FilterOverPlayers.
        :param nationality: The nationality of this FilterOverPlayers.
        :param role: The role of this FilterOverPlayers.
        :param slug: The slug of this FilterOverPlayers.
        :param team_id: The team_id of this FilterOverPlayers.
        :param videogame_id: The videogame_id of this FilterOverPlayers.
        """
        self.openapi_types = {
            'birth_year': List[float],
            'birthday': List[str],
            'first_name': List[str],
            'hometown': List[str],
            'id': List[int],
            'last_name': List[str],
            'name': List[str],
            'nationality': List[str],
            'role': List[str],
            'slug': List[str],
            'team_id': List[int],
            'videogame_id': List[VideogameID]
        }

        self.attribute_map = {
            'birth_year': 'birth_year',
            'birthday': 'birthday',
            'first_name': 'first_name',
            'hometown': 'hometown',
            'id': 'id',
            'last_name': 'last_name',
            'name': 'name',
            'nationality': 'nationality',
            'role': 'role',
            'slug': 'slug',
            'team_id': 'team_id',
            'videogame_id': 'videogame_id'
        }

        self._birth_year = birth_year
        self._birthday = birthday
        self._first_name = first_name
        self._hometown = hometown
        self._id = id
        self._last_name = last_name
        self._name = name
        self._nationality = nationality
        self._role = role
        self._slug = slug
        self._team_id = team_id
        self._videogame_id = videogame_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FilterOverPlayers':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The filter_over_Players of this FilterOverPlayers.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_year(self):
        """Gets the birth_year of this FilterOverPlayers.


        :return: The birth_year of this FilterOverPlayers.
        :rtype: List[float]
        """
        return self._birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        """Sets the birth_year of this FilterOverPlayers.


        :param birth_year: The birth_year of this FilterOverPlayers.
        :type birth_year: List[float]
        """
        if birth_year is not None and len(birth_year) < 1:
            raise ValueError("Invalid value for `birth_year`, number of items must be greater than or equal to `1`")

        self._birth_year = birth_year

    @property
    def birthday(self):
        """Gets the birthday of this FilterOverPlayers.


        :return: The birthday of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this FilterOverPlayers.


        :param birthday: The birthday of this FilterOverPlayers.
        :type birthday: List[str]
        """
        if birthday is not None and len(birthday) < 1:
            raise ValueError("Invalid value for `birthday`, number of items must be greater than or equal to `1`")

        self._birthday = birthday

    @property
    def first_name(self):
        """Gets the first_name of this FilterOverPlayers.


        :return: The first_name of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this FilterOverPlayers.


        :param first_name: The first_name of this FilterOverPlayers.
        :type first_name: List[str]
        """
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, number of items must be greater than or equal to `1`")

        self._first_name = first_name

    @property
    def hometown(self):
        """Gets the hometown of this FilterOverPlayers.


        :return: The hometown of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this FilterOverPlayers.


        :param hometown: The hometown of this FilterOverPlayers.
        :type hometown: List[str]
        """
        if hometown is not None and len(hometown) < 1:
            raise ValueError("Invalid value for `hometown`, number of items must be greater than or equal to `1`")

        self._hometown = hometown

    @property
    def id(self):
        """Gets the id of this FilterOverPlayers.


        :return: The id of this FilterOverPlayers.
        :rtype: List[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FilterOverPlayers.


        :param id: The id of this FilterOverPlayers.
        :type id: List[int]
        """
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, number of items must be greater than or equal to `1`")

        self._id = id

    @property
    def last_name(self):
        """Gets the last_name of this FilterOverPlayers.


        :return: The last_name of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this FilterOverPlayers.


        :param last_name: The last_name of this FilterOverPlayers.
        :type last_name: List[str]
        """
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, number of items must be greater than or equal to `1`")

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this FilterOverPlayers.


        :return: The name of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilterOverPlayers.


        :param name: The name of this FilterOverPlayers.
        :type name: List[str]
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, number of items must be greater than or equal to `1`")

        self._name = name

    @property
    def nationality(self):
        """Gets the nationality of this FilterOverPlayers.


        :return: The nationality of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this FilterOverPlayers.


        :param nationality: The nationality of this FilterOverPlayers.
        :type nationality: List[str]
        """
        if nationality is not None and len(nationality) < 1:
            raise ValueError("Invalid value for `nationality`, number of items must be greater than or equal to `1`")

        self._nationality = nationality

    @property
    def role(self):
        """Gets the role of this FilterOverPlayers.


        :return: The role of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this FilterOverPlayers.


        :param role: The role of this FilterOverPlayers.
        :type role: List[str]
        """
        if role is not None and len(role) < 1:
            raise ValueError("Invalid value for `role`, number of items must be greater than or equal to `1`")

        self._role = role

    @property
    def slug(self):
        """Gets the slug of this FilterOverPlayers.


        :return: The slug of this FilterOverPlayers.
        :rtype: List[str]
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FilterOverPlayers.


        :param slug: The slug of this FilterOverPlayers.
        :type slug: List[str]
        """
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, number of items must be greater than or equal to `1`")

        self._slug = slug

    @property
    def team_id(self):
        """Gets the team_id of this FilterOverPlayers.


        :return: The team_id of this FilterOverPlayers.
        :rtype: List[int]
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this FilterOverPlayers.


        :param team_id: The team_id of this FilterOverPlayers.
        :type team_id: List[int]
        """
        if team_id is not None and len(team_id) < 1:
            raise ValueError("Invalid value for `team_id`, number of items must be greater than or equal to `1`")

        self._team_id = team_id

    @property
    def videogame_id(self):
        """Gets the videogame_id of this FilterOverPlayers.


        :return: The videogame_id of this FilterOverPlayers.
        :rtype: List[VideogameID]
        """
        return self._videogame_id

    @videogame_id.setter
    def videogame_id(self, videogame_id):
        """Sets the videogame_id of this FilterOverPlayers.


        :param videogame_id: The videogame_id of this FilterOverPlayers.
        :type videogame_id: List[VideogameID]
        """
        if videogame_id is not None and len(videogame_id) < 1:
            raise ValueError("Invalid value for `videogame_id`, number of items must be greater than or equal to `1`")

        self._videogame_id = videogame_id
