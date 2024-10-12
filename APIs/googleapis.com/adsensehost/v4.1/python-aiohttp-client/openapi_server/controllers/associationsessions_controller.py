from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_session import AssociationSession
from openapi_server import util


async def adsensehost_associationsessions_start(request: web.Request, product_code, website_url, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, callback_url=None, user_locale=None, website_locale=None) -> web.Response:
    """adsensehost_associationsessions_start

    Create an association session for initiating an association with an AdSense user.

    :param product_code: Products to associate with the user.
    :type product_code: List[str]
    :param website_url: The URL of the user&#39;s hosted website.
    :type website_url: str
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
    :param callback_url: The URL to redirect the user to once association is completed. It receives a token parameter that can then be used to retrieve the associated account.
    :type callback_url: str
    :param user_locale: The preferred locale of the user.
    :type user_locale: str
    :param website_locale: The locale of the user&#39;s hosted website.
    :type website_locale: str

    """
    return web.Response(status=200)


async def adsensehost_associationsessions_verify(request: web.Request, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_associationsessions_verify

    Verify an association session after the association callback returns from AdSense signup.

    :param token: The token returned to the association callback URL.
    :type token: str
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
