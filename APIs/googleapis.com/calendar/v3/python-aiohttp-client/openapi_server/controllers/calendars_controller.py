from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar import Calendar
from openapi_server import util


async def calendar_calendars_clear(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_calendars_clear

    Clears a primary calendar. This operation deletes all events associated with the primary calendar of an account.

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


async def calendar_calendars_delete(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_calendars_delete

    Deletes a secondary calendar. Use calendars.clear for clearing all events on primary calendars.

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


async def calendar_calendars_get(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_calendars_get

    Returns metadata for a calendar.

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


async def calendar_calendars_insert(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """calendar_calendars_insert

    Creates a secondary calendar.

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
    :param body: 
    :type body: dict | bytes

    """
    body = Calendar.from_dict(body)
    return web.Response(status=200)


async def calendar_calendars_patch(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """calendar_calendars_patch

    Updates metadata for a calendar. This method supports patch semantics.

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
    :param body: 
    :type body: dict | bytes

    """
    body = Calendar.from_dict(body)
    return web.Response(status=200)


async def calendar_calendars_update(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """calendar_calendars_update

    Updates metadata for a calendar.

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
    :param body: 
    :type body: dict | bytes

    """
    body = Calendar.from_dict(body)
    return web.Response(status=200)
