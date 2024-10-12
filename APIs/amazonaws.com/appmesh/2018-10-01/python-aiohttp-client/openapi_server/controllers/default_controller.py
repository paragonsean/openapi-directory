from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_mesh_output import CreateMeshOutput
from openapi_server.models.create_mesh_request import CreateMeshRequest
from openapi_server.models.create_route_output import CreateRouteOutput
from openapi_server.models.create_route_request import CreateRouteRequest
from openapi_server.models.create_virtual_node_output import CreateVirtualNodeOutput
from openapi_server.models.create_virtual_node_request import CreateVirtualNodeRequest
from openapi_server.models.create_virtual_router_output import CreateVirtualRouterOutput
from openapi_server.models.create_virtual_router_request import CreateVirtualRouterRequest
from openapi_server.models.delete_mesh_output import DeleteMeshOutput
from openapi_server.models.delete_route_output import DeleteRouteOutput
from openapi_server.models.delete_virtual_node_output import DeleteVirtualNodeOutput
from openapi_server.models.delete_virtual_router_output import DeleteVirtualRouterOutput
from openapi_server.models.describe_mesh_output import DescribeMeshOutput
from openapi_server.models.describe_route_output import DescribeRouteOutput
from openapi_server.models.describe_virtual_node_output import DescribeVirtualNodeOutput
from openapi_server.models.describe_virtual_router_output import DescribeVirtualRouterOutput
from openapi_server.models.list_meshes_output import ListMeshesOutput
from openapi_server.models.list_routes_output import ListRoutesOutput
from openapi_server.models.list_virtual_nodes_output import ListVirtualNodesOutput
from openapi_server.models.list_virtual_routers_output import ListVirtualRoutersOutput
from openapi_server.models.update_route_output import UpdateRouteOutput
from openapi_server.models.update_route_request import UpdateRouteRequest
from openapi_server.models.update_virtual_node_output import UpdateVirtualNodeOutput
from openapi_server.models.update_virtual_node_request import UpdateVirtualNodeRequest
from openapi_server.models.update_virtual_router_output import UpdateVirtualRouterOutput
from openapi_server.models.update_virtual_router_request import UpdateVirtualRouterRequest
from openapi_server import util


async def create_mesh(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_mesh

    &lt;p&gt;Creates a new service mesh. A service mesh is a logical boundary for network traffic          between the services that reside within it.&lt;/p&gt;          &lt;p&gt;After you create your service mesh, you can create virtual nodes, virtual routers, and          routes to distribute traffic between the applications in your mesh.&lt;/p&gt;

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


async def create_route(request: web.Request, mesh_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_route

    &lt;p&gt;Creates a new route that is associated with a virtual router.&lt;/p&gt;          &lt;p&gt;You can use the &lt;code&gt;prefix&lt;/code&gt; parameter in your route specification for path-based          routing of requests. For example, if your virtual router service name is             &lt;code&gt;my-service.local&lt;/code&gt;, and you want the route to match requests to             &lt;code&gt;my-service.local/metrics&lt;/code&gt;, then your prefix should be          &lt;code&gt;/metrics&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;If your route matches a request, you can distribute traffic to one or more target          virtual nodes with relative weighting.&lt;/p&gt;

    :param mesh_name: The name of the service mesh in which to create the route.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router in which to create the route.
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

    """
    body = CreateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_node(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_virtual_node

    &lt;p&gt;Creates a new virtual node within a service mesh.&lt;/p&gt;          &lt;p&gt;A virtual node acts as logical pointer to a particular task group, such as an Amazon ECS          service or a Kubernetes deployment. When you create a virtual node, you must specify the          DNS service discovery name for your task group.&lt;/p&gt;          &lt;p&gt;Any inbound traffic that your virtual node expects should be specified as a             &lt;code&gt;listener&lt;/code&gt;. Any outbound traffic that your virtual node expects to reach          should be specified as a &lt;code&gt;backend&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;The response metadata for your new virtual node contains the &lt;code&gt;arn&lt;/code&gt; that is          associated with the virtual node. Set this value (either the full ARN or the truncated          resource name, for example, &lt;code&gt;mesh/default/virtualNode/simpleapp&lt;/code&gt;, as the             &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; environment variable for your task group&#39;s Envoy          proxy container in your task definition or pod spec. This is then mapped to the             &lt;code&gt;node.id&lt;/code&gt; and &lt;code&gt;node.cluster&lt;/code&gt; Envoy parameters.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;If you require your Envoy stats or tracing to use a different name, you can override             the &lt;code&gt;node.cluster&lt;/code&gt; value that is set by                &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; with the                &lt;code&gt;APPMESH_VIRTUAL_NODE_CLUSTER&lt;/code&gt; environment variable.&lt;/p&gt;          &lt;/note&gt;

    :param mesh_name: The name of the service mesh in which to create the virtual node.
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
    body = CreateVirtualNodeRequest.from_dict(body)
    return web.Response(status=200)


async def create_virtual_router(request: web.Request, mesh_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_virtual_router

    &lt;p&gt;Creates a new virtual router within a service mesh.&lt;/p&gt;          &lt;p&gt;Virtual routers handle traffic for one or more service names within your mesh. After you          create your virtual router, create and associate routes for your virtual router that direct          incoming requests to different virtual nodes.&lt;/p&gt;

    :param mesh_name: The name of the service mesh in which to create the virtual router.
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
    body = CreateVirtualRouterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_mesh(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_mesh

    &lt;p&gt;Deletes an existing service mesh.&lt;/p&gt;          &lt;p&gt;You must delete all resources (routes, virtual routers, virtual nodes) in the service          mesh before you can delete the mesh itself.&lt;/p&gt;

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


async def delete_route(request: web.Request, mesh_name, route_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_route

    Deletes an existing route.

    :param mesh_name: The name of the service mesh in which to delete the route.
    :type mesh_name: str
    :param route_name: The name of the route to delete.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router in which to delete the route.
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

    """
    return web.Response(status=200)


async def delete_virtual_node(request: web.Request, mesh_name, virtual_node_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_virtual_node

    Deletes an existing virtual node.

    :param mesh_name: The name of the service mesh in which to delete the virtual node.
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

    """
    return web.Response(status=200)


async def delete_virtual_router(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_virtual_router

    &lt;p&gt;Deletes an existing virtual router.&lt;/p&gt;          &lt;p&gt;You must delete any routes associated with the virtual router before you can delete the          router itself.&lt;/p&gt;

    :param mesh_name: The name of the service mesh in which to delete the virtual router.
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

    """
    return web.Response(status=200)


async def describe_mesh(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
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

    """
    return web.Response(status=200)


async def describe_route(request: web.Request, mesh_name, route_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_route

    Describes an existing route.

    :param mesh_name: The name of the service mesh in which the route resides.
    :type mesh_name: str
    :param route_name: The name of the route to describe.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router with which the route is associated.
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

    """
    return web.Response(status=200)


async def describe_virtual_node(request: web.Request, mesh_name, virtual_node_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_virtual_node

    Describes an existing virtual node.

    :param mesh_name: The name of the service mesh in which the virtual node resides.
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

    """
    return web.Response(status=200)


async def describe_virtual_router(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_virtual_router

    Describes an existing virtual router.

    :param mesh_name: The name of the service mesh in which the virtual router resides.
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
    :param limit: The maximum number of mesh results returned by &lt;code&gt;ListMeshes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListMeshes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListMeshes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListMeshes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListMeshes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;This token should be treated as an opaque identifier that is only used to                 retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt;         &lt;/note&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def list_routes(request: web.Request, mesh_name, virtual_router_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_routes

    Returns a list of existing routes in a service mesh.

    :param mesh_name: The name of the service mesh in which to list routes.
    :type mesh_name: str
    :param virtual_router_name: The name of the virtual router in which to list routes.
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
    :param limit: The maximum number of mesh results returned by &lt;code&gt;ListRoutes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListRoutes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListRoutes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_nodes(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_virtual_nodes

    Returns a list of existing virtual nodes.

    :param mesh_name: The name of the service mesh in which to list virtual nodes.
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
    :param limit: The maximum number of mesh results returned by &lt;code&gt;ListVirtualNodes&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualNodes&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualNodes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualNodes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_virtual_routers(request: web.Request, mesh_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_virtual_routers

    Returns a list of existing virtual routers in a service mesh.

    :param mesh_name: The name of the service mesh in which to list virtual routers.
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
    :param limit: The maximum number of mesh results returned by &lt;code&gt;ListVirtualRouters&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualRouters&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualRouters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.
    :type limit: int
    :param next_token: The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualRouters&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.
    :type next_token: str

    """
    return web.Response(status=200)


async def update_route(request: web.Request, mesh_name, route_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_route

    Updates an existing route for a specified service mesh and virtual router.

    :param mesh_name: The name of the service mesh in which the route resides.
    :type mesh_name: str
    :param route_name: The name of the route to update.
    :type route_name: str
    :param virtual_router_name: The name of the virtual router with which the route is associated.
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

    """
    body = UpdateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_node(request: web.Request, mesh_name, virtual_node_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_virtual_node

    Updates an existing virtual node in a specified service mesh.

    :param mesh_name: The name of the service mesh in which the virtual node resides.
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

    """
    body = UpdateVirtualNodeRequest.from_dict(body)
    return web.Response(status=200)


async def update_virtual_router(request: web.Request, mesh_name, virtual_router_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_virtual_router

    Updates an existing virtual router in a specified service mesh.

    :param mesh_name: The name of the service mesh in which the virtual router resides.
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

    """
    body = UpdateVirtualRouterRequest.from_dict(body)
    return web.Response(status=200)
