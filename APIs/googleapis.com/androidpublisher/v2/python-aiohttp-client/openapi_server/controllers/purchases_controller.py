from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_purchase import ProductPurchase
from openapi_server.models.subscription_purchase import SubscriptionPurchase
from openapi_server.models.subscription_purchases_defer_request import SubscriptionPurchasesDeferRequest
from openapi_server.models.subscription_purchases_defer_response import SubscriptionPurchasesDeferResponse
from openapi_server.models.voided_purchases_list_response import VoidedPurchasesListResponse
from openapi_server import util


async def androidpublisher_purchases_products_get(request: web.Request, package_name, product_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_products_get

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


async def androidpublisher_purchases_subscriptions_cancel(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_subscriptions_cancel

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


async def androidpublisher_purchases_subscriptions_defer(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_purchases_subscriptions_defer

    Defers a user&#39;s subscription purchase until a specified future expiration time.

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
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionPurchasesDeferRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_purchases_subscriptions_get(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_subscriptions_get

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


async def androidpublisher_purchases_subscriptions_refund(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_subscriptions_refund

    Refunds a user&#39;s subscription purchase, but the subscription remains valid until its expiration time and it will continue to recur.

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


async def androidpublisher_purchases_subscriptions_revoke(request: web.Request, package_name, subscription_id, token, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_purchases_subscriptions_revoke

    Refunds and immediately revokes a user&#39;s subscription purchase. Access to the subscription will be terminated immediately and it will stop recurring.

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


async def androidpublisher_purchases_voidedpurchases_list(request: web.Request, package_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, end_time=None, max_results=None, start_index=None, start_time=None, token=None) -> web.Response:
    """androidpublisher_purchases_voidedpurchases_list

    Lists the purchases that were canceled, refunded or charged-back.

    :param package_name: The package name of the application for which voided purchases need to be returned (for example, &#39;com.some.thing&#39;).
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
    :param end_time: The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
    :type end_time: str
    :param max_results: 
    :type max_results: int
    :param start_index: 
    :type start_index: int
    :param start_time: The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
    :type start_time: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)
