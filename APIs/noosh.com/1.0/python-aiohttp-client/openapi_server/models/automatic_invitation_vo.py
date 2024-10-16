# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.team_template_simple_vo import TeamTemplateSimpleVO
from openapi_server import util


class AutomaticInvitationVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, automatic_invitation_type_name: str=None, team_template: TeamTemplateSimpleVO=None):
        """AutomaticInvitationVO - a model defined in OpenAPI

        :param automatic_invitation_type_name: The automatic_invitation_type_name of this AutomaticInvitationVO.
        :param team_template: The team_template of this AutomaticInvitationVO.
        """
        self.openapi_types = {
            'automatic_invitation_type_name': str,
            'team_template': TeamTemplateSimpleVO
        }

        self.attribute_map = {
            'automatic_invitation_type_name': 'automatic_invitation_type_name',
            'team_template': 'team_template'
        }

        self._automatic_invitation_type_name = automatic_invitation_type_name
        self._team_template = team_template

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AutomaticInvitationVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AutomaticInvitationVO of this AutomaticInvitationVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def automatic_invitation_type_name(self):
        """Gets the automatic_invitation_type_name of this AutomaticInvitationVO.

        

        :return: The automatic_invitation_type_name of this AutomaticInvitationVO.
        :rtype: str
        """
        return self._automatic_invitation_type_name

    @automatic_invitation_type_name.setter
    def automatic_invitation_type_name(self, automatic_invitation_type_name):
        """Sets the automatic_invitation_type_name of this AutomaticInvitationVO.

        

        :param automatic_invitation_type_name: The automatic_invitation_type_name of this AutomaticInvitationVO.
        :type automatic_invitation_type_name: str
        """

        self._automatic_invitation_type_name = automatic_invitation_type_name

    @property
    def team_template(self):
        """Gets the team_template of this AutomaticInvitationVO.


        :return: The team_template of this AutomaticInvitationVO.
        :rtype: TeamTemplateSimpleVO
        """
        return self._team_template

    @team_template.setter
    def team_template(self, team_template):
        """Sets the team_template of this AutomaticInvitationVO.


        :param team_template: The team_template of this AutomaticInvitationVO.
        :type team_template: TeamTemplateSimpleVO
        """

        self._team_template = team_template
