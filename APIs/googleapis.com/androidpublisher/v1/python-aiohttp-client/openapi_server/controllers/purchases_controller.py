from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_purchase import SubscriptionPurchase
from openapi_server import util


async def androidpublisher_purchases_cancel(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_cancel

    Cancels a user&#39;s subscription purchase. The subscription remains valid until its expiration time.

    :param package_name: The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;).
    :type package_name: str
    :param subscription_id: The purchased subscription ID (for example, &#39;monthly001&#39;).
    :type subscription_id: str
    :param token: The token provided to the user&#39;s device when the subscription was purchased.
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


async def androidpublisher_purchases_get(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_get

    Checks whether a user&#39;s subscription purchase is valid and returns its expiry time.

    :param package_name: The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;).
    :type package_name: str
    :param subscription_id: The purchased subscription ID (for example, &#39;monthly001&#39;).
    :type subscription_id: str
    :param token: The token provided to the user&#39;s device when the subscription was purchased.
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
