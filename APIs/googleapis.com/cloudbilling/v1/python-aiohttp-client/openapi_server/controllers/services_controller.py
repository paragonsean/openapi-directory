from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_skus_response import ListSkusResponse
from openapi_server import util


async def cloudbilling_services_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_services_list

    Lists all public cloud services.

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
    :param page_size: Requested page size. Defaults to 5000.
    :type page_size: int
    :param page_token: A token identifying a page of results to return. This should be a &#x60;next_page_token&#x60; value returned from a previous &#x60;ListServices&#x60; call. If unspecified, the first page of results is returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudbilling_services_skus_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, currency_code=None, end_time=None, page_size=None, page_token=None, start_time=None) -> web.Response:
    """cloudbilling_services_skus_list

    Lists all publicly available SKUs for a given cloud service.

    :param parent: Required. The name of the service. Example: \&quot;services/DA34-426B-A397\&quot;
    :type parent: str
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
    :param currency_code: The ISO 4217 currency code for the pricing info in the response proto. Will use the conversion rate as of start_time. Optional. If not specified USD will be used.
    :type currency_code: str
    :param end_time: Optional exclusive end time of the time range for which the pricing versions will be returned. Timestamps in the future are not allowed. The time range has to be within a single calendar month in America/Los_Angeles timezone. Time range as a whole is optional. If not specified, the latest pricing will be returned (up to 12 hours old at most).
    :type end_time: str
    :param page_size: Requested page size. Defaults to 5000.
    :type page_size: int
    :param page_token: A token identifying a page of results to return. This should be a &#x60;next_page_token&#x60; value returned from a previous &#x60;ListSkus&#x60; call. If unspecified, the first page of results is returned.
    :type page_token: str
    :param start_time: Optional inclusive start time of the time range for which the pricing versions will be returned. Timestamps in the future are not allowed. The time range has to be within a single calendar month in America/Los_Angeles timezone. Time range as a whole is optional. If not specified, the latest pricing will be returned (up to 12 hours old at most).
    :type start_time: str

    """
    return web.Response(status=200)
