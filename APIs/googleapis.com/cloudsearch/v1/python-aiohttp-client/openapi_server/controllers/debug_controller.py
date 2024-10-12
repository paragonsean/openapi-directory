from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_access_response import CheckAccessResponse
from openapi_server.models.list_item_names_for_unmapped_identity_response import ListItemNamesForUnmappedIdentityResponse
from openapi_server.models.list_unmapped_identities_response import ListUnmappedIdentitiesResponse
from openapi_server.models.principal import Principal
from openapi_server.models.search_items_by_view_url_request import SearchItemsByViewUrlRequest
from openapi_server.models.search_items_by_view_url_response import SearchItemsByViewUrlResponse
from openapi_server import util


async def cloudsearch_debug_datasources_items_check_access(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, debug_options_enable_debugging=None, body=None) -> web.Response:
    """cloudsearch_debug_datasources_items_check_access

    Checks whether an item is accessible by specified principal. Principal must be a user; groups and domain values aren&#39;t supported. **Note:** This API requires an admin account to execute.

    :param name: Item name, format: datasources/{source_id}/items/{item_id}
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
    :param debug_options_enable_debugging: If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    :type debug_options_enable_debugging: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Principal.from_dict(body)
    return web.Response(status=200)


async def cloudsearch_debug_datasources_items_search_by_view_url(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudsearch_debug_datasources_items_search_by_view_url

    Fetches the item whose viewUrl exactly matches that of the URL provided in the request. **Note:** This API requires an admin account to execute.

    :param name: Source name, format: datasources/{source_id}
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
    :param body: 
    :type body: dict | bytes

    """
    body = SearchItemsByViewUrlRequest.from_dict(body)
    return web.Response(status=200)


async def cloudsearch_debug_identitysources_items_list_forunmappedidentity(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, debug_options_enable_debugging=None, group_resource_name=None, page_size=None, page_token=None, user_resource_name=None) -> web.Response:
    """cloudsearch_debug_identitysources_items_list_forunmappedidentity

    Lists names of items associated with an unmapped identity. **Note:** This API requires an admin account to execute.

    :param parent: The name of the identity source, in the following format: identitysources/{source_id}}
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
    :param debug_options_enable_debugging: If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    :type debug_options_enable_debugging: bool
    :param group_resource_name: 
    :type group_resource_name: str
    :param page_size: Maximum number of items to fetch in a request. Defaults to 100.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str
    :param user_resource_name: 
    :type user_resource_name: str

    """
    return web.Response(status=200)


async def cloudsearch_debug_identitysources_unmappedids_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, debug_options_enable_debugging=None, page_size=None, page_token=None, resolution_status_code=None) -> web.Response:
    """cloudsearch_debug_identitysources_unmappedids_list

    Lists unmapped user identities for an identity source. **Note:** This API requires an admin account to execute.

    :param parent: The name of the identity source, in the following format: identitysources/{source_id}
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
    :param debug_options_enable_debugging: If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    :type debug_options_enable_debugging: bool
    :param page_size: Maximum number of items to fetch in a request. Defaults to 100.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str
    :param resolution_status_code: Limit users selection to this status.
    :type resolution_status_code: str

    """
    return web.Response(status=200)
