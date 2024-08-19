from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_abuse_report_reason_list_response import VideoAbuseReportReasonListResponse
from openapi_server import util


async def youtube_video_abuse_report_reasons_list(request: web.Request, part, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, hl=None) -> web.Response:
    """youtube_video_abuse_report_reasons_list

    Retrieves a list of resources, possibly filtered.

    :param part: The *part* parameter specifies the videoCategory resource parts that the API response will include. Supported values are id and snippet.
    :type part: List[str]
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
    :param hl: 
    :type hl: str

    """
    return web.Response(status=200)
