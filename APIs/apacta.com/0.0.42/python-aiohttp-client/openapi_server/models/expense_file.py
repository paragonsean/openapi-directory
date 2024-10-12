# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ExpenseFile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: str=None, created_by_id: str=None, deleted: str=None, description: str=None, expense_id: str=None, file: str=None, file_extension: str=None, file_original_name: str=None, file_size: str=None, file_type: str=None, file_url: str=None, id: str=None, modified: str=None):
        """ExpenseFile - a model defined in OpenAPI

        :param created: The created of this ExpenseFile.
        :param created_by_id: The created_by_id of this ExpenseFile.
        :param deleted: The deleted of this ExpenseFile.
        :param description: The description of this ExpenseFile.
        :param expense_id: The expense_id of this ExpenseFile.
        :param file: The file of this ExpenseFile.
        :param file_extension: The file_extension of this ExpenseFile.
        :param file_original_name: The file_original_name of this ExpenseFile.
        :param file_size: The file_size of this ExpenseFile.
        :param file_type: The file_type of this ExpenseFile.
        :param file_url: The file_url of this ExpenseFile.
        :param id: The id of this ExpenseFile.
        :param modified: The modified of this ExpenseFile.
        """
        self.openapi_types = {
            'created': str,
            'created_by_id': str,
            'deleted': str,
            'description': str,
            'expense_id': str,
            'file': str,
            'file_extension': str,
            'file_original_name': str,
            'file_size': str,
            'file_type': str,
            'file_url': str,
            'id': str,
            'modified': str
        }

        self.attribute_map = {
            'created': 'created',
            'created_by_id': 'created_by_id',
            'deleted': 'deleted',
            'description': 'description',
            'expense_id': 'expense_id',
            'file': 'file',
            'file_extension': 'file_extension',
            'file_original_name': 'file_original_name',
            'file_size': 'file_size',
            'file_type': 'file_type',
            'file_url': 'file_url',
            'id': 'id',
            'modified': 'modified'
        }

        self._created = created
        self._created_by_id = created_by_id
        self._deleted = deleted
        self._description = description
        self._expense_id = expense_id
        self._file = file
        self._file_extension = file_extension
        self._file_original_name = file_original_name
        self._file_size = file_size
        self._file_type = file_type
        self._file_url = file_url
        self._id = id
        self._modified = modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpenseFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExpenseFile of this ExpenseFile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this ExpenseFile.


        :return: The created of this ExpenseFile.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ExpenseFile.


        :param created: The created of this ExpenseFile.
        :type created: str
        """

        self._created = created

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ExpenseFile.

        Read-only

        :return: The created_by_id of this ExpenseFile.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ExpenseFile.

        Read-only

        :param created_by_id: The created_by_id of this ExpenseFile.
        :type created_by_id: str
        """

        self._created_by_id = created_by_id

    @property
    def deleted(self):
        """Gets the deleted of this ExpenseFile.

        Only present if it's a deleted object

        :return: The deleted of this ExpenseFile.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ExpenseFile.

        Only present if it's a deleted object

        :param deleted: The deleted of this ExpenseFile.
        :type deleted: str
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this ExpenseFile.


        :return: The description of this ExpenseFile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpenseFile.


        :param description: The description of this ExpenseFile.
        :type description: str
        """
        if description is not None and len(description) > 8192:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")

        self._description = description

    @property
    def expense_id(self):
        """Gets the expense_id of this ExpenseFile.


        :return: The expense_id of this ExpenseFile.
        :rtype: str
        """
        return self._expense_id

    @expense_id.setter
    def expense_id(self, expense_id):
        """Sets the expense_id of this ExpenseFile.


        :param expense_id: The expense_id of this ExpenseFile.
        :type expense_id: str
        """

        self._expense_id = expense_id

    @property
    def file(self):
        """Gets the file of this ExpenseFile.

        File's name

        :return: The file of this ExpenseFile.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ExpenseFile.

        File's name

        :param file: The file of this ExpenseFile.
        :type file: str
        """
        if file is not None and len(file) > 255:
            raise ValueError("Invalid value for `file`, length must be less than or equal to `255`")

        self._file = file

    @property
    def file_extension(self):
        """Gets the file_extension of this ExpenseFile.


        :return: The file_extension of this ExpenseFile.
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this ExpenseFile.


        :param file_extension: The file_extension of this ExpenseFile.
        :type file_extension: str
        """
        if file_extension is not None and len(file_extension) > 255:
            raise ValueError("Invalid value for `file_extension`, length must be less than or equal to `255`")

        self._file_extension = file_extension

    @property
    def file_original_name(self):
        """Gets the file_original_name of this ExpenseFile.


        :return: The file_original_name of this ExpenseFile.
        :rtype: str
        """
        return self._file_original_name

    @file_original_name.setter
    def file_original_name(self, file_original_name):
        """Sets the file_original_name of this ExpenseFile.


        :param file_original_name: The file_original_name of this ExpenseFile.
        :type file_original_name: str
        """
        if file_original_name is not None and len(file_original_name) > 255:
            raise ValueError("Invalid value for `file_original_name`, length must be less than or equal to `255`")

        self._file_original_name = file_original_name

    @property
    def file_size(self):
        """Gets the file_size of this ExpenseFile.

        File size in bytes

        :return: The file_size of this ExpenseFile.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ExpenseFile.

        File size in bytes

        :param file_size: The file_size of this ExpenseFile.
        :type file_size: str
        """
        if file_size is not None and len(file_size) > 255:
            raise ValueError("Invalid value for `file_size`, length must be less than or equal to `255`")

        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this ExpenseFile.

        File's MIME type

        :return: The file_type of this ExpenseFile.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ExpenseFile.

        File's MIME type

        :param file_type: The file_type of this ExpenseFile.
        :type file_type: str
        """
        if file_type is not None and len(file_type) > 255:
            raise ValueError("Invalid value for `file_type`, length must be less than or equal to `255`")

        self._file_type = file_type

    @property
    def file_url(self):
        """Gets the file_url of this ExpenseFile.

        Read-only

        :return: The file_url of this ExpenseFile.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this ExpenseFile.

        Read-only

        :param file_url: The file_url of this ExpenseFile.
        :type file_url: str
        """
        if file_url is not None and len(file_url) > 255:
            raise ValueError("Invalid value for `file_url`, length must be less than or equal to `255`")

        self._file_url = file_url

    @property
    def id(self):
        """Gets the id of this ExpenseFile.

        Read-only

        :return: The id of this ExpenseFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpenseFile.

        Read-only

        :param id: The id of this ExpenseFile.
        :type id: str
        """

        self._id = id

    @property
    def modified(self):
        """Gets the modified of this ExpenseFile.


        :return: The modified of this ExpenseFile.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ExpenseFile.


        :param modified: The modified of this ExpenseFile.
        :type modified: str
        """

        self._modified = modified
