# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account import Account
from openapi_server.models.application import Application
from openapi_server.models.attachment import Attachment
from openapi_server.models.card import Card
from openapi_server.models.emoji import Emoji
from openapi_server.models.mention import Mention
from openapi_server.models.poll import Poll
from openapi_server.models.scheduled_status import ScheduledStatus
from openapi_server.models.status import Status
from openapi_server.models.status_params import StatusParams
from openapi_server.models.tag import Tag
from openapi_server import util


class ApiV1StatusesPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account: Account=None, application: Application=None, bookmarked: bool=None, card: Card=None, content: str=None, created_at: datetime=None, emojis: List[Emoji]=None, favourited: bool=None, favourites_count: int=None, id: str=None, in_reply_to_account_id: str=None, in_reply_to_id: str=None, language: str=None, media_attachments: List[Attachment]=None, mentions: List[Mention]=None, muted: bool=None, pinned: bool=None, poll: Poll=None, reblog: Status=None, reblogged: bool=None, reblogs_count: int=None, replies_count: int=None, sensitive: bool=None, spoiler_text: str=None, tags: List[Tag]=None, text: str=None, uri: str=None, url: str=None, visibility: str=None, params: StatusParams=None, scheduled_at: datetime=None):
        """ApiV1StatusesPost200Response - a model defined in OpenAPI

        :param account: The account of this ApiV1StatusesPost200Response.
        :param application: The application of this ApiV1StatusesPost200Response.
        :param bookmarked: The bookmarked of this ApiV1StatusesPost200Response.
        :param card: The card of this ApiV1StatusesPost200Response.
        :param content: The content of this ApiV1StatusesPost200Response.
        :param created_at: The created_at of this ApiV1StatusesPost200Response.
        :param emojis: The emojis of this ApiV1StatusesPost200Response.
        :param favourited: The favourited of this ApiV1StatusesPost200Response.
        :param favourites_count: The favourites_count of this ApiV1StatusesPost200Response.
        :param id: The id of this ApiV1StatusesPost200Response.
        :param in_reply_to_account_id: The in_reply_to_account_id of this ApiV1StatusesPost200Response.
        :param in_reply_to_id: The in_reply_to_id of this ApiV1StatusesPost200Response.
        :param language: The language of this ApiV1StatusesPost200Response.
        :param media_attachments: The media_attachments of this ApiV1StatusesPost200Response.
        :param mentions: The mentions of this ApiV1StatusesPost200Response.
        :param muted: The muted of this ApiV1StatusesPost200Response.
        :param pinned: The pinned of this ApiV1StatusesPost200Response.
        :param poll: The poll of this ApiV1StatusesPost200Response.
        :param reblog: The reblog of this ApiV1StatusesPost200Response.
        :param reblogged: The reblogged of this ApiV1StatusesPost200Response.
        :param reblogs_count: The reblogs_count of this ApiV1StatusesPost200Response.
        :param replies_count: The replies_count of this ApiV1StatusesPost200Response.
        :param sensitive: The sensitive of this ApiV1StatusesPost200Response.
        :param spoiler_text: The spoiler_text of this ApiV1StatusesPost200Response.
        :param tags: The tags of this ApiV1StatusesPost200Response.
        :param text: The text of this ApiV1StatusesPost200Response.
        :param uri: The uri of this ApiV1StatusesPost200Response.
        :param url: The url of this ApiV1StatusesPost200Response.
        :param visibility: The visibility of this ApiV1StatusesPost200Response.
        :param params: The params of this ApiV1StatusesPost200Response.
        :param scheduled_at: The scheduled_at of this ApiV1StatusesPost200Response.
        """
        self.openapi_types = {
            'account': Account,
            'application': Application,
            'bookmarked': bool,
            'card': Card,
            'content': str,
            'created_at': datetime,
            'emojis': List[Emoji],
            'favourited': bool,
            'favourites_count': int,
            'id': str,
            'in_reply_to_account_id': str,
            'in_reply_to_id': str,
            'language': str,
            'media_attachments': List[Attachment],
            'mentions': List[Mention],
            'muted': bool,
            'pinned': bool,
            'poll': Poll,
            'reblog': Status,
            'reblogged': bool,
            'reblogs_count': int,
            'replies_count': int,
            'sensitive': bool,
            'spoiler_text': str,
            'tags': List[Tag],
            'text': str,
            'uri': str,
            'url': str,
            'visibility': str,
            'params': StatusParams,
            'scheduled_at': datetime
        }

        self.attribute_map = {
            'account': 'account',
            'application': 'application',
            'bookmarked': 'bookmarked',
            'card': 'card',
            'content': 'content',
            'created_at': 'created_at',
            'emojis': 'emojis',
            'favourited': 'favourited',
            'favourites_count': 'favourites_count',
            'id': 'id',
            'in_reply_to_account_id': 'in_reply_to_account_id',
            'in_reply_to_id': 'in_reply_to_id',
            'language': 'language',
            'media_attachments': 'media_attachments',
            'mentions': 'mentions',
            'muted': 'muted',
            'pinned': 'pinned',
            'poll': 'poll',
            'reblog': 'reblog',
            'reblogged': 'reblogged',
            'reblogs_count': 'reblogs_count',
            'replies_count': 'replies_count',
            'sensitive': 'sensitive',
            'spoiler_text': 'spoiler_text',
            'tags': 'tags',
            'text': 'text',
            'uri': 'uri',
            'url': 'url',
            'visibility': 'visibility',
            'params': 'params',
            'scheduled_at': 'scheduled_at'
        }

        self._account = account
        self._application = application
        self._bookmarked = bookmarked
        self._card = card
        self._content = content
        self._created_at = created_at
        self._emojis = emojis
        self._favourited = favourited
        self._favourites_count = favourites_count
        self._id = id
        self._in_reply_to_account_id = in_reply_to_account_id
        self._in_reply_to_id = in_reply_to_id
        self._language = language
        self._media_attachments = media_attachments
        self._mentions = mentions
        self._muted = muted
        self._pinned = pinned
        self._poll = poll
        self._reblog = reblog
        self._reblogged = reblogged
        self._reblogs_count = reblogs_count
        self._replies_count = replies_count
        self._sensitive = sensitive
        self._spoiler_text = spoiler_text
        self._tags = tags
        self._text = text
        self._uri = uri
        self._url = url
        self._visibility = visibility
        self._params = params
        self._scheduled_at = scheduled_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiV1StatusesPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _api_v1_statuses_post_200_response of this ApiV1StatusesPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account(self):
        """Gets the account of this ApiV1StatusesPost200Response.


        :return: The account of this ApiV1StatusesPost200Response.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ApiV1StatusesPost200Response.


        :param account: The account of this ApiV1StatusesPost200Response.
        :type account: Account
        """

        self._account = account

    @property
    def application(self):
        """Gets the application of this ApiV1StatusesPost200Response.


        :return: The application of this ApiV1StatusesPost200Response.
        :rtype: Application
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ApiV1StatusesPost200Response.


        :param application: The application of this ApiV1StatusesPost200Response.
        :type application: Application
        """

        self._application = application

    @property
    def bookmarked(self):
        """Gets the bookmarked of this ApiV1StatusesPost200Response.

        Have you bookmarked this status?

        :return: The bookmarked of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._bookmarked

    @bookmarked.setter
    def bookmarked(self, bookmarked):
        """Sets the bookmarked of this ApiV1StatusesPost200Response.

        Have you bookmarked this status?

        :param bookmarked: The bookmarked of this ApiV1StatusesPost200Response.
        :type bookmarked: bool
        """

        self._bookmarked = bookmarked

    @property
    def card(self):
        """Gets the card of this ApiV1StatusesPost200Response.


        :return: The card of this ApiV1StatusesPost200Response.
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this ApiV1StatusesPost200Response.


        :param card: The card of this ApiV1StatusesPost200Response.
        :type card: Card
        """

        self._card = card

    @property
    def content(self):
        """Gets the content of this ApiV1StatusesPost200Response.

        HTML-encoded status content.

        :return: The content of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApiV1StatusesPost200Response.

        HTML-encoded status content.

        :param content: The content of this ApiV1StatusesPost200Response.
        :type content: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this ApiV1StatusesPost200Response.

        The date when this status was created.

        :return: The created_at of this ApiV1StatusesPost200Response.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiV1StatusesPost200Response.

        The date when this status was created.

        :param created_at: The created_at of this ApiV1StatusesPost200Response.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def emojis(self):
        """Gets the emojis of this ApiV1StatusesPost200Response.

        Custom emoji to be used when rendering status content.

        :return: The emojis of this ApiV1StatusesPost200Response.
        :rtype: List[Emoji]
        """
        return self._emojis

    @emojis.setter
    def emojis(self, emojis):
        """Sets the emojis of this ApiV1StatusesPost200Response.

        Custom emoji to be used when rendering status content.

        :param emojis: The emojis of this ApiV1StatusesPost200Response.
        :type emojis: List[Emoji]
        """

        self._emojis = emojis

    @property
    def favourited(self):
        """Gets the favourited of this ApiV1StatusesPost200Response.

        Have you favourited this status?

        :return: The favourited of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._favourited

    @favourited.setter
    def favourited(self, favourited):
        """Sets the favourited of this ApiV1StatusesPost200Response.

        Have you favourited this status?

        :param favourited: The favourited of this ApiV1StatusesPost200Response.
        :type favourited: bool
        """

        self._favourited = favourited

    @property
    def favourites_count(self):
        """Gets the favourites_count of this ApiV1StatusesPost200Response.

        How many favourites this status has received.

        :return: The favourites_count of this ApiV1StatusesPost200Response.
        :rtype: int
        """
        return self._favourites_count

    @favourites_count.setter
    def favourites_count(self, favourites_count):
        """Sets the favourites_count of this ApiV1StatusesPost200Response.

        How many favourites this status has received.

        :param favourites_count: The favourites_count of this ApiV1StatusesPost200Response.
        :type favourites_count: int
        """

        self._favourites_count = favourites_count

    @property
    def id(self):
        """Gets the id of this ApiV1StatusesPost200Response.

        ID of the scheduled status in the database. Cast from an integer, but not guaranteed to be a number.

        :return: The id of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiV1StatusesPost200Response.

        ID of the scheduled status in the database. Cast from an integer, but not guaranteed to be a number.

        :param id: The id of this ApiV1StatusesPost200Response.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def in_reply_to_account_id(self):
        """Gets the in_reply_to_account_id of this ApiV1StatusesPost200Response.

        ID of the account being replied to.

        :return: The in_reply_to_account_id of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._in_reply_to_account_id

    @in_reply_to_account_id.setter
    def in_reply_to_account_id(self, in_reply_to_account_id):
        """Sets the in_reply_to_account_id of this ApiV1StatusesPost200Response.

        ID of the account being replied to.

        :param in_reply_to_account_id: The in_reply_to_account_id of this ApiV1StatusesPost200Response.
        :type in_reply_to_account_id: str
        """

        self._in_reply_to_account_id = in_reply_to_account_id

    @property
    def in_reply_to_id(self):
        """Gets the in_reply_to_id of this ApiV1StatusesPost200Response.

        ID of the status being replied. Cast from an integer but not guaranteed to be a number.

        :return: The in_reply_to_id of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._in_reply_to_id

    @in_reply_to_id.setter
    def in_reply_to_id(self, in_reply_to_id):
        """Sets the in_reply_to_id of this ApiV1StatusesPost200Response.

        ID of the status being replied. Cast from an integer but not guaranteed to be a number.

        :param in_reply_to_id: The in_reply_to_id of this ApiV1StatusesPost200Response.
        :type in_reply_to_id: str
        """

        self._in_reply_to_id = in_reply_to_id

    @property
    def language(self):
        """Gets the language of this ApiV1StatusesPost200Response.

        Primary language of this status. ISO 639 Part 1 two-letter language code.

        :return: The language of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ApiV1StatusesPost200Response.

        Primary language of this status. ISO 639 Part 1 two-letter language code.

        :param language: The language of this ApiV1StatusesPost200Response.
        :type language: str
        """

        self._language = language

    @property
    def media_attachments(self):
        """Gets the media_attachments of this ApiV1StatusesPost200Response.

        Array of attachements

        :return: The media_attachments of this ApiV1StatusesPost200Response.
        :rtype: List[Attachment]
        """
        return self._media_attachments

    @media_attachments.setter
    def media_attachments(self, media_attachments):
        """Sets the media_attachments of this ApiV1StatusesPost200Response.

        Array of attachements

        :param media_attachments: The media_attachments of this ApiV1StatusesPost200Response.
        :type media_attachments: List[Attachment]
        """
        if media_attachments is None:
            raise ValueError("Invalid value for `media_attachments`, must not be `None`")

        self._media_attachments = media_attachments

    @property
    def mentions(self):
        """Gets the mentions of this ApiV1StatusesPost200Response.

        Mentions of users within the status content.

        :return: The mentions of this ApiV1StatusesPost200Response.
        :rtype: List[Mention]
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):
        """Sets the mentions of this ApiV1StatusesPost200Response.

        Mentions of users within the status content.

        :param mentions: The mentions of this ApiV1StatusesPost200Response.
        :type mentions: List[Mention]
        """

        self._mentions = mentions

    @property
    def muted(self):
        """Gets the muted of this ApiV1StatusesPost200Response.

        Have you muted notifications for this status's conversation?

        :return: The muted of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this ApiV1StatusesPost200Response.

        Have you muted notifications for this status's conversation?

        :param muted: The muted of this ApiV1StatusesPost200Response.
        :type muted: bool
        """

        self._muted = muted

    @property
    def pinned(self):
        """Gets the pinned of this ApiV1StatusesPost200Response.

        Have you pinned this status? Only appears if the status is pinnable.

        :return: The pinned of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this ApiV1StatusesPost200Response.

        Have you pinned this status? Only appears if the status is pinnable.

        :param pinned: The pinned of this ApiV1StatusesPost200Response.
        :type pinned: bool
        """

        self._pinned = pinned

    @property
    def poll(self):
        """Gets the poll of this ApiV1StatusesPost200Response.


        :return: The poll of this ApiV1StatusesPost200Response.
        :rtype: Poll
        """
        return self._poll

    @poll.setter
    def poll(self, poll):
        """Sets the poll of this ApiV1StatusesPost200Response.


        :param poll: The poll of this ApiV1StatusesPost200Response.
        :type poll: Poll
        """

        self._poll = poll

    @property
    def reblog(self):
        """Gets the reblog of this ApiV1StatusesPost200Response.


        :return: The reblog of this ApiV1StatusesPost200Response.
        :rtype: Status
        """
        return self._reblog

    @reblog.setter
    def reblog(self, reblog):
        """Sets the reblog of this ApiV1StatusesPost200Response.


        :param reblog: The reblog of this ApiV1StatusesPost200Response.
        :type reblog: Status
        """

        self._reblog = reblog

    @property
    def reblogged(self):
        """Gets the reblogged of this ApiV1StatusesPost200Response.

        Have you boosted this status?

        :return: The reblogged of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._reblogged

    @reblogged.setter
    def reblogged(self, reblogged):
        """Sets the reblogged of this ApiV1StatusesPost200Response.

        Have you boosted this status?

        :param reblogged: The reblogged of this ApiV1StatusesPost200Response.
        :type reblogged: bool
        """

        self._reblogged = reblogged

    @property
    def reblogs_count(self):
        """Gets the reblogs_count of this ApiV1StatusesPost200Response.

        How many boosts this status has received.

        :return: The reblogs_count of this ApiV1StatusesPost200Response.
        :rtype: int
        """
        return self._reblogs_count

    @reblogs_count.setter
    def reblogs_count(self, reblogs_count):
        """Sets the reblogs_count of this ApiV1StatusesPost200Response.

        How many boosts this status has received.

        :param reblogs_count: The reblogs_count of this ApiV1StatusesPost200Response.
        :type reblogs_count: int
        """

        self._reblogs_count = reblogs_count

    @property
    def replies_count(self):
        """Gets the replies_count of this ApiV1StatusesPost200Response.

        How many replies this status has received.

        :return: The replies_count of this ApiV1StatusesPost200Response.
        :rtype: int
        """
        return self._replies_count

    @replies_count.setter
    def replies_count(self, replies_count):
        """Sets the replies_count of this ApiV1StatusesPost200Response.

        How many replies this status has received.

        :param replies_count: The replies_count of this ApiV1StatusesPost200Response.
        :type replies_count: int
        """

        self._replies_count = replies_count

    @property
    def sensitive(self):
        """Gets the sensitive of this ApiV1StatusesPost200Response.

        Is this status marked as sensitive content?

        :return: The sensitive of this ApiV1StatusesPost200Response.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this ApiV1StatusesPost200Response.

        Is this status marked as sensitive content?

        :param sensitive: The sensitive of this ApiV1StatusesPost200Response.
        :type sensitive: bool
        """

        self._sensitive = sensitive

    @property
    def spoiler_text(self):
        """Gets the spoiler_text of this ApiV1StatusesPost200Response.

        Subject or summary line, below which status content is collapsed until expanded.

        :return: The spoiler_text of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._spoiler_text

    @spoiler_text.setter
    def spoiler_text(self, spoiler_text):
        """Sets the spoiler_text of this ApiV1StatusesPost200Response.

        Subject or summary line, below which status content is collapsed until expanded.

        :param spoiler_text: The spoiler_text of this ApiV1StatusesPost200Response.
        :type spoiler_text: str
        """

        self._spoiler_text = spoiler_text

    @property
    def tags(self):
        """Gets the tags of this ApiV1StatusesPost200Response.

        Hashtags used within the status content.

        :return: The tags of this ApiV1StatusesPost200Response.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiV1StatusesPost200Response.

        Hashtags used within the status content.

        :param tags: The tags of this ApiV1StatusesPost200Response.
        :type tags: List[Tag]
        """

        self._tags = tags

    @property
    def text(self):
        """Gets the text of this ApiV1StatusesPost200Response.

        Plain-text source of a status. Returned instead of `content` when status is deleted, so the user may redraft from the source text without the client having to reverse-engineer the original text from the HTML content.

        :return: The text of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ApiV1StatusesPost200Response.

        Plain-text source of a status. Returned instead of `content` when status is deleted, so the user may redraft from the source text without the client having to reverse-engineer the original text from the HTML content.

        :param text: The text of this ApiV1StatusesPost200Response.
        :type text: str
        """

        self._text = text

    @property
    def uri(self):
        """Gets the uri of this ApiV1StatusesPost200Response.

        URI of the status used for federation.

        :return: The uri of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ApiV1StatusesPost200Response.

        URI of the status used for federation.

        :param uri: The uri of this ApiV1StatusesPost200Response.
        :type uri: str
        """

        self._uri = uri

    @property
    def url(self):
        """Gets the url of this ApiV1StatusesPost200Response.

        A link to the status's HTML representation.

        :return: The url of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiV1StatusesPost200Response.

        A link to the status's HTML representation.

        :param url: The url of this ApiV1StatusesPost200Response.
        :type url: str
        """

        self._url = url

    @property
    def visibility(self):
        """Gets the visibility of this ApiV1StatusesPost200Response.

        Visibility of this status.

        :return: The visibility of this ApiV1StatusesPost200Response.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ApiV1StatusesPost200Response.

        Visibility of this status.

        :param visibility: The visibility of this ApiV1StatusesPost200Response.
        :type visibility: str
        """
        allowed_values = ["public", "unlisted", "private", "direct"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def params(self):
        """Gets the params of this ApiV1StatusesPost200Response.


        :return: The params of this ApiV1StatusesPost200Response.
        :rtype: StatusParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ApiV1StatusesPost200Response.


        :param params: The params of this ApiV1StatusesPost200Response.
        :type params: StatusParams
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")

        self._params = params

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this ApiV1StatusesPost200Response.

        ID of the status in the database. ISO 8601 Datetime.

        :return: The scheduled_at of this ApiV1StatusesPost200Response.
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this ApiV1StatusesPost200Response.

        ID of the status in the database. ISO 8601 Datetime.

        :param scheduled_at: The scheduled_at of this ApiV1StatusesPost200Response.
        :type scheduled_at: datetime
        """
        if scheduled_at is None:
            raise ValueError("Invalid value for `scheduled_at`, must not be `None`")

        self._scheduled_at = scheduled_at
