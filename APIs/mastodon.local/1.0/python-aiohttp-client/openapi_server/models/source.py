# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.model_field import ModelField
from openapi_server import util


class Source(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fields: List[ModelField]=None, follow_requests_count: int=None, language: str=None, note: str=None, privacy: str=None, sensitive: bool=None):
        """Source - a model defined in OpenAPI

        :param fields: The fields of this Source.
        :param follow_requests_count: The follow_requests_count of this Source.
        :param language: The language of this Source.
        :param note: The note of this Source.
        :param privacy: The privacy of this Source.
        :param sensitive: The sensitive of this Source.
        """
        self.openapi_types = {
            'fields': List[ModelField],
            'follow_requests_count': int,
            'language': str,
            'note': str,
            'privacy': str,
            'sensitive': bool
        }

        self.attribute_map = {
            'fields': 'fields',
            'follow_requests_count': 'follow_requests_count',
            'language': 'language',
            'note': 'note',
            'privacy': 'privacy',
            'sensitive': 'sensitive'
        }

        self._fields = fields
        self._follow_requests_count = follow_requests_count
        self._language = language
        self._note = note
        self._privacy = privacy
        self._sensitive = sensitive

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Source':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Source of this Source.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fields(self):
        """Gets the fields of this Source.

        Metadata about the account.

        :return: The fields of this Source.
        :rtype: List[ModelField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Source.

        Metadata about the account.

        :param fields: The fields of this Source.
        :type fields: List[ModelField]
        """

        self._fields = fields

    @property
    def follow_requests_count(self):
        """Gets the follow_requests_count of this Source.

        The number of pending follow requests

        :return: The follow_requests_count of this Source.
        :rtype: int
        """
        return self._follow_requests_count

    @follow_requests_count.setter
    def follow_requests_count(self, follow_requests_count):
        """Sets the follow_requests_count of this Source.

        The number of pending follow requests

        :param follow_requests_count: The follow_requests_count of this Source.
        :type follow_requests_count: int
        """

        self._follow_requests_count = follow_requests_count

    @property
    def language(self):
        """Gets the language of this Source.

        The default posting language for new statuses, ISO 639-1 language two-letter code.

        :return: The language of this Source.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Source.

        The default posting language for new statuses, ISO 639-1 language two-letter code.

        :param language: The language of this Source.
        :type language: str
        """

        self._language = language

    @property
    def note(self):
        """Gets the note of this Source.

        Profile bio

        :return: The note of this Source.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Source.

        Profile bio

        :param note: The note of this Source.
        :type note: str
        """

        self._note = note

    @property
    def privacy(self):
        """Gets the privacy of this Source.

        The default post privacy to be used for new statuses.

        :return: The privacy of this Source.
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this Source.

        The default post privacy to be used for new statuses.

        :param privacy: The privacy of this Source.
        :type privacy: str
        """
        allowed_values = ["public", "unlisted", "private", "direct"]  # noqa: E501
        if privacy not in allowed_values:
            raise ValueError(
                "Invalid value for `privacy` ({0}), must be one of {1}"
                .format(privacy, allowed_values)
            )

        self._privacy = privacy

    @property
    def sensitive(self):
        """Gets the sensitive of this Source.

        Whether new statuses should be marked sensitive by default.

        :return: The sensitive of this Source.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this Source.

        Whether new statuses should be marked sensitive by default.

        :param sensitive: The sensitive of this Source.
        :type sensitive: bool
        """

        self._sensitive = sensitive
