# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.project_parent_vo import ProjectParentVO
from openapi_server.models.property_pa_and_att_vo import PropertyPaAndAttVO
from openapi_server import util


class ProjectDetailVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category: str=None, client_account: str=None, client_user: str=None, client_user_id: int=None, client_workgroup_id: int=None, comments: str=None, completion_date: date=None, custom_fields: List[PropertyPaAndAttVO]=None, deactivation_reason: str=None, is_active: bool=None, is_hot: bool=None, last_spec_update: date=None, mod_date: date=None, owner_workgroup: str=None, parent_project: ProjectParentVO=None, project_create_date: date=None, project_description: str=None, project_id: int=None, project_name: str=None, project_number: str=None, project_status: str=None, team_owners: str=None):
        """ProjectDetailVO - a model defined in OpenAPI

        :param category: The category of this ProjectDetailVO.
        :param client_account: The client_account of this ProjectDetailVO.
        :param client_user: The client_user of this ProjectDetailVO.
        :param client_user_id: The client_user_id of this ProjectDetailVO.
        :param client_workgroup_id: The client_workgroup_id of this ProjectDetailVO.
        :param comments: The comments of this ProjectDetailVO.
        :param completion_date: The completion_date of this ProjectDetailVO.
        :param custom_fields: The custom_fields of this ProjectDetailVO.
        :param deactivation_reason: The deactivation_reason of this ProjectDetailVO.
        :param is_active: The is_active of this ProjectDetailVO.
        :param is_hot: The is_hot of this ProjectDetailVO.
        :param last_spec_update: The last_spec_update of this ProjectDetailVO.
        :param mod_date: The mod_date of this ProjectDetailVO.
        :param owner_workgroup: The owner_workgroup of this ProjectDetailVO.
        :param parent_project: The parent_project of this ProjectDetailVO.
        :param project_create_date: The project_create_date of this ProjectDetailVO.
        :param project_description: The project_description of this ProjectDetailVO.
        :param project_id: The project_id of this ProjectDetailVO.
        :param project_name: The project_name of this ProjectDetailVO.
        :param project_number: The project_number of this ProjectDetailVO.
        :param project_status: The project_status of this ProjectDetailVO.
        :param team_owners: The team_owners of this ProjectDetailVO.
        """
        self.openapi_types = {
            'category': str,
            'client_account': str,
            'client_user': str,
            'client_user_id': int,
            'client_workgroup_id': int,
            'comments': str,
            'completion_date': date,
            'custom_fields': List[PropertyPaAndAttVO],
            'deactivation_reason': str,
            'is_active': bool,
            'is_hot': bool,
            'last_spec_update': date,
            'mod_date': date,
            'owner_workgroup': str,
            'parent_project': ProjectParentVO,
            'project_create_date': date,
            'project_description': str,
            'project_id': int,
            'project_name': str,
            'project_number': str,
            'project_status': str,
            'team_owners': str
        }

        self.attribute_map = {
            'category': 'category',
            'client_account': 'client_account',
            'client_user': 'client_user',
            'client_user_id': 'client_user_id',
            'client_workgroup_id': 'client_workgroup_id',
            'comments': 'comments',
            'completion_date': 'completion_date',
            'custom_fields': 'custom_fields',
            'deactivation_reason': 'deactivation_reason',
            'is_active': 'is_active',
            'is_hot': 'is_hot',
            'last_spec_update': 'last_spec_update',
            'mod_date': 'mod_date',
            'owner_workgroup': 'owner_workgroup',
            'parent_project': 'parent_project',
            'project_create_date': 'project_create_date',
            'project_description': 'project_description',
            'project_id': 'project_id',
            'project_name': 'project_name',
            'project_number': 'project_number',
            'project_status': 'project_status',
            'team_owners': 'team_owners'
        }

        self._category = category
        self._client_account = client_account
        self._client_user = client_user
        self._client_user_id = client_user_id
        self._client_workgroup_id = client_workgroup_id
        self._comments = comments
        self._completion_date = completion_date
        self._custom_fields = custom_fields
        self._deactivation_reason = deactivation_reason
        self._is_active = is_active
        self._is_hot = is_hot
        self._last_spec_update = last_spec_update
        self._mod_date = mod_date
        self._owner_workgroup = owner_workgroup
        self._parent_project = parent_project
        self._project_create_date = project_create_date
        self._project_description = project_description
        self._project_id = project_id
        self._project_name = project_name
        self._project_number = project_number
        self._project_status = project_status
        self._team_owners = team_owners

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectDetailVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectDetailVO of this ProjectDetailVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self):
        """Gets the category of this ProjectDetailVO.

        

        :return: The category of this ProjectDetailVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ProjectDetailVO.

        

        :param category: The category of this ProjectDetailVO.
        :type category: str
        """

        self._category = category

    @property
    def client_account(self):
        """Gets the client_account of this ProjectDetailVO.

        

        :return: The client_account of this ProjectDetailVO.
        :rtype: str
        """
        return self._client_account

    @client_account.setter
    def client_account(self, client_account):
        """Sets the client_account of this ProjectDetailVO.

        

        :param client_account: The client_account of this ProjectDetailVO.
        :type client_account: str
        """

        self._client_account = client_account

    @property
    def client_user(self):
        """Gets the client_user of this ProjectDetailVO.

        

        :return: The client_user of this ProjectDetailVO.
        :rtype: str
        """
        return self._client_user

    @client_user.setter
    def client_user(self, client_user):
        """Sets the client_user of this ProjectDetailVO.

        

        :param client_user: The client_user of this ProjectDetailVO.
        :type client_user: str
        """

        self._client_user = client_user

    @property
    def client_user_id(self):
        """Gets the client_user_id of this ProjectDetailVO.

        

        :return: The client_user_id of this ProjectDetailVO.
        :rtype: int
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this ProjectDetailVO.

        

        :param client_user_id: The client_user_id of this ProjectDetailVO.
        :type client_user_id: int
        """

        self._client_user_id = client_user_id

    @property
    def client_workgroup_id(self):
        """Gets the client_workgroup_id of this ProjectDetailVO.

        

        :return: The client_workgroup_id of this ProjectDetailVO.
        :rtype: int
        """
        return self._client_workgroup_id

    @client_workgroup_id.setter
    def client_workgroup_id(self, client_workgroup_id):
        """Sets the client_workgroup_id of this ProjectDetailVO.

        

        :param client_workgroup_id: The client_workgroup_id of this ProjectDetailVO.
        :type client_workgroup_id: int
        """

        self._client_workgroup_id = client_workgroup_id

    @property
    def comments(self):
        """Gets the comments of this ProjectDetailVO.

        

        :return: The comments of this ProjectDetailVO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ProjectDetailVO.

        

        :param comments: The comments of this ProjectDetailVO.
        :type comments: str
        """

        self._comments = comments

    @property
    def completion_date(self):
        """Gets the completion_date of this ProjectDetailVO.

        

        :return: The completion_date of this ProjectDetailVO.
        :rtype: date
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this ProjectDetailVO.

        

        :param completion_date: The completion_date of this ProjectDetailVO.
        :type completion_date: date
        """

        self._completion_date = completion_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ProjectDetailVO.

        

        :return: The custom_fields of this ProjectDetailVO.
        :rtype: List[PropertyPaAndAttVO]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ProjectDetailVO.

        

        :param custom_fields: The custom_fields of this ProjectDetailVO.
        :type custom_fields: List[PropertyPaAndAttVO]
        """

        self._custom_fields = custom_fields

    @property
    def deactivation_reason(self):
        """Gets the deactivation_reason of this ProjectDetailVO.

        

        :return: The deactivation_reason of this ProjectDetailVO.
        :rtype: str
        """
        return self._deactivation_reason

    @deactivation_reason.setter
    def deactivation_reason(self, deactivation_reason):
        """Sets the deactivation_reason of this ProjectDetailVO.

        

        :param deactivation_reason: The deactivation_reason of this ProjectDetailVO.
        :type deactivation_reason: str
        """

        self._deactivation_reason = deactivation_reason

    @property
    def is_active(self):
        """Gets the is_active of this ProjectDetailVO.

        

        :return: The is_active of this ProjectDetailVO.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ProjectDetailVO.

        

        :param is_active: The is_active of this ProjectDetailVO.
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def is_hot(self):
        """Gets the is_hot of this ProjectDetailVO.

        

        :return: The is_hot of this ProjectDetailVO.
        :rtype: bool
        """
        return self._is_hot

    @is_hot.setter
    def is_hot(self, is_hot):
        """Sets the is_hot of this ProjectDetailVO.

        

        :param is_hot: The is_hot of this ProjectDetailVO.
        :type is_hot: bool
        """

        self._is_hot = is_hot

    @property
    def last_spec_update(self):
        """Gets the last_spec_update of this ProjectDetailVO.

        

        :return: The last_spec_update of this ProjectDetailVO.
        :rtype: date
        """
        return self._last_spec_update

    @last_spec_update.setter
    def last_spec_update(self, last_spec_update):
        """Sets the last_spec_update of this ProjectDetailVO.

        

        :param last_spec_update: The last_spec_update of this ProjectDetailVO.
        :type last_spec_update: date
        """

        self._last_spec_update = last_spec_update

    @property
    def mod_date(self):
        """Gets the mod_date of this ProjectDetailVO.

        

        :return: The mod_date of this ProjectDetailVO.
        :rtype: date
        """
        return self._mod_date

    @mod_date.setter
    def mod_date(self, mod_date):
        """Sets the mod_date of this ProjectDetailVO.

        

        :param mod_date: The mod_date of this ProjectDetailVO.
        :type mod_date: date
        """

        self._mod_date = mod_date

    @property
    def owner_workgroup(self):
        """Gets the owner_workgroup of this ProjectDetailVO.

        

        :return: The owner_workgroup of this ProjectDetailVO.
        :rtype: str
        """
        return self._owner_workgroup

    @owner_workgroup.setter
    def owner_workgroup(self, owner_workgroup):
        """Sets the owner_workgroup of this ProjectDetailVO.

        

        :param owner_workgroup: The owner_workgroup of this ProjectDetailVO.
        :type owner_workgroup: str
        """

        self._owner_workgroup = owner_workgroup

    @property
    def parent_project(self):
        """Gets the parent_project of this ProjectDetailVO.


        :return: The parent_project of this ProjectDetailVO.
        :rtype: ProjectParentVO
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this ProjectDetailVO.


        :param parent_project: The parent_project of this ProjectDetailVO.
        :type parent_project: ProjectParentVO
        """

        self._parent_project = parent_project

    @property
    def project_create_date(self):
        """Gets the project_create_date of this ProjectDetailVO.

        

        :return: The project_create_date of this ProjectDetailVO.
        :rtype: date
        """
        return self._project_create_date

    @project_create_date.setter
    def project_create_date(self, project_create_date):
        """Sets the project_create_date of this ProjectDetailVO.

        

        :param project_create_date: The project_create_date of this ProjectDetailVO.
        :type project_create_date: date
        """

        self._project_create_date = project_create_date

    @property
    def project_description(self):
        """Gets the project_description of this ProjectDetailVO.

        

        :return: The project_description of this ProjectDetailVO.
        :rtype: str
        """
        return self._project_description

    @project_description.setter
    def project_description(self, project_description):
        """Sets the project_description of this ProjectDetailVO.

        

        :param project_description: The project_description of this ProjectDetailVO.
        :type project_description: str
        """

        self._project_description = project_description

    @property
    def project_id(self):
        """Gets the project_id of this ProjectDetailVO.

        

        :return: The project_id of this ProjectDetailVO.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectDetailVO.

        

        :param project_id: The project_id of this ProjectDetailVO.
        :type project_id: int
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ProjectDetailVO.

        

        :return: The project_name of this ProjectDetailVO.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectDetailVO.

        

        :param project_name: The project_name of this ProjectDetailVO.
        :type project_name: str
        """

        self._project_name = project_name

    @property
    def project_number(self):
        """Gets the project_number of this ProjectDetailVO.

        

        :return: The project_number of this ProjectDetailVO.
        :rtype: str
        """
        return self._project_number

    @project_number.setter
    def project_number(self, project_number):
        """Sets the project_number of this ProjectDetailVO.

        

        :param project_number: The project_number of this ProjectDetailVO.
        :type project_number: str
        """

        self._project_number = project_number

    @property
    def project_status(self):
        """Gets the project_status of this ProjectDetailVO.

        

        :return: The project_status of this ProjectDetailVO.
        :rtype: str
        """
        return self._project_status

    @project_status.setter
    def project_status(self, project_status):
        """Sets the project_status of this ProjectDetailVO.

        

        :param project_status: The project_status of this ProjectDetailVO.
        :type project_status: str
        """

        self._project_status = project_status

    @property
    def team_owners(self):
        """Gets the team_owners of this ProjectDetailVO.

        

        :return: The team_owners of this ProjectDetailVO.
        :rtype: str
        """
        return self._team_owners

    @team_owners.setter
    def team_owners(self, team_owners):
        """Sets the team_owners of this ProjectDetailVO.

        

        :param team_owners: The team_owners of this ProjectDetailVO.
        :type team_owners: str
        """

        self._team_owners = team_owners
