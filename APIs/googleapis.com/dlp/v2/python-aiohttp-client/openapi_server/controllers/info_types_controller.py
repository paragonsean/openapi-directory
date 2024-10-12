from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_privacy_dlp_v2_list_info_types_response import GooglePrivacyDlpV2ListInfoTypesResponse
from openapi_server import util


async def dlp_info_types_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, language_code=None, location_id=None, parent=None) -> web.Response:
    """dlp_info_types_list

    Returns a list of the sensitive information types that DLP API supports. See https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference to learn more.

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
    :param filter: filter to only return infoTypes supported by certain parts of the API. Defaults to supported_by&#x3D;INSPECT.
    :type filter: str
    :param language_code: BCP-47 language code for localized infoType friendly names. If omitted, or if localized strings are not available, en-US strings will be returned.
    :type language_code: str
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param parent: The parent resource name. The format of this value is as follows: locations/ LOCATION_ID
    :type parent: str

    """
    return web.Response(status=200)
