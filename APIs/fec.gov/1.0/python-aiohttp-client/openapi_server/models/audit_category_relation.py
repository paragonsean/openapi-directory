# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AuditCategoryRelation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sub_category_id: str=None, sub_category_name: str=None):
        """AuditCategoryRelation - a model defined in OpenAPI

        :param sub_category_id: The sub_category_id of this AuditCategoryRelation.
        :param sub_category_name: The sub_category_name of this AuditCategoryRelation.
        """
        self.openapi_types = {
            'sub_category_id': str,
            'sub_category_name': str
        }

        self.attribute_map = {
            'sub_category_id': 'sub_category_id',
            'sub_category_name': 'sub_category_name'
        }

        self._sub_category_id = sub_category_id
        self._sub_category_name = sub_category_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuditCategoryRelation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuditCategoryRelation of this AuditCategoryRelation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_category_id(self):
        """Gets the sub_category_id of this AuditCategoryRelation.


        :return: The sub_category_id of this AuditCategoryRelation.
        :rtype: str
        """
        return self._sub_category_id

    @sub_category_id.setter
    def sub_category_id(self, sub_category_id):
        """Sets the sub_category_id of this AuditCategoryRelation.


        :param sub_category_id: The sub_category_id of this AuditCategoryRelation.
        :type sub_category_id: str
        """

        self._sub_category_id = sub_category_id

    @property
    def sub_category_name(self):
        """Gets the sub_category_name of this AuditCategoryRelation.


        :return: The sub_category_name of this AuditCategoryRelation.
        :rtype: str
        """
        return self._sub_category_name

    @sub_category_name.setter
    def sub_category_name(self, sub_category_name):
        """Sets the sub_category_name of this AuditCategoryRelation.


        :param sub_category_name: The sub_category_name of this AuditCategoryRelation.
        :type sub_category_name: str
        """

        self._sub_category_name = sub_category_name
