from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_gateway_route_output import CreateGatewayRouteOutput
from openapi_server.models.create_gateway_route_request import CreateGatewayRouteRequest
from openapi_server.models.create_mesh_output import CreateMeshOutput
from openapi_server.models.create_mesh_request import CreateMeshRequest
from openapi_server.models.create_route_output import CreateRouteOutput
from openapi_server.models.create_route_request import CreateRouteRequest
from openapi_server.models.create_virtual_gateway_output import CreateVirtualGatewayOutput
from openapi_server.models.create_virtual_gateway_request import CreateVirtualGatewayRequest
from openapi_server.models.create_virtual_node_output import CreateVirtualNodeOutput
from openapi_server.models.create_virtual_node_request import CreateVirtualNodeRequest
from openapi_server.models.create_virtual_router_output import CreateVirtualRouterOutput
from openapi_server.models.create_virtual_router_request import CreateVirtualRouterRequest
from openapi_server.models.create_virtual_service_output import CreateVirtualServiceOutput
from openapi_server.models.create_virtual_service_request import CreateVirtualServiceRequest
from openapi_server.models.delete_gateway_route_output import DeleteGatewayRouteOutput
from openapi_server.models.delete_mesh_output import DeleteMeshOutput
from openapi_server.models.delete_route_output import DeleteRouteOutput
from openapi_server.models.delete_virtual_gateway_output import DeleteVirtualGatewayOutput
from openapi_server.models.delete_virtual_node_output import DeleteVirtualNodeOutput
from openapi_server.models.delete_virtual_router_output import DeleteVirtualRouterOutput
from openapi_server.models.delete_virtual_service_output import DeleteVirtualServiceOutput
from openapi_server.models.describe_gateway_route_output import DescribeGatewayRouteOutput
from openapi_server.models.describe_mesh_output import DescribeMeshOutput
from openapi_server.models.describe_route_output import DescribeRouteOutput
from openapi_server.models.describe_virtual_gateway_output import DescribeVirtualGatewayOutput
from openapi_server.models.describe_virtual_node_output import DescribeVirtualNodeOutput
from openapi_server.models.describe_virtual_router_output import DescribeVirtualRouterOutput
from openapi_server.models.describe_virtual_service_output import DescribeVirtualServiceOutput
from openapi_server.models.list_gateway_routes_output import ListGatewayRoutesOutput
from openapi_server.models.list_meshes_output import ListMeshesOutput
from openapi_server.models.list_routes_output import ListRoutesOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_virtual_gateways_output import ListVirtualGatewaysOutput
from openapi_server.models.list_virtual_nodes_output import ListVirtualNodesOutput
from openapi_server.models.list_virtual_routers_output import ListVirtualRoutersOutput
from openapi_server.models.list_virtual_services_output import ListVirtualServicesOutput
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_gateway_route_output import UpdateGatewayRouteOutput
from openapi_server.models.update_gateway_route_request import UpdateGatewayRouteRequest
from openapi_server.models.update_mesh_output import UpdateMeshOutput
from openapi_server.models.update_mesh_request import UpdateMeshRequest
from openapi_server.models.update_route_output import UpdateRouteOutput
from openapi_server.models.update_route_request import UpdateRouteRequest
from openapi_server.models.update_virtual_gateway_output import UpdateVirtualGatewayOutput
from openapi_server.models.update_virtual_gateway_request import UpdateVirtualGatewayRequest
from openapi_server.models.update_virtual_node_output import UpdateVirtualNodeOutput
from openapi_server.models.update_virtual_node_request import UpdateVirtualNodeRequest
from openapi_server.models.update_virtual_router_output import UpdateVirtualRouterOutput
from openapi_server.models.update_virtual_router_request import UpdateVirtualRouterRequest
from openapi_server.models.update_virtual_service_output import UpdateVirtualServiceOutput
from openapi_server.models.update_virtual_service_request import UpdateVirtualServiceRequest
from openapi_server import util


async def create_gateway_route(request: web.Request, mesh_name, virtual_gateway_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_gateway_route

    &lt;p&gt;Creates a gateway route.&lt;/p&gt; &lt;p&gt;A gateway route is attached to a virtual gateway and routes traffic to an existing virtual service. If a route matches a request, it can distribute traffic to a target virtual service.&lt;/p&gt; &lt;p&gt;For more information about gateway routes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/gateway-routes.html\&quot;&gt;Gateway routes&lt;/a&gt;.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the gateway route in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to associate the gateway route with. If the virtual gateway is in a shared mesh, then you must be the owner of the virtual gateway resource.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateGatewayRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_mesh(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_mesh

    &lt;p&gt;Creates a service mesh.&lt;/p&gt; &lt;p&gt; A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.&lt;/p&gt; &lt;p&gt;For more information about service meshes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html\&quot;&gt;Service meshes&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateMeshRequest.from_dict(body)
    return web.Response(status=200)


async def create_route(request: web.Request, mesh_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_route

    &lt;p&gt;Creates a route that is associated with a virtual router.&lt;/p&gt; &lt;p&gt; You can route several different protocols and define a retry policy for a route. Traffic can be routed to one or more virtual nodes.&lt;/p&gt; &lt;p&gt;For more information about routes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html\&quot;&gt;Routes&lt;/a&gt;.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the route in.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_gateway(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_virtual_gateway

    &lt;p&gt;Creates a virtual gateway.&lt;/p&gt; &lt;p&gt;A virtual gateway allows resources outside your mesh to communicate to resources that are inside your mesh. The virtual gateway represents an Envoy proxy running in an Amazon ECS task, in a Kubernetes service, or on an Amazon EC2 instance. Unlike a virtual node, which represents an Envoy running with an application, a virtual gateway represents Envoy deployed by itself.&lt;/p&gt; &lt;p&gt;For more information about virtual gateways, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html\&quot;&gt;Virtual gateways&lt;/a&gt;. &lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the virtual gateway in.
    :type mesh_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateVirtualGatewayRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_node(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_virtual_node

    &lt;p&gt;Creates a virtual node within a service mesh.&lt;/p&gt; &lt;p&gt; A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery information for your task group, and whether the proxy running in a task group will communicate with other proxies using Transport Layer Security (TLS).&lt;/p&gt; &lt;p&gt;You define a &lt;code&gt;listener&lt;/code&gt; for any inbound traffic that your virtual node expects. Any virtual service that your virtual node expects to communicate to is specified as a &lt;code&gt;backend&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The response metadata for your new virtual node contains the &lt;code&gt;arn&lt;/code&gt; that is associated with the virtual node. Set this value to the full ARN; for example, &lt;code&gt;arn:aws:appmesh:us-west-2:123456789012:myMesh/default/virtualNode/myApp&lt;/code&gt;) as the &lt;code&gt;APPMESH_RESOURCE_ARN&lt;/code&gt; environment variable for your task group&#39;s Envoy proxy container in your task definition or pod spec. This is then mapped to the &lt;code&gt;node.id&lt;/code&gt; and &lt;code&gt;node.cluster&lt;/code&gt; Envoy parameters.&lt;/p&gt; &lt;note&gt; &lt;p&gt;By default, App Mesh uses the name of the resource you specified in &lt;code&gt;APPMESH_RESOURCE_ARN&lt;/code&gt; when Envoy is referring to itself in metrics and traces. You can override this behavior by setting the &lt;code&gt;APPMESH_RESOURCE_CLUSTER&lt;/code&gt; environment variable with your own name.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information about virtual nodes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html\&quot;&gt;Virtual nodes&lt;/a&gt;. You must be using &lt;code&gt;1.15.0&lt;/code&gt; or later of the Envoy image when setting these variables. For more information aboutApp Mesh Envoy variables, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html\&quot;&gt;Envoy image&lt;/a&gt; in the App Mesh User Guide.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the virtual node in.
    :type mesh_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateVirtualNodeRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_router(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_virtual_router

    &lt;p&gt;Creates a virtual router within a service mesh.&lt;/p&gt; &lt;p&gt;Specify a &lt;code&gt;listener&lt;/code&gt; for any inbound traffic that your virtual router receives. Create a virtual router for each protocol and port that you need to route. Virtual routers handle traffic for one or more virtual services within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.&lt;/p&gt; &lt;p&gt;For more information about virtual routers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html\&quot;&gt;Virtual routers&lt;/a&gt;.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the virtual router in.
    :type mesh_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateVirtualRouterRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_service(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """create_virtual_service

    &lt;p&gt;Creates a virtual service within a service mesh.&lt;/p&gt; &lt;p&gt;A virtual service is an abstraction of a real service that is provided by a virtual node directly or indirectly by means of a virtual router. Dependent services call your virtual service by its &lt;code&gt;virtualServiceName&lt;/code&gt;, and those requests are routed to the virtual node or virtual router that is specified as the provider for the virtual service.&lt;/p&gt; &lt;p&gt;For more information about virtual services, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html\&quot;&gt;Virtual services&lt;/a&gt;.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to create the virtual service in.
    :type mesh_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = CreateVirtualServiceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_gateway_route(request: web.Request, gateway_route_name, mesh_name, virtual_gateway_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_gateway_route

    Deletes an existing gateway route.

    :param gateway_route_name: The name of the gateway route to delete.
    :type gateway_route_name: str
    :param mesh_name: The name of the service mesh to delete the gateway route from.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to delete the route from.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def delete_mesh(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_mesh

    &lt;p&gt;Deletes an existing service mesh.&lt;/p&gt; &lt;p&gt;You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to delete.
    :type mesh_name: str
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


async def delete_route(request: web.Request, mesh_name, route_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_route

    Deletes an existing route.

    :param mesh_name: The name of the service mesh to delete the route in.
    :type mesh_name: str
    :param route_name: The name of the route to delete.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router to delete the route in.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def delete_virtual_gateway(request: web.Request, mesh_name, virtual_gateway_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_virtual_gateway

    Deletes an existing virtual gateway. You cannot delete a virtual gateway if any gateway routes are associated to it.

    :param mesh_name: The name of the service mesh to delete the virtual gateway from.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to delete.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def delete_virtual_node(request: web.Request, mesh_name, virtual_node_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_virtual_node

    &lt;p&gt;Deletes an existing virtual node.&lt;/p&gt; &lt;p&gt;You must delete any virtual services that list a virtual node as a service provider before you can delete the virtual node itself.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to delete the virtual node in.
    :type mesh_name: str
    :param virtual_node_name: The name of the virtual node to delete.
    :type virtual_node_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def delete_virtual_router(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_virtual_router

    &lt;p&gt;Deletes an existing virtual router.&lt;/p&gt; &lt;p&gt;You must delete any routes associated with the virtual router before you can delete the router itself.&lt;/p&gt;

    :param mesh_name: The name of the service mesh to delete the virtual router in.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router to delete.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def delete_virtual_service(request: web.Request, mesh_name, virtual_service_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """delete_virtual_service

    Deletes an existing virtual service.

    :param mesh_name: The name of the service mesh to delete the virtual service in.
    :type mesh_name: str
    :param virtual_service_name: The name of the virtual service to delete.
    :type virtual_service_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_gateway_route(request: web.Request, gateway_route_name, mesh_name, virtual_gateway_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_gateway_route

    Describes an existing gateway route.

    :param gateway_route_name: The name of the gateway route to describe.
    :type gateway_route_name: str
    :param mesh_name: The name of the service mesh that the gateway route resides in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway that the gateway route is associated with.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_mesh(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_mesh

    Describes an existing service mesh.

    :param mesh_name: The name of the service mesh to describe.
    :type mesh_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_route(request: web.Request, mesh_name, route_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_route

    Describes an existing route.

    :param mesh_name: The name of the service mesh that the route resides in.
    :type mesh_name: str
    :param route_name: The name of the route to describe.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router that the route is associated with.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_virtual_gateway(request: web.Request, mesh_name, virtual_gateway_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_virtual_gateway

    Describes an existing virtual gateway.

    :param mesh_name: The name of the service mesh that the gateway route resides in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to describe.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_virtual_node(request: web.Request, mesh_name, virtual_node_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_virtual_node

    Describes an existing virtual node.

    :param mesh_name: The name of the service mesh that the virtual node resides in.
    :type mesh_name: str
    :param virtual_node_name: The name of the virtual node to describe.
    :type virtual_node_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_virtual_router(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_virtual_router

    Describes an existing virtual router.

    :param mesh_name: The name of the service mesh that the virtual router resides in.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router to describe.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def describe_virtual_service(request: web.Request, mesh_name, virtual_service_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """describe_virtual_service

    Describes an existing virtual service.

    :param mesh_name: The name of the service mesh that the virtual service resides in.
    :type mesh_name: str
    :param virtual_service_name: The name of the virtual service to describe.
    :type virtual_service_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    return web.Response(status=200)


async def list_gateway_routes(request: web.Request, mesh_name, virtual_gateway_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_gateway_routes

    Returns a list of existing gateway routes that are associated to a virtual gateway.

    :param mesh_name: The name of the service mesh to list gateway routes in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to list gateway routes in.
    :type virtual_gateway_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListGatewayRoutes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListGatewayRoutes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListGatewayRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListGatewayRoutes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListGatewayRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_meshes(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_meshes

    Returns a list of existing service meshes.

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
    :param limit: The maximum number of results returned by &lt;code&gt;ListMeshes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListMeshes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListMeshes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListMeshes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListMeshes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_routes(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_routes

    Returns a list of existing routes in a service mesh.

    :param mesh_name: The name of the service mesh to list routes in.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router to list routes in.
    :type virtual_router_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListRoutes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListRoutes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListRoutes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    List the tags for an App Mesh resource.

    :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource to list the tags for.
    :type resource_arn: str
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
    :param limit: The maximum number of tag results returned by &lt;code&gt;ListTagsForResource&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListTagsForResource&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListTagsForResource&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListTagsForResource&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListTagsForResource&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_gateways(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_virtual_gateways

    Returns a list of existing virtual gateways in a service mesh.

    :param mesh_name: The name of the service mesh to list virtual gateways in.
    :type mesh_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListVirtualGateways&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualGateways&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualGateways&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualGateways&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualGateways&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_nodes(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_virtual_nodes

    Returns a list of existing virtual nodes.

    :param mesh_name: The name of the service mesh to list virtual nodes in.
    :type mesh_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListVirtualNodes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualNodes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualNodes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_routers(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_virtual_routers

    Returns a list of existing virtual routers in a service mesh.

    :param mesh_name: The name of the service mesh to list virtual routers in.
    :type mesh_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListVirtualRouters&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualRouters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualRouters&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_services(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, mesh_owner=None, next_token=None) -> web.Response:
    """list_virtual_services

    Returns a list of existing virtual services in a service mesh.

    :param mesh_name: The name of the service mesh to list virtual services in.
    :type mesh_name: str
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
    :param limit: The maximum number of results returned by &lt;code&gt;ListVirtualServices&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualServices&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualServices&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualServices&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualServices&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource aren&#39;t specified in the request parameters, they aren&#39;t changed. When a resource is deleted, the tags associated with that resource are also deleted.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to add tags to.
    :type resource_arn: str
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


async def untag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Deletes specified tags from a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to delete tags from.
    :type resource_arn: str
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


async def update_gateway_route(request: web.Request, gateway_route_name, mesh_name, virtual_gateway_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_gateway_route

    Updates an existing gateway route that is associated to a specified virtual gateway in a service mesh.

    :param gateway_route_name: The name of the gateway route to update.
    :type gateway_route_name: str
    :param mesh_name: The name of the service mesh that the gateway route resides in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway that the gateway route is associated with.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateGatewayRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_mesh(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_mesh

    Updates an existing service mesh.

    :param mesh_name: The name of the service mesh to update.
    :type mesh_name: str
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
    body = UpdateMeshRequest.from_dict(body)
    return web.Response(status=200)


async def update_route(request: web.Request, mesh_name, route_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_route

    Updates an existing route for a specified service mesh and virtual router.

    :param mesh_name: The name of the service mesh that the route resides in.
    :type mesh_name: str
    :param route_name: The name of the route to update.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router that the route is associated with.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_gateway(request: web.Request, mesh_name, virtual_gateway_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_virtual_gateway

    Updates an existing virtual gateway in a specified service mesh.

    :param mesh_name: The name of the service mesh that the virtual gateway resides in.
    :type mesh_name: str
    :param virtual_gateway_name: The name of the virtual gateway to update.
    :type virtual_gateway_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateVirtualGatewayRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_node(request: web.Request, mesh_name, virtual_node_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_virtual_node

    Updates an existing virtual node in a specified service mesh.

    :param mesh_name: The name of the service mesh that the virtual node resides in.
    :type mesh_name: str
    :param virtual_node_name: The name of the virtual node to update.
    :type virtual_node_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateVirtualNodeRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_router(request: web.Request, mesh_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_virtual_router

    Updates an existing virtual router in a specified service mesh.

    :param mesh_name: The name of the service mesh that the virtual router resides in.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router to update.
    :type virtual_router_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateVirtualRouterRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_service(request: web.Request, mesh_name, virtual_service_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mesh_owner=None) -> web.Response:
    """update_virtual_service

    Updates an existing virtual service in a specified service mesh.

    :param mesh_name: The name of the service mesh that the virtual service resides in.
    :type mesh_name: str
    :param virtual_service_name: The name of the virtual service to update.
    :type virtual_service_name: str
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
    :param mesh_owner: The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;.
    :type mesh_owner: str

    """
    body = UpdateVirtualServiceRequest.from_dict(body)
    return web.Response(status=200)
