from typing import List, Dict
from aiohttp import web

from openapi_server.models.free_busy_request import FreeBusyRequest
from openapi_server.models.free_busy_response import FreeBusyResponse
from openapi_server import util


async def calendar_freebusy_query(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """calendar_freebusy_query

    Returns free/busy information for a set of calendars.

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
    body = FreeBusyRequest.from_dict(body)
    return web.Response(status=200)
