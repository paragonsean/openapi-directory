from typing import List, Dict
from aiohttp import web

from openapi_server.models.advertiser import Advertiser
from openapi_server.models.assigned_location import AssignedLocation
from openapi_server.models.assigned_targeting_option import AssignedTargetingOption
from openapi_server.models.audit_advertiser_response import AuditAdvertiserResponse
from openapi_server.models.bulk_edit_advertiser_assigned_targeting_options_request import BulkEditAdvertiserAssignedTargetingOptionsRequest
from openapi_server.models.bulk_edit_advertiser_assigned_targeting_options_response import BulkEditAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.bulk_edit_assigned_locations_request import BulkEditAssignedLocationsRequest
from openapi_server.models.bulk_edit_assigned_locations_response import BulkEditAssignedLocationsResponse
from openapi_server.models.bulk_edit_line_item_assigned_targeting_options_request import BulkEditLineItemAssignedTargetingOptionsRequest
from openapi_server.models.bulk_edit_line_item_assigned_targeting_options_response import BulkEditLineItemAssignedTargetingOptionsResponse
from openapi_server.models.bulk_edit_negative_keywords_request import BulkEditNegativeKeywordsRequest
from openapi_server.models.bulk_edit_negative_keywords_response import BulkEditNegativeKeywordsResponse
from openapi_server.models.bulk_edit_sites_request import BulkEditSitesRequest
from openapi_server.models.bulk_edit_sites_response import BulkEditSitesResponse
from openapi_server.models.bulk_list_advertiser_assigned_targeting_options_response import BulkListAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_campaign_assigned_targeting_options_response import BulkListCampaignAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_insertion_order_assigned_targeting_options_response import BulkListInsertionOrderAssignedTargetingOptionsResponse
from openapi_server.models.bulk_list_line_item_assigned_targeting_options_response import BulkListLineItemAssignedTargetingOptionsResponse
from openapi_server.models.campaign import Campaign
from openapi_server.models.channel import Channel
from openapi_server.models.create_asset_request import CreateAssetRequest
from openapi_server.models.create_asset_response import CreateAssetResponse
from openapi_server.models.creative import Creative
from openapi_server.models.generate_default_line_item_request import GenerateDefaultLineItemRequest
from openapi_server.models.insertion_order import InsertionOrder
from openapi_server.models.line_item import LineItem
from openapi_server.models.list_advertiser_assigned_targeting_options_response import ListAdvertiserAssignedTargetingOptionsResponse
from openapi_server.models.list_advertisers_response import ListAdvertisersResponse
from openapi_server.models.list_assigned_locations_response import ListAssignedLocationsResponse
from openapi_server.models.list_campaign_assigned_targeting_options_response import ListCampaignAssignedTargetingOptionsResponse
from openapi_server.models.list_campaigns_response import ListCampaignsResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_creatives_response import ListCreativesResponse
from openapi_server.models.list_insertion_order_assigned_targeting_options_response import ListInsertionOrderAssignedTargetingOptionsResponse
from openapi_server.models.list_insertion_orders_response import ListInsertionOrdersResponse
from openapi_server.models.list_invoices_response import ListInvoicesResponse
from openapi_server.models.list_line_item_assigned_targeting_options_response import ListLineItemAssignedTargetingOptionsResponse
from openapi_server.models.list_line_items_response import ListLineItemsResponse
from openapi_server.models.list_location_lists_response import ListLocationListsResponse
from openapi_server.models.list_manual_triggers_response import ListManualTriggersResponse
from openapi_server.models.list_negative_keyword_lists_response import ListNegativeKeywordListsResponse
from openapi_server.models.list_negative_keywords_response import ListNegativeKeywordsResponse
from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server.models.location_list import LocationList
from openapi_server.models.lookup_invoice_currency_response import LookupInvoiceCurrencyResponse
from openapi_server.models.manual_trigger import ManualTrigger
from openapi_server.models.negative_keyword_list import NegativeKeywordList
from openapi_server.models.replace_negative_keywords_request import ReplaceNegativeKeywordsRequest
from openapi_server.models.replace_negative_keywords_response import ReplaceNegativeKeywordsResponse
from openapi_server.models.replace_sites_request import ReplaceSitesRequest
from openapi_server.models.replace_sites_response import ReplaceSitesResponse
from openapi_server import util


async def displayvideo_advertisers_assets_upload(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_assets_upload

    Uploads an asset. Returns the ID of the newly uploaded asset if successful. The asset file size should be no more than 10 MB for images, 200 MB for ZIP files, and 1 GB for videos. Must be used within the [multipart media upload process](/display-video/api/guides/how-tos/upload#multipart). Examples using provided client libraries can be found in our [Creating Creatives guide](/display-video/api/guides/creating-creatives/overview#upload_an_asset).

    :param advertiser_id: Required. The ID of the advertiser this asset belongs to.
    :type advertiser_id: str
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
    body = CreateAssetRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_audit(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, read_mask=None) -> web.Response:
    """displayvideo_advertisers_audit

    Audits an advertiser. Returns the counts of used entities per resource type under the advertiser provided. Used entities count towards their respective resource limit. See https://support.google.com/displayvideo/answer/6071450.

    :param advertiser_id: Required. The ID of the advertiser to audit.
    :type advertiser_id: str
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
    :param read_mask: Optional. The specific fields to return. If no mask is specified, all fields in the response proto will be filled. Valid values are: * usedLineItemsCount * usedInsertionOrdersCount * usedCampaignsCount * channelsCount * negativelyTargetedChannelsCount * negativeKeywordListsCount * adGroupCriteriaCount * campaignCriteriaCount
    :type read_mask: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_bulk_edit_advertiser_assigned_targeting_options(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_bulk_edit_advertiser_assigned_targeting_options

    Bulk edits targeting options under a single advertiser. The operation will delete the assigned targeting options provided in BulkEditAdvertiserAssignedTargetingOptionsRequest.delete_requests and then create the assigned targeting options provided in BulkEditAdvertiserAssignedTargetingOptionsRequest.create_requests .

    :param advertiser_id: Required. The ID of the advertiser.
    :type advertiser_id: str
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
    body = BulkEditAdvertiserAssignedTargetingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_bulk_list_advertiser_assigned_targeting_options(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_bulk_list_advertiser_assigned_targeting_options

    Lists assigned targeting options of an advertiser across targeting types.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the &#x60;OR&#x60; logical operator. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;) operator&#x60;. Supported fields: * &#x60;targetingType&#x60; Examples: * targetingType with value TARGETING_TYPE_CHANNEL &#x60;targetingType&#x3D;\&quot;TARGETING_TYPE_CHANNEL\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;targetingType&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingType desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. The size must be an integer between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified, the default is &#39;5000&#39;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token that lets the client fetch the next page of results. Typically, this is the value of next_page_token returned from the previous call to &#x60;BulkListAdvertiserAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_campaigns_bulk_list_campaign_assigned_targeting_options(request: web.Request, advertiser_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_campaigns_bulk_list_campaign_assigned_targeting_options

    Lists assigned targeting options of a campaign across targeting types.

    :param advertiser_id: Required. The ID of the advertiser the campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: Required. The ID of the campaign to list assigned targeting options for.
    :type campaign_id: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the &#x60;OR&#x60; logical operator. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;targetingType&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources of targeting type &#x60;TARGETING_TYPE_LANGUAGE&#x60; or &#x60;TARGETING_TYPE_GENDER&#x60;: &#x60;targetingType&#x3D;\&quot;TARGETING_TYPE_LANGUAGE\&quot; OR targetingType&#x3D;\&quot;TARGETING_TYPE_GENDER\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60;: &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;targetingType&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingType desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. The size must be an integer between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified, the default is &#x60;5000&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token that lets the client fetch the next page of results. Typically, this is the value of next_page_token returned from the previous call to &#x60;BulkListCampaignAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_campaigns_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_campaigns_create

    Creates a new campaign. Returns the newly created campaign if successful.

    :param advertiser_id: Output only. The unique ID of the advertiser the campaign belongs to.
    :type advertiser_id: str
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
    body = Campaign.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_campaigns_delete(request: web.Request, advertiser_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_campaigns_delete

    Permanently deletes a campaign. A deleted campaign cannot be recovered. The campaign should be archived first, i.e. set entity_status to &#x60;ENTITY_STATUS_ARCHIVED&#x60;, to be able to delete it. **This method regularly experiences high latency.** We recommend [increasing your default timeout](/display-video/api/guides/best-practices/timeouts#client_library_timeout) to avoid errors.

    :param advertiser_id: The ID of the advertiser this campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: The ID of the campaign we need to delete.
    :type campaign_id: str
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


async def displayvideo_advertisers_campaigns_get(request: web.Request, advertiser_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_campaigns_get

    Gets a campaign.

    :param advertiser_id: Required. The ID of the advertiser this campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: Required. The ID of the campaign to fetch.
    :type campaign_id: str
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


async def displayvideo_advertisers_campaigns_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_campaigns_list

    Lists campaigns in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, campaigns with &#x60;ENTITY_STATUS_ARCHIVED&#x60; will not be included in the results.

    :param advertiser_id: The ID of the advertiser to list campaigns for.
    :type advertiser_id: str
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
    :param filter: Allows filtering by campaign fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;updateTime&#x60; field must use the &#x60;GREATER THAN OR EQUAL TO (&gt;&#x3D;)&#x60; or &#x60;LESS THAN OR EQUAL TO (&lt;&#x3D;)&#x60; operators. * All other fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;campaignId&#x60; * &#x60;displayName&#x60; * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; (input in ISO 8601 format, or &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) Examples: * All &#x60;ENTITY_STATUS_ACTIVE&#x60; or &#x60;ENTITY_STATUS_PAUSED&#x60; campaigns under an advertiser: &#x60;(entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot; OR entityStatus&#x3D;\&quot;ENTITY_STATUS_PAUSED\&quot;)&#x60; * All campaigns with an update time less than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&lt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; * All campaigns with an update time greater than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&gt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCampaigns&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_campaigns_patch(request: web.Request, advertiser_id, campaign_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_campaigns_patch

    Updates an existing campaign. Returns the updated campaign if successful.

    :param advertiser_id: Output only. The unique ID of the advertiser the campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: Output only. The unique ID of the campaign. Assigned by the system.
    :type campaign_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Campaign.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_get(request: web.Request, advertiser_id, campaign_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_get

    Gets a single targeting option assigned to a campaign.

    :param advertiser_id: Required. The ID of the advertiser the campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: Required. The ID of the campaign the assigned targeting option belongs to.
    :type campaign_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. An identifier unique to the targeting type in this campaign that identifies the assigned targeting option being requested.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_list(request: web.Request, advertiser_id, campaign_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_campaigns_targeting_types_assigned_targeting_options_list

    Lists the targeting options assigned to a campaign for a specified targeting type.

    :param advertiser_id: Required. The ID of the advertiser the campaign belongs to.
    :type advertiser_id: str
    :param campaign_id: Required. The ID of the campaign to list assigned targeting options for.
    :type campaign_id: str
    :param targeting_type: Required. Identifies the type of assigned targeting options to list. Supported targeting types: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the &#x60;OR&#x60; logical operator. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedTargetingOptionId&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources with ID 1 or 2 &#x60;assignedTargetingOptionId&#x3D;\&quot;1\&quot; OR assignedTargetingOptionId&#x3D;\&quot;2\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60; &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;assignedTargetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;assignedTargetingOptionId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCampaignAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_channels_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, partner_id=None, body=None) -> web.Response:
    """displayvideo_advertisers_channels_create

    Creates a new channel. Returns the newly created channel if successful.

    :param advertiser_id: The ID of the advertiser that owns the created channel.
    :type advertiser_id: str
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
    :param partner_id: The ID of the partner that owns the created channel.
    :type partner_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_channels_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_advertisers_channels_list

    Lists channels for a partner or advertiser.

    :param advertiser_id: The ID of the advertiser that owns the channels.
    :type advertiser_id: str
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
    :param filter: Allows filtering by channel fields. Supported syntax: * Filter expressions for channel can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;displayName&#x60; Examples: * All channels for which the display name contains \&quot;google\&quot;: &#x60;displayName : \&quot;google\&quot;&#x60;. The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;channelId&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListChannels&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the partner that owns the channels.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_channels_patch(request: web.Request, advertiser_id, channel_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, partner_id=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_channels_patch

    Updates a channel. Returns the updated channel if successful.

    :param advertiser_id: The ID of the advertiser that owns the created channel.
    :type advertiser_id: str
    :param channel_id: Output only. The unique ID of the channel. Assigned by the system.
    :type channel_id: str
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
    :param partner_id: The ID of the partner that owns the created channel.
    :type partner_id: str
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_channels_sites_bulk_edit(request: web.Request, advertiser_id, channel_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_channels_sites_bulk_edit

    Bulk edits sites under a single channel. The operation will delete the sites provided in BulkEditSitesRequest.deleted_sites and then create the sites provided in BulkEditSitesRequest.created_sites.

    :param advertiser_id: The ID of the advertiser that owns the parent channel.
    :type advertiser_id: str
    :param channel_id: Required. The ID of the parent channel to which the sites belong.
    :type channel_id: str
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
    body = BulkEditSitesRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_channels_sites_delete(request: web.Request, advertiser_id, channel_id, url_or_app_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, partner_id=None) -> web.Response:
    """displayvideo_advertisers_channels_sites_delete

    Deletes a site from a channel.

    :param advertiser_id: The ID of the advertiser that owns the parent channel.
    :type advertiser_id: str
    :param channel_id: Required. The ID of the parent channel to which the site belongs.
    :type channel_id: str
    :param url_or_app_id: Required. The URL or app ID of the site to delete.
    :type url_or_app_id: str
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
    :param partner_id: The ID of the partner that owns the parent channel.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_channels_sites_list(request: web.Request, advertiser_id, channel_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_advertisers_channels_sites_list

    Lists sites in a channel.

    :param advertiser_id: The ID of the advertiser that owns the parent channel.
    :type advertiser_id: str
    :param channel_id: Required. The ID of the parent channel to which the requested sites belong.
    :type channel_id: str
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
    :param filter: Allows filtering by site fields. Supported syntax: * Filter expressions for site retrieval can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;urlOrAppId&#x60; Examples: * All sites for which the URL or app ID contains \&quot;google\&quot;: &#x60;urlOrAppId : \&quot;google\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;urlOrAppId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;urlOrAppId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;10000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListSites&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the partner that owns the parent channel.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_channels_sites_replace(request: web.Request, advertiser_id, channel_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_channels_sites_replace

    Replaces all of the sites under a single channel. The operation will replace the sites under a channel with the sites provided in ReplaceSitesRequest.new_sites. **This method regularly experiences high latency.** We recommend [increasing your default timeout](/display-video/api/guides/best-practices/timeouts#client_library_timeout) to avoid errors.

    :param advertiser_id: The ID of the advertiser that owns the parent channel.
    :type advertiser_id: str
    :param channel_id: Required. The ID of the parent channel whose sites will be replaced.
    :type channel_id: str
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
    body = ReplaceSitesRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_create

    Creates a new advertiser. Returns the newly created advertiser if successful. **This method regularly experiences high latency.** We recommend [increasing your default timeout](/display-video/api/guides/best-practices/timeouts#client_library_timeout) to avoid errors.

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
    body = Advertiser.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_creatives_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_creatives_create

    Creates a new creative. Returns the newly created creative if successful. A [\&quot;Standard\&quot; user role](//support.google.com/displayvideo/answer/2723011) or greater for the parent advertiser or partner is required to make this request.

    :param advertiser_id: Output only. The unique ID of the advertiser the creative belongs to.
    :type advertiser_id: str
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
    body = Creative.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_creatives_delete(request: web.Request, advertiser_id, creative_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_creatives_delete

    Deletes a creative. Returns error code &#x60;NOT_FOUND&#x60; if the creative does not exist. The creative should be archived first, i.e. set entity_status to &#x60;ENTITY_STATUS_ARCHIVED&#x60;, before it can be deleted. A [\&quot;Standard\&quot; user role](//support.google.com/displayvideo/answer/2723011) or greater for the parent advertiser or partner is required to make this request.

    :param advertiser_id: The ID of the advertiser this creative belongs to.
    :type advertiser_id: str
    :param creative_id: The ID of the creative to be deleted.
    :type creative_id: str
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


async def displayvideo_advertisers_creatives_get(request: web.Request, advertiser_id, creative_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_creatives_get

    Gets a creative.

    :param advertiser_id: Required. The ID of the advertiser this creative belongs to.
    :type advertiser_id: str
    :param creative_id: Required. The ID of the creative to fetch.
    :type creative_id: str
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


async def displayvideo_advertisers_creatives_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_creatives_list

    Lists creatives in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, creatives with &#x60;ENTITY_STATUS_ARCHIVED&#x60; will not be included in the results.

    :param advertiser_id: Required. The ID of the advertiser to list creatives for.
    :type advertiser_id: str
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
    :param filter: Allows filtering by creative fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;lineItemIds&#x60; field must use the &#x60;HAS (:)&#x60; operator. * The &#x60;updateTime&#x60; field must use the &#x60;GREATER THAN OR EQUAL TO (&gt;&#x3D;)&#x60; or &#x60;LESS THAN OR EQUAL TO (&lt;&#x3D;)&#x60; operators. * All other fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. * For &#x60;entityStatus&#x60;, &#x60;minDuration&#x60;, &#x60;maxDuration&#x60;, &#x60;updateTime&#x60;, and &#x60;dynamic&#x60; fields, there may be at most one restriction. Supported Fields: * &#x60;approvalStatus&#x60; * &#x60;creativeId&#x60; * &#x60;creativeType&#x60; * &#x60;dimensions&#x60; (input in the form of &#x60;{width}x{height}&#x60;) * &#x60;dynamic&#x60; * &#x60;entityStatus&#x60; * &#x60;exchangeReviewStatus&#x60; (input in the form of &#x60;{exchange}-{reviewStatus}&#x60;) * &#x60;lineItemIds&#x60; * &#x60;maxDuration&#x60; (input in the form of &#x60;{duration}s&#x60;. Only seconds are supported) * &#x60;minDuration&#x60; (input in the form of &#x60;{duration}s&#x60;. Only seconds are supported) * &#x60;updateTime&#x60; (input in ISO 8601 format, or &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) Notes: * For &#x60;updateTime&#x60;, a creative resource&#39;s field value reflects the last time that a creative has been updated, which includes updates made by the system (e.g. creative review updates). Examples: * All native creatives: &#x60;creativeType&#x3D;\&quot;CREATIVE_TYPE_NATIVE\&quot;&#x60; * All active creatives with 300x400 or 50x100 dimensions: &#x60;entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot; AND (dimensions&#x3D;\&quot;300x400\&quot; OR dimensions&#x3D;\&quot;50x100\&quot;)&#x60; * All dynamic creatives that are approved by AdX or AppNexus, with a minimum duration of 5 seconds and 200ms: &#x60;dynamic&#x3D;\&quot;true\&quot; AND minDuration&#x3D;\&quot;5.2s\&quot; AND (exchangeReviewStatus&#x3D;\&quot;EXCHANGE_GOOGLE_AD_MANAGER-REVIEW_STATUS_APPROVED\&quot; OR exchangeReviewStatus&#x3D;\&quot;EXCHANGE_APPNEXUS-REVIEW_STATUS_APPROVED\&quot;)&#x60; * All video creatives that are associated with line item ID 1 or 2: &#x60;creativeType&#x3D;\&quot;CREATIVE_TYPE_VIDEO\&quot; AND (lineItemIds:1 OR lineItemIds:2)&#x60; * Find creatives by multiple creative IDs: &#x60;creativeId&#x3D;1 OR creativeId&#x3D;2&#x60; * All creatives with an update time greater than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&gt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;creativeId&#x60; (default) * &#x60;createTime&#x60; * &#x60;mediaDuration&#x60; * &#x60;dimensions&#x60; (sorts by width first, then by height) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;createTime desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCreatives&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_creatives_patch(request: web.Request, advertiser_id, creative_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_creatives_patch

    Updates an existing creative. Returns the updated creative if successful. A [\&quot;Standard\&quot; user role](//support.google.com/displayvideo/answer/2723011) or greater for the parent advertiser or partner is required to make this request.

    :param advertiser_id: Output only. The unique ID of the advertiser the creative belongs to.
    :type advertiser_id: str
    :param creative_id: Output only. The unique ID of the creative. Assigned by the system.
    :type creative_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Creative.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_delete(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_delete

    Deletes an advertiser. Deleting an advertiser will delete all of its child resources, for example, campaigns, insertion orders and line items. A deleted advertiser cannot be recovered.

    :param advertiser_id: The ID of the advertiser we need to delete.
    :type advertiser_id: str
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


async def displayvideo_advertisers_get(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_get

    Gets an advertiser.

    :param advertiser_id: Required. The ID of the advertiser to fetch.
    :type advertiser_id: str
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


async def displayvideo_advertisers_insertion_orders_bulk_list_insertion_order_assigned_targeting_options(request: web.Request, advertiser_id, insertion_order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_bulk_list_insertion_order_assigned_targeting_options

    Lists assigned targeting options of an insertion order across targeting types.

    :param advertiser_id: Required. The ID of the advertiser the insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: Required. The ID of the insertion order to list assigned targeting options for.
    :type insertion_order_id: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator &#x60;OR&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;targetingType&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources of targeting type &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; or &#x60;TARGETING_TYPE_CHANNEL&#x60;: &#x60;targetingType&#x3D;\&quot;TARGETING_TYPE_PROXIMITY_LOCATION_LIST\&quot; OR targetingType&#x3D;\&quot;TARGETING_TYPE_CHANNEL\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60;: &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;targetingType&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingType desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. The size must be an integer between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified, the default is &#x60;5000&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token that lets the client fetch the next page of results. Typically, this is the value of next_page_token returned from the previous call to &#x60;BulkListInsertionOrderAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_insertion_orders_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_create

    Creates a new insertion order. Returns the newly created insertion order if successful.

    :param advertiser_id: Output only. The unique ID of the advertiser the insertion order belongs to.
    :type advertiser_id: str
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
    body = InsertionOrder.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_insertion_orders_delete(request: web.Request, advertiser_id, insertion_order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_delete

    Deletes an insertion order. Returns error code &#x60;NOT_FOUND&#x60; if the insertion order does not exist. The insertion order should be archived first, i.e. set entity_status to &#x60;ENTITY_STATUS_ARCHIVED&#x60;, to be able to delete it.

    :param advertiser_id: The ID of the advertiser this insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: The ID of the insertion order to delete.
    :type insertion_order_id: str
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


async def displayvideo_advertisers_insertion_orders_get(request: web.Request, advertiser_id, insertion_order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_get

    Gets an insertion order. Returns error code &#x60;NOT_FOUND&#x60; if the insertion order does not exist.

    :param advertiser_id: Required. The ID of the advertiser this insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: Required. The ID of the insertion order to fetch.
    :type insertion_order_id: str
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


async def displayvideo_advertisers_insertion_orders_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_list

    Lists insertion orders in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, insertion orders with &#x60;ENTITY_STATUS_ARCHIVED&#x60; will not be included in the results.

    :param advertiser_id: Required. The ID of the advertiser to list insertion orders for.
    :type advertiser_id: str
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
    :param filter: Allows filtering by insertion order fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;updateTime&#x60; field must use the &#x60;GREATER THAN OR EQUAL TO (&gt;&#x3D;)&#x60; or &#x60;LESS THAN OR EQUAL TO (&lt;&#x3D;)&#x60; operators. * All other fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;campaignId&#x60; * &#x60;displayName&#x60; * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; (input in ISO 8601 format, or &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) Examples: * All insertion orders under a campaign: &#x60;campaignId&#x3D;\&quot;1234\&quot;&#x60; * All &#x60;ENTITY_STATUS_ACTIVE&#x60; or &#x60;ENTITY_STATUS_PAUSED&#x60; insertion orders under an advertiser: &#x60;(entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot; OR entityStatus&#x3D;\&quot;ENTITY_STATUS_PAUSED\&quot;)&#x60; * All insertion orders with an update time less than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&lt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; * All insertion orders with an update time greater than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&gt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * \&quot;displayName\&quot; (default) * \&quot;entityStatus\&quot; * \&quot;updateTime\&quot; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;100&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListInsertionOrders&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_insertion_orders_patch(request: web.Request, advertiser_id, insertion_order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_patch

    Updates an existing insertion order. Returns the updated insertion order if successful.

    :param advertiser_id: Output only. The unique ID of the advertiser the insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: Output only. The unique ID of the insertion order. Assigned by the system.
    :type insertion_order_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = InsertionOrder.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_get(request: web.Request, advertiser_id, insertion_order_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_get

    Gets a single targeting option assigned to an insertion order.

    :param advertiser_id: Required. The ID of the advertiser the insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: Required. The ID of the insertion order the assigned targeting option belongs to.
    :type insertion_order_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. An identifier unique to the targeting type in this insertion order that identifies the assigned targeting option being requested.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_list(request: web.Request, advertiser_id, insertion_order_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_insertion_orders_targeting_types_assigned_targeting_options_list

    Lists the targeting options assigned to an insertion order.

    :param advertiser_id: Required. The ID of the advertiser the insertion order belongs to.
    :type advertiser_id: str
    :param insertion_order_id: Required. The ID of the insertion order to list assigned targeting options for.
    :type insertion_order_id: str
    :param targeting_type: Required. Identifies the type of assigned targeting options to list. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator &#x60;OR&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedTargetingOptionId&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources with ID 1 or 2: &#x60;assignedTargetingOptionId&#x3D;\&quot;1\&quot; OR assignedTargetingOptionId&#x3D;\&quot;2\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60;: &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;assignedTargetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;assignedTargetingOptionId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListInsertionOrderAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_invoices_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, issue_month=None, loi_sapin_invoice_type=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_invoices_list

    Lists invoices posted for an advertiser in a given month. Invoices generated by billing profiles with a \&quot;Partner\&quot; invoice level are not retrievable through this method.

    :param advertiser_id: Required. The ID of the advertiser to list invoices for.
    :type advertiser_id: str
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
    :param issue_month: The month to list the invoices for. If not set, the request will retrieve invoices for the previous month. Must be in the format YYYYMM.
    :type issue_month: str
    :param loi_sapin_invoice_type: Select type of invoice to retrieve for Loi Sapin advertisers. Only applicable to Loi Sapin advertisers. Will be ignored otherwise.
    :type loi_sapin_invoice_type: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListInvoices&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_invoices_lookup_invoice_currency(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, invoice_month=None) -> web.Response:
    """displayvideo_advertisers_invoices_lookup_invoice_currency

    Retrieves the invoice currency used by an advertiser in a given month.

    :param advertiser_id: Required. The ID of the advertiser to lookup currency for.
    :type advertiser_id: str
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
    :param invoice_month: Month for which the currency is needed. If not set, the request will return existing currency settings for the advertiser. Must be in the format YYYYMM.
    :type invoice_month: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_bulk_edit_line_item_assigned_targeting_options(request: web.Request, advertiser_id, line_item_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_line_items_bulk_edit_line_item_assigned_targeting_options

    Bulk edits targeting options under a single line item. The operation will delete the assigned targeting options provided in BulkEditLineItemAssignedTargetingOptionsRequest.delete_requests and then create the assigned targeting options provided in BulkEditLineItemAssignedTargetingOptionsRequest.create_requests. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * lineItems.patch * assignedTargetingOptions.create * assignedTargetingOptions.delete YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item the assigned targeting option will belong to.
    :type line_item_id: str
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
    body = BulkEditLineItemAssignedTargetingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_bulk_list_line_item_assigned_targeting_options(request: web.Request, advertiser_id, line_item_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_line_items_bulk_list_line_item_assigned_targeting_options

    Lists assigned targeting options of a line item across targeting types.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item to list assigned targeting options for.
    :type line_item_id: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator &#x60;OR&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;targetingType&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources of targeting type &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; or &#x60;TARGETING_TYPE_CHANNEL&#x60;: &#x60;targetingType&#x3D;\&quot;TARGETING_TYPE_PROXIMITY_LOCATION_LIST\&quot; OR targetingType&#x3D;\&quot;TARGETING_TYPE_CHANNEL\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60;: &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;targetingType&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingType desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. The size must be an integer between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified, the default is &#x60;5000&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token that lets the client fetch the next page of results. Typically, this is the value of next_page_token returned from the previous call to &#x60;BulkListLineItemAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_line_items_create

    Creates a new line item. Returns the newly created line item if successful. YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: Output only. The unique ID of the advertiser the line item belongs to.
    :type advertiser_id: str
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
    body = LineItem.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_delete(request: web.Request, advertiser_id, line_item_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_line_items_delete

    Deletes a line item. Returns error code &#x60;NOT_FOUND&#x60; if the line item does not exist. The line item should be archived first, i.e. set entity_status to &#x60;ENTITY_STATUS_ARCHIVED&#x60;, to be able to delete it. YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: The ID of the advertiser this line item belongs to.
    :type advertiser_id: str
    :param line_item_id: The ID of the line item to delete.
    :type line_item_id: str
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


async def displayvideo_advertisers_line_items_generate_default(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_line_items_generate_default

    Creates a new line item with settings (including targeting) inherited from the insertion order and an &#x60;ENTITY_STATUS_DRAFT&#x60; entity_status. Returns the newly created line item if successful. There are default values based on the three fields: * The insertion order&#39;s insertion_order_type * The insertion order&#39;s automation_type * The given line_item_type YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: Required. The ID of the advertiser this line item belongs to.
    :type advertiser_id: str
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
    body = GenerateDefaultLineItemRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_get(request: web.Request, advertiser_id, line_item_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_line_items_get

    Gets a line item.

    :param advertiser_id: Required. The ID of the advertiser this line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item to fetch.
    :type line_item_id: str
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


async def displayvideo_advertisers_line_items_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_line_items_list

    Lists line items in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, line items with &#x60;ENTITY_STATUS_ARCHIVED&#x60; will not be included in the results.

    :param advertiser_id: Required. The ID of the advertiser to list line items for.
    :type advertiser_id: str
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
    :param filter: Allows filtering by line item fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;updateTime&#x60; field must use the &#x60;GREATER THAN OR EQUAL TO (&gt;&#x3D;)&#x60; or &#x60;LESS THAN OR EQUAL TO (&lt;&#x3D;)&#x60; operators. * All other fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;campaignId&#x60; * &#x60;displayName&#x60; * &#x60;entityStatus&#x60; * &#x60;insertionOrderId&#x60; * &#x60;lineItemId&#x60; * &#x60;lineItemType&#x60; * &#x60;updateTime&#x60; (input in ISO 8601 format, or &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) Examples: * All line items under an insertion order: &#x60;insertionOrderId&#x3D;\&quot;1234\&quot;&#x60; * All &#x60;ENTITY_STATUS_ACTIVE&#x60; or &#x60;ENTITY_STATUS_PAUSED&#x60; and &#x60;LINE_ITEM_TYPE_DISPLAY_DEFAULT&#x60; line items under an advertiser: &#x60;(entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot; OR entityStatus&#x3D;\&quot;ENTITY_STATUS_PAUSED\&quot;) AND lineItemType&#x3D;\&quot;LINE_ITEM_TYPE_DISPLAY_DEFAULT\&quot;&#x60; * All line items with an update time less than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&lt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; * All line items with an update time greater than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&gt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListLineItems&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_patch(request: web.Request, advertiser_id, line_item_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_line_items_patch

    Updates an existing line item. Returns the updated line item if successful. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * BulkEditAssignedTargetingOptions * BulkUpdateLineItems * assignedTargetingOptions.create * assignedTargetingOptions.delete YouTube &amp; Partners line items cannot be created or updated using the API. **This method regularly experiences high latency.** We recommend [increasing your default timeout](/display-video/api/guides/best-practices/timeouts#client_library_timeout) to avoid errors.

    :param advertiser_id: Output only. The unique ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Output only. The unique ID of the line item. Assigned by the system.
    :type line_item_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = LineItem.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_create(request: web.Request, advertiser_id, line_item_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_create

    Assigns a targeting option to a line item. Returns the assigned targeting option if successful. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * lineItems.bulkEditAssignedTargetingOptions * lineItems.bulkUpdate * lineItems.patch * DeleteLineItemAssignedTargetingOption YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item the assigned targeting option will belong to.
    :type line_item_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
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
    body = AssignedTargetingOption.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_delete(request: web.Request, advertiser_id, line_item_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_delete

    Deletes an assigned targeting option from a line item. Requests to this endpoint cannot be made concurrently with the following requests updating the same line item: * lineItems.bulkEditAssignedTargetingOptions * lineItems.bulkUpdate * lineItems.patch * CreateLineItemAssignedTargetingOption YouTube &amp; Partners line items cannot be created or updated using the API.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item the assigned targeting option belongs to.
    :type line_item_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60;
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. The ID of the assigned targeting option to delete.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_get(request: web.Request, advertiser_id, line_item_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_get

    Gets a single targeting option assigned to a line item.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item the assigned targeting option belongs to.
    :type line_item_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_CHANNEL&#x60; (only for &#x60;LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE&#x60; line items) * &#x60;TARGETING_TYPE_YOUTUBE_VIDEO&#x60; (only for &#x60;LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE&#x60; line items)
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. An identifier unique to the targeting type in this line item that identifies the assigned targeting option being requested.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_list(request: web.Request, advertiser_id, line_item_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_line_items_targeting_types_assigned_targeting_options_list

    Lists the targeting options assigned to a line item.

    :param advertiser_id: Required. The ID of the advertiser the line item belongs to.
    :type advertiser_id: str
    :param line_item_id: Required. The ID of the line item to list assigned targeting options for.
    :type line_item_id: str
    :param targeting_type: Required. Identifies the type of assigned targeting options to list. Supported targeting types include: * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_APP&#x60; * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AUDIENCE_GROUP&#x60; * &#x60;TARGETING_TYPE_AUDIO_CONTENT_TYPE&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60; * &#x60;TARGETING_TYPE_CONTENT_GENRE&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60; * &#x60;TARGETING_TYPE_DAY_AND_TIME&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE&#x60; * &#x60;TARGETING_TYPE_INVENTORY_SOURCE_GROUP&#x60; * &#x60;TARGETING_TYPE_KEYWORD&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_NEGATIVE_KEYWORD_LIST&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_PROXIMITY_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_REGIONAL_LOCATION_LIST&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_THIRD_PARTY_VERIFIER&#x60; * &#x60;TARGETING_TYPE_URL&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_CHANNEL&#x60; (only for &#x60;LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE&#x60; line items) * &#x60;TARGETING_TYPE_YOUTUBE_VIDEO&#x60; (only for &#x60;LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE&#x60; line items)
    :type targeting_type: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the logical operator &#x60;OR&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedTargetingOptionId&#x60; * &#x60;inheritance&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; resources with ID 1 or 2: &#x60;assignedTargetingOptionId&#x3D;\&quot;1\&quot; OR assignedTargetingOptionId&#x3D;\&quot;2\&quot;&#x60; * &#x60;AssignedTargetingOption&#x60; resources with inheritance status of &#x60;NOT_INHERITED&#x60; or &#x60;INHERITED_FROM_PARTNER&#x60;: &#x60;inheritance&#x3D;\&quot;NOT_INHERITED\&quot; OR inheritance&#x3D;\&quot;INHERITED_FROM_PARTNER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;assignedTargetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;assignedTargetingOptionId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListLineItemAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_advertisers_list

    Lists advertisers that are accessible to the current user. The order is defined by the order_by parameter. A single partner_id is required. Cross-partner listing is not supported.

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
    :param filter: Allows filtering by advertiser fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;updateTime&#x60; field must use the &#x60;GREATER THAN OR EQUAL TO (&gt;&#x3D;)&#x60; or &#x60;LESS THAN OR EQUAL TO (&lt;&#x3D;)&#x60; operators. * All other fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;advertiserId&#x60; * &#x60;displayName&#x60; * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; (input in ISO 8601 format, or &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) Examples: * All active advertisers under a partner: &#x60;entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot;&#x60; * All advertisers with an update time less than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&lt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; * All advertisers with an update time greater than or equal to 2020-11-04T18:54:47Z (format of ISO 8601): &#x60;updateTime&gt;&#x3D;\&quot;2020-11-04T18:54:47Z\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;entityStatus&#x60; * &#x60;updateTime&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. For example, &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListAdvertisers&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: Required. The ID of the partner that the fetched advertisers should all belong to. The system only supports listing advertisers for one partner at a time.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_assigned_locations_bulk_edit(request: web.Request, advertiser_id, location_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_location_lists_assigned_locations_bulk_edit

    Bulk edits multiple assignments between locations and a single location list. The operation will delete the assigned locations provided in deletedAssignedLocations and then create the assigned locations provided in createdAssignedLocations.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location list belongs.
    :type advertiser_id: str
    :param location_list_id: Required. The ID of the location list to which these assignments are assigned.
    :type location_list_id: str
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
    body = BulkEditAssignedLocationsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_assigned_locations_create(request: web.Request, advertiser_id, location_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_location_lists_assigned_locations_create

    Creates an assignment between a location and a location list.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location list belongs.
    :type advertiser_id: str
    :param location_list_id: Required. The ID of the location list for which the assignment will be created.
    :type location_list_id: str
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
    body = AssignedLocation.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_assigned_locations_delete(request: web.Request, advertiser_id, location_list_id, assigned_location_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_location_lists_assigned_locations_delete

    Deletes the assignment between a location and a location list.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location list belongs.
    :type advertiser_id: str
    :param location_list_id: Required. The ID of the location list to which this assignment is assigned.
    :type location_list_id: str
    :param assigned_location_id: Required. The ID of the assigned location to delete.
    :type assigned_location_id: str
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


async def displayvideo_advertisers_location_lists_assigned_locations_list(request: web.Request, advertiser_id, location_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_location_lists_assigned_locations_list

    Lists locations assigned to a location list.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location list belongs.
    :type advertiser_id: str
    :param location_list_id: Required. The ID of the location list to which these assignments are assigned.
    :type location_list_id: str
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
    :param filter: Allows filtering by location list assignment fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the &#x60;OR&#x60; logical operator. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedLocationId&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;assignedLocationId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;assignedLocationId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListAssignedLocations&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_location_lists_create

    Creates a new location list. Returns the newly created location list if successful.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location list belongs.
    :type advertiser_id: str
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
    body = LocationList.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_location_lists_list

    Lists location lists based on a given advertiser id.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the fetched location lists belong.
    :type advertiser_id: str
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
    :param filter: Allows filtering by location list fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;locationType&#x60; Examples: * All regional location list: &#x60;locationType&#x3D;\&quot;TARGETING_LOCATION_TYPE_REGIONAL\&quot;&#x60; * All proximity location list: &#x60;locationType&#x3D;\&quot;TARGETING_LOCATION_TYPE_PROXIMITY\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;locationListId&#x60; (default) * &#x60;displayName&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. Defaults to &#x60;100&#x60; if not set. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListLocationLists&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_location_lists_patch(request: web.Request, advertiser_id, location_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_location_lists_patch

    Updates a location list. Returns the updated location list if successful.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the location lists belongs.
    :type advertiser_id: str
    :param location_list_id: Output only. The unique ID of the location list. Assigned by the system.
    :type location_list_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = LocationList.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_manual_triggers_activate(request: web.Request, advertiser_id, trigger_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_activate

    Activates a manual trigger. Each activation of the manual trigger must be at least 5 minutes apart, otherwise an error will be returned. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. The ID of the advertiser that the manual trigger belongs.
    :type advertiser_id: str
    :param trigger_id: Required. The ID of the manual trigger to activate.
    :type trigger_id: str
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
    :type body: 

    """
    return web.Response(status=200)


async def displayvideo_advertisers_manual_triggers_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_create

    Creates a new manual trigger. Returns the newly created manual trigger if successful. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. Immutable. The unique ID of the advertiser that the manual trigger belongs to.
    :type advertiser_id: str
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
    body = ManualTrigger.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_manual_triggers_deactivate(request: web.Request, advertiser_id, trigger_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_deactivate

    Deactivates a manual trigger. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. The ID of the advertiser that the manual trigger belongs.
    :type advertiser_id: str
    :param trigger_id: Required. The ID of the manual trigger to deactivate.
    :type trigger_id: str
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
    :type body: 

    """
    return web.Response(status=200)


async def displayvideo_advertisers_manual_triggers_get(request: web.Request, advertiser_id, trigger_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_get

    Gets a manual trigger. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. The ID of the advertiser this manual trigger belongs to.
    :type advertiser_id: str
    :param trigger_id: Required. The ID of the manual trigger to fetch.
    :type trigger_id: str
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


async def displayvideo_advertisers_manual_triggers_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_list

    Lists manual triggers that are accessible to the current user for a given advertiser ID. The order is defined by the order_by parameter. A single advertiser_id is required. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. The ID of the advertiser that the fetched manual triggers belong to.
    :type advertiser_id: str
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
    :param filter: Allows filtering by manual trigger fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;displayName&#x60; * &#x60;state&#x60; Examples: * All active manual triggers under an advertiser: &#x60;state&#x3D;\&quot;ACTIVE\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;state&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. For example, &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListManualTriggers&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_manual_triggers_patch(request: web.Request, advertiser_id, trigger_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_manual_triggers_patch

    Updates a manual trigger. Returns the updated manual trigger if successful. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This method will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information.

    :param advertiser_id: Required. Immutable. The unique ID of the advertiser that the manual trigger belongs to.
    :type advertiser_id: str
    :param trigger_id: Output only. The unique ID of the manual trigger.
    :type trigger_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManualTrigger.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_create(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_create

    Creates a new negative keyword list. Returns the newly created negative keyword list if successful.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the negative keyword list will belong.
    :type advertiser_id: str
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
    body = NegativeKeywordList.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_list(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_list

    Lists negative keyword lists based on a given advertiser id.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the fetched negative keyword lists belong.
    :type advertiser_id: str
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
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. Defaults to &#x60;100&#x60; if not set. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListNegativeKeywordLists&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_negative_keywords_bulk_edit(request: web.Request, advertiser_id, negative_keyword_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_negative_keywords_bulk_edit

    Bulk edits negative keywords in a single negative keyword list. The operation will delete the negative keywords provided in BulkEditNegativeKeywordsRequest.deleted_negative_keywords and then create the negative keywords provided in BulkEditNegativeKeywordsRequest.created_negative_keywords. This operation is guaranteed to be atomic and will never result in a partial success or partial failure.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the parent negative keyword list belongs.
    :type advertiser_id: str
    :param negative_keyword_list_id: Required. The ID of the parent negative keyword list to which the negative keywords belong.
    :type negative_keyword_list_id: str
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
    body = BulkEditNegativeKeywordsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_negative_keywords_delete(request: web.Request, advertiser_id, negative_keyword_list_id, keyword_value, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_negative_keywords_delete

    Deletes a negative keyword from a negative keyword list.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the parent negative keyword list belongs.
    :type advertiser_id: str
    :param negative_keyword_list_id: Required. The ID of the parent negative keyword list to which the negative keyword belongs.
    :type negative_keyword_list_id: str
    :param keyword_value: Required. The keyword value of the negative keyword to delete.
    :type keyword_value: str
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


async def displayvideo_advertisers_negative_keyword_lists_negative_keywords_list(request: web.Request, advertiser_id, negative_keyword_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_negative_keywords_list

    Lists negative keywords in a negative keyword list.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the parent negative keyword list belongs.
    :type advertiser_id: str
    :param negative_keyword_list_id: Required. The ID of the parent negative keyword list to which the requested negative keywords belong.
    :type negative_keyword_list_id: str
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
    :param filter: Allows filtering by negative keyword fields. Supported syntax: * Filter expressions for negative keywords can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;keywordValue&#x60; Examples: * All negative keywords for which the keyword value contains \&quot;google\&quot;: &#x60;keywordValue : \&quot;google\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;keywordValue&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be added to the field name. Example: &#x60;keywordValue desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;1000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListNegativeKeywords&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_negative_keywords_replace(request: web.Request, advertiser_id, negative_keyword_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_negative_keywords_replace

    Replaces all negative keywords in a single negative keyword list. The operation will replace the keywords in a negative keyword list with keywords provided in ReplaceNegativeKeywordsRequest.new_negative_keywords.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the parent negative keyword list belongs.
    :type advertiser_id: str
    :param negative_keyword_list_id: Required. The ID of the parent negative keyword list to which the negative keywords belong.
    :type negative_keyword_list_id: str
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
    body = ReplaceNegativeKeywordsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_negative_keyword_lists_patch(request: web.Request, advertiser_id, negative_keyword_list_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_negative_keyword_lists_patch

    Updates a negative keyword list. Returns the updated negative keyword list if successful.

    :param advertiser_id: Required. The ID of the DV360 advertiser to which the negative keyword list belongs.
    :type advertiser_id: str
    :param negative_keyword_list_id: Output only. The unique ID of the negative keyword list. Assigned by the system.
    :type negative_keyword_list_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = NegativeKeywordList.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_patch(request: web.Request, advertiser_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_advertisers_patch

    Updates an existing advertiser. Returns the updated advertiser if successful.

    :param advertiser_id: Output only. The unique ID of the advertiser. Assigned by the system.
    :type advertiser_id: str
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
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Advertiser.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_targeting_types_assigned_targeting_options_create(request: web.Request, advertiser_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_advertisers_targeting_types_assigned_targeting_options_create

    Assigns a targeting option to an advertiser. Returns the assigned targeting option if successful.

    :param advertiser_id: Required. The ID of the advertiser.
    :type advertiser_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60;
    :type targeting_type: str
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
    body = AssignedTargetingOption.from_dict(body)
    return web.Response(status=200)


async def displayvideo_advertisers_targeting_types_assigned_targeting_options_delete(request: web.Request, advertiser_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_targeting_types_assigned_targeting_options_delete

    Deletes an assigned targeting option from an advertiser.

    :param advertiser_id: Required. The ID of the advertiser.
    :type advertiser_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60;
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. The ID of the assigned targeting option to delete.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_targeting_types_assigned_targeting_options_get(request: web.Request, advertiser_id, targeting_type, assigned_targeting_option_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """displayvideo_advertisers_targeting_types_assigned_targeting_options_get

    Gets a single targeting option assigned to an advertiser.

    :param advertiser_id: Required. The ID of the advertiser.
    :type advertiser_id: str
    :param targeting_type: Required. Identifies the type of this assigned targeting option. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_VIDEO&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_CHANNEL&#x60;
    :type targeting_type: str
    :param assigned_targeting_option_id: Required. An identifier unique to the targeting type in this advertiser that identifies the assigned targeting option being requested.
    :type assigned_targeting_option_id: str
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


async def displayvideo_advertisers_targeting_types_assigned_targeting_options_list(request: web.Request, advertiser_id, targeting_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """displayvideo_advertisers_targeting_types_assigned_targeting_options_list

    Lists the targeting options assigned to an advertiser.

    :param advertiser_id: Required. The ID of the advertiser.
    :type advertiser_id: str
    :param targeting_type: Required. Identifies the type of assigned targeting options to list. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_VIDEO&#x60; * &#x60;TARGETING_TYPE_YOUTUBE_CHANNEL&#x60;
    :type targeting_type: str
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
    :param filter: Allows filtering by assigned targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by the &#x60;OR&#x60; logical operator. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;assignedTargetingOptionId&#x60; Examples: * &#x60;AssignedTargetingOption&#x60; with ID 123456: &#x60;assignedTargetingOptionId&#x3D;\&quot;123456\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;assignedTargetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;assignedTargetingOptionId desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;5000&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListAdvertiserAssignedTargetingOptions&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str

    """
    return web.Response(status=200)
