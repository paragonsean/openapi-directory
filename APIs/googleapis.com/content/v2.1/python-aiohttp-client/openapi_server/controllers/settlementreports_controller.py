from typing import List, Dict
from aiohttp import web

from openapi_server.models.settlement_report import SettlementReport
from openapi_server.models.settlementreports_list_response import SettlementreportsListResponse
from openapi_server import util


async def content_settlementreports_get(request: web.Request, merchant_id, settlement_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """content_settlementreports_get

    Retrieves a settlement report from your Merchant Center account.

    :param merchant_id: The Merchant Center account of the settlement report.
    :type merchant_id: str
    :param settlement_id: The Google-provided ID of the settlement.
    :type settlement_id: str
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

    """
    return web.Response(status=200)


async def content_settlementreports_list(request: web.Request, merchant_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None, transfer_end_date=None, transfer_start_date=None) -> web.Response:
    """content_settlementreports_list

    Retrieves a list of settlement reports from your Merchant Center account.

    :param merchant_id: The Merchant Center account to list settlements for.
    :type merchant_id: str
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
    :param max_results: The maximum number of settlements to return in the response, used for paging. The default value is 200 returns per page, and the maximum allowed value is 5000 returns per page.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str
    :param transfer_end_date: Obtains settlements which have transactions before this date (inclusively), in ISO 8601 format.
    :type transfer_end_date: str
    :param transfer_start_date: Obtains settlements which have transactions after this date (inclusively), in ISO 8601 format.
    :type transfer_start_date: str

    """
    return web.Response(status=200)
