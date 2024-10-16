# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner_counts_inner import GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner
from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner_editions_inner import GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner
from openapi_server import util


class GetOrganizationLicensingCotermLicenses200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, claimed_at: datetime=None, counts: List[GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner]=None, duration: int=None, editions: List[GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner]=None, expired: bool=None, invalidated: bool=None, invalidated_at: datetime=None, key: str=None, mode: str=None, organization_id: str=None, started_at: datetime=None):
        """GetOrganizationLicensingCotermLicenses200ResponseInner - a model defined in OpenAPI

        :param claimed_at: The claimed_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param counts: The counts of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param duration: The duration of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param editions: The editions of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param expired: The expired of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param invalidated: The invalidated of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param invalidated_at: The invalidated_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param key: The key of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param mode: The mode of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param organization_id: The organization_id of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :param started_at: The started_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        """
        self.openapi_types = {
            'claimed_at': datetime,
            'counts': List[GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner],
            'duration': int,
            'editions': List[GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner],
            'expired': bool,
            'invalidated': bool,
            'invalidated_at': datetime,
            'key': str,
            'mode': str,
            'organization_id': str,
            'started_at': datetime
        }

        self.attribute_map = {
            'claimed_at': 'claimedAt',
            'counts': 'counts',
            'duration': 'duration',
            'editions': 'editions',
            'expired': 'expired',
            'invalidated': 'invalidated',
            'invalidated_at': 'invalidatedAt',
            'key': 'key',
            'mode': 'mode',
            'organization_id': 'organizationId',
            'started_at': 'startedAt'
        }

        self._claimed_at = claimed_at
        self._counts = counts
        self._duration = duration
        self._editions = editions
        self._expired = expired
        self._invalidated = invalidated
        self._invalidated_at = invalidated_at
        self._key = key
        self._mode = mode
        self._organization_id = organization_id
        self._started_at = started_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationLicensingCotermLicenses200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationLicensingCotermLicenses_200_response_inner of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claimed_at(self):
        """Gets the claimed_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license was claimed into the organization

        :return: The claimed_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: datetime
        """
        return self._claimed_at

    @claimed_at.setter
    def claimed_at(self, claimed_at):
        """Sets the claimed_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license was claimed into the organization

        :param claimed_at: The claimed_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type claimed_at: datetime
        """

        self._claimed_at = claimed_at

    @property
    def counts(self):
        """Gets the counts of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The counts of the license by model type

        :return: The counts of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: List[GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The counts of the license by model type

        :param counts: The counts of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type counts: List[GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner]
        """

        self._counts = counts

    @property
    def duration(self):
        """Gets the duration of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The duration (term length) of the license, measured in days

        :return: The duration of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The duration (term length) of the license, measured in days

        :param duration: The duration of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type duration: int
        """

        self._duration = duration

    @property
    def editions(self):
        """Gets the editions of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The editions of the license for each relevant product type

        :return: The editions of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: List[GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner]
        """
        return self._editions

    @editions.setter
    def editions(self, editions):
        """Sets the editions of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The editions of the license for each relevant product type

        :param editions: The editions of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type editions: List[GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner]
        """

        self._editions = editions

    @property
    def expired(self):
        """Gets the expired of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        Flag to indicate if the license is expired

        :return: The expired of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        Flag to indicate if the license is expired

        :param expired: The expired of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type expired: bool
        """

        self._expired = expired

    @property
    def invalidated(self):
        """Gets the invalidated of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        Flag to indicated that the license is invalidated

        :return: The invalidated of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: bool
        """
        return self._invalidated

    @invalidated.setter
    def invalidated(self, invalidated):
        """Sets the invalidated of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        Flag to indicated that the license is invalidated

        :param invalidated: The invalidated of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type invalidated: bool
        """

        self._invalidated = invalidated

    @property
    def invalidated_at(self):
        """Gets the invalidated_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license was invalidated. Will be null for active licenses

        :return: The invalidated_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: datetime
        """
        return self._invalidated_at

    @invalidated_at.setter
    def invalidated_at(self, invalidated_at):
        """Sets the invalidated_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license was invalidated. Will be null for active licenses

        :param invalidated_at: The invalidated_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type invalidated_at: datetime
        """

        self._invalidated_at = invalidated_at

    @property
    def key(self):
        """Gets the key of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The key of the license

        :return: The key of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The key of the license

        :param key: The key of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type key: str
        """

        self._key = key

    @property
    def mode(self):
        """Gets the mode of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The operation mode of the license when it was claimed

        :return: The mode of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The operation mode of the license when it was claimed

        :param mode: The mode of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type mode: str
        """
        allowed_values = ["addDevices", "renew"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def organization_id(self):
        """Gets the organization_id of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The ID of the organization that the license is claimed in

        :return: The organization_id of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        The ID of the organization that the license is claimed in

        :param organization_id: The organization_id of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type organization_id: str
        """

        self._organization_id = organization_id

    @property
    def started_at(self):
        """Gets the started_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license's term began (approximately the date when the license was created)

        :return: The started_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.

        When the license's term began (approximately the date when the license was created)

        :param started_at: The started_at of this GetOrganizationLicensingCotermLicenses200ResponseInner.
        :type started_at: datetime
        """

        self._started_at = started_at
