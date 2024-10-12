from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_orgpolicy_v2_list_constraints_response import GoogleCloudOrgpolicyV2ListConstraintsResponse
from openapi_server.models.google_cloud_orgpolicy_v2_list_policies_response import GoogleCloudOrgpolicyV2ListPoliciesResponse
from openapi_server.models.google_cloud_orgpolicy_v2_policy import GoogleCloudOrgpolicyV2Policy
from openapi_server import util


async def orgpolicy_projects_constraints_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """orgpolicy_projects_constraints_list

    Lists constraints that could be applied on the specified resource.

    :param parent: Required. The Google Cloud resource that parents the constraint. Must be in one of the following forms: * &#x60;projects/{project_number}&#x60; * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60;
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
    :param page_size: Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size.
    :type page_size: int
    :param page_token: Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field.
    :type page_token: str

    """
    return web.Response(status=200)


async def orgpolicy_projects_policies_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """orgpolicy_projects_policies_create

    Creates a policy. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the constraint does not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ALREADY_EXISTS&#x60; if the policy already exists on the given Google Cloud resource.

    :param parent: Required. The Google Cloud resource that will parent the new policy. Must be in one of the following forms: * &#x60;projects/{project_number}&#x60; * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60;
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudOrgpolicyV2Policy.from_dict(body)
    return web.Response(status=200)


async def orgpolicy_projects_policies_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, etag=None) -> web.Response:
    """orgpolicy_projects_policies_delete

    Deletes a policy. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the constraint or organization policy does not exist.

    :param name: Required. Name of the policy to delete. See the policy entry for naming rules.
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
    :param etag: Optional. The current etag of policy. If an etag is provided and does not match the current etag of the policy, deletion will be blocked and an ABORTED error will be returned.
    :type etag: str

    """
    return web.Response(status=200)


async def orgpolicy_projects_policies_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """orgpolicy_projects_policies_get

    Gets a policy on a resource. If no policy is set on the resource, &#x60;NOT_FOUND&#x60; is returned. The &#x60;etag&#x60; value can be used with &#x60;UpdatePolicy()&#x60; to update a policy during read-modify-write.

    :param name: Required. Resource name of the policy. See Policy for naming requirements.
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


async def orgpolicy_projects_policies_get_effective_policy(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """orgpolicy_projects_policies_get_effective_policy

    Gets the effective policy on a resource. This is the result of merging policies in the resource hierarchy and evaluating conditions. The returned policy will not have an &#x60;etag&#x60; or &#x60;condition&#x60; set because it is an evaluated policy across multiple resources. Subtrees of Resource Manager resource hierarchy with &#39;under:&#39; prefix will not be expanded.

    :param name: Required. The effective policy to compute. See Policy for naming requirements.
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


async def orgpolicy_projects_policies_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """orgpolicy_projects_policies_list

    Retrieves all of the policies that exist on a particular resource.

    :param parent: Required. The target Google Cloud resource that parents the set of constraints and policies that will be returned from this call. Must be in one of the following forms: * &#x60;projects/{project_number}&#x60; * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60;
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
    :param page_size: Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size.
    :type page_size: int
    :param page_token: Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field.
    :type page_token: str

    """
    return web.Response(status=200)


async def orgpolicy_projects_policies_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """orgpolicy_projects_policies_patch

    Updates a policy. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the constraint or the policy do not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ABORTED&#x60; if the etag supplied in the request does not match the persisted etag of the policy Note: the supplied policy will perform a full overwrite of all fields.

    :param name: Immutable. The resource name of the policy. Must be one of the following forms, where &#x60;constraint_name&#x60; is the name of the constraint which this policy configures: * &#x60;projects/{project_number}/policies/{constraint_name}&#x60; * &#x60;folders/{folder_id}/policies/{constraint_name}&#x60; * &#x60;organizations/{organization_id}/policies/{constraint_name}&#x60; For example, &#x60;projects/123/policies/compute.disableSerialPortAccess&#x60;. Note: &#x60;projects/{project_id}/policies/{constraint_name}&#x60; is also an acceptable name for API requests, but responses will return the name using the equivalent project number.
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
    :param update_mask: Field mask used to specify the fields to be overwritten in the policy by the set. The fields specified in the update_mask are relative to the policy, not the full request.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudOrgpolicyV2Policy.from_dict(body)
    return web.Response(status=200)
