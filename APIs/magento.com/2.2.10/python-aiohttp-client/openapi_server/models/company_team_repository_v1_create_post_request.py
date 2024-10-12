# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.company_data_team_interface import CompanyDataTeamInterface
from openapi_server import util


class CompanyTeamRepositoryV1CreatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, team: CompanyDataTeamInterface=None):
        """CompanyTeamRepositoryV1CreatePostRequest - a model defined in OpenAPI

        :param team: The team of this CompanyTeamRepositoryV1CreatePostRequest.
        """
        self.openapi_types = {
            'team': CompanyDataTeamInterface
        }

        self.attribute_map = {
            'team': 'team'
        }

        self._team = team

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompanyTeamRepositoryV1CreatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The companyTeamRepositoryV1CreatePost_request of this CompanyTeamRepositoryV1CreatePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def team(self):
        """Gets the team of this CompanyTeamRepositoryV1CreatePostRequest.


        :return: The team of this CompanyTeamRepositoryV1CreatePostRequest.
        :rtype: CompanyDataTeamInterface
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this CompanyTeamRepositoryV1CreatePostRequest.


        :param team: The team of this CompanyTeamRepositoryV1CreatePostRequest.
        :type team: CompanyDataTeamInterface
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")

        self._team = team
