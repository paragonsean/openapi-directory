# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EmailListAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, emails: List[str]=None, modified: datetime=None, name: str=None):
        """EmailListAttributes - a model defined in OpenAPI

        :param created: The created of this EmailListAttributes.
        :param emails: The emails of this EmailListAttributes.
        :param modified: The modified of this EmailListAttributes.
        :param name: The name of this EmailListAttributes.
        """
        self.openapi_types = {
            'created': datetime,
            'emails': List[str],
            'modified': datetime,
            'name': str
        }

        self.attribute_map = {
            'created': 'created',
            'emails': 'emails',
            'modified': 'modified',
            'name': 'name'
        }

        self._created = created
        self._emails = emails
        self._modified = modified
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EmailListAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EmailListAttributes of this EmailListAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this EmailListAttributes.

        Created datetime

        :return: The created of this EmailListAttributes.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EmailListAttributes.

        Created datetime

        :param created: The created of this EmailListAttributes.
        :type created: datetime
        """

        self._created = created

    @property
    def emails(self):
        """Gets the emails of this EmailListAttributes.

        Recipient emails in the email list

        :return: The emails of this EmailListAttributes.
        :rtype: List[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this EmailListAttributes.

        Recipient emails in the email list

        :param emails: The emails of this EmailListAttributes.
        :type emails: List[str]
        """

        self._emails = emails

    @property
    def modified(self):
        """Gets the modified of this EmailListAttributes.

        Modified datetime

        :return: The modified of this EmailListAttributes.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this EmailListAttributes.

        Modified datetime

        :param modified: The modified of this EmailListAttributes.
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this EmailListAttributes.

        Short title for email list

        :return: The name of this EmailListAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailListAttributes.

        Short title for email list

        :param name: The name of this EmailListAttributes.
        :type name: str
        """

        self._name = name
