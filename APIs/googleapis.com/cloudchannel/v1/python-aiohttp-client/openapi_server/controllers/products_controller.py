from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_channel_v1_list_products_response import GoogleCloudChannelV1ListProductsResponse
from openapi_server.models.google_cloud_channel_v1_list_skus_response import GoogleCloudChannelV1ListSkusResponse
from openapi_server import util


async def cloudchannel_products_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, account=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_products_list

    Lists the Products the reseller is authorized to sell. Possible error codes: * INVALID_ARGUMENT: Required request parameters are missing or invalid.

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
    :param account: Required. The resource name of the reseller account. Format: accounts/{account_id}.
    :type account: str
    :param language_code: Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Products. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_products_skus_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, account=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_products_skus_list

    Lists the SKUs for a product the reseller is authorized to sell. Possible error codes: * INVALID_ARGUMENT: Required request parameters are missing or invalid.

    :param parent: Required. The resource name of the Product to list SKUs for. Parent uses the format: products/{product_id}. Supports products/- to retrieve SKUs for all products.
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
    :param account: Required. Resource name of the reseller. Format: accounts/{account_id}.
    :type account: str
    :param language_code: Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page. Optional.
    :type page_token: str

    """
    return web.Response(status=200)
