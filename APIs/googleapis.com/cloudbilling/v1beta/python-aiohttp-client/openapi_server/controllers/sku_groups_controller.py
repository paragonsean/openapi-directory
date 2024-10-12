from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_billing_skugroups_v1beta_list_sku_groups_response import GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse
from openapi_server.models.google_cloud_billing_skugroupskus_v1beta_list_sku_group_skus_response import GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse
from openapi_server import util


async def cloudbilling_sku_groups_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_sku_groups_list

    Lists all publicly listed SKU groups.

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
    :param page_size: Maximum number of SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    :type page_size: int
    :param page_token: Page token received from a previous ListSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudbilling_sku_groups_skus_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_sku_groups_skus_list

    Lists all publicly listed SKUs contained by a publicly listed SKU group.

    :param parent: Required. The SkuGroup to list SkuGroupSku from. Format: skuGroups/{sku_group}
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
    :param page_size: Maximum number of SKU group SKUs to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    :type page_size: int
    :param page_token: Page token received from a previous ListSkuGroupSkus call to retrieve the next page of results. If this field is empty, the first page is returned.
    :type page_token: str

    """
    return web.Response(status=200)
