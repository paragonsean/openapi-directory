# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.me_business_card import MeBusinessCard
from openapi_server.models.me_usage import MeUsage
from openapi_server.models.member import Member
from openapi_server.models.user_profile import UserProfile
from openapi_server import util


class User(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, business_card: MeBusinessCard=None, community_persona: Member=None, id: float=None, profile: UserProfile=None, usage: MeUsage=None):
        """User - a model defined in OpenAPI

        :param business_card: The business_card of this User.
        :param community_persona: The community_persona of this User.
        :param id: The id of this User.
        :param profile: The profile of this User.
        :param usage: The usage of this User.
        """
        self.openapi_types = {
            'business_card': MeBusinessCard,
            'community_persona': Member,
            'id': float,
            'profile': UserProfile,
            'usage': MeUsage
        }

        self.attribute_map = {
            'business_card': 'business_card',
            'community_persona': 'community_persona',
            'id': 'id',
            'profile': 'profile',
            'usage': 'usage'
        }

        self._business_card = business_card
        self._community_persona = community_persona
        self._id = id
        self._profile = profile
        self._usage = usage

    @classmethod
    def from_dict(cls, dikt: dict) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The User of this User.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_card(self):
        """Gets the business_card of this User.


        :return: The business_card of this User.
        :rtype: MeBusinessCard
        """
        return self._business_card

    @business_card.setter
    def business_card(self, business_card):
        """Sets the business_card of this User.


        :param business_card: The business_card of this User.
        :type business_card: MeBusinessCard
        """

        self._business_card = business_card

    @property
    def community_persona(self):
        """Gets the community_persona of this User.


        :return: The community_persona of this User.
        :rtype: Member
        """
        return self._community_persona

    @community_persona.setter
    def community_persona(self, community_persona):
        """Sets the community_persona of this User.


        :param community_persona: The community_persona of this User.
        :type community_persona: Member
        """

        self._community_persona = community_persona

    @property
    def id(self):
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def profile(self):
        """Gets the profile of this User.


        :return: The profile of this User.
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this User.


        :param profile: The profile of this User.
        :type profile: UserProfile
        """

        self._profile = profile

    @property
    def usage(self):
        """Gets the usage of this User.


        :return: The usage of this User.
        :rtype: MeUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this User.


        :param usage: The usage of this User.
        :type usage: MeUsage
        """

        self._usage = usage
