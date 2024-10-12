from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_custom_routing_endpoints_request import AddCustomRoutingEndpointsRequest
from openapi_server.models.add_custom_routing_endpoints_response import AddCustomRoutingEndpointsResponse
from openapi_server.models.add_endpoints_request import AddEndpointsRequest
from openapi_server.models.add_endpoints_response import AddEndpointsResponse
from openapi_server.models.advertise_byoip_cidr_request import AdvertiseByoipCidrRequest
from openapi_server.models.advertise_byoip_cidr_response import AdvertiseByoipCidrResponse
from openapi_server.models.allow_custom_routing_traffic_request import AllowCustomRoutingTrafficRequest
from openapi_server.models.create_accelerator_request import CreateAcceleratorRequest
from openapi_server.models.create_accelerator_response import CreateAcceleratorResponse
from openapi_server.models.create_custom_routing_accelerator_request import CreateCustomRoutingAcceleratorRequest
from openapi_server.models.create_custom_routing_accelerator_response import CreateCustomRoutingAcceleratorResponse
from openapi_server.models.create_custom_routing_endpoint_group_request import CreateCustomRoutingEndpointGroupRequest
from openapi_server.models.create_custom_routing_endpoint_group_response import CreateCustomRoutingEndpointGroupResponse
from openapi_server.models.create_custom_routing_listener_request import CreateCustomRoutingListenerRequest
from openapi_server.models.create_custom_routing_listener_response import CreateCustomRoutingListenerResponse
from openapi_server.models.create_endpoint_group_request import CreateEndpointGroupRequest
from openapi_server.models.create_endpoint_group_response import CreateEndpointGroupResponse
from openapi_server.models.create_listener_request import CreateListenerRequest
from openapi_server.models.create_listener_response import CreateListenerResponse
from openapi_server.models.delete_accelerator_request import DeleteAcceleratorRequest
from openapi_server.models.delete_custom_routing_accelerator_request import DeleteCustomRoutingAcceleratorRequest
from openapi_server.models.delete_custom_routing_endpoint_group_request import DeleteCustomRoutingEndpointGroupRequest
from openapi_server.models.delete_custom_routing_listener_request import DeleteCustomRoutingListenerRequest
from openapi_server.models.delete_endpoint_group_request import DeleteEndpointGroupRequest
from openapi_server.models.delete_listener_request import DeleteListenerRequest
from openapi_server.models.deny_custom_routing_traffic_request import DenyCustomRoutingTrafficRequest
from openapi_server.models.deprovision_byoip_cidr_request import DeprovisionByoipCidrRequest
from openapi_server.models.deprovision_byoip_cidr_response import DeprovisionByoipCidrResponse
from openapi_server.models.describe_accelerator_attributes_request import DescribeAcceleratorAttributesRequest
from openapi_server.models.describe_accelerator_attributes_response import DescribeAcceleratorAttributesResponse
from openapi_server.models.describe_accelerator_request import DescribeAcceleratorRequest
from openapi_server.models.describe_accelerator_response import DescribeAcceleratorResponse
from openapi_server.models.describe_custom_routing_accelerator_attributes_request import DescribeCustomRoutingAcceleratorAttributesRequest
from openapi_server.models.describe_custom_routing_accelerator_attributes_response import DescribeCustomRoutingAcceleratorAttributesResponse
from openapi_server.models.describe_custom_routing_accelerator_request import DescribeCustomRoutingAcceleratorRequest
from openapi_server.models.describe_custom_routing_accelerator_response import DescribeCustomRoutingAcceleratorResponse
from openapi_server.models.describe_custom_routing_endpoint_group_request import DescribeCustomRoutingEndpointGroupRequest
from openapi_server.models.describe_custom_routing_endpoint_group_response import DescribeCustomRoutingEndpointGroupResponse
from openapi_server.models.describe_custom_routing_listener_request import DescribeCustomRoutingListenerRequest
from openapi_server.models.describe_custom_routing_listener_response import DescribeCustomRoutingListenerResponse
from openapi_server.models.describe_endpoint_group_request import DescribeEndpointGroupRequest
from openapi_server.models.describe_endpoint_group_response import DescribeEndpointGroupResponse
from openapi_server.models.describe_listener_request import DescribeListenerRequest
from openapi_server.models.describe_listener_response import DescribeListenerResponse
from openapi_server.models.list_accelerators_request import ListAcceleratorsRequest
from openapi_server.models.list_accelerators_response import ListAcceleratorsResponse
from openapi_server.models.list_byoip_cidrs_request import ListByoipCidrsRequest
from openapi_server.models.list_byoip_cidrs_response import ListByoipCidrsResponse
from openapi_server.models.list_custom_routing_accelerators_request import ListCustomRoutingAcceleratorsRequest
from openapi_server.models.list_custom_routing_accelerators_response import ListCustomRoutingAcceleratorsResponse
from openapi_server.models.list_custom_routing_endpoint_groups_request import ListCustomRoutingEndpointGroupsRequest
from openapi_server.models.list_custom_routing_endpoint_groups_response import ListCustomRoutingEndpointGroupsResponse
from openapi_server.models.list_custom_routing_listeners_request import ListCustomRoutingListenersRequest
from openapi_server.models.list_custom_routing_listeners_response import ListCustomRoutingListenersResponse
from openapi_server.models.list_custom_routing_port_mappings_by_destination_request import ListCustomRoutingPortMappingsByDestinationRequest
from openapi_server.models.list_custom_routing_port_mappings_by_destination_response import ListCustomRoutingPortMappingsByDestinationResponse
from openapi_server.models.list_custom_routing_port_mappings_request import ListCustomRoutingPortMappingsRequest
from openapi_server.models.list_custom_routing_port_mappings_response import ListCustomRoutingPortMappingsResponse
from openapi_server.models.list_endpoint_groups_request import ListEndpointGroupsRequest
from openapi_server.models.list_endpoint_groups_response import ListEndpointGroupsResponse
from openapi_server.models.list_listeners_request import ListListenersRequest
from openapi_server.models.list_listeners_response import ListListenersResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.provision_byoip_cidr_request import ProvisionByoipCidrRequest
from openapi_server.models.provision_byoip_cidr_response import ProvisionByoipCidrResponse
from openapi_server.models.remove_custom_routing_endpoints_request import RemoveCustomRoutingEndpointsRequest
from openapi_server.models.remove_endpoints_request import RemoveEndpointsRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_accelerator_attributes_request import UpdateAcceleratorAttributesRequest
from openapi_server.models.update_accelerator_attributes_response import UpdateAcceleratorAttributesResponse
from openapi_server.models.update_accelerator_request import UpdateAcceleratorRequest
from openapi_server.models.update_accelerator_response import UpdateAcceleratorResponse
from openapi_server.models.update_custom_routing_accelerator_attributes_request import UpdateCustomRoutingAcceleratorAttributesRequest
from openapi_server.models.update_custom_routing_accelerator_attributes_response import UpdateCustomRoutingAcceleratorAttributesResponse
from openapi_server.models.update_custom_routing_accelerator_request import UpdateCustomRoutingAcceleratorRequest
from openapi_server.models.update_custom_routing_accelerator_response import UpdateCustomRoutingAcceleratorResponse
from openapi_server.models.update_custom_routing_listener_request import UpdateCustomRoutingListenerRequest
from openapi_server.models.update_custom_routing_listener_response import UpdateCustomRoutingListenerResponse
from openapi_server.models.update_endpoint_group_request import UpdateEndpointGroupRequest
from openapi_server.models.update_endpoint_group_response import UpdateEndpointGroupResponse
from openapi_server.models.update_listener_request import UpdateListenerRequest
from openapi_server.models.update_listener_response import UpdateListenerResponse
from openapi_server.models.withdraw_byoip_cidr_request import WithdrawByoipCidrRequest
from openapi_server.models.withdraw_byoip_cidr_response import WithdrawByoipCidrResponse
from openapi_server import util


async def add_custom_routing_endpoints(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_custom_routing_endpoints

    &lt;p&gt;Associate a virtual private cloud (VPC) subnet endpoint with your custom routing accelerator.&lt;/p&gt; &lt;p&gt;The listener port range must be large enough to support the number of IP addresses that can be specified in your subnet. The number of ports required is: subnet size times the number of ports per destination EC2 instances. For example, a subnet defined as /24 requires a listener port range of at least 255 ports. &lt;/p&gt; &lt;p&gt;Note: You must have enough remaining listener ports available to map to the subnet ports, or the call will fail with a LimitExceededException.&lt;/p&gt; &lt;p&gt;By default, all destinations in a subnet in a custom routing accelerator cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html\&quot;&gt; AllowCustomRoutingTraffic&lt;/a&gt; operation.&lt;/p&gt;

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
    body = AddCustomRoutingEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def add_endpoints(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_endpoints

    &lt;p&gt;Add endpoints to an endpoint group. The &lt;code&gt;AddEndpoints&lt;/code&gt; API operation is the recommended option for adding endpoints. The alternative options are to add endpoints when you create an endpoint group (with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html\&quot;&gt;CreateEndpointGroup&lt;/a&gt; API) or when you update an endpoint group (with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html\&quot;&gt;UpdateEndpointGroup&lt;/a&gt; API). &lt;/p&gt; &lt;p&gt;There are two advantages to using &lt;code&gt;AddEndpoints&lt;/code&gt; to add endpoints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;It&#39;s faster, because Global Accelerator only has to resolve the new endpoints that you&#39;re adding.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;It&#39;s more convenient, because you don&#39;t need to specify all of the current endpoints that are already in the endpoint group in addition to the new endpoints that you want to add.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = AddEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def advertise_byoip_cidr(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """advertise_byoip_cidr

    &lt;p&gt;Advertises an IPv4 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP). It can take a few minutes before traffic to the specified addresses starts routing to Amazon Web Services because of propagation delays. &lt;/p&gt; &lt;p&gt;To stop advertising the BYOIP address range, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html\&quot;&gt; WithdrawByoipCidr&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\&quot;&gt;Bring your own IP addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = AdvertiseByoipCidrRequest.from_dict(body)
    return web.Response(status=200)


async def allow_custom_routing_traffic(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """allow_custom_routing_traffic

    &lt;p&gt;Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that can receive traffic for a custom routing accelerator. You can allow traffic to all destinations in the subnet endpoint, or allow traffic to a specified list of destination IP addresses and ports in the subnet. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.&lt;/p&gt; &lt;p&gt;After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN_PROGRESS to DEPLOYED.&lt;/p&gt;

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
    body = AllowCustomRoutingTrafficRequest.from_dict(body)
    return web.Response(status=200)


async def create_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_accelerator

    &lt;p&gt;Create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Network Load Balancers. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify &lt;code&gt;--region us-west-2&lt;/code&gt; on AWS CLI commands.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def create_custom_routing_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_custom_routing_accelerator

    &lt;p&gt;Create a custom routing accelerator. A custom routing accelerator directs traffic to one of possibly thousands of Amazon EC2 instance destinations running in a single or multiple virtual private clouds (VPC) subnet endpoints.&lt;/p&gt; &lt;p&gt;Be aware that, by default, all destination EC2 instances in a VPC subnet endpoint cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html\&quot;&gt; AllowCustomRoutingTraffic&lt;/a&gt; operation.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify &lt;code&gt;--region us-west-2&lt;/code&gt; on AWS CLI commands.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateCustomRoutingAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def create_custom_routing_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_custom_routing_endpoint_group

    Create an endpoint group for the specified listener for a custom routing accelerator. An endpoint group is a collection of endpoints in one Amazon Web Services Region. 

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
    body = CreateCustomRoutingEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_custom_routing_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_custom_routing_listener

    Create a listener to process inbound connections from clients to a custom routing accelerator. Connections arrive to assigned static IP addresses on the port range that you specify. 

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
    body = CreateCustomRoutingListenerRequest.from_dict(body)
    return web.Response(status=200)


async def create_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_endpoint_group

    Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one Amazon Web Services Region. A resource must be valid and active when you add it as an endpoint.

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
    body = CreateEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_listener

    Create a listener to process inbound connections from clients to an accelerator. Connections arrive to assigned static IP addresses on a port, port range, or list of port ranges that you specify. 

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
    body = CreateListenerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_accelerator

    &lt;p&gt;Delete an accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set &lt;code&gt;Enabled&lt;/code&gt; to false.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you create an accelerator, by default, Global Accelerator provides you with a set of two static IP addresses. Alternatively, you can bring your own IP address ranges to Global Accelerator and assign IP addresses from those ranges. &lt;/p&gt; &lt;p&gt;The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you &lt;i&gt;delete&lt;/i&gt; an accelerator, you lose the static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html\&quot;&gt;Identity and access management&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

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
    body = DeleteAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_custom_routing_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_custom_routing_accelerator

    &lt;p&gt;Delete a custom routing accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set &lt;code&gt;Enabled&lt;/code&gt; to false.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you create a custom routing accelerator, by default, Global Accelerator provides you with a set of two static IP addresses. &lt;/p&gt; &lt;p&gt;The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you &lt;i&gt;delete&lt;/i&gt; an accelerator, you lose the static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html\&quot;&gt;Identity and access management&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

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
    body = DeleteCustomRoutingAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_custom_routing_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_custom_routing_endpoint_group

    Delete an endpoint group from a listener for a custom routing accelerator.

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
    body = DeleteCustomRoutingEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_custom_routing_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_custom_routing_listener

    Delete a listener for a custom routing accelerator.

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
    body = DeleteCustomRoutingListenerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_endpoint_group

    Delete an endpoint group from a listener.

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
    body = DeleteEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_listener

    Delete a listener from an accelerator.

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
    body = DeleteListenerRequest.from_dict(body)
    return web.Response(status=200)


async def deny_custom_routing_traffic(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deny_custom_routing_traffic

    &lt;p&gt;Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that cannot receive traffic for a custom routing accelerator. You can deny traffic to all destinations in the VPC endpoint, or deny traffic to a specified list of destination IP addresses and ports. Note that you cannot specify IP addresses or ports outside of the range that you configured for the endpoint group.&lt;/p&gt; &lt;p&gt;After you make changes, you can verify that the updates are complete by checking the status of your accelerator: the status changes from IN_PROGRESS to DEPLOYED.&lt;/p&gt;

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
    body = DenyCustomRoutingTrafficRequest.from_dict(body)
    return web.Response(status=200)


async def deprovision_byoip_cidr(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deprovision_byoip_cidr

    &lt;p&gt;Releases the specified address range that you provisioned to use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. &lt;/p&gt; &lt;p&gt;Before you can release an address range, you must stop advertising it by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html\&quot;&gt;WithdrawByoipCidr&lt;/a&gt; and you must not have any accelerators that are using static IP addresses allocated from its address range. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\&quot;&gt;Bring your own IP addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeprovisionByoipCidrRequest.from_dict(body)
    return web.Response(status=200)


async def describe_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_accelerator

    Describe an accelerator. 

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
    body = DescribeAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_accelerator_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_accelerator_attributes

    Describe the attributes of an accelerator. 

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
    body = DescribeAcceleratorAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_custom_routing_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_custom_routing_accelerator

    Describe a custom routing accelerator. 

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
    body = DescribeCustomRoutingAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_custom_routing_accelerator_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_custom_routing_accelerator_attributes

    Describe the attributes of a custom routing accelerator. 

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
    body = DescribeCustomRoutingAcceleratorAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_custom_routing_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_custom_routing_endpoint_group

    Describe an endpoint group for a custom routing accelerator. 

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
    body = DescribeCustomRoutingEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def describe_custom_routing_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_custom_routing_listener

    The description of a listener for a custom routing accelerator.

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
    body = DescribeCustomRoutingListenerRequest.from_dict(body)
    return web.Response(status=200)


async def describe_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_endpoint_group

    Describe an endpoint group. 

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
    body = DescribeEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def describe_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_listener

    Describe a listener. 

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
    body = DescribeListenerRequest.from_dict(body)
    return web.Response(status=200)


async def list_accelerators(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_accelerators

    List the accelerators for an Amazon Web Services account. 

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
    body = ListAcceleratorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_byoip_cidrs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_byoip_cidrs

    Lists the IP address ranges that were specified in calls to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/ProvisionByoipCidr.html\&quot;&gt;ProvisionByoipCidr&lt;/a&gt;, including the current state and a history of state changes.

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
    body = ListByoipCidrsRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_routing_accelerators(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_routing_accelerators

    List the custom routing accelerators for an Amazon Web Services account. 

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
    body = ListCustomRoutingAcceleratorsRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_routing_endpoint_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_routing_endpoint_groups

    List the endpoint groups that are associated with a listener for a custom routing accelerator. 

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
    body = ListCustomRoutingEndpointGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_routing_listeners(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_routing_listeners

    List the listeners for a custom routing accelerator. 

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
    body = ListCustomRoutingListenersRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_routing_port_mappings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_routing_port_mappings

    &lt;p&gt;Provides a complete mapping from the public accelerator IP address and port to destination EC2 instance IP addresses and ports in the virtual public cloud (VPC) subnet endpoint for a custom routing accelerator. For each subnet endpoint that you add, Global Accelerator creates a new static port mapping for the accelerator. The port mappings don&#39;t change after Global Accelerator generates them, so you can retrieve and cache the full mapping on your servers. &lt;/p&gt; &lt;p&gt;If you remove a subnet from your accelerator, Global Accelerator removes (reclaims) the port mappings. If you add a subnet to your accelerator, Global Accelerator creates new port mappings (the existing ones don&#39;t change). If you add or remove EC2 instances in your subnet, the port mappings don&#39;t change, because the mappings are created when you add the subnet to Global Accelerator.&lt;/p&gt; &lt;p&gt;The mappings also include a flag for each destination denoting which destination IP addresses and ports are allowed or denied traffic.&lt;/p&gt;

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
    body = ListCustomRoutingPortMappingsRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_routing_port_mappings_by_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_custom_routing_port_mappings_by_destination

    List the port mappings for a specific EC2 instance (destination) in a VPC subnet endpoint. The response is the mappings for one destination IP address. This is useful when your subnet endpoint has mappings that span multiple custom routing accelerators in your account, or for scenarios where you only want to list the port mappings for a specific destination instance.

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
    body = ListCustomRoutingPortMappingsByDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def list_endpoint_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_endpoint_groups

    List the endpoint groups that are associated with a listener. 

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
    body = ListEndpointGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_listeners(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_listeners

    List the listeners for an accelerator. 

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
    body = ListListenersRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;List all tags for an accelerator. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html\&quot;&gt;Tagging in Global Accelerator&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;. &lt;/p&gt;

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


async def provision_byoip_cidr(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """provision_byoip_cidr

    &lt;p&gt;Provisions an IP address range to use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/AdvertiseByoipCidr.html\&quot;&gt; AdvertiseByoipCidr&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\&quot;&gt;Bring your own IP addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = ProvisionByoipCidrRequest.from_dict(body)
    return web.Response(status=200)


async def remove_custom_routing_endpoints(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_custom_routing_endpoints

    Remove endpoints from a custom routing accelerator.

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
    body = RemoveCustomRoutingEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def remove_endpoints(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_endpoints

    &lt;p&gt;Remove endpoints from an endpoint group. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;RemoveEndpoints&lt;/code&gt; API operation is the recommended option for removing endpoints. The alternative is to remove endpoints by updating an endpoint group by using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html\&quot;&gt;UpdateEndpointGroup&lt;/a&gt; API operation. There are two advantages to using &lt;code&gt;AddEndpoints&lt;/code&gt; to remove endpoints instead:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;It&#39;s more convenient, because you only need to specify the endpoints that you want to remove. With the &lt;code&gt;UpdateEndpointGroup&lt;/code&gt; API operation, you must specify all of the endpoints in the endpoint group except the ones that you want to remove from the group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;It&#39;s faster, because Global Accelerator doesn&#39;t need to resolve any endpoints. With the &lt;code&gt;UpdateEndpointGroup&lt;/code&gt; API operation, Global Accelerator must resolve all of the endpoints that remain in the group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = RemoveEndpointsRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Add tags to an accelerator resource. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html\&quot;&gt;Tagging in Global Accelerator&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;. &lt;/p&gt;

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

    &lt;p&gt;Remove tags from a Global Accelerator resource. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from an accelerator that was already removed.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html\&quot;&gt;Tagging in Global Accelerator&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt;

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


async def update_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_accelerator

    &lt;p&gt;Update an accelerator. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify &lt;code&gt;--region us-west-2&lt;/code&gt; on AWS CLI commands.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def update_accelerator_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_accelerator_attributes

    Update the attributes for an accelerator. 

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
    body = UpdateAcceleratorAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_custom_routing_accelerator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_custom_routing_accelerator

    Update a custom routing accelerator. 

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
    body = UpdateCustomRoutingAcceleratorRequest.from_dict(body)
    return web.Response(status=200)


async def update_custom_routing_accelerator_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_custom_routing_accelerator_attributes

    Update the attributes for a custom routing accelerator. 

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
    body = UpdateCustomRoutingAcceleratorAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_custom_routing_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_custom_routing_listener

    Update a listener for a custom routing accelerator. 

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
    body = UpdateCustomRoutingListenerRequest.from_dict(body)
    return web.Response(status=200)


async def update_endpoint_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_endpoint_group

    Update an endpoint group. A resource must be valid and active when you add it as an endpoint.

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
    body = UpdateEndpointGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_listener(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_listener

    Update a listener. 

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
    body = UpdateListenerRequest.from_dict(body)
    return web.Response(status=200)


async def withdraw_byoip_cidr(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """withdraw_byoip_cidr

    &lt;p&gt;Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.&lt;/p&gt; &lt;p&gt;It can take a few minutes before traffic to the specified addresses stops routing to Amazon Web Services because of propagation delays.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\&quot;&gt;Bring your own IP addresses (BYOIP)&lt;/a&gt; in the &lt;i&gt;Global Accelerator Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = WithdrawByoipCidrRequest.from_dict(body)
    return web.Response(status=200)
