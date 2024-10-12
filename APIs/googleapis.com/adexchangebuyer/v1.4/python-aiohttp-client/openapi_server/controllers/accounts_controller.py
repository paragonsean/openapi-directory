from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts_list import AccountsList
from openapi_server import util


async def adexchangebuyer_accounts_get(request: web.Request, id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adexchangebuyer_accounts_get

    Gets one account by ID.

    :param id: The account id
    :type id: int
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


async def adexchangebuyer_accounts_list(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adexchangebuyer_accounts_list

    Retrieves the authenticated user&#39;s list of accounts.

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


async def adexchangebuyer_accounts_patch(request: web.Request, id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, confirm_unsafe_account_change=None, body=None) -> web.Response:
    """adexchangebuyer_accounts_patch

    Updates an existing account. This method supports patch semantics.

    :param id: The account id
    :type id: int
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
    :param confirm_unsafe_account_change: Confirmation for erasing bidder and cookie matching urls.
    :type confirm_unsafe_account_change: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Account.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer_accounts_update(request: web.Request, id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, confirm_unsafe_account_change=None, body=None) -> web.Response:
    """adexchangebuyer_accounts_update

    Updates an existing account.

    :param id: The account id
    :type id: int
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
    :param confirm_unsafe_account_change: Confirmation for erasing bidder and cookie matching urls.
    :type confirm_unsafe_account_change: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Account.from_dict(body)
    return web.Response(status=200)
