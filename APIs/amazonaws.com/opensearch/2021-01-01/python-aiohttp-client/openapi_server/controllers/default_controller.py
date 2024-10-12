from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_inbound_connection_response import AcceptInboundConnectionResponse
from openapi_server.models.add_tags_request import AddTagsRequest
from openapi_server.models.associate_package_response import AssociatePackageResponse
from openapi_server.models.authorize_vpc_endpoint_access_request import AuthorizeVpcEndpointAccessRequest
from openapi_server.models.authorize_vpc_endpoint_access_response import AuthorizeVpcEndpointAccessResponse
from openapi_server.models.cancel_service_software_update_request import CancelServiceSoftwareUpdateRequest
from openapi_server.models.cancel_service_software_update_response import CancelServiceSoftwareUpdateResponse
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_response import CreateDomainResponse
from openapi_server.models.create_outbound_connection_request import CreateOutboundConnectionRequest
from openapi_server.models.create_outbound_connection_response import CreateOutboundConnectionResponse
from openapi_server.models.create_package_request import CreatePackageRequest
from openapi_server.models.create_package_response import CreatePackageResponse
from openapi_server.models.create_vpc_endpoint_request import CreateVpcEndpointRequest
from openapi_server.models.create_vpc_endpoint_response import CreateVpcEndpointResponse
from openapi_server.models.delete_domain_response import DeleteDomainResponse
from openapi_server.models.delete_inbound_connection_response import DeleteInboundConnectionResponse
from openapi_server.models.delete_outbound_connection_response import DeleteOutboundConnectionResponse
from openapi_server.models.delete_package_response import DeletePackageResponse
from openapi_server.models.delete_vpc_endpoint_response import DeleteVpcEndpointResponse
from openapi_server.models.describe_domain_auto_tunes_request import DescribeDomainAutoTunesRequest
from openapi_server.models.describe_domain_auto_tunes_response import DescribeDomainAutoTunesResponse
from openapi_server.models.describe_domain_change_progress_response import DescribeDomainChangeProgressResponse
from openapi_server.models.describe_domain_config_response import DescribeDomainConfigResponse
from openapi_server.models.describe_domain_health_response import DescribeDomainHealthResponse
from openapi_server.models.describe_domain_nodes_response import DescribeDomainNodesResponse
from openapi_server.models.describe_domain_response import DescribeDomainResponse
from openapi_server.models.describe_domains_request import DescribeDomainsRequest
from openapi_server.models.describe_domains_response import DescribeDomainsResponse
from openapi_server.models.describe_dry_run_progress_response import DescribeDryRunProgressResponse
from openapi_server.models.describe_inbound_connections_request import DescribeInboundConnectionsRequest
from openapi_server.models.describe_inbound_connections_response import DescribeInboundConnectionsResponse
from openapi_server.models.describe_instance_type_limits_response import DescribeInstanceTypeLimitsResponse
from openapi_server.models.describe_outbound_connections_request import DescribeOutboundConnectionsRequest
from openapi_server.models.describe_outbound_connections_response import DescribeOutboundConnectionsResponse
from openapi_server.models.describe_packages_request import DescribePackagesRequest
from openapi_server.models.describe_packages_response import DescribePackagesResponse
from openapi_server.models.describe_reserved_instance_offerings_response import DescribeReservedInstanceOfferingsResponse
from openapi_server.models.describe_reserved_instances_response import DescribeReservedInstancesResponse
from openapi_server.models.describe_vpc_endpoints_request import DescribeVpcEndpointsRequest
from openapi_server.models.describe_vpc_endpoints_response import DescribeVpcEndpointsResponse
from openapi_server.models.dissociate_package_response import DissociatePackageResponse
from openapi_server.models.get_compatible_versions_response import GetCompatibleVersionsResponse
from openapi_server.models.get_package_version_history_response import GetPackageVersionHistoryResponse
from openapi_server.models.get_upgrade_history_response import GetUpgradeHistoryResponse
from openapi_server.models.get_upgrade_status_response import GetUpgradeStatusResponse
from openapi_server.models.list_domain_names_response import ListDomainNamesResponse
from openapi_server.models.list_domains_for_package_response import ListDomainsForPackageResponse
from openapi_server.models.list_instance_type_details_response import ListInstanceTypeDetailsResponse
from openapi_server.models.list_packages_for_domain_response import ListPackagesForDomainResponse
from openapi_server.models.list_scheduled_actions_response import ListScheduledActionsResponse
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_versions_response import ListVersionsResponse
from openapi_server.models.list_vpc_endpoint_access_response import ListVpcEndpointAccessResponse
from openapi_server.models.list_vpc_endpoints_for_domain_response import ListVpcEndpointsForDomainResponse
from openapi_server.models.list_vpc_endpoints_response import ListVpcEndpointsResponse
from openapi_server.models.purchase_reserved_instance_offering_request import PurchaseReservedInstanceOfferingRequest
from openapi_server.models.purchase_reserved_instance_offering_response import PurchaseReservedInstanceOfferingResponse
from openapi_server.models.reject_inbound_connection_response import RejectInboundConnectionResponse
from openapi_server.models.remove_tags_request import RemoveTagsRequest
from openapi_server.models.revoke_vpc_endpoint_access_request import RevokeVpcEndpointAccessRequest
from openapi_server.models.start_service_software_update_request import StartServiceSoftwareUpdateRequest
from openapi_server.models.start_service_software_update_response import StartServiceSoftwareUpdateResponse
from openapi_server.models.update_domain_config_request import UpdateDomainConfigRequest
from openapi_server.models.update_domain_config_response import UpdateDomainConfigResponse
from openapi_server.models.update_package_request import UpdatePackageRequest
from openapi_server.models.update_package_response import UpdatePackageResponse
from openapi_server.models.update_scheduled_action_request import UpdateScheduledActionRequest
from openapi_server.models.update_scheduled_action_response import UpdateScheduledActionResponse
from openapi_server.models.update_vpc_endpoint_request import UpdateVpcEndpointRequest
from openapi_server.models.update_vpc_endpoint_response import UpdateVpcEndpointResponse
from openapi_server.models.upgrade_domain_request import UpgradeDomainRequest
from openapi_server.models.upgrade_domain_response import UpgradeDomainResponse
from openapi_server import util


async def accept_inbound_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_inbound_connection

    Allows the destination Amazon OpenSearch Service domain owner to accept an inbound cross-cluster search connection request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param connection_id: The ID of the inbound connection to accept.
    :type connection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def add_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags

    Attaches tags to an existing Amazon OpenSearch Service domain. Tags are a set of case-sensitive key-value pairs. A domain can have up to 10 tags. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\&quot;&gt;Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AddTagsRequest.from_dict(body)
    return web.Response(status=200)


async def associate_package(request: web.Request, package_id, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_package

    Associates a package with an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param package_id: Internal ID of the package to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value. 
    :type package_id: str
    :param domain_name: Name of the domain to associate the package with.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def authorize_vpc_endpoint_access(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """authorize_vpc_endpoint_access

    Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

    :param domain_name: The name of the OpenSearch Service domain to provide access to.
    :type domain_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AuthorizeVpcEndpointAccessRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_service_software_update(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_service_software_update

    Cancels a scheduled service software update for an Amazon OpenSearch Service domain. You can only perform this operation before the &lt;code&gt;AutomatedUpdateDate&lt;/code&gt; and when the domain&#39;s &lt;code&gt;UpdateStatus&lt;/code&gt; is &lt;code&gt;PENDING_UPDATE&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;Service software updates in Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelServiceSoftwareUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def create_domain(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_domain

    Creates an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html\&quot;&gt;Creating and managing Amazon OpenSearch Service domains&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def create_outbound_connection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_outbound_connection

    Creates a new cross-cluster search connection from a source Amazon OpenSearch Service domain to a destination domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateOutboundConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_package

    Creates a package for use with Amazon OpenSearch Service domains. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePackageRequest.from_dict(body)
    return web.Response(status=200)


async def create_vpc_endpoint(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_endpoint

    Creates an Amazon OpenSearch Service-managed VPC endpoint.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateVpcEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def delete_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_domain

    Deletes an Amazon OpenSearch Service domain and all of its data. You can&#39;t recover a domain after you delete it.

    :param domain_name: The name of the domain you want to permanently delete.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_inbound_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_inbound_connection

    Allows the destination Amazon OpenSearch Service domain owner to delete an existing inbound cross-cluster search connection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param connection_id: The ID of the inbound connection to permanently delete.
    :type connection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_outbound_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_outbound_connection

    Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param connection_id: The ID of the outbound connection you want to permanently delete.
    :type connection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_package(request: web.Request, package_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_package

    Deletes an Amazon OpenSearch Service package. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param package_id: The internal ID of the package you want to delete. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value.
    :type package_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_vpc_endpoint(request: web.Request, vpc_endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_endpoint

    Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

    :param vpc_endpoint_id: The unique identifier of the endpoint.
    :type vpc_endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domain

    Describes the domain configuration for the specified Amazon OpenSearch Service domain, including the domain ID, domain service endpoint, and domain ARN.

    :param domain_name: The name of the domain that you want information about.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_domain_auto_tunes(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_domain_auto_tunes

    Returns the list of optimizations that Auto-Tune has made to an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html\&quot;&gt;Auto-Tune for Amazon OpenSearch Service&lt;/a&gt;.

    :param domain_name: Name of the domain that you want Auto-Tune details about.
    :type domain_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeDomainAutoTunesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_domain_change_progress(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, changeid=None) -> web.Response:
    """describe_domain_change_progress

    Returns information about the current blue/green deployment happening on an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html\&quot;&gt;Making configuration changes in Amazon OpenSearch Service&lt;/a&gt;.

    :param domain_name: The name of the domain to get progress information for.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param changeid: The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.
    :type changeid: str

    """
    return web.Response(status=200)


async def describe_domain_config(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domain_config

    Returns the configuration of an Amazon OpenSearch Service domain.

    :param domain_name: Name of the OpenSearch Service domain configuration that you want to describe.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_domain_health(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domain_health

    Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.

    :param domain_name: The name of the domain.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_domain_nodes(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domain_nodes

    Returns information about domain and nodes, including data nodes, master nodes, ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and node states.

    :param domain_name: The name of the domain.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_domains(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domains

    Returns domain configuration information about the specified Amazon OpenSearch Service domains.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_dry_run_progress(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, dry_run_id=None, load_dry_run_config=None) -> web.Response:
    """describe_dry_run_progress

    Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun\&quot;&gt;Determining whether a change will cause a blue/green deployment&lt;/a&gt;.

    :param domain_name: The name of the domain.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param dry_run_id: The unique identifier of the dry run.
    :type dry_run_id: str
    :param load_dry_run_config: Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you&#39;re planning to make on the domain.
    :type load_dry_run_config: bool

    """
    return web.Response(status=200)


async def describe_inbound_connections(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_inbound_connections

    Lists all the inbound cross-cluster search connections for a destination (remote) Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeInboundConnectionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_type_limits(request: web.Request, instance_type, engine_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None) -> web.Response:
    """describe_instance_type_limits

    Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.

    :param instance_type: The OpenSearch Service instance type for which you need limit information.
    :type instance_type: str
    :param engine_version: Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.
    :type engine_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param domain_name: The name of the domain. Only specify if you need the limits for an existing domain.
    :type domain_name: str

    """
    return web.Response(status=200)


async def describe_outbound_connections(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_outbound_connections

    Lists all the outbound cross-cluster connections for a local (source) Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\&quot;&gt;Cross-cluster search for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeOutboundConnectionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_packages(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_packages

    Describes all packages available to OpenSearch Service. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribePackagesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_reserved_instance_offerings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, offering_id=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """describe_reserved_instance_offerings

    Describes the available Amazon OpenSearch Service Reserved Instance offerings for a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\&quot;&gt;Reserved Instances in Amazon OpenSearch Service&lt;/a&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param offering_id: The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier.
    :type offering_id: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;DescribeReservedInstanceOfferings&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;DescribeReservedInstanceOfferings&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def describe_reserved_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reservation_id=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """describe_reserved_instances

    Describes the Amazon OpenSearch Service instances that you have reserved in a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\&quot;&gt;Reserved Instances in Amazon OpenSearch Service&lt;/a&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reservation_id: The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.
    :type reservation_id: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;DescribeReservedInstances&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;DescribeReservedInstances&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def describe_vpc_endpoints(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vpc_endpoints

    Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeVpcEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def dissociate_package(request: web.Request, package_id, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """dissociate_package

    Removes a package from the specified Amazon OpenSearch Service domain. The package can&#39;t be in use with any OpenSearch index for the dissociation to succeed. The package is still available in OpenSearch Service for association later. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param package_id: Internal ID of the package to dissociate from the domain. Use &lt;code&gt;ListPackagesForDomain&lt;/code&gt; to find this value.
    :type package_id: str
    :param domain_name: Name of the domain to dissociate the package from.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_compatible_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None) -> web.Response:
    """get_compatible_versions

    Returns a map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param domain_name: The name of an existing domain. Provide this parameter to limit the results to a single domain.
    :type domain_name: str

    """
    return web.Response(status=200)


async def get_package_version_history(request: web.Request, package_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """get_package_version_history

    Returns a list of Amazon OpenSearch Service package versions, along with their creation time, commit message, and plugin properties (if the package is a zip plugin package). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param package_id: The unique identifier of the package.
    :type package_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;GetPackageVersionHistory&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;GetPackageVersionHistory&lt;/code&gt; operations, which returns results in the next page. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def get_upgrade_history(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """get_upgrade_history

    Retrieves the complete history of the last 10 upgrades performed on an Amazon OpenSearch Service domain.

    :param domain_name: The name of an existing domain.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;GetUpgradeHistory&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;GetUpgradeHistory&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def get_upgrade_status(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_upgrade_status

    Returns the most recent status of the last upgrade or upgrade eligibility check performed on an Amazon OpenSearch Service domain.

    :param domain_name: The domain of the domain to get upgrade status information for.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_domain_names(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine_type=None) -> web.Response:
    """list_domain_names

    Returns the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param engine_type: Filters the output by domain engine type.
    :type engine_type: str

    """
    return web.Response(status=200)


async def list_domains_for_package(request: web.Request, package_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_domains_for_package

    Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param package_id: The unique identifier of the package for which to list associated domains.
    :type package_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;ListDomainsForPackage&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListDomainsForPackage&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_instance_type_details(request: web.Request, engine_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None, max_results=None, next_token=None, retrieve_azs=None, instance_type=None, max_results2=None, next_token2=None) -> web.Response:
    """list_instance_type_details

    Lists all instance types and available features for a given OpenSearch or Elasticsearch version.

    :param engine_version: The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.
    :type engine_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param domain_name: The name of the domain.
    :type domain_name: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;ListInstanceTypeDetails&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListInstanceTypeDetails&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param retrieve_azs: An optional parameter that specifies the Availability Zones for the domain.
    :type retrieve_azs: bool
    :param instance_type: An optional parameter that lists information for a given instance type.
    :type instance_type: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_packages_for_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_packages_for_domain

    Lists all packages associated with an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param domain_name: The name of the domain for which you want to list associated packages.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;ListPackagesForDomain&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListPackagesForDomain&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_scheduled_actions(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_scheduled_actions

    Retrieves a list of configuration changes that are scheduled for a domain. These changes can be &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;service software updates&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\&quot;&gt;blue/green Auto-Tune enhancements&lt;/a&gt;.

    :param domain_name: The name of the domain.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;ListScheduledActions&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListScheduledActions&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags

    Returns all resource tags for an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\&quot;&gt;Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

    :param arn: Amazon Resource Name (ARN) for the domain to view tags for.
    :type arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_versions

    Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: An optional parameter that specifies the maximum number of results to return. You can use &lt;code&gt;nextToken&lt;/code&gt; to get the next page of results.
    :type max_results: int
    :param next_token: If your initial &lt;code&gt;ListVersions&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVersions&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_vpc_endpoint_access(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoint_access

    Retrieves information about each Amazon Web Services principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

    :param domain_name: The name of the OpenSearch Service domain to retrieve access information for.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: If your initial &lt;code&gt;ListVpcEndpointAccess&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVpcEndpointAccess&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_vpc_endpoints(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoints

    Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current Amazon Web Services account and Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: If your initial &lt;code&gt;ListVpcEndpoints&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListVpcEndpoints&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_vpc_endpoints_for_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoints_for_domain

    Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.

    :param domain_name: The name of the domain to list associated VPC endpoints for.
    :type domain_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: If your initial &lt;code&gt;ListEndpointsForDomain&lt;/code&gt; operation returns a &lt;code&gt;nextToken&lt;/code&gt;, you can include the returned &lt;code&gt;nextToken&lt;/code&gt; in subsequent &lt;code&gt;ListEndpointsForDomain&lt;/code&gt; operations, which returns results in the next page.
    :type next_token: str

    """
    return web.Response(status=200)


async def purchase_reserved_instance_offering(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """purchase_reserved_instance_offering

    Allows you to purchase Amazon OpenSearch Service Reserved Instances.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PurchaseReservedInstanceOfferingRequest.from_dict(body)
    return web.Response(status=200)


async def reject_inbound_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_inbound_connection

    Allows the remote Amazon OpenSearch Service domain owner to reject an inbound cross-cluster connection request.

    :param connection_id: The unique identifier of the inbound connection to reject.
    :type connection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def remove_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags

    Removes the specified set of tags from an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html#managedomains-awsresorcetagging\&quot;&gt; Tagging Amazon OpenSearch Service domains&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RemoveTagsRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_vpc_endpoint_access(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_vpc_endpoint_access

    Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.

    :param domain_name: The name of the OpenSearch Service domain.
    :type domain_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RevokeVpcEndpointAccessRequest.from_dict(body)
    return web.Response(status=200)


async def start_service_software_update(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_service_software_update

    Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;Service software updates in Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartServiceSoftwareUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain_config(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain_config

    Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.sl

    :param domain_name: The name of the domain that you&#39;re updating.
    :type domain_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDomainConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_package

    Updates a package for use with Amazon OpenSearch Service domains. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\&quot;&gt;Custom packages for Amazon OpenSearch Service&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePackageRequest.from_dict(body)
    return web.Response(status=200)


async def update_scheduled_action(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_scheduled_action

    Reschedules a planned domain configuration change for a later time. This change can be a scheduled &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\&quot;&gt;service software update&lt;/a&gt; or a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\&quot;&gt;blue/green Auto-Tune enhancement&lt;/a&gt;.

    :param domain_name: The name of the domain to reschedule an action for.
    :type domain_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateScheduledActionRequest.from_dict(body)
    return web.Response(status=200)


async def update_vpc_endpoint(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vpc_endpoint

    Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateVpcEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_domain(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_domain

    Allows you to either upgrade your Amazon OpenSearch Service domain or perform an upgrade eligibility check to a compatible version of OpenSearch or Elasticsearch.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpgradeDomainRequest.from_dict(body)
    return web.Response(status=200)
