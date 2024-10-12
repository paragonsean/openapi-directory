# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.company_data_permission_interface import CompanyDataPermissionInterface
from openapi_server import util


class CompanyDataRoleInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_id: int=None, extension_attributes: object=None, id: int=None, permissions: List[CompanyDataPermissionInterface]=None, role_name: str=None):
        """CompanyDataRoleInterface - a model defined in OpenAPI

        :param company_id: The company_id of this CompanyDataRoleInterface.
        :param extension_attributes: The extension_attributes of this CompanyDataRoleInterface.
        :param id: The id of this CompanyDataRoleInterface.
        :param permissions: The permissions of this CompanyDataRoleInterface.
        :param role_name: The role_name of this CompanyDataRoleInterface.
        """
        self.openapi_types = {
            'company_id': int,
            'extension_attributes': object,
            'id': int,
            'permissions': List[CompanyDataPermissionInterface],
            'role_name': str
        }

        self.attribute_map = {
            'company_id': 'company_id',
            'extension_attributes': 'extension_attributes',
            'id': 'id',
            'permissions': 'permissions',
            'role_name': 'role_name'
        }

        self._company_id = company_id
        self._extension_attributes = extension_attributes
        self._id = id
        self._permissions = permissions
        self._role_name = role_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompanyDataRoleInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The company-data-role-interface of this CompanyDataRoleInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_id(self):
        """Gets the company_id of this CompanyDataRoleInterface.

        Company id.

        :return: The company_id of this CompanyDataRoleInterface.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CompanyDataRoleInterface.

        Company id.

        :param company_id: The company_id of this CompanyDataRoleInterface.
        :type company_id: int
        """

        self._company_id = company_id

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CompanyDataRoleInterface.

        ExtensionInterface class for @see \\Magento\\Company\\Api\\Data\\RoleInterface

        :return: The extension_attributes of this CompanyDataRoleInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CompanyDataRoleInterface.

        ExtensionInterface class for @see \\Magento\\Company\\Api\\Data\\RoleInterface

        :param extension_attributes: The extension_attributes of this CompanyDataRoleInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this CompanyDataRoleInterface.

        Role id.

        :return: The id of this CompanyDataRoleInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyDataRoleInterface.

        Role id.

        :param id: The id of this CompanyDataRoleInterface.
        :type id: int
        """

        self._id = id

    @property
    def permissions(self):
        """Gets the permissions of this CompanyDataRoleInterface.

        Permissions.

        :return: The permissions of this CompanyDataRoleInterface.
        :rtype: List[CompanyDataPermissionInterface]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CompanyDataRoleInterface.

        Permissions.

        :param permissions: The permissions of this CompanyDataRoleInterface.
        :type permissions: List[CompanyDataPermissionInterface]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions

    @property
    def role_name(self):
        """Gets the role_name of this CompanyDataRoleInterface.

        Role name.

        :return: The role_name of this CompanyDataRoleInterface.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this CompanyDataRoleInterface.

        Role name.

        :param role_name: The role_name of this CompanyDataRoleInterface.
        :type role_name: str
        """

        self._role_name = role_name
