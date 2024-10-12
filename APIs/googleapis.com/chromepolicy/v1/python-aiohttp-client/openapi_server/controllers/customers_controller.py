from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_chrome_policy_versions_v1_batch_delete_group_policies_request import GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_inherit_org_unit_policies_request import GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_modify_group_policies_request import GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_modify_org_unit_policies_request import GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_certificate_request import GoogleChromePolicyVersionsV1DefineCertificateRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_certificate_response import GoogleChromePolicyVersionsV1DefineCertificateResponse
from openapi_server.models.google_chrome_policy_versions_v1_define_network_request import GoogleChromePolicyVersionsV1DefineNetworkRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_network_response import GoogleChromePolicyVersionsV1DefineNetworkResponse
from openapi_server.models.google_chrome_policy_versions_v1_list_group_priority_ordering_request import GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequest
from openapi_server.models.google_chrome_policy_versions_v1_list_group_priority_ordering_response import GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponse
from openapi_server.models.google_chrome_policy_versions_v1_list_policy_schemas_response import GoogleChromePolicyVersionsV1ListPolicySchemasResponse
from openapi_server.models.google_chrome_policy_versions_v1_policy_schema import GoogleChromePolicyVersionsV1PolicySchema
from openapi_server.models.google_chrome_policy_versions_v1_remove_certificate_request import GoogleChromePolicyVersionsV1RemoveCertificateRequest
from openapi_server.models.google_chrome_policy_versions_v1_remove_network_request import GoogleChromePolicyVersionsV1RemoveNetworkRequest
from openapi_server.models.google_chrome_policy_versions_v1_resolve_request import GoogleChromePolicyVersionsV1ResolveRequest
from openapi_server.models.google_chrome_policy_versions_v1_resolve_response import GoogleChromePolicyVersionsV1ResolveResponse
from openapi_server.models.google_chrome_policy_versions_v1_update_group_priority_ordering_request import GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequest
from openapi_server import util


async def chromepolicy_customers_policies_groups_batch_delete(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_groups_batch_delete

    Delete multiple policy values that are applied to a specific group. All targets must have the same target format. That is to say that they must point to the same target resource and must have the same keys specified in &#x60;additionalTargetKeyNames&#x60;, though the values for those keys may be different. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: ID of the Google Workspace account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_groups_batch_modify(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_groups_batch_modify

    Modify multiple policy values that are applied to a specific group. All targets must have the same target format. That is to say that they must point to the same target resource and must have the same keys specified in &#x60;additionalTargetKeyNames&#x60;, though the values for those keys may be different. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: ID of the Google Workspace account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_groups_list_group_priority_ordering(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_groups_list_group_priority_ordering

    Retrieve a group priority ordering for an app. The target app must be supplied in &#x60;additionalTargetKeyNames&#x60; in the PolicyTargetKey. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: Required. ID of the Google Workspace account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_groups_update_group_priority_ordering(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_groups_update_group_priority_ordering

    Update a group priority ordering for an app. The target app must be supplied in &#x60;additionalTargetKeyNames&#x60; in the PolicyTargetKey. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: Required. ID of the Google Workspace account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_networks_define_certificate(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_networks_define_certificate

    Creates a certificate at a specified OU for a customer.

    :param customer: Required. The customer for which the certificate will apply.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1DefineCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_networks_define_network(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_networks_define_network

    Define a new network.

    :param customer: Required. The customer who will own this new network.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1DefineNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_networks_remove_certificate(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_networks_remove_certificate

    Remove an existing certificate by guid.

    :param customer: Required. The customer whose certificate will be removed.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1RemoveCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_networks_remove_network(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_networks_remove_network

    Remove an existing network by guid.

    :param customer: Required. The customer whose network will be removed.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1RemoveNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_orgunits_batch_inherit(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_orgunits_batch_inherit

    Modify multiple policy values that are applied to a specific org unit so that they now inherit the value from a parent (if applicable). All targets must have the same target format. That is to say that they must point to the same target resource and must have the same keys specified in &#x60;additionalTargetKeyNames&#x60;, though the values for those keys may be different. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: ID of the G Suite account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_orgunits_batch_modify(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_orgunits_batch_modify

    Modify multiple policy values that are applied to a specific org unit. All targets must have the same target format. That is to say that they must point to the same target resource and must have the same keys specified in &#x60;additionalTargetKeyNames&#x60;, though the values for those keys may be different. On failure the request will return the error details as part of the google.rpc.Status.

    :param customer: ID of the G Suite account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policies_resolve(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chromepolicy_customers_policies_resolve

    Gets the resolved policy values for a list of policies that match a search query.

    :param customer: ID of the G Suite account or literal \&quot;my_customer\&quot; for the customer associated to the request.
    :type customer: str
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
    body = GoogleChromePolicyVersionsV1ResolveRequest.from_dict(body)
    return web.Response(status=200)


async def chromepolicy_customers_policy_schemas_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """chromepolicy_customers_policy_schemas_get

    Get a specific policy schema for a customer by its resource name.

    :param name: Required. The policy schema resource name to query.
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


async def chromepolicy_customers_policy_schemas_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """chromepolicy_customers_policy_schemas_list

    Gets a list of policy schemas that match a specified filter value for a given customer.

    :param parent: Required. The customer for which the listing request will apply.
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
    :param filter: The schema filter used to find a particular schema based on fields like its resource name, description and &#x60;additionalTargetKeyNames&#x60;.
    :type filter: str
    :param page_size: The maximum number of policy schemas to return, defaults to 100 and has a maximum of 1000.
    :type page_size: int
    :param page_token: The page token used to retrieve a specific page of the listing request.
    :type page_token: str

    """
    return web.Response(status=200)
