from typing import List, Dict
from aiohttp import web

from openapi_server.models.filter_set import FilterSet
from openapi_server.models.list_bid_metrics_response import ListBidMetricsResponse
from openapi_server.models.list_bid_response_errors_response import ListBidResponseErrorsResponse
from openapi_server.models.list_bid_responses_without_bids_response import ListBidResponsesWithoutBidsResponse
from openapi_server.models.list_creative_status_breakdown_by_creative_response import ListCreativeStatusBreakdownByCreativeResponse
from openapi_server.models.list_creative_status_breakdown_by_detail_response import ListCreativeStatusBreakdownByDetailResponse
from openapi_server.models.list_filter_sets_response import ListFilterSetsResponse
from openapi_server.models.list_filtered_bid_requests_response import ListFilteredBidRequestsResponse
from openapi_server.models.list_filtered_bids_response import ListFilteredBidsResponse
from openapi_server.models.list_impression_metrics_response import ListImpressionMetricsResponse
from openapi_server.models.list_losing_bids_response import ListLosingBidsResponse
from openapi_server.models.list_non_billable_winning_bids_response import ListNonBillableWinningBidsResponse
from openapi_server import util


async def adexchangebuyer2_buyers_filter_sets_bid_metrics_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_bid_metrics_list

    Lists all metrics that are measured in terms of number of bids.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListBidMetricsResponse.nextPageToken returned from the previous call to the bidMetrics.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_bid_response_errors_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_bid_response_errors_list

    List all errors that occurred in bid responses, with the number of bid responses affected for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListBidResponseErrorsResponse.nextPageToken returned from the previous call to the bidResponseErrors.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_bid_responses_without_bids_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_bid_responses_without_bids_list

    List all reasons for which bid responses were considered to have no applicable bids, with the number of bid responses affected for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListBidResponsesWithoutBidsResponse.nextPageToken returned from the previous call to the bidResponsesWithoutBids.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_create(request: web.Request, owner_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, is_transient=None, body=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_create

    Creates the specified filter set for the account with the given account ID.

    :param owner_name: Name of the owner (bidder or account) of the filter set to be created. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456&#x60;
    :type owner_name: str
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
    :param is_transient: Whether the filter set is transient, or should be persisted indefinitely. By default, filter sets are not transient. If transient, it will be available for at least 1 hour after creation.
    :type is_transient: bool
    :param body: 
    :type body: dict | bytes

    """
    body = FilterSet.from_dict(body)
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_delete

    Deletes the requested filter set from the account with the given account ID.

    :param name: Full name of the resource to delete. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
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

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_filtered_bid_requests_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_filtered_bid_requests_list

    List all reasons that caused a bid request not to be sent for an impression, with the number of bid requests not sent for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidRequestsResponse.nextPageToken returned from the previous call to the filteredBidRequests.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_filtered_bids_creatives_list(request: web.Request, filter_set_name, creative_status_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_filtered_bids_creatives_list

    List all creatives associated with a specific reason for which bids were filtered, with the number of bids filtered for each creative.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
    :param creative_status_id: The ID of the creative status for which to retrieve a breakdown by creative. See [creative-status-codes](https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes).
    :type creative_status_id: int
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByCreativeResponse.nextPageToken returned from the previous call to the filteredBids.creatives.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_filtered_bids_details_list(request: web.Request, filter_set_name, creative_status_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_filtered_bids_details_list

    List all details associated with a specific reason for which bids were filtered, with the number of bids filtered for each detail.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
    :param creative_status_id: The ID of the creative status for which to retrieve a breakdown by detail. See [creative-status-codes](https://developers.google.com/authorized-buyers/rtb/downloads/creative-status-codes). Details are only available for statuses 10, 14, 15, 17, 18, 19, 86, and 87.
    :type creative_status_id: int
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListCreativeStatusBreakdownByDetailResponse.nextPageToken returned from the previous call to the filteredBids.details.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_filtered_bids_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_filtered_bids_list

    List all reasons for which bids were filtered, with the number of bids filtered for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListFilteredBidsResponse.nextPageToken returned from the previous call to the filteredBids.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_get

    Retrieves the requested filter set for the account with the given account ID.

    :param name: Full name of the resource being requested. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
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

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_impression_metrics_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_impression_metrics_list

    Lists all metrics that are measured in terms of number of impressions.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListImpressionMetricsResponse.nextPageToken returned from the previous call to the impressionMetrics.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_list(request: web.Request, owner_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_list

    Lists all filter sets for the account with the given account ID.

    :param owner_name: Name of the owner (bidder or account) of the filter sets to be listed. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456&#x60;
    :type owner_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListFilterSetsResponse.nextPageToken returned from the previous call to the accounts.filterSets.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_losing_bids_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_losing_bids_list

    List all reasons for which bids lost in the auction, with the number of bids that lost for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListLosingBidsResponse.nextPageToken returned from the previous call to the losingBids.list method.
    :type page_token: str

    """
    return web.Response(status=200)


async def adexchangebuyer2_buyers_filter_sets_non_billable_winning_bids_list(request: web.Request, filter_set_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """adexchangebuyer2_buyers_filter_sets_non_billable_winning_bids_list

    List all reasons for which winning bids were not billable, with the number of bids not billed for each reason.

    :param filter_set_name: Name of the filter set that should be applied to the requested metrics. For example: - For a bidder-level filter set for bidder 123: &#x60;bidders/123/filterSets/abc&#x60; - For an account-level filter set for the buyer account representing bidder 123: &#x60;bidders/123/accounts/123/filterSets/abc&#x60; - For an account-level filter set for the child seat buyer account 456 whose bidder is 123: &#x60;bidders/123/accounts/456/filterSets/abc&#x60;
    :type filter_set_name: str
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
    :param page_size: Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of ListNonBillableWinningBidsResponse.nextPageToken returned from the previous call to the nonBillableWinningBids.list method.
    :type page_token: str

    """
    return web.Response(status=200)
