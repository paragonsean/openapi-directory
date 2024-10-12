from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server import util


async def storagetransfer_transfer_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """storagetransfer_transfer_operations_cancel

    Cancels a transfer. Use the transferOperations.get method to check if the cancellation succeeded or if the operation completed despite the &#x60;cancel&#x60; request. When you cancel an operation, the currently running transfer is interrupted. For recurring transfer jobs, the next instance of the transfer job will still run. For example, if your job is configured to run every day at 1pm and you cancel Monday&#39;s operation at 1:05pm, Monday&#39;s transfer will stop. However, a transfer job will still be attempted on Tuesday. This applies only to currently running operations. If an operation is not currently running, &#x60;cancel&#x60; does nothing. *Caution:* Canceling a transfer job can leave your data in an unknown state. We recommend that you restore the state at both the destination and the source after the &#x60;cancel&#x60; request completes so that your data is in a consistent state. When you cancel a job, the next job computes a delta of files and may repair any inconsistent state. For instance, if you run a job every day, and today&#39;s job found 10 new files and transferred five files before you canceled the job, tomorrow&#39;s transfer operation will compute a new delta with the five files that were not copied today plus any new files discovered tomorrow.

    :param name: The name of the operation resource to be cancelled.
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
    :type body: 

    """
    return web.Response(status=200)


async def storagetransfer_transfer_operations_list(request: web.Request, name, filter, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """storagetransfer_transfer_operations_list

    Lists transfer operations. Operations are ordered by their creation time in reverse chronological order.

    :param name: Required. The name of the type being listed; must be &#x60;transferOperations&#x60;.
    :type name: str
    :param filter: Required. A list of query parameters specified as JSON text in the form of: &#x60;{\&quot;projectId\&quot;:\&quot;my_project_id\&quot;, \&quot;jobNames\&quot;:[\&quot;jobid1\&quot;,\&quot;jobid2\&quot;,...], \&quot;jobNamePattern\&quot;: \&quot;job_name_pattern\&quot;, \&quot;operationNames\&quot;:[\&quot;opid1\&quot;,\&quot;opid2\&quot;,...], \&quot;operationNamePattern\&quot;: \&quot;operation_name_pattern\&quot;, \&quot;minCreationTime\&quot;: \&quot;min_creation_time\&quot;, \&quot;maxCreationTime\&quot;: \&quot;max_creation_time\&quot;, \&quot;transferStatuses\&quot;:[\&quot;status1\&quot;,\&quot;status2\&quot;,...]}&#x60; Since &#x60;jobNames&#x60;, &#x60;operationNames&#x60;, and &#x60;transferStatuses&#x60; support multiple values, they must be specified with array notation. &#x60;projectId&#x60; is the only argument that is required. If specified, &#x60;jobNamePattern&#x60; and &#x60;operationNamePattern&#x60; must match the full job or operation name respectively. &#39;*&#39; is a wildcard matching 0 or more characters. &#x60;minCreationTime&#x60; and &#x60;maxCreationTime&#x60; should be timestamps encoded as a string in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. The valid values for &#x60;transferStatuses&#x60; are case-insensitive: IN_PROGRESS, PAUSED, SUCCESS, FAILED, and ABORTED.
    :type filter: str
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
    :param page_size: The list page size. The max allowed value is 256.
    :type page_size: int
    :param page_token: The list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def storagetransfer_transfer_operations_pause(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """storagetransfer_transfer_operations_pause

    Pauses a transfer operation.

    :param name: Required. The name of the transfer operation.
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
    :type body: 

    """
    return web.Response(status=200)


async def storagetransfer_transfer_operations_resume(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """storagetransfer_transfer_operations_resume

    Resumes a transfer operation that is paused.

    :param name: Required. The name of the transfer operation.
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
    :type body: 

    """
    return web.Response(status=200)
