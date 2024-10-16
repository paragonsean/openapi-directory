# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProjectStatusType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, locale: str=None, created: str=None, created_by_id: str=None, deleted: str=None, description: str=None, id: str=None, identifier: str=None, modified: str=None, name: str=None):
        """ProjectStatusType - a model defined in OpenAPI

        :param locale: The locale of this ProjectStatusType.
        :param created: The created of this ProjectStatusType.
        :param created_by_id: The created_by_id of this ProjectStatusType.
        :param deleted: The deleted of this ProjectStatusType.
        :param description: The description of this ProjectStatusType.
        :param id: The id of this ProjectStatusType.
        :param identifier: The identifier of this ProjectStatusType.
        :param modified: The modified of this ProjectStatusType.
        :param name: The name of this ProjectStatusType.
        """
        self.openapi_types = {
            'locale': str,
            'created': str,
            'created_by_id': str,
            'deleted': str,
            'description': str,
            'id': str,
            'identifier': str,
            'modified': str,
            'name': str
        }

        self.attribute_map = {
            'locale': '_locale',
            'created': 'created',
            'created_by_id': 'created_by_id',
            'deleted': 'deleted',
            'description': 'description',
            'id': 'id',
            'identifier': 'identifier',
            'modified': 'modified',
            'name': 'name'
        }

        self._locale = locale
        self._created = created
        self._created_by_id = created_by_id
        self._deleted = deleted
        self._description = description
        self._id = id
        self._identifier = identifier
        self._modified = modified
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectStatusType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectStatusType of this ProjectStatusType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def locale(self):
        """Gets the locale of this ProjectStatusType.


        :return: The locale of this ProjectStatusType.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ProjectStatusType.


        :param locale: The locale of this ProjectStatusType.
        :type locale: str
        """

        self._locale = locale

    @property
    def created(self):
        """Gets the created of this ProjectStatusType.


        :return: The created of this ProjectStatusType.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ProjectStatusType.


        :param created: The created of this ProjectStatusType.
        :type created: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProjectStatusType.


        :return: The created_by_id of this ProjectStatusType.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProjectStatusType.


        :param created_by_id: The created_by_id of this ProjectStatusType.
        :type created_by_id: str
        """

        self._created_by_id = created_by_id

    @property
    def deleted(self):
        """Gets the deleted of this ProjectStatusType.

        Only present if it's a deleted object

        :return: The deleted of this ProjectStatusType.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ProjectStatusType.

        Only present if it's a deleted object

        :param deleted: The deleted of this ProjectStatusType.
        :type deleted: str
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this ProjectStatusType.


        :return: The description of this ProjectStatusType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectStatusType.


        :param description: The description of this ProjectStatusType.
        :type description: str
        """
        if description is not None and len(description) > 8192:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")

        self._description = description

    @property
    def id(self):
        """Gets the id of this ProjectStatusType.


        :return: The id of this ProjectStatusType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectStatusType.


        :param id: The id of this ProjectStatusType.
        :type id: str
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this ProjectStatusType.


        :return: The identifier of this ProjectStatusType.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ProjectStatusType.


        :param identifier: The identifier of this ProjectStatusType.
        :type identifier: str
        """
        if identifier is not None and len(identifier) > 255:
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `255`")

        self._identifier = identifier

    @property
    def modified(self):
        """Gets the modified of this ProjectStatusType.


        :return: The modified of this ProjectStatusType.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ProjectStatusType.


        :param modified: The modified of this ProjectStatusType.
        :type modified: str
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this ProjectStatusType.


        :return: The name of this ProjectStatusType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectStatusType.


        :param name: The name of this ProjectStatusType.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")

        self._name = name
