from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_report_types_response import ListReportTypesResponse
from openapi_server import util


async def youtubereporting_report_types_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_system_managed=None, on_behalf_of_content_owner=None, page_size=None, page_token=None) -> web.Response:
    """youtubereporting_report_types_list

    Lists report types.

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
    :param include_system_managed: If set to true, also system-managed report types will be returned; otherwise only the report types that can be used to create new reporting jobs will be returned.
    :type include_system_managed: bool
    :param on_behalf_of_content_owner: The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    :type on_behalf_of_content_owner: str
    :param page_size: Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the &#x60;ListReportTypes&#x60; method.
    :type page_token: str

    """
    return web.Response(status=200)
