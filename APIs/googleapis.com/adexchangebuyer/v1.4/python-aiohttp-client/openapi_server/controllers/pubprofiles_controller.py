from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_publisher_profiles_by_account_id_response import GetPublisherProfilesByAccountIdResponse
from openapi_server import util


async def adexchangebuyer_pubprofiles_list(request: web.Request, account_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adexchangebuyer_pubprofiles_list

    Gets the requested publisher profile(s) by publisher accountId.

    :param account_id: The accountId of the publisher to get profiles for.
    :type account_id: int
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
