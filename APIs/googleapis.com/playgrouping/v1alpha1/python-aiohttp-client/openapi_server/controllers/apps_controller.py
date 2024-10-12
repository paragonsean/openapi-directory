from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_tags_request import CreateOrUpdateTagsRequest
from openapi_server.models.create_or_update_tags_response import CreateOrUpdateTagsResponse
from openapi_server.models.verify_token_request import VerifyTokenRequest
from openapi_server import util


async def playgrouping_apps_tokens_tags_create_or_update(request: web.Request, app_package, token, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """playgrouping_apps_tokens_tags_create_or_update

    Create or update tags for the user and app that are represented by the given token.

    :param app_package: Required. App whose tags are being manipulated. Format: apps/{package_name}
    :type app_package: str
    :param token: Required. Token for which the tags are being inserted or updated. Format: tokens/{token}
    :type token: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateTagsRequest.from_dict(body)
    return web.Response(status=200)


async def playgrouping_apps_tokens_verify(request: web.Request, app_package, token, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """playgrouping_apps_tokens_verify

    Verify an API token by asserting the app and persona it belongs to. The verification is a protection against client-side attacks and will fail if the contents of the token don&#39;t match the provided values. A token must be verified before it can be used to manipulate user tags.

    :param app_package: Required. App the token belongs to. Format: apps/{package_name}
    :type app_package: str
    :param token: Required. The token to be verified. Format: tokens/{token}
    :type token: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = VerifyTokenRequest.from_dict(body)
    return web.Response(status=200)
