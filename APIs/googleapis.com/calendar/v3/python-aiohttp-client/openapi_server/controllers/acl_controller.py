from typing import List, Dict
from aiohttp import web

from openapi_server.models.acl import Acl
from openapi_server.models.acl_rule import AclRule
from openapi_server.models.channel import Channel
from openapi_server import util


async def calendar_acl_delete(request: web.Request, calendar_id, rule_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_acl_delete

    Deletes an access control rule.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param rule_id: ACL rule identifier.
    :type rule_id: str
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


async def calendar_acl_get(request: web.Request, calendar_id, rule_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """calendar_acl_get

    Returns an access control rule.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param rule_id: ACL rule identifier.
    :type rule_id: str
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


async def calendar_acl_insert(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, body=None) -> web.Response:
    """calendar_acl_insert

    Creates an access control rule.

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
    :param send_notifications: Whether to send notifications about the calendar sharing change. Optional. The default is True.
    :type send_notifications: bool
    :param body: 
    :type body: dict | bytes

    """
    body = AclRule.from_dict(body)
    return web.Response(status=200)


async def calendar_acl_list(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None, show_deleted=None, sync_token=None) -> web.Response:
    """calendar_acl_list

    Returns the rules in the access control list for the calendar.

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
    :param max_results: Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    :type max_results: int
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param show_deleted: Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \&quot;none\&quot;. Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.
    :type show_deleted: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str

    """
    return web.Response(status=200)


async def calendar_acl_patch(request: web.Request, calendar_id, rule_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, body=None) -> web.Response:
    """calendar_acl_patch

    Updates an access control rule. This method supports patch semantics.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param rule_id: ACL rule identifier.
    :type rule_id: str
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
    :param send_notifications: Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.
    :type send_notifications: bool
    :param body: 
    :type body: dict | bytes

    """
    body = AclRule.from_dict(body)
    return web.Response(status=200)


async def calendar_acl_update(request: web.Request, calendar_id, rule_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, body=None) -> web.Response:
    """calendar_acl_update

    Updates an access control rule.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param rule_id: ACL rule identifier.
    :type rule_id: str
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
    :param send_notifications: Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.
    :type send_notifications: bool
    :param body: 
    :type body: dict | bytes

    """
    body = AclRule.from_dict(body)
    return web.Response(status=200)


async def calendar_acl_watch(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None, show_deleted=None, sync_token=None, body=None) -> web.Response:
    """calendar_acl_watch

    Watch for changes to ACL resources.

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
    :param max_results: Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.
    :type max_results: int
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param show_deleted: Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to \&quot;none\&quot;. Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.
    :type show_deleted: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
