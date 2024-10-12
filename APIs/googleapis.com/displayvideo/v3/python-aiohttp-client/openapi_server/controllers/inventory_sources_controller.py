from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_inventory_source_read_write_accessors_request import EditInventorySourceReadWriteAccessorsRequest
from openapi_server.models.inventory_source import InventorySource
from openapi_server.models.inventory_source_accessors import InventorySourceAccessors
from openapi_server.models.list_inventory_sources_response import ListInventorySourcesResponse
from openapi_server import util


async def displayvideo_inventory_sources_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None, body=None) -> web.Response:
    """displayvideo_inventory_sources_create

    Creates a new inventory source. Returns the newly created inventory source if successful.

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
    :param advertiser_id: The ID of the advertiser that the request is being made within.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that the request is being made within.
    :type partner_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InventorySource.from_dict(body)
    return web.Response(status=200)


async def displayvideo_inventory_sources_edit_inventory_source_read_write_accessors(request: web.Request, inventory_source_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """displayvideo_inventory_sources_edit_inventory_source_read_write_accessors

    Edits read/write accessors of an inventory source. Returns the updated read_write_accessors for the inventory source.

    :param inventory_source_id: Required. The ID of inventory source to update.
    :type inventory_source_id: str
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
    body = EditInventorySourceReadWriteAccessorsRequest.from_dict(body)
    return web.Response(status=200)


async def displayvideo_inventory_sources_get(request: web.Request, inventory_source_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None) -> web.Response:
    """displayvideo_inventory_sources_get

    Gets an inventory source.

    :param inventory_source_id: Required. The ID of the inventory source to fetch.
    :type inventory_source_id: str
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
    :param advertiser_id: Optional. The ID of the DV360 advertiser to which the fetched inventory source is permissioned. If the user only has access to the advertiser and not the parent partner, use this field to specify the relevant advertiser.
    :type advertiser_id: str
    :param partner_id: Required. The ID of the DV360 partner to which the fetched inventory source is permissioned.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_inventory_sources_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, filter=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_inventory_sources_list

    Lists inventory sources that are accessible to the current user. The order is defined by the order_by parameter. If a filter by entity_status is not specified, inventory sources with entity status &#x60;ENTITY_STATUS_ARCHIVED&#x60; will not be included in the results.

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
    :param advertiser_id: The ID of the advertiser that has access to the inventory source.
    :type advertiser_id: str
    :param filter: Allows filtering by inventory source fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;status.entityStatus&#x60; * &#x60;commitment&#x60; * &#x60;deliveryMethod&#x60; * &#x60;rateDetails.rateType&#x60; * &#x60;exchange&#x60; Examples: * All active inventory sources: &#x60;status.entityStatus&#x3D;\&quot;ENTITY_STATUS_ACTIVE\&quot;&#x60; * Inventory sources belonging to Google Ad Manager or Rubicon exchanges: &#x60;exchange&#x3D;\&quot;EXCHANGE_GOOGLE_AD_MANAGER\&quot; OR exchange&#x3D;\&quot;EXCHANGE_RUBICON\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information.
    :type filter: str
    :param order_by: Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. For example, &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;.
    :type page_size: int
    :param page_token: A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListInventorySources&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: The ID of the partner that has access to the inventory source.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_inventory_sources_patch(request: web.Request, inventory_source_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, advertiser_id=None, partner_id=None, update_mask=None, body=None) -> web.Response:
    """displayvideo_inventory_sources_patch

    Updates an existing inventory source. Returns the updated inventory source if successful.

    :param inventory_source_id: Output only. The unique ID of the inventory source. Assigned by the system.
    :type inventory_source_id: str
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
    :param advertiser_id: The ID of the advertiser that the request is being made within.
    :type advertiser_id: str
    :param partner_id: The ID of the partner that the request is being made within.
    :type partner_id: str
    :param update_mask: Required. The mask to control which fields to update.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = InventorySource.from_dict(body)
    return web.Response(status=200)
