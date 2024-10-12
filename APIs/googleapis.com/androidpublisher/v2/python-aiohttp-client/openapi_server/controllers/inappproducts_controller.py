from typing import List, Dict
from aiohttp import web

from openapi_server.models.in_app_product import InAppProduct
from openapi_server.models.inappproducts_list_response import InappproductsListResponse
from openapi_server import util


async def androidpublisher_inappproducts_delete(request: web.Request, package_name, sku, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_inappproducts_delete

    Delete an in-app product for an app.

    :param package_name: Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param sku: Unique identifier for the in-app product.
    :type sku: str
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


async def androidpublisher_inappproducts_get(request: web.Request, package_name, sku, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_inappproducts_get

    Returns information about the in-app product specified.

    :param package_name: 
    :type package_name: str
    :param sku: Unique identifier for the in-app product.
    :type sku: str
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


async def androidpublisher_inappproducts_insert(request: web.Request, package_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, auto_convert_missing_prices=None, body=None) -> web.Response:
    """androidpublisher_inappproducts_insert

    Creates a new in-app product for an app.

    :param package_name: Unique identifier for the Android app; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
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
    :param auto_convert_missing_prices: If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    :type auto_convert_missing_prices: bool
    :param body: 
    :type body: dict | bytes

    """
    body = InAppProduct.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_inappproducts_list(request: web.Request, package_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, start_index=None, token=None) -> web.Response:
    """androidpublisher_inappproducts_list

    List all the in-app products for an Android app, both subscriptions and managed in-app products..

    :param package_name: Unique identifier for the Android app with in-app products; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
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
    :param max_results: 
    :type max_results: int
    :param start_index: 
    :type start_index: int
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def androidpublisher_inappproducts_patch(request: web.Request, package_name, sku, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, auto_convert_missing_prices=None, body=None) -> web.Response:
    """androidpublisher_inappproducts_patch

    Updates the details of an in-app product. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param sku: Unique identifier for the in-app product.
    :type sku: str
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
    :param auto_convert_missing_prices: If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    :type auto_convert_missing_prices: bool
    :param body: 
    :type body: dict | bytes

    """
    body = InAppProduct.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_inappproducts_update(request: web.Request, package_name, sku, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, auto_convert_missing_prices=None, body=None) -> web.Response:
    """androidpublisher_inappproducts_update

    Updates the details of an in-app product.

    :param package_name: Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param sku: Unique identifier for the in-app product.
    :type sku: str
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
    :param auto_convert_missing_prices: If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    :type auto_convert_missing_prices: bool
    :param body: 
    :type body: dict | bytes

    """
    body = InAppProduct.from_dict(body)
    return web.Response(status=200)
