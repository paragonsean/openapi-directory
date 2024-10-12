from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server import util


async def servicemanagement_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """servicemanagement_operations_get

    Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

    :param name: The name of the operation resource.
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

    """
    return web.Response(status=200)


async def servicemanagement_operations_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, name=None, page_size=None, page_token=None) -> web.Response:
    """servicemanagement_operations_list

    Lists service operations that match the specified filter in the request.

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
    :param filter: A string for filtering Operations. The following filter fields are supported: * serviceName: Required. Only &#x60;&#x3D;&#x60; operator is allowed. * startTime: The time this job was started, in ISO 8601 format. Allowed operators are &#x60;&gt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, and &#x60;&lt;&#x60;. * status: Can be &#x60;done&#x60;, &#x60;in_progress&#x60;, or &#x60;failed&#x60;. Allowed operators are &#x60;&#x3D;&#x60;, and &#x60;!&#x3D;&#x60;. Filter expression supports conjunction (AND) and disjunction (OR) logical operators. However, the serviceName restriction must be at the top-level and can only be combined with other restrictions via the AND logical operator. Examples: * &#x60;serviceName&#x3D;{some-service}.googleapis.com&#x60; * &#x60;serviceName&#x3D;{some-service}.googleapis.com AND startTime&gt;&#x3D;\&quot;2017-02-01\&quot;&#x60; * &#x60;serviceName&#x3D;{some-service}.googleapis.com AND status&#x3D;done&#x60; * &#x60;serviceName&#x3D;{some-service}.googleapis.com AND (status&#x3D;done OR startTime&gt;&#x3D;\&quot;2017-02-01\&quot;)&#x60;
    :type filter: str
    :param name: Not used.
    :type name: str
    :param page_size: The maximum number of operations to return. If unspecified, defaults to 50. The maximum value is 100.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)
