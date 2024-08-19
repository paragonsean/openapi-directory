from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_status import ProductStatus
from openapi_server.models.productstatuses_custom_batch_request import ProductstatusesCustomBatchRequest
from openapi_server.models.productstatuses_custom_batch_response import ProductstatusesCustomBatchResponse
from openapi_server.models.productstatuses_list_response import ProductstatusesListResponse
from openapi_server import util


async def content_productstatuses_custombatch(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_attributes=None, body=None) -> web.Response:
    """content_productstatuses_custombatch

    Gets the statuses of multiple products in a single request.

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
    :param include_attributes: Flag to include full product data in the results of this request. The default value is false.
    :type include_attributes: bool
    :param body: 
    :type body: dict | bytes

    """
    body = ProductstatusesCustomBatchRequest.from_dict(body)
    return web.Response(status=200)


async def content_productstatuses_get(request: web.Request, merchant_id, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, destinations=None, include_attributes=None) -> web.Response:
    """content_productstatuses_get

    Gets the status of a product from your Merchant Center account.

    :param merchant_id: The ID of the account that contains the product. This account cannot be a multi-client account.
    :type merchant_id: str
    :param product_id: The REST ID of the product.
    :type product_id: str
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
    :param destinations: If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination.
    :type destinations: List[str]
    :param include_attributes: Flag to include full product data in the result of this get request. The default value is false.
    :type include_attributes: bool

    """
    return web.Response(status=200)


async def content_productstatuses_list(request: web.Request, merchant_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, destinations=None, include_attributes=None, include_invalid_inserted_items=None, max_results=None, page_token=None) -> web.Response:
    """content_productstatuses_list

    Lists the statuses of the products in your Merchant Center account.

    :param merchant_id: The ID of the account that contains the products. This account cannot be a multi-client account.
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
    :param destinations: If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination.
    :type destinations: List[str]
    :param include_attributes: Flag to include full product data in the results of the list request. The default value is false.
    :type include_attributes: bool
    :param include_invalid_inserted_items: Flag to include the invalid inserted items in the result of the list request. By default the invalid items are not shown (the default value is false).
    :type include_invalid_inserted_items: bool
    :param max_results: The maximum number of product statuses to return in the response, used for paging.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str

    """
    return web.Response(status=200)
