from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server import util


async def servicebroker_get_iam_policy(request: web.Request, resource, fields=None, upload_type=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, access_token=None, key=None, upload_protocol=None, quota_user=None, pretty_print=None, options_requested_policy_version=None) -> web.Response:
    """servicebroker_get_iam_policy

    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

    :param resource: REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
    :type resource: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param options_requested_policy_version: Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset.
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def servicebroker_set_iam_policy(request: web.Request, resource, fields=None, upload_type=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, access_token=None, key=None, upload_protocol=None, quota_user=None, pretty_print=None, body=None) -> web.Response:
    """servicebroker_set_iam_policy

    Sets the access control policy on the specified resource. Replaces any existing policy.  Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

    :param resource: REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
    :type resource: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleIamV1SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def servicebroker_test_iam_permissions(request: web.Request, resource, fields=None, upload_type=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, access_token=None, key=None, upload_protocol=None, quota_user=None, pretty_print=None, body=None) -> web.Response:
    """servicebroker_test_iam_permissions

    Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.  Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
    :type resource: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleIamV1TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)
