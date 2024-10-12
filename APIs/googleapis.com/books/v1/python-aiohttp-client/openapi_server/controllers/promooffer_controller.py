from typing import List, Dict
from aiohttp import web

from openapi_server.models.offers import Offers
from openapi_server import util


async def books_promooffer_accept(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, android_id=None, device=None, manufacturer=None, model=None, offer_id=None, product=None, serial=None, volume_id=None) -> web.Response:
    """books_promooffer_accept

    Accepts the promo offer.

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
    :param android_id: device android_id
    :type android_id: str
    :param device: device device
    :type device: str
    :param manufacturer: device manufacturer
    :type manufacturer: str
    :param model: device model
    :type model: str
    :param offer_id: 
    :type offer_id: str
    :param product: device product
    :type product: str
    :param serial: device serial
    :type serial: str
    :param volume_id: Volume id to exercise the offer
    :type volume_id: str

    """
    return web.Response(status=200)


async def books_promooffer_dismiss(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, android_id=None, device=None, manufacturer=None, model=None, offer_id=None, product=None, serial=None) -> web.Response:
    """books_promooffer_dismiss

    Marks the promo offer as dismissed.

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
    :param android_id: device android_id
    :type android_id: str
    :param device: device device
    :type device: str
    :param manufacturer: device manufacturer
    :type manufacturer: str
    :param model: device model
    :type model: str
    :param offer_id: Offer to dimiss
    :type offer_id: str
    :param product: device product
    :type product: str
    :param serial: device serial
    :type serial: str

    """
    return web.Response(status=200)


async def books_promooffer_get(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, android_id=None, device=None, manufacturer=None, model=None, product=None, serial=None) -> web.Response:
    """books_promooffer_get

    Returns a list of promo offers available to the user

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
    :param android_id: device android_id
    :type android_id: str
    :param device: device device
    :type device: str
    :param manufacturer: device manufacturer
    :type manufacturer: str
    :param model: device model
    :type model: str
    :param product: device product
    :type product: str
    :param serial: device serial
    :type serial: str

    """
    return web.Response(status=200)
