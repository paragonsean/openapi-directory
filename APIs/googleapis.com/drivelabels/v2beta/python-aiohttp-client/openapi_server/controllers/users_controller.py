from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_apps_drive_labels_v2beta_user_capabilities import GoogleAppsDriveLabelsV2betaUserCapabilities
from openapi_server import util


async def drivelabels_users_get_capabilities(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, use_admin_access=None, view=None) -> web.Response:
    """drivelabels_users_get_capabilities

    Gets the user capabilities.

    :param name: Required. The resource name of the user. Only \&quot;users/me/capabilities\&quot; is supported.
    :type name: str
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
    :param customer: The customer to scope this request to. For example: \&quot;customers/abcd1234\&quot;. If unset, will return settings within the current customer.
    :type customer: str
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server verifies that the user is an admin for the label before allowing access.
    :type use_admin_access: bool
    :param view: When specified, only certain fields belonging to the indicated view are returned.
    :type view: str

    """
    return web.Response(status=200)
