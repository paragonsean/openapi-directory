from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def androidpublisher_orders_refund(request: web.Request, package_name, order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, revoke=None) -> web.Response:
    """androidpublisher_orders_refund

    Refunds a user&#39;s subscription or in-app purchase order. Orders older than 3 years cannot be refunded.

    :param package_name: The package name of the application for which this subscription or in-app item was purchased (for example, &#39;com.some.thing&#39;).
    :type package_name: str
    :param order_id: The order ID provided to the user when the subscription or in-app order was purchased.
    :type order_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param revoke: Whether to revoke the purchased item. If set to true, access to the subscription or in-app item will be terminated immediately. If the item is a recurring subscription, all future payments will also be terminated. Consumed in-app items need to be handled by developer&#39;s app. (optional).
    :type revoke: bool

    """
    return web.Response(status=200)
