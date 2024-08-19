from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_inbound_cross_cluster_search_connection_response import AcceptInboundCrossClusterSearchConnectionResponse
from openapi_server.models.add_tags_request import AddTagsRequest
from openapi_server.models.associate_package_response import AssociatePackageResponse
from openapi_server.models.authorize_vpc_endpoint_access_request import AuthorizeVpcEndpointAccessRequest
from openapi_server.models.authorize_vpc_endpoint_access_response import AuthorizeVpcEndpointAccessResponse
from openapi_server.models.cancel_elasticsearch_service_software_update_request import CancelElasticsearchServiceSoftwareUpdateRequest
from openapi_server.models.cancel_elasticsearch_service_software_update_response import CancelElasticsearchServiceSoftwareUpdateResponse
from openapi_server.models.create_elasticsearch_domain_request import CreateElasticsearchDomainRequest
from openapi_server.models.create_elasticsearch_domain_response import CreateElasticsearchDomainResponse
from openapi_server.models.create_outbound_cross_cluster_search_connection_request import CreateOutboundCrossClusterSearchConnectionRequest
from openapi_server.models.create_outbound_cross_cluster_search_connection_response import CreateOutboundCrossClusterSearchConnectionResponse
from openapi_server.models.create_package_request import CreatePackageRequest
from openapi_server.models.create_package_response import CreatePackageResponse
from openapi_server.models.create_vpc_endpoint_request import CreateVpcEndpointRequest
from openapi_server.models.create_vpc_endpoint_response import CreateVpcEndpointResponse
from openapi_server.models.delete_elasticsearch_domain_response import DeleteElasticsearchDomainResponse
from openapi_server.models.delete_inbound_cross_cluster_search_connection_response import DeleteInboundCrossClusterSearchConnectionResponse
from openapi_server.models.delete_outbound_cross_cluster_search_connection_response import DeleteOutboundCrossClusterSearchConnectionResponse
from openapi_server.models.delete_package_response import DeletePackageResponse
from openapi_server.models.delete_vpc_endpoint_response import DeleteVpcEndpointResponse
from openapi_server.models.describe_domain_auto_tunes_request import DescribeDomainAutoTunesRequest
from openapi_server.models.describe_domain_auto_tunes_response import DescribeDomainAutoTunesResponse
from openapi_server.models.describe_domain_change_progress_response import DescribeDomainChangeProgressResponse
from openapi_server.models.describe_elasticsearch_domain_config_response import DescribeElasticsearchDomainConfigResponse
from openapi_server.models.describe_elasticsearch_domain_response import DescribeElasticsearchDomainResponse
from openapi_server.models.describe_elasticsearch_domains_request import DescribeElasticsearchDomainsRequest
from openapi_server.models.describe_elasticsearch_domains_response import DescribeElasticsearchDomainsResponse
from openapi_server.models.describe_elasticsearch_instance_type_limits_response import DescribeElasticsearchInstanceTypeLimitsResponse
from openapi_server.models.describe_inbound_cross_cluster_search_connections_request import DescribeInboundCrossClusterSearchConnectionsRequest
from openapi_server.models.describe_inbound_cross_cluster_search_connections_response import DescribeInboundCrossClusterSearchConnectionsResponse
from openapi_server.models.describe_outbound_cross_cluster_search_connections_request import DescribeOutboundCrossClusterSearchConnectionsRequest
from openapi_server.models.describe_outbound_cross_cluster_search_connections_response import DescribeOutboundCrossClusterSearchConnectionsResponse
from openapi_server.models.describe_packages_request import DescribePackagesRequest
from openapi_server.models.describe_packages_response import DescribePackagesResponse
from openapi_server.models.describe_reserved_elasticsearch_instance_offerings_response import DescribeReservedElasticsearchInstanceOfferingsResponse
from openapi_server.models.describe_reserved_elasticsearch_instances_response import DescribeReservedElasticsearchInstancesResponse
from openapi_server.models.describe_vpc_endpoints_request import DescribeVpcEndpointsRequest
from openapi_server.models.describe_vpc_endpoints_response import DescribeVpcEndpointsResponse
from openapi_server.models.dissociate_package_response import DissociatePackageResponse
from openapi_server.models.get_compatible_elasticsearch_versions_response import GetCompatibleElasticsearchVersionsResponse
from openapi_server.models.get_package_version_history_response import GetPackageVersionHistoryResponse
from openapi_server.models.get_upgrade_history_response import GetUpgradeHistoryResponse
from openapi_server.models.get_upgrade_status_response import GetUpgradeStatusResponse
from openapi_server.models.list_domain_names_response import ListDomainNamesResponse
from openapi_server.models.list_domains_for_package_response import ListDomainsForPackageResponse
from openapi_server.models.list_elasticsearch_instance_types_response import ListElasticsearchInstanceTypesResponse
from openapi_server.models.list_elasticsearch_versions_response import ListElasticsearchVersionsResponse
from openapi_server.models.list_packages_for_domain_response import ListPackagesForDomainResponse
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_vpc_endpoint_access_response import ListVpcEndpointAccessResponse
from openapi_server.models.list_vpc_endpoints_for_domain_response import ListVpcEndpointsForDomainResponse
from openapi_server.models.list_vpc_endpoints_response import ListVpcEndpointsResponse
from openapi_server.models.purchase_reserved_elasticsearch_instance_offering_request import PurchaseReservedElasticsearchInstanceOfferingRequest
from openapi_server.models.purchase_reserved_elasticsearch_instance_offering_response import PurchaseReservedElasticsearchInstanceOfferingResponse
from openapi_server.models.reject_inbound_cross_cluster_search_connection_response import RejectInboundCrossClusterSearchConnectionResponse
from openapi_server.models.remove_tags_request import RemoveTagsRequest
from openapi_server.models.revoke_vpc_endpoint_access_request import RevokeVpcEndpointAccessRequest
from openapi_server.models.start_elasticsearch_service_software_update_response import StartElasticsearchServiceSoftwareUpdateResponse
from openapi_server.models.update_elasticsearch_domain_config_request import UpdateElasticsearchDomainConfigRequest
from openapi_server.models.update_elasticsearch_domain_config_response import UpdateElasticsearchDomainConfigResponse
from openapi_server.models.update_package_request import UpdatePackageRequest
from openapi_server.models.update_package_response import UpdatePackageResponse
from openapi_server.models.update_vpc_endpoint_request import UpdateVpcEndpointRequest
from openapi_server.models.update_vpc_endpoint_response import UpdateVpcEndpointResponse
from openapi_server.models.upgrade_elasticsearch_domain_request import UpgradeElasticsearchDomainRequest
from openapi_server.models.upgrade_elasticsearch_domain_response import UpgradeElasticsearchDomainResponse
from openapi_server import util


async def accept_inbound_cross_cluster_search_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_inbound_cross_cluster_search_connection

    Allows the destination domain owner to accept an inbound cross-cluster search connection request.

    :param connection_id: The id of the inbound connection that you want to accept.
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

    Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-awsresorcetagging\&quot; target&#x3D;\&quot;_blank\&quot;&gt; Tagging Amazon Elasticsearch Service Domains for more information.&lt;/a&gt;

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

    Associates a package with an Amazon ES domain.

    :param package_id: Internal ID of the package that you want to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value.
    :type package_id: str
    :param domain_name: Name of the domain that you want to associate the package with.
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


async def cancel_elasticsearch_service_software_update(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_elasticsearch_service_software_update

    Cancels a scheduled service software update for an Amazon ES domain. You can only perform this operation before the &lt;code&gt;AutomatedUpdateDate&lt;/code&gt; and when the &lt;code&gt;UpdateStatus&lt;/code&gt; is in the &lt;code&gt;PENDING_UPDATE&lt;/code&gt; state.

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
    body = CancelElasticsearchServiceSoftwareUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def create_elasticsearch_domain(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_elasticsearch_domain

    Creates a new Elasticsearch domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Creating Elasticsearch Domains&lt;/a&gt; in the &lt;i&gt;Amazon Elasticsearch Service Developer Guide&lt;/i&gt;.

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
    body = CreateElasticsearchDomainRequest.from_dict(body)
    return web.Response(status=200)


async def create_outbound_cross_cluster_search_connection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_outbound_cross_cluster_search_connection

    Creates a new cross-cluster search connection from a source domain to a destination domain.

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
    body = CreateOutboundCrossClusterSearchConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_package

    Create a package for use with Amazon ES domains.

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


async def delete_elasticsearch_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_elasticsearch_domain

    Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.

    :param domain_name: The name of the Elasticsearch domain that you want to permanently delete.
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


async def delete_elasticsearch_service_role(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_elasticsearch_service_role

    Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-enabling-slr\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Deleting Elasticsearch Service Role&lt;/a&gt; in &lt;i&gt;VPC Endpoints for Amazon Elasticsearch Service Domains&lt;/i&gt;.

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


async def delete_inbound_cross_cluster_search_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_inbound_cross_cluster_search_connection

    Allows the destination domain owner to delete an existing inbound cross-cluster search connection.

    :param connection_id: The id of the inbound connection that you want to permanently delete.
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


async def delete_outbound_cross_cluster_search_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_outbound_cross_cluster_search_connection

    Allows the source domain owner to delete an existing outbound cross-cluster search connection.

    :param connection_id: The id of the outbound connection that you want to permanently delete.
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

    Delete the package.

    :param package_id: Internal ID of the package that you want to delete. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value.
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

    :param vpc_endpoint_id: The unique identifier of the endpoint to be deleted.
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


async def describe_domain_auto_tunes(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_domain_auto_tunes

    Provides scheduled Auto-Tune action details for the Elasticsearch domain, such as Auto-Tune action type, description, severity, and scheduled date.

    :param domain_name: Specifies the domain name for which you want Auto-Tune action details.
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

    Returns information about the current blue/green deployment happening on a domain, including a change ID, status, and progress stages.

    :param domain_name: The domain you want to get the progress information about.
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
    :param changeid: The specific change ID for which you want to get progress information. This is an optional parameter. If omitted, the service returns information about the most recent configuration change. 
    :type changeid: str

    """
    return web.Response(status=200)


async def describe_elasticsearch_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_elasticsearch_domain

    Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.

    :param domain_name: The name of the Elasticsearch domain for which you want information.
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


async def describe_elasticsearch_domain_config(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_elasticsearch_domain_config

    Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.

    :param domain_name: The Elasticsearch domain that you want to get information about.
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


async def describe_elasticsearch_domains(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_elasticsearch_domains

    Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.

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
    body = DescribeElasticsearchDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_elasticsearch_instance_type_limits(request: web.Request, instance_type, elasticsearch_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None) -> web.Response:
    """describe_elasticsearch_instance_type_limits

     Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the &lt;code&gt; &lt;a&gt;DomainName&lt;/a&gt; &lt;/code&gt; to know what Limits are supported for modifying. 

    :param instance_type:  The instance type for an Elasticsearch cluster for which Elasticsearch &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; are needed. 
    :type instance_type: str
    :param elasticsearch_version:  Version of Elasticsearch for which &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; are needed. 
    :type elasticsearch_version: str
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
    :param domain_name:  DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch &lt;code&gt; &lt;a&gt;Limits&lt;/a&gt; &lt;/code&gt; for existing domain. 
    :type domain_name: str

    """
    return web.Response(status=200)


async def describe_inbound_cross_cluster_search_connections(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_inbound_cross_cluster_search_connections

    Lists all the inbound cross-cluster search connections for a destination domain.

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
    body = DescribeInboundCrossClusterSearchConnectionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_outbound_cross_cluster_search_connections(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_outbound_cross_cluster_search_connections

    Lists all the outbound cross-cluster search connections for a source domain.

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
    body = DescribeOutboundCrossClusterSearchConnectionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_packages(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_packages

    Describes all packages available to Amazon ES. Includes options for filtering, limiting the number of results, and pagination.

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


async def describe_reserved_elasticsearch_instance_offerings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, offering_id=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """describe_reserved_elasticsearch_instance_offerings

    Lists available reserved Elasticsearch instance offerings.

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
    :param offering_id: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
    :type offering_id: str
    :param max_results: Set this value to limit the number of results returned. If not specified, defaults to 100.
    :type max_results: int
    :param next_token: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def describe_reserved_elasticsearch_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reservation_id=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """describe_reserved_elasticsearch_instances

    Returns information about reserved Elasticsearch instances for this account.

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
    :param reservation_id: The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.
    :type reservation_id: str
    :param max_results: Set this value to limit the number of results returned. If not specified, defaults to 100.
    :type max_results: int
    :param next_token: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.
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

    Dissociates a package from the Amazon ES domain.

    :param package_id: Internal ID of the package that you want to associate with a domain. Use &lt;code&gt;DescribePackages&lt;/code&gt; to find this value.
    :type package_id: str
    :param domain_name: Name of the domain that you want to associate the package with.
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


async def get_compatible_elasticsearch_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None) -> web.Response:
    """get_compatible_elasticsearch_versions

     Returns a list of upgrade compatible Elastisearch versions. You can optionally pass a &lt;code&gt; &lt;a&gt;DomainName&lt;/a&gt; &lt;/code&gt; to get all upgrade compatible Elasticsearch versions for that specific domain. 

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
    :param domain_name: 
    :type domain_name: str

    """
    return web.Response(status=200)


async def get_package_version_history(request: web.Request, package_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """get_package_version_history

    Returns a list of versions of the package, along with their creation time and commit message.

    :param package_id: Returns an audit history of versions of the package.
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
    :param max_results: Limits results to a maximum number of versions.
    :type max_results: int
    :param next_token: Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def get_upgrade_history(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """get_upgrade_history

    Retrieves the complete history of the last 10 upgrades that were performed on the domain.

    :param domain_name: 
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
    :param max_results: 
    :type max_results: int
    :param next_token: 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def get_upgrade_status(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_upgrade_status

    Retrieves the latest status of the last upgrade or upgrade eligibility check that was performed on the domain.

    :param domain_name: 
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

    Returns the name of all Elasticsearch domains owned by the current user&#39;s account. 

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
    :param engine_type:  Optional parameter to filter the output by domain engine type. Acceptable values are &#39;Elasticsearch&#39; and &#39;OpenSearch&#39;. 
    :type engine_type: str

    """
    return web.Response(status=200)


async def list_domains_for_package(request: web.Request, package_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_domains_for_package

    Lists all Amazon ES domains associated with the package.

    :param package_id: The package for which to list domains.
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
    :param max_results: Limits results to a maximum number of domains.
    :type max_results: int
    :param next_token: Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_elasticsearch_instance_types(request: web.Request, elasticsearch_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_name=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_elasticsearch_instance_types

    List all Elasticsearch instance types that are supported for given ElasticsearchVersion

    :param elasticsearch_version: Version of Elasticsearch for which list of supported elasticsearch instance types are needed. 
    :type elasticsearch_version: str
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
    :param domain_name: DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. 
    :type domain_name: str
    :param max_results:  Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. 
    :type max_results: int
    :param next_token: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_elasticsearch_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_elasticsearch_versions

    List all supported Elasticsearch versions

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
    :param max_results:  Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. 
    :type max_results: int
    :param next_token: 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_packages_for_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_packages_for_domain

    Lists all packages associated with the Amazon ES domain.

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
    :param max_results: Limits results to a maximum number of packages.
    :type max_results: int
    :param next_token: Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags

    Returns all tags for the given Elasticsearch domain.

    :param arn:  Specify the &lt;code&gt;ARN&lt;/code&gt; for the Elasticsearch domain to which the tags are attached that you want to view.
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


async def list_vpc_endpoint_access(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoint_access

    Retrieves information about each principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

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
    :param next_token: Provides an identifier to allow retrieval of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_vpc_endpoints(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoints

    Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current account and Region.

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
    :param next_token: Identifier to allow retrieval of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_vpc_endpoints_for_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_vpc_endpoints_for_domain

    Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.

    :param domain_name: Name of the ElasticSearch domain whose VPC endpoints are to be listed.
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
    :param next_token: Provides an identifier to allow retrieval of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def purchase_reserved_elasticsearch_instance_offering(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """purchase_reserved_elasticsearch_instance_offering

    Allows you to purchase reserved Elasticsearch instances.

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
    body = PurchaseReservedElasticsearchInstanceOfferingRequest.from_dict(body)
    return web.Response(status=200)


async def reject_inbound_cross_cluster_search_connection(request: web.Request, connection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_inbound_cross_cluster_search_connection

    Allows the destination domain owner to reject an inbound cross-cluster search connection request.

    :param connection_id: The id of the inbound connection that you want to reject.
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

    Removes the specified set of tags from the specified Elasticsearch domain.

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


async def start_elasticsearch_service_software_update(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_elasticsearch_service_software_update

    Schedules a service software update for an Amazon ES domain.

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
    body = CancelElasticsearchServiceSoftwareUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def update_elasticsearch_domain_config(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_elasticsearch_domain_config

    Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances. 

    :param domain_name: The name of the Elasticsearch domain that you are updating. 
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
    body = UpdateElasticsearchDomainConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_package(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_package

    Updates a package for use with Amazon ES domains.

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


async def upgrade_elasticsearch_domain(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_elasticsearch_domain

    Allows you to either upgrade your domain or perform an Upgrade eligibility check to a compatible Elasticsearch version.

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
    body = UpgradeElasticsearchDomainRequest.from_dict(body)
    return web.Response(status=200)
