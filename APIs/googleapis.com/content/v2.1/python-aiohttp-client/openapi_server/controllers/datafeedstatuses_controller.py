from typing import List, Dict
from aiohttp import web

from openapi_server.models.datafeed_status import DatafeedStatus
from openapi_server.models.datafeedstatuses_custom_batch_request import DatafeedstatusesCustomBatchRequest
from openapi_server.models.datafeedstatuses_custom_batch_response import DatafeedstatusesCustomBatchResponse
from openapi_server.models.datafeedstatuses_list_response import DatafeedstatusesListResponse
from openapi_server import util


async def content_datafeedstatuses_custombatch(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """content_datafeedstatuses_custombatch

    Gets multiple Merchant Center datafeed statuses in a single request.

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
    body = DatafeedstatusesCustomBatchRequest.from_dict(body)
    return web.Response(status=200)


async def content_datafeedstatuses_get(request: web.Request, merchant_id, datafeed_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, country=None, feed_label=None, language=None) -> web.Response:
    """content_datafeedstatuses_get

    Retrieves the status of a datafeed from your Merchant Center account.

    :param merchant_id: The ID of the account that manages the datafeed. This account cannot be a multi-client account.
    :type merchant_id: str
    :param datafeed_id: The ID of the datafeed.
    :type datafeed_id: str
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
    :param country: Deprecated. Use &#x60;feedLabel&#x60; instead. The country to get the datafeed status for. If this parameter is provided then &#x60;language&#x60; must also be provided. Note that this parameter is required for feeds targeting multiple countries and languages, since a feed may have a different status for each target.
    :type country: str
    :param feed_label: The feed label to get the datafeed status for. If this parameter is provided then &#x60;language&#x60; must also be provided. Note that this parameter is required for feeds targeting multiple countries and languages, since a feed may have a different status for each target.
    :type feed_label: str
    :param language: The language to get the datafeed status for. If this parameter is provided then &#x60;country&#x60; must also be provided. Note that this parameter is required for feeds targeting multiple countries and languages, since a feed may have a different status for each target.
    :type language: str

    """
    return web.Response(status=200)


async def content_datafeedstatuses_list(request: web.Request, merchant_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None) -> web.Response:
    """content_datafeedstatuses_list

    Lists the statuses of the datafeeds in your Merchant Center account.

    :param merchant_id: The ID of the account that manages the datafeeds. This account cannot be a multi-client account.
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
    :param max_results: The maximum number of products to return in the response, used for paging.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str

    """
    return web.Response(status=200)
