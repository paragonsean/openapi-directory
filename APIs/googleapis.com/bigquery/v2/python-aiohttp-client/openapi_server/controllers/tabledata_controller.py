from typing import List, Dict
from aiohttp import web

from openapi_server.models.table_data_insert_all_request import TableDataInsertAllRequest
from openapi_server.models.table_data_insert_all_response import TableDataInsertAllResponse
from openapi_server.models.table_data_list import TableDataList
from openapi_server import util


async def bigquery_tabledata_insert_all(request: web.Request, project_id, dataset_id, table_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquery_tabledata_insert_all

    Streams data into BigQuery one record at a time without needing to run a load job.

    :param project_id: Required. Project ID of the destination.
    :type project_id: str
    :param dataset_id: Required. Dataset ID of the destination.
    :type dataset_id: str
    :param table_id: Required. Table ID of the destination.
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
    :param body: 
    :type body: dict | bytes

    """
    body = TableDataInsertAllRequest.from_dict(body)
    return web.Response(status=200)


async def bigquery_tabledata_list(request: web.Request, project_id, dataset_id, table_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, format_options_use_int64_timestamp=None, max_results=None, page_token=None, selected_fields=None, start_index=None) -> web.Response:
    """bigquery_tabledata_list

    List the content of a table in rows.

    :param project_id: Required. Project id of the table to list.
    :type project_id: str
    :param dataset_id: Required. Dataset id of the table to list.
    :type dataset_id: str
    :param table_id: Required. Table id of the table to list.
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
    :param format_options_use_int64_timestamp: Optional. Output timestamp as usec int64. Default is false.
    :type format_options_use_int64_timestamp: bool
    :param max_results: Row limit of the table.
    :type max_results: int
    :param page_token: To retrieve the next page of table data, set this field to the string provided in the pageToken field of the response body from your previous call to tabledata.list.
    :type page_token: str
    :param selected_fields: Subset of fields to return, supports select into sub fields. Example: selected_fields &#x3D; \&quot;a,e.d.f\&quot;;
    :type selected_fields: str
    :param start_index: Start row index of the table.
    :type start_index: str

    """
    return web.Response(status=200)
