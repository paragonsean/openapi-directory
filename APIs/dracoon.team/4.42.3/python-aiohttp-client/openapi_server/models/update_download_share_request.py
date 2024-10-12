# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.object_expiration import ObjectExpiration
from openapi_server import util


class UpdateDownloadShareRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_country: str=None, expiration: ObjectExpiration=None, internal_notes: str=None, max_downloads: int=None, name: str=None, notes: str=None, notify_creator: bool=None, password: str=None, receiver_language: str=None, reset_max_downloads: bool=None, reset_password: bool=None, show_creator_name: bool=None, show_creator_username: bool=None, text_message_recipients: List[str]=None):
        """UpdateDownloadShareRequest - a model defined in OpenAPI

        :param default_country: The default_country of this UpdateDownloadShareRequest.
        :param expiration: The expiration of this UpdateDownloadShareRequest.
        :param internal_notes: The internal_notes of this UpdateDownloadShareRequest.
        :param max_downloads: The max_downloads of this UpdateDownloadShareRequest.
        :param name: The name of this UpdateDownloadShareRequest.
        :param notes: The notes of this UpdateDownloadShareRequest.
        :param notify_creator: The notify_creator of this UpdateDownloadShareRequest.
        :param password: The password of this UpdateDownloadShareRequest.
        :param receiver_language: The receiver_language of this UpdateDownloadShareRequest.
        :param reset_max_downloads: The reset_max_downloads of this UpdateDownloadShareRequest.
        :param reset_password: The reset_password of this UpdateDownloadShareRequest.
        :param show_creator_name: The show_creator_name of this UpdateDownloadShareRequest.
        :param show_creator_username: The show_creator_username of this UpdateDownloadShareRequest.
        :param text_message_recipients: The text_message_recipients of this UpdateDownloadShareRequest.
        """
        self.openapi_types = {
            'default_country': str,
            'expiration': ObjectExpiration,
            'internal_notes': str,
            'max_downloads': int,
            'name': str,
            'notes': str,
            'notify_creator': bool,
            'password': str,
            'receiver_language': str,
            'reset_max_downloads': bool,
            'reset_password': bool,
            'show_creator_name': bool,
            'show_creator_username': bool,
            'text_message_recipients': List[str]
        }

        self.attribute_map = {
            'default_country': 'defaultCountry',
            'expiration': 'expiration',
            'internal_notes': 'internalNotes',
            'max_downloads': 'maxDownloads',
            'name': 'name',
            'notes': 'notes',
            'notify_creator': 'notifyCreator',
            'password': 'password',
            'receiver_language': 'receiverLanguage',
            'reset_max_downloads': 'resetMaxDownloads',
            'reset_password': 'resetPassword',
            'show_creator_name': 'showCreatorName',
            'show_creator_username': 'showCreatorUsername',
            'text_message_recipients': 'textMessageRecipients'
        }

        self._default_country = default_country
        self._expiration = expiration
        self._internal_notes = internal_notes
        self._max_downloads = max_downloads
        self._name = name
        self._notes = notes
        self._notify_creator = notify_creator
        self._password = password
        self._receiver_language = receiver_language
        self._reset_max_downloads = reset_max_downloads
        self._reset_password = reset_password
        self._show_creator_name = show_creator_name
        self._show_creator_username = show_creator_username
        self._text_message_recipients = text_message_recipients

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateDownloadShareRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateDownloadShareRequest of this UpdateDownloadShareRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_country(self):
        """Gets the default_country of this UpdateDownloadShareRequest.

        Country shorthand symbol (cf. ISO 3166-2)

        :return: The default_country of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._default_country

    @default_country.setter
    def default_country(self, default_country):
        """Sets the default_country of this UpdateDownloadShareRequest.

        Country shorthand symbol (cf. ISO 3166-2)

        :param default_country: The default_country of this UpdateDownloadShareRequest.
        :type default_country: str
        """

        self._default_country = default_country

    @property
    def expiration(self):
        """Gets the expiration of this UpdateDownloadShareRequest.


        :return: The expiration of this UpdateDownloadShareRequest.
        :rtype: ObjectExpiration
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this UpdateDownloadShareRequest.


        :param expiration: The expiration of this UpdateDownloadShareRequest.
        :type expiration: ObjectExpiration
        """

        self._expiration = expiration

    @property
    def internal_notes(self):
        """Gets the internal_notes of this UpdateDownloadShareRequest.

        &#128640; Since v4.11.0  Internal notes

        :return: The internal_notes of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._internal_notes

    @internal_notes.setter
    def internal_notes(self, internal_notes):
        """Sets the internal_notes of this UpdateDownloadShareRequest.

        &#128640; Since v4.11.0  Internal notes

        :param internal_notes: The internal_notes of this UpdateDownloadShareRequest.
        :type internal_notes: str
        """

        self._internal_notes = internal_notes

    @property
    def max_downloads(self):
        """Gets the max_downloads of this UpdateDownloadShareRequest.

        Max allowed downloads

        :return: The max_downloads of this UpdateDownloadShareRequest.
        :rtype: int
        """
        return self._max_downloads

    @max_downloads.setter
    def max_downloads(self, max_downloads):
        """Sets the max_downloads of this UpdateDownloadShareRequest.

        Max allowed downloads

        :param max_downloads: The max_downloads of this UpdateDownloadShareRequest.
        :type max_downloads: int
        """

        self._max_downloads = max_downloads

    @property
    def name(self):
        """Gets the name of this UpdateDownloadShareRequest.

        Alias name

        :return: The name of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDownloadShareRequest.

        Alias name

        :param name: The name of this UpdateDownloadShareRequest.
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this UpdateDownloadShareRequest.

        User notes

        :return: The notes of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UpdateDownloadShareRequest.

        User notes

        :param notes: The notes of this UpdateDownloadShareRequest.
        :type notes: str
        """

        self._notes = notes

    @property
    def notify_creator(self):
        """Gets the notify_creator of this UpdateDownloadShareRequest.

        &#128679; Deprecated since v4.20.0  Notify creator on every download.

        :return: The notify_creator of this UpdateDownloadShareRequest.
        :rtype: bool
        """
        return self._notify_creator

    @notify_creator.setter
    def notify_creator(self, notify_creator):
        """Sets the notify_creator of this UpdateDownloadShareRequest.

        &#128679; Deprecated since v4.20.0  Notify creator on every download.

        :param notify_creator: The notify_creator of this UpdateDownloadShareRequest.
        :type notify_creator: bool
        """

        self._notify_creator = notify_creator

    @property
    def password(self):
        """Gets the password of this UpdateDownloadShareRequest.

        Access password, not allowed for encrypted shares

        :return: The password of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateDownloadShareRequest.

        Access password, not allowed for encrypted shares

        :param password: The password of this UpdateDownloadShareRequest.
        :type password: str
        """

        self._password = password

    @property
    def receiver_language(self):
        """Gets the receiver_language of this UpdateDownloadShareRequest.

        Language tag for messages to receiver

        :return: The receiver_language of this UpdateDownloadShareRequest.
        :rtype: str
        """
        return self._receiver_language

    @receiver_language.setter
    def receiver_language(self, receiver_language):
        """Sets the receiver_language of this UpdateDownloadShareRequest.

        Language tag for messages to receiver

        :param receiver_language: The receiver_language of this UpdateDownloadShareRequest.
        :type receiver_language: str
        """

        self._receiver_language = receiver_language

    @property
    def reset_max_downloads(self):
        """Gets the reset_max_downloads of this UpdateDownloadShareRequest.

        Set 'true' to reset 'maxDownloads' for Download Share.

        :return: The reset_max_downloads of this UpdateDownloadShareRequest.
        :rtype: bool
        """
        return self._reset_max_downloads

    @reset_max_downloads.setter
    def reset_max_downloads(self, reset_max_downloads):
        """Sets the reset_max_downloads of this UpdateDownloadShareRequest.

        Set 'true' to reset 'maxDownloads' for Download Share.

        :param reset_max_downloads: The reset_max_downloads of this UpdateDownloadShareRequest.
        :type reset_max_downloads: bool
        """

        self._reset_max_downloads = reset_max_downloads

    @property
    def reset_password(self):
        """Gets the reset_password of this UpdateDownloadShareRequest.

        Set 'true' to reset 'password' for Download Share.

        :return: The reset_password of this UpdateDownloadShareRequest.
        :rtype: bool
        """
        return self._reset_password

    @reset_password.setter
    def reset_password(self, reset_password):
        """Sets the reset_password of this UpdateDownloadShareRequest.

        Set 'true' to reset 'password' for Download Share.

        :param reset_password: The reset_password of this UpdateDownloadShareRequest.
        :type reset_password: bool
        """

        self._reset_password = reset_password

    @property
    def show_creator_name(self):
        """Gets the show_creator_name of this UpdateDownloadShareRequest.

        Show creator first and last name.

        :return: The show_creator_name of this UpdateDownloadShareRequest.
        :rtype: bool
        """
        return self._show_creator_name

    @show_creator_name.setter
    def show_creator_name(self, show_creator_name):
        """Sets the show_creator_name of this UpdateDownloadShareRequest.

        Show creator first and last name.

        :param show_creator_name: The show_creator_name of this UpdateDownloadShareRequest.
        :type show_creator_name: bool
        """

        self._show_creator_name = show_creator_name

    @property
    def show_creator_username(self):
        """Gets the show_creator_username of this UpdateDownloadShareRequest.

        Show creator email address.

        :return: The show_creator_username of this UpdateDownloadShareRequest.
        :rtype: bool
        """
        return self._show_creator_username

    @show_creator_username.setter
    def show_creator_username(self, show_creator_username):
        """Sets the show_creator_username of this UpdateDownloadShareRequest.

        Show creator email address.

        :param show_creator_username: The show_creator_username of this UpdateDownloadShareRequest.
        :type show_creator_username: bool
        """

        self._show_creator_username = show_creator_username

    @property
    def text_message_recipients(self):
        """Gets the text_message_recipients of this UpdateDownloadShareRequest.

        List of recipient FQTNs  E.123 / E.164 Format

        :return: The text_message_recipients of this UpdateDownloadShareRequest.
        :rtype: List[str]
        """
        return self._text_message_recipients

    @text_message_recipients.setter
    def text_message_recipients(self, text_message_recipients):
        """Sets the text_message_recipients of this UpdateDownloadShareRequest.

        List of recipient FQTNs  E.123 / E.164 Format

        :param text_message_recipients: The text_message_recipients of this UpdateDownloadShareRequest.
        :type text_message_recipients: List[str]
        """

        self._text_message_recipients = text_message_recipients
