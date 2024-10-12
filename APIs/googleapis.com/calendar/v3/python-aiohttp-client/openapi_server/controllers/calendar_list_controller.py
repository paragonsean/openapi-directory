from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_list import CalendarList
from openapi_server.models.calendar_list_entry import CalendarListEntry
from openapi_server.models.channel import Channel
from openapi_server import util


async def calendar_calendar_list_delete(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_calendar_list_delete

    Removes a calendar from the user&#39;s calendar list.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def calendar_calendar_list_get(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_calendar_list_get

    Returns a calendar from the user&#39;s calendar list.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def calendar_calendar_list_insert(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, color_rgb_format=None, body=None) -> web.Response:
    """calendar_calendar_list_insert

    Inserts an existing calendar into the user&#39;s calendar list.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param color_rgb_format: Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    :type color_rgb_format: bool
    :param body: 
    :type body: dict | bytes

    """
    body = CalendarListEntry.from_dict(body)
    return web.Response(status=200)


async def calendar_calendar_list_list(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, min_access_role=None, page_token=None, show_deleted=None, show_hidden=None, sync_token=None) -> web.Response:
    """calendar_calendar_list_list

    Returns the calendars on the user&#39;s calendar list.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    :type max_results: int
    :param min_access_role: The minimum access role for the user in the returned entries. Optional. The default is no restriction.
    :type min_access_role: str
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param show_deleted: Whether to include deleted calendar list entries in the result. Optional. The default is False.
    :type show_deleted: bool
    :param show_hidden: Whether to show hidden entries. Optional. The default is False.
    :type show_hidden: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won&#39;t be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str

    """
    return web.Response(status=200)


async def calendar_calendar_list_patch(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, color_rgb_format=None, body=None) -> web.Response:
    """calendar_calendar_list_patch

    Updates an existing calendar on the user&#39;s calendar list. This method supports patch semantics.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param color_rgb_format: Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    :type color_rgb_format: bool
    :param body: 
    :type body: dict | bytes

    """
    body = CalendarListEntry.from_dict(body)
    return web.Response(status=200)


async def calendar_calendar_list_update(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, color_rgb_format=None, body=None) -> web.Response:
    """calendar_calendar_list_update

    Updates an existing calendar on the user&#39;s calendar list.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param color_rgb_format: Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.
    :type color_rgb_format: bool
    :param body: 
    :type body: dict | bytes

    """
    body = CalendarListEntry.from_dict(body)
    return web.Response(status=200)


async def calendar_calendar_list_watch(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, min_access_role=None, page_token=None, show_deleted=None, show_hidden=None, sync_token=None, body=None) -> web.Response:
    """calendar_calendar_list_watch

    Watch for changes to CalendarList resources.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    :type max_results: int
    :param min_access_role: The minimum access role for the user in the returned entries. Optional. The default is no restriction.
    :type min_access_role: str
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param show_deleted: Whether to include deleted calendar list entries in the result. Optional. The default is False.
    :type show_deleted: bool
    :param show_hidden: Whether to show hidden entries. Optional. The default is False.
    :type show_hidden: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won&#39;t be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False. To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
