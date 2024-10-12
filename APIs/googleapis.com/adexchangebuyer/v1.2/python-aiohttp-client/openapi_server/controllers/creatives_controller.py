from typing import List, Dict
from aiohttp import web

from openapi_server.models.creative import Creative
from openapi_server.models.creatives_list import CreativesList
from openapi_server import util


async def adexchangebuyer_creatives_get(request: web.Request, account_id, buyer_creative_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adexchangebuyer_creatives_get

    Gets the status for a single creative. A creative will be available 30-40 minutes after submission.

    :param account_id: The id for the account that will serve this creative.
    :type account_id: int
    :param buyer_creative_id: The buyer-specific id for this creative.
    :type buyer_creative_id: str
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


async def adexchangebuyer_creatives_insert(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adexchangebuyer_creatives_insert

    Submit a new creative.

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
    body = Creative.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer_creatives_list(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None, status_filter=None) -> web.Response:
    """adexchangebuyer_creatives_list

    Retrieves a list of the authenticated user&#39;s active creatives. A creative will be available 30-40 minutes after submission.

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
    :param max_results: Maximum number of entries returned on one result page. If not set, the default is 100. Optional.
    :type max_results: int
    :param page_token: A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. Optional.
    :type page_token: str
    :param status_filter: When specified, only creatives having the given status are returned.
    :type status_filter: str

    """
    return web.Response(status=200)
