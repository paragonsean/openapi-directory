# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.audit_category_relation import AuditCategoryRelation
from openapi_server import util


class AuditCategory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, primary_category_id: str=None, primary_category_name: str=None, sub_category_list: List[AuditCategoryRelation]=None):
        """AuditCategory - a model defined in OpenAPI

        :param primary_category_id: The primary_category_id of this AuditCategory.
        :param primary_category_name: The primary_category_name of this AuditCategory.
        :param sub_category_list: The sub_category_list of this AuditCategory.
        """
        self.openapi_types = {
            'primary_category_id': str,
            'primary_category_name': str,
            'sub_category_list': List[AuditCategoryRelation]
        }

        self.attribute_map = {
            'primary_category_id': 'primary_category_id',
            'primary_category_name': 'primary_category_name',
            'sub_category_list': 'sub_category_list'
        }

        self._primary_category_id = primary_category_id
        self._primary_category_name = primary_category_name
        self._sub_category_list = sub_category_list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuditCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuditCategory of this AuditCategory.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def primary_category_id(self):
        """Gets the primary_category_id of this AuditCategory.


        :return: The primary_category_id of this AuditCategory.
        :rtype: str
        """
        return self._primary_category_id

    @primary_category_id.setter
    def primary_category_id(self, primary_category_id):
        """Sets the primary_category_id of this AuditCategory.


        :param primary_category_id: The primary_category_id of this AuditCategory.
        :type primary_category_id: str
        """

        self._primary_category_id = primary_category_id

    @property
    def primary_category_name(self):
        """Gets the primary_category_name of this AuditCategory.


        :return: The primary_category_name of this AuditCategory.
        :rtype: str
        """
        return self._primary_category_name

    @primary_category_name.setter
    def primary_category_name(self, primary_category_name):
        """Sets the primary_category_name of this AuditCategory.


        :param primary_category_name: The primary_category_name of this AuditCategory.
        :type primary_category_name: str
        """

        self._primary_category_name = primary_category_name

    @property
    def sub_category_list(self):
        """Gets the sub_category_list of this AuditCategory.


        :return: The sub_category_list of this AuditCategory.
        :rtype: List[AuditCategoryRelation]
        """
        return self._sub_category_list

    @sub_category_list.setter
    def sub_category_list(self, sub_category_list):
        """Sets the sub_category_list of this AuditCategory.


        :param sub_category_list: The sub_category_list of this AuditCategory.
        :type sub_category_list: List[AuditCategoryRelation]
        """

        self._sub_category_list = sub_category_list
