from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_http_namespace_request import CreateHttpNamespaceRequest
from openapi_server.models.create_http_namespace_response import CreateHttpNamespaceResponse
from openapi_server.models.create_private_dns_namespace_request import CreatePrivateDnsNamespaceRequest
from openapi_server.models.create_private_dns_namespace_response import CreatePrivateDnsNamespaceResponse
from openapi_server.models.create_public_dns_namespace_request import CreatePublicDnsNamespaceRequest
from openapi_server.models.create_public_dns_namespace_response import CreatePublicDnsNamespaceResponse
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.create_service_response import CreateServiceResponse
from openapi_server.models.delete_namespace_request import DeleteNamespaceRequest
from openapi_server.models.delete_namespace_response import DeleteNamespaceResponse
from openapi_server.models.delete_service_request import DeleteServiceRequest
from openapi_server.models.deregister_instance_request import DeregisterInstanceRequest
from openapi_server.models.deregister_instance_response import DeregisterInstanceResponse
from openapi_server.models.discover_instances_request import DiscoverInstancesRequest
from openapi_server.models.discover_instances_response import DiscoverInstancesResponse
from openapi_server.models.get_instance_request import GetInstanceRequest
from openapi_server.models.get_instance_response import GetInstanceResponse
from openapi_server.models.get_instances_health_status_request import GetInstancesHealthStatusRequest
from openapi_server.models.get_instances_health_status_response import GetInstancesHealthStatusResponse
from openapi_server.models.get_namespace_request import GetNamespaceRequest
from openapi_server.models.get_namespace_response import GetNamespaceResponse
from openapi_server.models.get_operation_request import GetOperationRequest
from openapi_server.models.get_operation_response import GetOperationResponse
from openapi_server.models.get_service_request import GetServiceRequest
from openapi_server.models.get_service_response import GetServiceResponse
from openapi_server.models.list_instances_request import ListInstancesRequest
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_namespaces_request import ListNamespacesRequest
from openapi_server.models.list_namespaces_response import ListNamespacesResponse
from openapi_server.models.list_operations_request import ListOperationsRequest
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_services_request import ListServicesRequest
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.register_instance_request import RegisterInstanceRequest
from openapi_server.models.register_instance_response import RegisterInstanceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_http_namespace_request import UpdateHttpNamespaceRequest
from openapi_server.models.update_http_namespace_response import UpdateHttpNamespaceResponse
from openapi_server.models.update_instance_custom_health_status_request import UpdateInstanceCustomHealthStatusRequest
from openapi_server.models.update_private_dns_namespace_request import UpdatePrivateDnsNamespaceRequest
from openapi_server.models.update_private_dns_namespace_response import UpdatePrivateDnsNamespaceResponse
from openapi_server.models.update_public_dns_namespace_request import UpdatePublicDnsNamespaceRequest
from openapi_server.models.update_public_dns_namespace_response import UpdatePublicDnsNamespaceResponse
from openapi_server.models.update_service_request import UpdateServiceRequest
from openapi_server.models.update_service_response import UpdateServiceResponse
from openapi_server import util


async def create_http_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_http_namespace

    &lt;p&gt;Creates an HTTP namespace. Service instances registered using an HTTP namespace can be discovered using a &lt;code&gt;DiscoverInstances&lt;/code&gt; request but can&#39;t be discovered using DNS.&lt;/p&gt; &lt;p&gt;For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateHttpNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_private_dns_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_private_dns_namespace

    Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace &lt;code&gt;example.com&lt;/code&gt; and name your service &lt;code&gt;backend&lt;/code&gt;, the resulting DNS name for the service is &lt;code&gt;backend.example.com&lt;/code&gt;. Service instances that are registered using a private DNS namespace can be discovered using either a &lt;code&gt;DiscoverInstances&lt;/code&gt; request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreatePrivateDnsNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_public_dns_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_public_dns_namespace

    &lt;p&gt;Creates a public namespace based on DNS, which is visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace &lt;code&gt;example.com&lt;/code&gt; and name your service &lt;code&gt;backend&lt;/code&gt;, the resulting DNS name for the service is &lt;code&gt;backend.example.com&lt;/code&gt;. You can discover instances that were registered with a public DNS namespace by using either a &lt;code&gt;DiscoverInstances&lt;/code&gt; request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The &lt;code&gt;CreatePublicDnsNamespace&lt;/code&gt; API operation is not supported in the Amazon Web Services GovCloud (US) Regions.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreatePublicDnsNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service

    &lt;p&gt;Creates a service. This action defines the configuration for the following entities:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For public and private DNS namespaces, one of the following combinations of DNS records in Amazon Route 53:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;A&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AAAA&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;A&lt;/code&gt; and &lt;code&gt;AAAA&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SRV&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CNAME&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optionally, a health check&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you create the service, you can submit a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html\&quot;&gt;RegisterInstance&lt;/a&gt; request, and Cloud Map uses the values in the configuration to create the specified entities.&lt;/p&gt; &lt;p&gt;For the current quota on the number of instances that you can register using the same namespace and using the same service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_namespace

    Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service

    Deletes a specified service. If the service still contains one or more registered instances, the request fails.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteServiceRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_instance

    Deletes the Amazon Route 53 DNS records and health check, if any, that Cloud Map created for the specified instance.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeregisterInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def discover_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """discover_instances

    Discovers registered instances for a specified namespace and service. You can use &lt;code&gt;DiscoverInstances&lt;/code&gt; to discover instances for any type of namespace. For public and private DNS namespaces, you can also use DNS queries to discover instances.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DiscoverInstancesRequest.from_dict(body)
    return web.Response(status=200)


async def get_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_instance

    Gets information about a specified instance.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_instances_health_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_instances_health_status

    &lt;p&gt;Gets the current health status (&lt;code&gt;Healthy&lt;/code&gt;, &lt;code&gt;Unhealthy&lt;/code&gt;, or &lt;code&gt;Unknown&lt;/code&gt;) of one or more instances that are associated with a specified service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;There&#39;s a brief delay between when you register an instance and when the health status for the instance is available. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetInstancesHealthStatusRequest.from_dict(body)
    return web.Response(status=200)


async def get_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_namespace

    Gets information about a namespace.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def get_operation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_operation

    &lt;p&gt;Gets information about any operation that returns an operation ID in the response, such as a &lt;code&gt;CreateService&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To get a list of operations that match specified criteria, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html\&quot;&gt;ListOperations&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetOperationRequest.from_dict(body)
    return web.Response(status=200)


async def get_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service

    Gets the settings for a specified service.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetServiceRequest.from_dict(body)
    return web.Response(status=200)


async def list_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_instances

    Lists summary information about the instances that you registered by using a specified service.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListInstancesRequest.from_dict(body)
    return web.Response(status=200)


async def list_namespaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_namespaces

    Lists summary information about the namespaces that were created by the current Amazon Web Services account.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListNamespacesRequest.from_dict(body)
    return web.Response(status=200)


async def list_operations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_operations

    Lists operations that match the criteria that you specify.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListOperationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_services(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_services

    Lists summary information for all the services that are associated with one or more specified namespaces.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListServicesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists tags for the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def register_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_instance

    &lt;p&gt;Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service. When you submit a &lt;code&gt;RegisterInstance&lt;/code&gt; request, the following occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For each DNS record that you define in the service that&#39;s specified by &lt;code&gt;ServiceId&lt;/code&gt;, a record is created or updated in the hosted zone that&#39;s associated with the corresponding namespace.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the service includes &lt;code&gt;HealthCheckConfig&lt;/code&gt;, a health check is created based on the settings in the health check configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The health check, if any, is associated with each of the new or updated records.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;One &lt;code&gt;RegisterInstance&lt;/code&gt; request must complete before you can submit another request and specify the same service ID and instance ID.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html\&quot;&gt;CreateService&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When Cloud Map receives a DNS query for the specified DNS name, it returns the applicable value:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If the health check is healthy&lt;/b&gt;: returns all the records&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If the health check is unhealthy&lt;/b&gt;: returns the applicable value for the last healthy instance&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you didn&#39;t specify a health check configuration&lt;/b&gt;: returns all the records&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For the current quota on the number of instances that you can register using the same namespace and using the same service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html\&quot;&gt;Cloud Map quotas&lt;/a&gt; in the &lt;i&gt;Cloud Map Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RegisterInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tags to the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_http_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_http_namespace

    Updates an HTTP namespace.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateHttpNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_instance_custom_health_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_instance_custom_health_status

    &lt;p&gt;Submits a request to change the health status of a custom health check to healthy or unhealthy.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;UpdateInstanceCustomHealthStatus&lt;/code&gt; to change the status only for custom health checks, which you define using &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; when you create a service. You can&#39;t use it to change the status for Route 53 health checks, which you define using &lt;code&gt;HealthCheckConfig&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html\&quot;&gt;HealthCheckCustomConfig&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateInstanceCustomHealthStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_private_dns_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_private_dns_namespace

    Updates a private DNS namespace.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdatePrivateDnsNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_public_dns_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_public_dns_namespace

    Updates a public DNS namespace.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdatePublicDnsNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service

    &lt;p&gt;Submits a request to perform the following operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update the TTL setting for existing &lt;code&gt;DnsRecords&lt;/code&gt; configurations&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add, update, or delete &lt;code&gt;HealthCheckConfig&lt;/code&gt; for a specified service&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t add, update, or delete a &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; configuration.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For public and private DNS namespaces, note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you omit any existing &lt;code&gt;DnsRecords&lt;/code&gt; or &lt;code&gt;HealthCheckConfig&lt;/code&gt; configurations from an &lt;code&gt;UpdateService&lt;/code&gt; request, the configurations are deleted from the service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you omit an existing &lt;code&gt;HealthCheckCustomConfig&lt;/code&gt; configuration from an &lt;code&gt;UpdateService&lt;/code&gt; request, the configuration isn&#39;t deleted from the service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you update settings for a service, Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateServiceRequest.from_dict(body)
    return web.Response(status=200)
