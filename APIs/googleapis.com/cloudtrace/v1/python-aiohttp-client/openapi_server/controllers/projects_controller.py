from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_traces_response import ListTracesResponse
from openapi_server.models.trace import Trace
from openapi_server.models.traces import Traces
from openapi_server import util


async def cloudtrace_projects_patch_traces(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudtrace_projects_patch_traces

    Sends new traces to Cloud Trace or updates existing traces. If the ID of a trace that you send matches that of an existing trace, any fields in the existing trace and its spans are overwritten by the provided values, and any new fields provided are merged with the existing trace data. If the ID does not match, a new trace is created.

    :param project_id: Required. ID of the Cloud project where the trace data is stored.
    :type project_id: str
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
    body = Traces.from_dict(body)
    return web.Response(status=200)


async def cloudtrace_projects_traces_get(request: web.Request, project_id, trace_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """cloudtrace_projects_traces_get

    Gets a single trace by its ID.

    :param project_id: Required. ID of the Cloud project where the trace data is stored.
    :type project_id: str
    :param trace_id: Required. ID of the trace to return.
    :type trace_id: str
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


async def cloudtrace_projects_traces_list(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_time=None, filter=None, order_by=None, page_size=None, page_token=None, start_time=None, view=None) -> web.Response:
    """cloudtrace_projects_traces_list

    Returns a list of traces that match the specified filter conditions.

    :param project_id: Required. ID of the Cloud project where the trace data is stored.
    :type project_id: str
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
    :param end_time: End of the time interval (inclusive) during which the trace data was collected from the application.
    :type end_time: str
    :param filter: Optional. A filter against labels for the request. By default, searches use prefix matching. To specify exact match, prepend a plus symbol (&#x60;+&#x60;) to the search term. Multiple terms are ANDed. Syntax: * &#x60;root:NAME_PREFIX&#x60; or &#x60;NAME_PREFIX&#x60;: Return traces where any root span starts with &#x60;NAME_PREFIX&#x60;. * &#x60;+root:NAME&#x60; or &#x60;+NAME&#x60;: Return traces where any root span&#39;s name is exactly &#x60;NAME&#x60;. * &#x60;span:NAME_PREFIX&#x60;: Return traces where any span starts with &#x60;NAME_PREFIX&#x60;. * &#x60;+span:NAME&#x60;: Return traces where any span&#39;s name is exactly &#x60;NAME&#x60;. * &#x60;latency:DURATION&#x60;: Return traces whose overall latency is greater or equal to than &#x60;DURATION&#x60;. Accepted units are nanoseconds (&#x60;ns&#x60;), milliseconds (&#x60;ms&#x60;), and seconds (&#x60;s&#x60;). Default is &#x60;ms&#x60;. For example, &#x60;latency:24ms&#x60; returns traces whose overall latency is greater than or equal to 24 milliseconds. * &#x60;label:LABEL_KEY&#x60;: Return all traces containing the specified label key (exact match, case-sensitive) regardless of the key:value pair&#39;s value (including empty values). * &#x60;LABEL_KEY:VALUE_PREFIX&#x60;: Return all traces containing the specified label key (exact match, case-sensitive) whose value starts with &#x60;VALUE_PREFIX&#x60;. Both a key and a value must be specified. * &#x60;+LABEL_KEY:VALUE&#x60;: Return all traces containing a key:value pair exactly matching the specified text. Both a key and a value must be specified. * &#x60;method:VALUE&#x60;: Equivalent to &#x60;/http/method:VALUE&#x60;. * &#x60;url:VALUE&#x60;: Equivalent to &#x60;/http/url:VALUE&#x60;.
    :type filter: str
    :param order_by: Optional. Field used to sort the returned traces. Can be one of the following: * &#x60;trace_id&#x60; * &#x60;name&#x60; (&#x60;name&#x60; field of root span in the trace) * &#x60;duration&#x60; (difference between &#x60;end_time&#x60; and &#x60;start_time&#x60; fields of the root span) * &#x60;start&#x60; (&#x60;start_time&#x60; field of the root span) Descending order can be specified by appending &#x60;desc&#x60; to the sort field (for example, &#x60;name desc&#x60;). Only one sort field is permitted.
    :type order_by: str
    :param page_size: Optional. Maximum number of traces to return. If not specified or &lt;&#x3D; 0, the implementation selects a reasonable value. The implementation may return fewer traces than the requested page size.
    :type page_size: int
    :param page_token: Token identifying the page of results to return. If provided, use the value of the &#x60;next_page_token&#x60; field from a previous request.
    :type page_token: str
    :param start_time: Start of the time interval (inclusive) during which the trace data was collected from the application.
    :type start_time: str
    :param view: Optional. Type of data returned for traces in the list. Default is &#x60;MINIMAL&#x60;.
    :type view: str

    """
    return web.Response(status=200)
