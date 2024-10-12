# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiV1AccountsUpdateCredentialsPatchRequestSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, language: str=None, privacy: str=None, sensitive: bool=None):
        """ApiV1AccountsUpdateCredentialsPatchRequestSource - a model defined in OpenAPI

        :param language: The language of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :param privacy: The privacy of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :param sensitive: The sensitive of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        """
        self.openapi_types = {
            'language': str,
            'privacy': str,
            'sensitive': bool
        }

        self.attribute_map = {
            'language': 'language',
            'privacy': 'privacy',
            'sensitive': 'sensitive'
        }

        self._language = language
        self._privacy = privacy
        self._sensitive = sensitive

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiV1AccountsUpdateCredentialsPatchRequestSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _api_v1_accounts_update_credentials_patch_request_source of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def language(self):
        """Gets the language of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Default language to use for authored statuses. (ISO 6391)

        :return: The language of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Default language to use for authored statuses. (ISO 6391)

        :param language: The language of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :type language: str
        """

        self._language = language

    @property
    def privacy(self):
        """Gets the privacy of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Default post privacy for authored statuses.

        :return: The privacy of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Default post privacy for authored statuses.

        :param privacy: The privacy of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :type privacy: str
        """

        self._privacy = privacy

    @property
    def sensitive(self):
        """Gets the sensitive of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Whether to mark authored statuses as sensitive by default.

        :return: The sensitive of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this ApiV1AccountsUpdateCredentialsPatchRequestSource.

        Whether to mark authored statuses as sensitive by default.

        :param sensitive: The sensitive of this ApiV1AccountsUpdateCredentialsPatchRequestSource.
        :type sensitive: bool
        """

        self._sensitive = sensitive
