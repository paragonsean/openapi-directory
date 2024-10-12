from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server import util


async def cloudprivatecatalogproducer_operations_cancel(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_operations_cancel

    Starts asynchronous cancellation on a long-running operation.  The server makes a best effort to cancel the operation, but success is not guaranteed.  If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;.  Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

    :param name: The name of the operation resource to be cancelled.
    :type name: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_operations_list(request: web.Request, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, filter=None, name=None, page_size=None, page_token=None) -> web.Response:
    """cloudprivatecatalogproducer_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.  NOTE: the &#x60;name&#x60; binding allows API services to override the binding to use different resource name schemes, such as &#x60;users/*/operations&#x60;. To override the binding, API services can add a binding such as &#x60;\&quot;/v1/{name&#x3D;users/*}/operations\&quot;&#x60; to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param filter: The standard list filter.
    :type filter: str
    :param name: The name of the operation&#39;s parent resource.
    :type name: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)
