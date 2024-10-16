# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PostRestoreAppRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, responsible_admin_id: str=None):
        """PostRestoreAppRequest - a model defined in OpenAPI

        :param responsible_admin_id: The responsible_admin_id of this PostRestoreAppRequest.
        """
        self.openapi_types = {
            'responsible_admin_id': str
        }

        self.attribute_map = {
            'responsible_admin_id': 'responsibleAdminId'
        }

        self._responsible_admin_id = responsible_admin_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PostRestoreAppRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PostRestoreAppRequest of this PostRestoreAppRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def responsible_admin_id(self):
        """Gets the responsible_admin_id of this PostRestoreAppRequest.

        The internal unique id (UUID) of the account of the user, who makes the request.

        :return: The responsible_admin_id of this PostRestoreAppRequest.
        :rtype: str
        """
        return self._responsible_admin_id

    @responsible_admin_id.setter
    def responsible_admin_id(self, responsible_admin_id):
        """Sets the responsible_admin_id of this PostRestoreAppRequest.

        The internal unique id (UUID) of the account of the user, who makes the request.

        :param responsible_admin_id: The responsible_admin_id of this PostRestoreAppRequest.
        :type responsible_admin_id: str
        """
        if responsible_admin_id is None:
            raise ValueError("Invalid value for `responsible_admin_id`, must not be `None`")

        self._responsible_admin_id = responsible_admin_id
