from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_link import AccountLink
from openapi_server.models.brand import Brand
from openapi_server.models.create_reconciliation_report_response import CreateReconciliationReportResponse
from openapi_server.models.icon import Icon
from openapi_server.models.list_account_links_response import ListAccountLinksResponse
from openapi_server.models.list_brands_response import ListBrandsResponse
from openapi_server.models.list_hotel_views_response import ListHotelViewsResponse
from openapi_server.models.list_icons_response import ListIconsResponse
from openapi_server.models.list_price_accuracy_views_response import ListPriceAccuracyViewsResponse
from openapi_server.models.list_price_coverage_views_response import ListPriceCoverageViewsResponse
from openapi_server.models.list_reconciliation_reports_response import ListReconciliationReportsResponse
from openapi_server.models.price_coverage_view import PriceCoverageView
from openapi_server.models.query_free_booking_links_report_response import QueryFreeBookingLinksReportResponse
from openapi_server.models.query_participation_report_response import QueryParticipationReportResponse
from openapi_server.models.query_property_performance_report_response import QueryPropertyPerformanceReportResponse
from openapi_server.models.reconciliation_report import ReconciliationReport
from openapi_server.models.set_live_on_google_request import SetLiveOnGoogleRequest
from openapi_server.models.set_live_on_google_response import SetLiveOnGoogleResponse
from openapi_server.models.summarize_hotel_views_response import SummarizeHotelViewsResponse
from openapi_server.models.summarize_price_accuracy_response import SummarizePriceAccuracyResponse
from openapi_server.models.validate_reconciliation_report_response import ValidateReconciliationReportResponse
from openapi_server.models.verify_listings_request import VerifyListingsRequest
from openapi_server.models.verify_listings_response import VerifyListingsResponse
from openapi_server import util


async def travelpartner_accounts_account_links_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_account_links_create

    Creates a new account link between a Hotel Center account and a Google Ads account.

    :param parent: The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = AccountLink.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_account_links_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_account_links_delete

    Deletes an account link.

    :param name: Required. The resource name of the account link being deleted. The format is &#x60;accounts/{account_id}/accountLinks/{account_link_id}&#x60;.
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


async def travelpartner_accounts_account_links_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_account_links_list

    Returns the account links for a Hotel Center account.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_brands_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, brand_id=None, body=None) -> web.Response:
    """travelpartner_accounts_brands_create

    Creates a new brand. Because Google detects brands from your existing properties, you only need this operation when you want to configure a brand before you send its properties to Google. Note that it might take a couple of days after your listing feed first provides a brand for the brand to appear.

    :param parent: Required. The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param brand_id: Required. The partner-determined brand identifier.
    :type brand_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Brand.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_brands_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_brands_list

    Returns the brands for a partner account.

    :param parent: Required. The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_brands_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_missing=None, update_mask=None, body=None) -> web.Response:
    """travelpartner_accounts_brands_patch

    Updates a brand.

    :param name: Output only. The resource name for the brand in the format &#x60;accounts/{account_id}/brands/{brand_id}&#x60;. The &#x60;brand_id&#x60; corresponds to the partner&#39;s brand identifier used for landing page matching and the property-level brand identifier. A default brand is applied to properties that do not have a brand. The &#x60;brand_id&#x60; of the default brand is &#x60;NO_BRAND_ID&#x60;. It can be fetched and updated like any configured brand.
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
    :param allow_missing: When true, and the Brand is not found, a new Brand will be created. In this situation, &#x60;update_mask&#x60; is ignored.
    :type allow_missing: bool
    :param update_mask: Required. The field to update. Only the &#x60;display_names&#x60; and &#x60;icon&#x60; fields can be updated. Use the syntax shown in the example URI below and provide the new value in the request body. Example request URI and request body: &#x60;&#x60;&#x60; PATCH https://travelpartner.googleapis.com/v3/accounts/123456789/ brands/my-brand?update_mask&#x3D;brand.display_names &#x60;&#x60;&#x60; &#x60;&#x60;&#x60; { \&quot;display_names\&quot;: [{ \&quot;language\&quot;: \&quot;en\&quot; \&quot;text\&quot;: \&quot;Gilles&#39; Gites\&quot; }] } &#x60;&#x60;&#x60; The information above is sufficient for forming the URI and request body. The sentence below is auto-generated, supplemental information about the &#x60;FieldMask&#x60; format in general.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Brand.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_free_booking_links_report_views_query(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, aggregate_by=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """travelpartner_accounts_free_booking_links_report_views_query

    **DEPRECATED:** Use PropertyPerformanceReportService.QueryPropertyPerformanceReport, which also has impression reporting, instead. Provides the ability to query (get, filter, and segment) a free booking links report for a specific account.

    :param name: The resource name of the account being queried. Format: accounts/{account_id}
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
    :param aggregate_by: Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;freeBookingLinksResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, and &#x60;partnerHotelDisplayName&#x60;. Only fields specified here are included in the FreeBookingLinksResult.
    :type aggregate_by: str
    :param filter: The conditions (fields and expressions) used to filter the free booking link metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerHotelDisplayName&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerHotelDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerHotelDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60;
    :type filter: str
    :param page_size: The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    :type page_size: int
    :param page_token: A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def travelpartner_accounts_hotel_views_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """travelpartner_accounts_hotel_views_list

    Returns the list of hotel views.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param filter: Optional. The conditions (fields and expressions) used to filter HotelViews. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions cannot be joined. The &#x60;hotelId&#x60; field can be used to select specific hotels. The &#x60;liveOnGoogle&#x60; field can select properties that Google shows, or properties that are omitted in google search results. The &#x60;matchStatus&#x60; field can be used to filter the list of HotelViews returned for the account. Examples of valid conditions and their syntax are as follows: * &#x60;hotelId &#x3D; &#39;hotel_ABC&#39;&#x60; * &#x60;hotelId in (&#39;hotel_ABC&#39;, &#39;hotel_XYZ&#39;)&#x60; * &#x60;liveOnGoogle &#x3D; &#39;TRUE&#39;&#x60; * &#x60;liveOnGoogle &#x3D; &#39;FALSE&#39;&#x60; * &#x60;matchStatus &#x3D; &#39;NOT_MATCHED&#39;&#x60; * &#x60;matchStatus in (&#39;NOT_MATCHED&#39;, &#39;MATCHED&#39;, &#39;MAP_OVERLAP&#39;)&#x60;
    :type filter: str
    :param page_size: Number of elements to retrieve in a single page.
    :type page_size: int
    :param page_token: Token of the page to retrieve.
    :type page_token: str

    """
    return web.Response(status=200)


async def travelpartner_accounts_hotel_views_summarize(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_hotel_views_summarize

    Returns summarized information about hotels.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_hotels_set_live_on_google(request: web.Request, account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_hotels_set_live_on_google

    Collection-level custom method to update the Live on Google status for multiple properties. Each call can turn on or off multiple hotels. To turn some hotels on and turn some hotels off, you will have to make multiple calls.

    :param account: Required. The resource name of the account. The format is accounts/{account_id}.
    :type account: str
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
    body = SetLiveOnGoogleRequest.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_icons_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_icons_create

    Uploads a new icon and starts its review process. Generates an &#x60;icon_id&#x60; and includes it in the icon&#39;s resource name, which is the format &#x60;accounts/{account_id}/icons/{icon_id}&#x60; Returns HTTP status 400 and doesn&#39;t trigger the review process if the icon has any of these conditions: * Image is not in PNG format, or not convertible to PNG format. * Size less than 72 pixels * Size greater than 1200 pixels * Aspect ratio other than 1:1

    :param parent: Required. The resource name of the partner account owning the icon. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = Icon.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_icons_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_icons_list

    Returns the &#x60;Icon&#x60;s for a partner account.

    :param parent: Required. The resource name of the queried partner account. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_listings_verify(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_listings_verify

    returns verified listings with data issues and serving eligibilities

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = VerifyListingsRequest.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_participation_report_views_query(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, aggregate_by=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """travelpartner_accounts_participation_report_views_query

    Provides the ability to query (get, filter, and segment) a participation report for a particular account.

    :param name: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param aggregate_by: Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified as the &#x60;aggregate_by&#x60; value, the &#x60;participationResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, &#x60;hotelRegionCode&#x60;, &#x60;advanceBookingWindow&#x60;, &#x60;lengthOfStayDays&#x60;, &#x60;checkinDate&#x60;, and &#x60;occupancy&#x60;. Fields that are not specified are not included in the ParticipationResult. Using an &#x60;aggregateBy&#x60; specification that produces a large number of rows will cause an error. This is especially true when aggregating by &#x60;partnerHotelId&#x60; or more than two fields. To reduce the possibiliy of an error, filter by &#x60;partnerHotelId&#x60; and &#x60;date&#x60; to only include a select number of hotels and dates. Accounts with a large number of hotels will need to further reduce data with more filtering.
    :type aggregate_by: str
    :param filter: The conditions (fields and expressions) used to filter the participation metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; 2&#x60; * &#x60;advanceBookingWindow &gt;&#x3D; 0&#x60; * &#x60;advanceBookingWindow &lt;&#x3D; 5&#x60; * &#x60;advanceBookingWindow between 1 and 5&#x60; * &#x60;checkinDate &#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &gt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &lt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate between &#39;2020-10-01&#39; and &#39;2020-10-05&#39;&#x60; * &#x60;date &#x3D; &#39;2020-02-04&#39;&#x60; * &#x60;date between &#39;2020-02-04&#39; and &#39;2020-02-09&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;hotelRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;hotelRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;lengthOfStayDays &#x3D; 2&#x60; * &#x60;lengthOfStayDays &gt;&#x3D; 0&#x60; * &#x60;lengthOfStayDays &lt;&#x3D; 5&#x60; * &#x60;lengthOfStayDays between 1 and 5&#x60; * &#x60;occupancy &#x3D; 2&#x60; * &#x60;occupancy &gt;&#x3D; 0&#x60; * &#x60;occupancy &lt;&#x3D; 5&#x60; * &#x60;occupancy between 1 and 5&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60;
    :type filter: str
    :param page_size: The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    :type page_size: int
    :param page_token: A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def travelpartner_accounts_price_accuracy_views_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_price_accuracy_views_list

    Lists the available price accuracy views.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_price_accuracy_views_summarize(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_price_accuracy_views_summarize

    Returns the price accuracy summary.

    :param parent: The resource name of the account that is being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_price_coverage_views_get_latest(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_price_coverage_views_get_latest

    Returns the latest price coverage view in full detail.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_price_coverage_views_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """travelpartner_accounts_price_coverage_views_list

    Returns the entire price coverage history.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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

    """
    return web.Response(status=200)


async def travelpartner_accounts_property_performance_report_views_query(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, aggregate_by=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """travelpartner_accounts_property_performance_report_views_query

    Provides the ability to query (get, filter, and segment) a property performance links report for a specific account.

    :param name: The resource name of the account being queried. Format: accounts/{account_id}
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
    :param aggregate_by: Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;PropertyPerformanceResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;advanceBookingWindow&#x60;, &#x60;brand&#x60;, &#x60;date&#x60;, &#x60;deviceType&#x60;, &#x60;highIntentUsers&#x60;, &#x60;lengthOfStay&#x60;, &#x60;propertyRegionCode&#x60;, &#x60;occupancy&#x60;, &#x60;partnerPropertyId&#x60;, &#x60;partnerPropertyDisplayName&#x60;, and &#x60;userRegionCode&#x60;. Only fields specified here are included in the PropertyPerformanceResult.
    :type aggregate_by: str
    :param filter: The conditions (fields and expressions) used to filter the property performance metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerPropertyDisplayName&#x60; and &#x60;brand&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; &#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;&#x60; * &#x60;advanceBookingWindow in (&#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;, &#39;ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90&#39;)&#x60; * &#x60;brand &#x3D; &#39;Brand A&#39;&#x60; * &#x60;brand in (&#39;Brand A&#39;, &#39;brand B&#39;)&#x60; * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;highIntentUsers &#x3D; &#39;TRUE&#39;&#x60; * &#x60;highIntentUsers &#x3D; &#39;FALSE&#39;&#x60; * &#x60;lengthOfStay &#x3D; &#39;LENGTH_OF_STAY_NIGHTS_2&#39;&#x60; * &#x60;lengthOfStay in (&#39;LENGTH_OF_STAY_NIGHTS_2&#39;, &#39;LENGTH_OF_STAY_NIGHTS_4_TO_7&#39;)&#x60; * &#x60;propertyRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;propertyRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;occupancy &#x3D; &#39;OCCUPANCY_2&#39;&#x60; * &#x60;occupancy in (&#39;OCCUPANCY_2&#39;, &#39;OCCUPANCY_OVER_4&#39;)&#x60; * &#x60;partnerPropertyId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerPropertyId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerPropertyDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerPropertyDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60;
    :type filter: str
    :param page_size: The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    :type page_size: int
    :param page_token: A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def travelpartner_accounts_reconciliation_reports_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_reconciliation_reports_create

    Creates a reconciliation report and uploads it to Google.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ReconciliationReport.from_dict(body)
    return web.Response(status=200)


async def travelpartner_accounts_reconciliation_reports_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_matched_prices=None, include_non_scoring=None, include_pixels=None) -> web.Response:
    """travelpartner_accounts_reconciliation_reports_get

    Returns a reconciliation report.

    :param name: The resource name of the reconciliation report to fetch. The format is &#x60;accounts/{account_id}/reconciliationReports/{datetime}~{filename}&#x60;.
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
    :param include_matched_prices: Set to true if matched prices are to be added into the report.
    :type include_matched_prices: bool
    :param include_non_scoring: Set to true if non-account impacting rows are to be added into the report.
    :type include_non_scoring: bool
    :param include_pixels: Set to true if pixel signals are to be added into the report.
    :type include_pixels: bool

    """
    return web.Response(status=200)


async def travelpartner_accounts_reconciliation_reports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_date=None, start_date=None) -> web.Response:
    """travelpartner_accounts_reconciliation_reports_list

    Returns a list of the names of created reconciliation reports.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param end_date: End of date range to fetch files for. Format is yyyy-mm-dd[THH[:MM[:SS]]]. If empty, reports until the end of time are fetched.
    :type end_date: str
    :param start_date: Beginning of date range to fetch files for. Format is yyyy-MM-dd[THH[:mm[:SS]]]. If empty, reports from the beginning of time onwards are fetched.
    :type start_date: str

    """
    return web.Response(status=200)


async def travelpartner_accounts_reconciliation_reports_validate(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """travelpartner_accounts_reconciliation_reports_validate

    Validates a reconciliation report.

    :param parent: The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ReconciliationReport.from_dict(body)
    return web.Response(status=200)
