from typing import List, Dict
from aiohttp import web

from openapi_server.models.policies_list_response import PoliciesListResponse
from openapi_server.models.policies_patch_response import PoliciesPatchResponse
from openapi_server.models.policies_update_response import PoliciesUpdateResponse
from openapi_server.models.policy import Policy
from openapi_server import util


async def dns_policies_create(request: web.Request, project, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None, body=None) -> web.Response:
    """dns_policies_create

    Creates a new Policy.

    :param project: Identifies the project addressed by this request.
    :type project: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Policy.from_dict(body)
    return web.Response(status=200)


async def dns_policies_delete(request: web.Request, project, policy, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None) -> web.Response:
    """dns_policies_delete

    Deletes a previously created Policy. Fails if the policy is still being referenced by a network.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param policy: User given friendly name of the policy addressed by this request.
    :type policy: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str

    """
    return web.Response(status=200)


async def dns_policies_get(request: web.Request, project, policy, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None) -> web.Response:
    """dns_policies_get

    Fetches the representation of an existing Policy.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param policy: User given friendly name of the policy addressed by this request.
    :type policy: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str

    """
    return web.Response(status=200)


async def dns_policies_list(request: web.Request, project, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None) -> web.Response:
    """dns_policies_list

    Enumerates all Policies associated with a project.

    :param project: Identifies the project addressed by this request.
    :type project: str
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
    :param max_results: Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
    :type max_results: int
    :param page_token: Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
    :type page_token: str

    """
    return web.Response(status=200)


async def dns_policies_patch(request: web.Request, project, policy, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None, body=None) -> web.Response:
    """dns_policies_patch

    Applies a partial update to an existing Policy.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param policy: User given friendly name of the policy addressed by this request.
    :type policy: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Policy.from_dict(body)
    return web.Response(status=200)


async def dns_policies_update(request: web.Request, project, policy, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, client_operation_id=None, body=None) -> web.Response:
    """dns_policies_update

    Updates an existing Policy.

    :param project: Identifies the project addressed by this request.
    :type project: str
    :param policy: User given friendly name of the policy addressed by this request.
    :type policy: str
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
    :param client_operation_id: For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    :type client_operation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Policy.from_dict(body)
    return web.Response(status=200)
