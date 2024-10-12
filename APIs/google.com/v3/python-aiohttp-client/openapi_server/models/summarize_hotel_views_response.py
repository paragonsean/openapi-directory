# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SummarizeHotelViewsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, last_feed_submission_time: str=None, last_manifest_update_time: str=None, live_on_google_property_count: str=None, matched_property_count: str=None, overclustered_property_count: str=None, overclustered_property_with_errors_count: str=None, unmatched_property_count: str=None, unmatched_property_with_errors_count: str=None):
        """SummarizeHotelViewsResponse - a model defined in OpenAPI

        :param last_feed_submission_time: The last_feed_submission_time of this SummarizeHotelViewsResponse.
        :param last_manifest_update_time: The last_manifest_update_time of this SummarizeHotelViewsResponse.
        :param live_on_google_property_count: The live_on_google_property_count of this SummarizeHotelViewsResponse.
        :param matched_property_count: The matched_property_count of this SummarizeHotelViewsResponse.
        :param overclustered_property_count: The overclustered_property_count of this SummarizeHotelViewsResponse.
        :param overclustered_property_with_errors_count: The overclustered_property_with_errors_count of this SummarizeHotelViewsResponse.
        :param unmatched_property_count: The unmatched_property_count of this SummarizeHotelViewsResponse.
        :param unmatched_property_with_errors_count: The unmatched_property_with_errors_count of this SummarizeHotelViewsResponse.
        """
        self.openapi_types = {
            'last_feed_submission_time': str,
            'last_manifest_update_time': str,
            'live_on_google_property_count': str,
            'matched_property_count': str,
            'overclustered_property_count': str,
            'overclustered_property_with_errors_count': str,
            'unmatched_property_count': str,
            'unmatched_property_with_errors_count': str
        }

        self.attribute_map = {
            'last_feed_submission_time': 'lastFeedSubmissionTime',
            'last_manifest_update_time': 'lastManifestUpdateTime',
            'live_on_google_property_count': 'liveOnGooglePropertyCount',
            'matched_property_count': 'matchedPropertyCount',
            'overclustered_property_count': 'overclusteredPropertyCount',
            'overclustered_property_with_errors_count': 'overclusteredPropertyWithErrorsCount',
            'unmatched_property_count': 'unmatchedPropertyCount',
            'unmatched_property_with_errors_count': 'unmatchedPropertyWithErrorsCount'
        }

        self._last_feed_submission_time = last_feed_submission_time
        self._last_manifest_update_time = last_manifest_update_time
        self._live_on_google_property_count = live_on_google_property_count
        self._matched_property_count = matched_property_count
        self._overclustered_property_count = overclustered_property_count
        self._overclustered_property_with_errors_count = overclustered_property_with_errors_count
        self._unmatched_property_count = unmatched_property_count
        self._unmatched_property_with_errors_count = unmatched_property_with_errors_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SummarizeHotelViewsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SummarizeHotelViewsResponse of this SummarizeHotelViewsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_feed_submission_time(self):
        """Gets the last_feed_submission_time of this SummarizeHotelViewsResponse.

        Timestamp of the last hotel feed submission.

        :return: The last_feed_submission_time of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._last_feed_submission_time

    @last_feed_submission_time.setter
    def last_feed_submission_time(self, last_feed_submission_time):
        """Sets the last_feed_submission_time of this SummarizeHotelViewsResponse.

        Timestamp of the last hotel feed submission.

        :param last_feed_submission_time: The last_feed_submission_time of this SummarizeHotelViewsResponse.
        :type last_feed_submission_time: str
        """

        self._last_feed_submission_time = last_feed_submission_time

    @property
    def last_manifest_update_time(self):
        """Gets the last_manifest_update_time of this SummarizeHotelViewsResponse.

        Timestamp of the last hotel manifest update.

        :return: The last_manifest_update_time of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._last_manifest_update_time

    @last_manifest_update_time.setter
    def last_manifest_update_time(self, last_manifest_update_time):
        """Sets the last_manifest_update_time of this SummarizeHotelViewsResponse.

        Timestamp of the last hotel manifest update.

        :param last_manifest_update_time: The last_manifest_update_time of this SummarizeHotelViewsResponse.
        :type last_manifest_update_time: str
        """

        self._last_manifest_update_time = last_manifest_update_time

    @property
    def live_on_google_property_count(self):
        """Gets the live_on_google_property_count of this SummarizeHotelViewsResponse.

        The number of properties that are Live on Google.

        :return: The live_on_google_property_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._live_on_google_property_count

    @live_on_google_property_count.setter
    def live_on_google_property_count(self, live_on_google_property_count):
        """Sets the live_on_google_property_count of this SummarizeHotelViewsResponse.

        The number of properties that are Live on Google.

        :param live_on_google_property_count: The live_on_google_property_count of this SummarizeHotelViewsResponse.
        :type live_on_google_property_count: str
        """

        self._live_on_google_property_count = live_on_google_property_count

    @property
    def matched_property_count(self):
        """Gets the matched_property_count of this SummarizeHotelViewsResponse.

        The number of properties that match Google's manifest.

        :return: The matched_property_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._matched_property_count

    @matched_property_count.setter
    def matched_property_count(self, matched_property_count):
        """Sets the matched_property_count of this SummarizeHotelViewsResponse.

        The number of properties that match Google's manifest.

        :param matched_property_count: The matched_property_count of this SummarizeHotelViewsResponse.
        :type matched_property_count: str
        """

        self._matched_property_count = matched_property_count

    @property
    def overclustered_property_count(self):
        """Gets the overclustered_property_count of this SummarizeHotelViewsResponse.

        The number of hotels that are considered overclustered.

        :return: The overclustered_property_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._overclustered_property_count

    @overclustered_property_count.setter
    def overclustered_property_count(self, overclustered_property_count):
        """Sets the overclustered_property_count of this SummarizeHotelViewsResponse.

        The number of hotels that are considered overclustered.

        :param overclustered_property_count: The overclustered_property_count of this SummarizeHotelViewsResponse.
        :type overclustered_property_count: str
        """

        self._overclustered_property_count = overclustered_property_count

    @property
    def overclustered_property_with_errors_count(self):
        """Gets the overclustered_property_with_errors_count of this SummarizeHotelViewsResponse.

        The number of overclustered properties that have data-related errors.

        :return: The overclustered_property_with_errors_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._overclustered_property_with_errors_count

    @overclustered_property_with_errors_count.setter
    def overclustered_property_with_errors_count(self, overclustered_property_with_errors_count):
        """Sets the overclustered_property_with_errors_count of this SummarizeHotelViewsResponse.

        The number of overclustered properties that have data-related errors.

        :param overclustered_property_with_errors_count: The overclustered_property_with_errors_count of this SummarizeHotelViewsResponse.
        :type overclustered_property_with_errors_count: str
        """

        self._overclustered_property_with_errors_count = overclustered_property_with_errors_count

    @property
    def unmatched_property_count(self):
        """Gets the unmatched_property_count of this SummarizeHotelViewsResponse.

        The number of properties that are considered unmatched.

        :return: The unmatched_property_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._unmatched_property_count

    @unmatched_property_count.setter
    def unmatched_property_count(self, unmatched_property_count):
        """Sets the unmatched_property_count of this SummarizeHotelViewsResponse.

        The number of properties that are considered unmatched.

        :param unmatched_property_count: The unmatched_property_count of this SummarizeHotelViewsResponse.
        :type unmatched_property_count: str
        """

        self._unmatched_property_count = unmatched_property_count

    @property
    def unmatched_property_with_errors_count(self):
        """Gets the unmatched_property_with_errors_count of this SummarizeHotelViewsResponse.

        The number of unmatched properties that have data-related errors.

        :return: The unmatched_property_with_errors_count of this SummarizeHotelViewsResponse.
        :rtype: str
        """
        return self._unmatched_property_with_errors_count

    @unmatched_property_with_errors_count.setter
    def unmatched_property_with_errors_count(self, unmatched_property_with_errors_count):
        """Sets the unmatched_property_with_errors_count of this SummarizeHotelViewsResponse.

        The number of unmatched properties that have data-related errors.

        :param unmatched_property_with_errors_count: The unmatched_property_with_errors_count of this SummarizeHotelViewsResponse.
        :type unmatched_property_with_errors_count: str
        """

        self._unmatched_property_with_errors_count = unmatched_property_with_errors_count
