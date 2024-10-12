from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.credentials import Credentials
from openapi_server.models.external_access_rule import ExternalAccessRule
from openapi_server.models.external_address import ExternalAddress
from openapi_server.models.fetch_network_policy_external_addresses_response import FetchNetworkPolicyExternalAddressesResponse
from openapi_server.models.grant_dns_bind_permission_request import GrantDnsBindPermissionRequest
from openapi_server.models.hcx_activation_key import HcxActivationKey
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_external_access_rules_response import ListExternalAccessRulesResponse
from openapi_server.models.list_external_addresses_response import ListExternalAddressesResponse
from openapi_server.models.list_hcx_activation_keys_response import ListHcxActivationKeysResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_logging_servers_response import ListLoggingServersResponse
from openapi_server.models.list_management_dns_zone_bindings_response import ListManagementDnsZoneBindingsResponse
from openapi_server.models.list_network_peerings_response import ListNetworkPeeringsResponse
from openapi_server.models.list_network_policies_response import ListNetworkPoliciesResponse
from openapi_server.models.list_node_types_response import ListNodeTypesResponse
from openapi_server.models.list_nodes_response import ListNodesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_private_clouds_response import ListPrivateCloudsResponse
from openapi_server.models.list_private_connection_peering_routes_response import ListPrivateConnectionPeeringRoutesResponse
from openapi_server.models.list_private_connections_response import ListPrivateConnectionsResponse
from openapi_server.models.list_subnets_response import ListSubnetsResponse
from openapi_server.models.list_vmware_engine_networks_response import ListVmwareEngineNetworksResponse
from openapi_server.models.logging_server import LoggingServer
from openapi_server.models.management_dns_zone_binding import ManagementDnsZoneBinding
from openapi_server.models.network_peering import NetworkPeering
from openapi_server.models.network_policy import NetworkPolicy
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.private_cloud import PrivateCloud
from openapi_server.models.private_connection import PrivateConnection
from openapi_server.models.repair_management_dns_zone_binding_request import RepairManagementDnsZoneBindingRequest
from openapi_server.models.reset_nsx_credentials_request import ResetNsxCredentialsRequest
from openapi_server.models.reset_vcenter_credentials_request import ResetVcenterCredentialsRequest
from openapi_server.models.revoke_dns_bind_permission_request import RevokeDnsBindPermissionRequest
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.undelete_private_cloud_request import UndeletePrivateCloudRequest
from openapi_server.models.vmware_engine_network import VmwareEngineNetwork
from openapi_server import util


async def vmwareengine_projects_locations_dns_bind_permission_grant(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_dns_bind_permission_grant

    Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

    :param name: Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/dnsBindPermission&#x60;
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
    :type body: dict | bytes

    """
    body = GrantDnsBindPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_dns_bind_permission_revoke(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_dns_bind_permission_revoke

    Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

    :param name: Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/dnsBindPermission&#x60;
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
    :type body: dict | bytes

    """
    body = RevokeDnsBindPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_list

    Lists information about the supported locations for this service.

    :param name: The resource that owns the locations collection, if applicable.
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
    :param filter: A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
    :type filter: str
    :param page_size: The maximum number of results to return. If not set, the service selects a default.
    :type page_size: int
    :param page_token: A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_peerings_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, network_peering_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_network_peerings_create

    Creates a new network peering between the peer network and VMware Engine network provided in a &#x60;NetworkPeering&#x60; resource. NetworkPeering is a global resource and location can only be global.

    :param parent: Required. The resource name of the location to create the new network peering in. This value is always &#x60;global&#x60;, because &#x60;NetworkPeering&#x60; is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global&#x60;
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
    :param network_peering_id: Required. The user-provided identifier of the new &#x60;NetworkPeering&#x60;. This identifier must be unique among &#x60;NetworkPeering&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type network_peering_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NetworkPeering.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_peerings_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_network_peerings_list

    Lists &#x60;NetworkPeering&#x60; resources in a given project. NetworkPeering is a global resource and location can only be global.

    :param parent: Required. The resource name of the location (global) to query for network peerings. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of network peerings, you can exclude the ones named &#x60;example-peering&#x60; by specifying &#x60;name !&#x3D; \&quot;example-peering\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-peering\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-peering-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-peering-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of network peerings to return in one page. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListNetworkPeerings&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListNetworkPeerings&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_policies_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, network_policy_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_network_policies_create

    Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

    :param parent: Required. The resource name of the location (region) to create the new network policy in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1&#x60;
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
    :param network_policy_id: Required. The user-provided identifier of the network policy to be created. This identifier must be unique within parent &#x60;projects/{my-project}/locations/{us-central1}/networkPolicies&#x60; and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type network_policy_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NetworkPolicy.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_policies_external_access_rules_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, external_access_rule_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_network_policies_external_access_rules_create

    Creates a new external access rule in a given network policy.

    :param parent: Required. The resource name of the network policy to create a new external access firewall rule in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/networkPolicies/my-policy&#x60;
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
    :param external_access_rule_id: Required. The user-provided identifier of the &#x60;ExternalAccessRule&#x60; to be created. This identifier must be unique among &#x60;ExternalAccessRule&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type external_access_rule_id: str
    :param request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExternalAccessRule.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_policies_external_access_rules_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_network_policies_external_access_rules_list

    Lists &#x60;ExternalAccessRule&#x60; resources in the specified network policy.

    :param parent: Required. The resource name of the network policy to query for external access firewall rules. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/networkPolicies/my-policy&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of external access rules, you can exclude the ones named &#x60;example-rule&#x60; by specifying &#x60;name !&#x3D; \&quot;example-rule\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-rule\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-rule-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-rule-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of external access rules to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListExternalAccessRulesRequest&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListExternalAccessRulesRequest&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_policies_fetch_external_addresses(request: web.Request, network_policy, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_network_policies_fetch_external_addresses

    Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

    :param network_policy: Required. The resource name of the network policy to query for assigned external IP addresses. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/networkPolicies/my-policy&#x60;
    :type network_policy: str
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
    :param page_size: The maximum number of external IP addresses to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;FetchNetworkPolicyExternalAddresses&#x60; call. Provide this to retrieve the subsequent page. When paginating, all parameters provided to &#x60;FetchNetworkPolicyExternalAddresses&#x60;, except for &#x60;page_size&#x60; and &#x60;page_token&#x60;, must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_network_policies_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_network_policies_list

    Lists &#x60;NetworkPolicy&#x60; resources in a specified project and location.

    :param parent: Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of network policies, you can exclude the ones named &#x60;example-policy&#x60; by specifying &#x60;name !&#x3D; \&quot;example-policy\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-policy\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-policy-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-policy-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of network policies to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListNetworkPolicies&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListNetworkPolicies&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_node_types_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_node_types_list

    Lists node types

    :param parent: Required. The resource name of the location to be queried for node types. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of node types, you can exclude the ones named &#x60;standard-72&#x60; by specifying &#x60;name !&#x3D; \&quot;standard-72\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;standard-72\&quot;) (virtual_cpu_count &gt; 2) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;standard-96\&quot;) AND (virtual_cpu_count &gt; 2) OR (name &#x3D; \&quot;standard-72\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param page_size: The maximum number of node types to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListNodeTypes&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListNodeTypes&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
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
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_clusters_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, cluster_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_clusters_create

    Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

    :param parent: Required. The resource name of the private cloud to create a new cluster in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param cluster_id: Required. The user-provided identifier of the new &#x60;Cluster&#x60;. This identifier must be unique among clusters within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type cluster_id: str
    :param request_id: Optional. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. True if you want the request to be validated and not executed; false otherwise.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Cluster.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_clusters_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_clusters_list

    Lists &#x60;Cluster&#x60; resources in a given private cloud.

    :param parent: Required. The resource name of the private cloud to query for clusters. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param filter:  To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-cluster\&quot;) (nodeCount &#x3D; \&quot;3\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-cluster-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-cluster-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of clusters to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListClusters&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListClusters&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_clusters_nodes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_clusters_nodes_list

    Lists nodes in a given cluster.

    :param parent: Required. The resource name of the cluster to be queried for nodes. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster&#x60;
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
    :param page_size: The maximum number of nodes to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListNodes&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListNodes&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, private_cloud_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_create

    Creates a new &#x60;PrivateCloud&#x60; resource in a given project and location. Private clouds of type &#x60;STANDARD&#x60; and &#x60;TIME_LIMITED&#x60; are zonal resources, &#x60;STRETCHED&#x60; private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

    :param parent: Required. The resource name of the location to create the new private cloud in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a&#x60;
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
    :param private_cloud_id: Required. The user-provided identifier of the private cloud to be created. This identifier must be unique among each &#x60;PrivateCloud&#x60; within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type private_cloud_id: str
    :param request_id: Optional. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. True if you want the request to be validated and not executed; false otherwise.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = PrivateCloud.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_external_addresses_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, external_address_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_external_addresses_create

    Creates a new &#x60;ExternalAddress&#x60; resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (&#x60;NetworkPolicy.external_ip&#x60;).

    :param parent: Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param external_address_id: Required. The user-provided identifier of the &#x60;ExternalAddress&#x60; to be created. This identifier must be unique among &#x60;ExternalAddress&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type external_address_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExternalAddress.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_external_addresses_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_external_addresses_list

    Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

    :param parent: Required. The resource name of the private cloud to be queried for external IP addresses. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of IP addresses, you can exclude the ones named &#x60;example-ip&#x60; by specifying &#x60;name !&#x3D; \&quot;example-ip\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-ip\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-ip-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-ip-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of external IP addresses to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListExternalAddresses&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListExternalAddresses&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_hcx_activation_keys_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, hcx_activation_key_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_hcx_activation_keys_create

    Creates a new HCX activation key in a given private cloud.

    :param parent: Required. The resource name of the private cloud to create the key for. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/privateClouds/my-cloud&#x60;
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
    :param hcx_activation_key_id: Required. The user-provided identifier of the &#x60;HcxActivationKey&#x60; to be created. This identifier must be unique among &#x60;HcxActivationKey&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type hcx_activation_key_id: str
    :param request_id: A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HcxActivationKey.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_hcx_activation_keys_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, options_requested_policy_version=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_hcx_activation_keys_get_iam_policy

    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

    :param resource: REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    :param options_requested_policy_version: Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_hcx_activation_keys_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_hcx_activation_keys_list

    Lists &#x60;HcxActivationKey&#x60; resources in a given private cloud.

    :param parent: Required. The resource name of the private cloud to be queried for HCX activation keys. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/privateClouds/my-cloud&#x60;
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
    :param page_size: The maximum number of HCX activation keys to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListHcxActivationKeys&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListHcxActivationKeys&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_hcx_activation_keys_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_hcx_activation_keys_set_iam_policy

    Sets the access control policy on the specified resource. Replaces any existing policy. Can return &#x60;NOT_FOUND&#x60;, &#x60;INVALID_ARGUMENT&#x60;, and &#x60;PERMISSION_DENIED&#x60; errors.

    :param resource: REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_hcx_activation_keys_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_hcx_activation_keys_test_iam_permissions

    Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a &#x60;NOT_FOUND&#x60; error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_list

    Lists &#x60;PrivateCloud&#x60; resources in a given project and location.

    :param parent: Required. The resource name of the private cloud to be queried for clusters. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of private clouds, you can exclude the ones named &#x60;example-pc&#x60; by specifying &#x60;name !&#x3D; \&quot;example-pc\&quot;&#x60;. You can also filter nested fields. For example, you could specify &#x60;networkConfig.managementCidr &#x3D; \&quot;192.168.0.0/24\&quot;&#x60; to include private clouds only if they have a matching address in their network configuration. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-pc\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;private-cloud-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;private-cloud-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of private clouds to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListPrivateClouds&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPrivateClouds&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_logging_servers_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, logging_server_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_logging_servers_create

    Create a new logging server for a given private cloud.

    :param parent: Required. The resource name of the private cloud to create a new Logging Server in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param logging_server_id: Required. The user-provided identifier of the &#x60;LoggingServer&#x60; to be created. This identifier must be unique among &#x60;LoggingServer&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type logging_server_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LoggingServer.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_logging_servers_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_logging_servers_list

    Lists logging servers configured for a given private cloud.

    :param parent: Required. The resource name of the private cloud to be queried for logging servers. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of logging servers, you can exclude the ones named &#x60;example-server&#x60; by specifying &#x60;name !&#x3D; \&quot;example-server\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-server\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-server-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-server-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of logging servers to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListLoggingServersRequest&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListLoggingServersRequest&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, management_dns_zone_binding_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_create

    Creates a new &#x60;ManagementDnsZoneBinding&#x60; resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud&#39;s ESXi hosts and management VM appliances like vCenter and NSX Manager.

    :param parent: Required. The resource name of the private cloud to create a new management DNS zone binding for. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param management_dns_zone_binding_id: Required. The user-provided identifier of the &#x60;ManagementDnsZoneBinding&#x60; resource to be created. This identifier must be unique among &#x60;ManagementDnsZoneBinding&#x60; resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type management_dns_zone_binding_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementDnsZoneBinding.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_list

    Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

    :param parent: Required. The resource name of the private cloud to be queried for management DNS zone bindings. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of Management DNS Zone Bindings, you can exclude the ones named &#x60;example-management-dns-zone-binding&#x60; by specifying &#x60;name !&#x3D; \&quot;example-management-dns-zone-binding\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-management-dns-zone-binding\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-management-dns-zone-binding-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-management-dns-zone-binding-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of management DNS zone bindings to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListManagementDnsZoneBindings&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListManagementDnsZoneBindings&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_repair(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_management_dns_zone_bindings_repair

    Retries to create a &#x60;ManagementDnsZoneBinding&#x60; resource that is in failed state.

    :param name: Required. The resource name of the management DNS zone binding to repair. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding&#x60;
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
    :type body: dict | bytes

    """
    body = RepairManagementDnsZoneBindingRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_reset_nsx_credentials(request: web.Request, private_cloud, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_reset_nsx_credentials

    Resets credentials of the NSX appliance.

    :param private_cloud: Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
    :type private_cloud: str
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
    body = ResetNsxCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_reset_vcenter_credentials(request: web.Request, private_cloud, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_reset_vcenter_credentials

    Resets credentials of the Vcenter appliance.

    :param private_cloud: Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
    :type private_cloud: str
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
    body = ResetVcenterCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_show_nsx_credentials(request: web.Request, private_cloud, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_show_nsx_credentials

    Gets details of credentials for NSX appliance.

    :param private_cloud: Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
    :type private_cloud: str
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


async def vmwareengine_projects_locations_private_clouds_show_vcenter_credentials(request: web.Request, private_cloud, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, username=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_show_vcenter_credentials

    Gets details of credentials for Vcenter appliance.

    :param private_cloud: Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
    :type private_cloud: str
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
    :param username: Optional. The username of the user to be queried for credentials. The default value of this field is CloudOwner@gve.local. The provided value must be one of the following: CloudOwner@gve.local, solution-user-01@gve.local, solution-user-02@gve.local, solution-user-03@gve.local, solution-user-04@gve.local, solution-user-05@gve.local, zertoadmin@gve.local.
    :type username: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_subnets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_subnets_list

    Lists subnets in a given private cloud.

    :param parent: Required. The resource name of the private cloud to be queried for subnets. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :param page_size: The maximum number of subnets to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSubnetsRequest&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubnetsRequest&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_clouds_undelete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_clouds_undelete

    Restores a private cloud that was previously scheduled for deletion by &#x60;DeletePrivateCloud&#x60;. A &#x60;PrivateCloud&#x60; resource scheduled for deletion has &#x60;PrivateCloud.state&#x60; set to &#x60;DELETED&#x60; and &#x60;PrivateCloud.expireTime&#x60; set to the time when deletion can no longer be reversed.

    :param name: Required. The resource name of the private cloud scheduled for deletion. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60;
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
    :type body: dict | bytes

    """
    body = UndeletePrivateCloudRequest.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_connections_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, private_connection_id=None, request_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_private_connections_create

    Creates a new private connection that can be used for accessing private Clouds.

    :param parent: Required. The resource name of the location to create the new private connection in. Private connection is a regional resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1&#x60;
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
    :param private_connection_id: Required. The user-provided identifier of the new private connection. This identifier must be unique among private connection resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type private_connection_id: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PrivateConnection.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_connections_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_connections_list

    Lists &#x60;PrivateConnection&#x60; resources in a given project and location.

    :param parent: Required. The resource name of the location to query for private connections. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of private connections, you can exclude the ones named &#x60;example-connection&#x60; by specifying &#x60;name !&#x3D; \&quot;example-connection\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-connection\&quot;) (createTime &gt; \&quot;2022-09-22T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-connection-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-connection-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of private connections to return in one page. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListPrivateConnections&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPrivateConnections&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_private_connections_peering_routes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_private_connections_peering_routes_list

    Lists the private connection routes exchanged over a peering connection.

    :param parent: Required. The resource name of the private connection to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-west1/privateConnections/my-connection&#x60;
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
    :param page_size: The maximum number of peering routes to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListPrivateConnectionPeeringRoutes&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPrivateConnectionPeeringRoutes&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_vmware_engine_networks_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, vmware_engine_network_id=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_vmware_engine_networks_create

    Creates a new VMware Engine network that can be used by a private cloud.

    :param parent: Required. The resource name of the location to create the new VMware Engine network in. A VMware Engine network of type &#x60;LEGACY&#x60; is a regional resource, and a VMware Engine network of type &#x60;STANDARD&#x60; is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global&#x60;
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
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param vmware_engine_network_id: Required. The user-provided identifier of the new VMware Engine network. This identifier must be unique among VMware Engine network resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: * For networks of type LEGACY, adheres to the format: &#x60;{region-id}-default&#x60;. Replace &#x60;{region-id}&#x60; with the region where you want to create the VMware Engine network. For example, \&quot;us-central1-default\&quot;. * Only contains 1-63 alphanumeric characters and hyphens * Begins with an alphabetical character * Ends with a non-hyphen character * Not formatted as a UUID * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)
    :type vmware_engine_network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VmwareEngineNetwork.from_dict(body)
    return web.Response(status=200)


async def vmwareengine_projects_locations_vmware_engine_networks_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, etag=None, request_id=None) -> web.Response:
    """vmwareengine_projects_locations_vmware_engine_networks_delete

    Deletes a &#x60;VmwareEngineNetwork&#x60; resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

    :param name: Required. The resource name of the VMware Engine network to be deleted. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/vmwareEngineNetworks/my-network&#x60;
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
    :param etag: Optional. Checksum used to ensure that the user-provided value is up to date before the server processes the request. The server compares provided checksum with the current checksum of the resource. If the user-provided value is out of date, this request returns an &#x60;ABORTED&#x60; error.
    :type etag: str
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_vmware_engine_networks_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """vmwareengine_projects_locations_vmware_engine_networks_get

    Retrieves a &#x60;VmwareEngineNetwork&#x60; resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, &#x60;CREATING&#x60;, &#x60;ACTIVE&#x60;, &#x60;DELETING&#x60;).

    :param name: Required. The resource name of the VMware Engine network to retrieve. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/vmwareEngineNetworks/my-network&#x60;
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


async def vmwareengine_projects_locations_vmware_engine_networks_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """vmwareengine_projects_locations_vmware_engine_networks_list

    Lists &#x60;VmwareEngineNetwork&#x60; resources in a given project and location.

    :param parent: Required. The resource name of the location to query for VMware Engine networks. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global&#x60;
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
    :param filter: A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&gt;&#x60;, or &#x60;&lt;&#x60;. For example, if you are filtering a list of network peerings, you can exclude the ones named &#x60;example-network&#x60; by specifying &#x60;name !&#x3D; \&quot;example-network\&quot;&#x60;. To filter on multiple expressions, provide each separate expression within parentheses. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-network\&quot;) (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) &#x60;&#x60;&#x60; By default, each expression is an &#x60;AND&#x60; expression. However, you can include &#x60;AND&#x60; and &#x60;OR&#x60; expressions explicitly. For example: &#x60;&#x60;&#x60; (name &#x3D; \&quot;example-network-1\&quot;) AND (createTime &gt; \&quot;2021-04-12T08:15:10.40Z\&quot;) OR (name &#x3D; \&quot;example-network-2\&quot;) &#x60;&#x60;&#x60;
    :type filter: str
    :param order_by: Sorts list results by a certain order. By default, returned results are ordered by &#x60;name&#x60; in ascending order. You can also sort results in descending order based on the &#x60;name&#x60; value using &#x60;orderBy&#x3D;\&quot;name desc\&quot;&#x60;. Currently, only ordering by &#x60;name&#x60; is supported.
    :type order_by: str
    :param page_size: The maximum number of results to return in one page. The maximum value is coerced to 1000. The default value of this field is 500.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListVmwareEngineNetworks&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListVmwareEngineNetworks&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def vmwareengine_projects_locations_vmware_engine_networks_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, update_mask=None, validate_only=None, body=None) -> web.Response:
    """vmwareengine_projects_locations_vmware_engine_networks_patch

    Modifies a VMware Engine network resource. Only the following fields can be updated: &#x60;description&#x60;. Only fields specified in &#x60;updateMask&#x60; are applied.

    :param name: Output only. The resource name of the VMware Engine network. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/vmwareEngineNetworks/my-network&#x60;
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
    :param request_id: Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn&#39;t result in creation of duplicate commitments for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param update_mask: Required. Field mask is used to specify the fields to be overwritten in the VMware Engine network resource by the update. The fields specified in the &#x60;update_mask&#x60; are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. Only the following fields can be updated: &#x60;description&#x60;.
    :type update_mask: str
    :param validate_only: Optional. True if you want the request to be validated and not executed; false otherwise.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = VmwareEngineNetwork.from_dict(body)
    return web.Response(status=200)
