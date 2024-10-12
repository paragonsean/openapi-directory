from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_row_access_policies_response import ListRowAccessPoliciesResponse
from openapi_server import util


async def bigquery_row_access_policies_list(request: web.Request, project_id, dataset_id, table_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """bigquery_row_access_policies_list

    Lists all row access policies on the specified table.

    :param project_id: Required. Project ID of the row access policies to list.
    :type project_id: str
    :param dataset_id: Required. Dataset ID of row access policies to list.
    :type dataset_id: str
    :param table_id: Required. Table ID of the table to list row access policies.
    :type table_id: str
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
    :param page_size: The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.
    :type page_size: int
    :param page_token: Page token, returned by a previous call, to request the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)
