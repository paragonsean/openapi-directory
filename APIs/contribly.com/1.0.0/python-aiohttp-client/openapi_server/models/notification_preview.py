# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NotificationPreview(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email: str=None, html: str=None, subject: str=None):
        """NotificationPreview - a model defined in OpenAPI

        :param email: The email of this NotificationPreview.
        :param html: The html of this NotificationPreview.
        :param subject: The subject of this NotificationPreview.
        """
        self.openapi_types = {
            'email': str,
            'html': str,
            'subject': str
        }

        self.attribute_map = {
            'email': 'email',
            'html': 'html',
            'subject': 'subject'
        }

        self._email = email
        self._html = html
        self._subject = subject

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationPreview':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationPreview of this NotificationPreview.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this NotificationPreview.


        :return: The email of this NotificationPreview.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NotificationPreview.


        :param email: The email of this NotificationPreview.
        :type email: str
        """

        self._email = email

    @property
    def html(self):
        """Gets the html of this NotificationPreview.


        :return: The html of this NotificationPreview.
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this NotificationPreview.


        :param html: The html of this NotificationPreview.
        :type html: str
        """

        self._html = html

    @property
    def subject(self):
        """Gets the subject of this NotificationPreview.


        :return: The subject of this NotificationPreview.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NotificationPreview.


        :param subject: The subject of this NotificationPreview.
        :type subject: str
        """

        self._subject = subject
