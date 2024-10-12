from typing import List, Dict
from aiohttp import web

from openapi_server.models.inapp_purchase import InappPurchase
from openapi_server import util


async def androidpublisher_inapppurchases_get(request: web.Request, package_name, product_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_inapppurchases_get

    Checks the purchase and consumption status of an inapp item.

    :param package_name: The package name of the application the inapp product was sold in (for example, &#39;com.some.thing&#39;).
    :type package_name: str
    :param product_id: The inapp product SKU (for example, &#39;com.some.thing.inapp1&#39;).
    :type product_id: str
    :param token: The token provided to the user&#39;s device when the inapp product was purchased.
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
