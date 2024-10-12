from typing import List, Dict
from aiohttp import web

from openapi_server.models.license_assignment import LicenseAssignment
from openapi_server.models.license_assignment_insert import LicenseAssignmentInsert
from openapi_server.models.license_assignment_list import LicenseAssignmentList
from openapi_server import util


async def licensing_license_assignments_delete(request: web.Request, product_id, sku_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """licensing_license_assignments_delete

    Revoke a license.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
    :param user_id: The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes.
    :type user_id: str
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


async def licensing_license_assignments_get(request: web.Request, product_id, sku_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """licensing_license_assignments_get

    Get a specific user&#39;s license by product SKU.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
    :param user_id: The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes.
    :type user_id: str
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


async def licensing_license_assignments_insert(request: web.Request, product_id, sku_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """licensing_license_assignments_insert

    Assign a license.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
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
    body = LicenseAssignmentInsert.from_dict(body)
    return web.Response(status=200)


async def licensing_license_assignments_list_for_product(request: web.Request, product_id, customer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None) -> web.Response:
    """licensing_license_assignments_list_for_product

    List all users assigned licenses for a specific product SKU.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param customer_id: The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error.
    :type customer_id: str
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
    :param max_results: The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
    :type max_results: int
    :param page_token: Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def licensing_license_assignments_list_for_product_and_sku(request: web.Request, product_id, sku_id, customer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None) -> web.Response:
    """licensing_license_assignments_list_for_product_and_sku

    List all users assigned licenses for a specific product SKU.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
    :param customer_id: The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error.
    :type customer_id: str
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
    :param max_results: The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
    :type max_results: int
    :param page_token: Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def licensing_license_assignments_patch(request: web.Request, product_id, sku_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """licensing_license_assignments_patch

    Reassign a user&#39;s product SKU with a different SKU in the same product. This method supports patch semantics.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
    :param user_id: The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes.
    :type user_id: str
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
    body = LicenseAssignment.from_dict(body)
    return web.Response(status=200)


async def licensing_license_assignments_update(request: web.Request, product_id, sku_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """licensing_license_assignments_update

    Reassign a user&#39;s product SKU with a different SKU in the same product.

    :param product_id: A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs.
    :type product_id: str
    :param sku_id: A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    :type sku_id: str
    :param user_id: The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes.
    :type user_id: str
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
    body = LicenseAssignment.from_dict(body)
    return web.Response(status=200)
