from typing import List, Dict
from aiohttp import web

from openapi_server.models.containers_groups_get_list_item import ContainersGroupsGetListItem
from openapi_server.models.containers_groups_name_or_id_get_details import ContainersGroupsNameOrIdGetDetails
from openapi_server.models.containers_groups_name_or_id_maproute_post_info import ContainersGroupsNameOrIdMaproutePostInfo
from openapi_server.models.containers_groups_name_or_id_patch_updated_info import ContainersGroupsNameOrIdPatchUpdatedInfo
from openapi_server.models.containers_groups_post_created_info import ContainersGroupsPostCreatedInfo
from openapi_server.models.containers_groups_post_required_attributes import ContainersGroupsPostRequiredAttributes
from openapi_server.models.route import Route
from openapi_server import util


async def containers_groups_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List all container groups in a space

    This endpoint returns a list of all container groups in a space independent of their current state. (corresponding IBM Containers command: &#x60;cf ic group list&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def containers_groups_name_or_id_delete(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, force=None) -> web.Response:
    """Stop and delete all container instances in a container group.

    Stops and deletes the container instances that run in a container group (corresponding IBM Containers command: &#x60;cf ic group rm &lt;group_name&gt;&#x60;). When you delete a container group, all floating private IP addresses are released.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or unique ID of the container group that you want to delete. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space.
    :type name_or_id: str
    :param force: If you want to force the deletion of a container group that has running container instances, use the force option. This parameter needs to be set to either true or false. If set to &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60;, running container instances are deleted. If set to &#x60;force&#x3D;false&#x60;, &#x60;force&#x3D;False&#x60;, or &#x60;force&#x3D;0&#x60;, running container instances are not deleted. If you do not specify this paramater, running container instances are not deleted by default. 
    :type force: str

    """
    return web.Response(status=200)


async def containers_groups_name_or_id_get(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Inspect a container group.

    This endpoint retrieves detailed information about a container group with a given name (corresponding IBM Containers command: &#x60;cf ic group inspect GROUP&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or unique ID of the container group that you want to inspect. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space.
    :type name_or_id: str

    """
    return web.Response(status=200)


async def containers_groups_name_or_id_maproute_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, body) -> web.Response:
    """Map a public route to a container group.

    If you want your container group to be accessible from the Internet, you need to expose a public port and map a public route to it (corresponding IBM Containers command: &#x60;cf ic route map -n &lt;host&gt; -d &lt;domain&gt; &lt;group&gt;&#x60;). Every route consists of the host name and domain.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or unique ID of the container group to which you want to map a public route. Run &#x60;cf ic group list&#x60; or call the &#x60;GET /containers/groups&#x60; endpoint to retrieve a list of container groups in your space.
    :type name_or_id: str
    :param body: The public route that is mapped to the container group. A public route consists of the host name and domain.
    :type body: dict | bytes

    """
    body = Route.from_dict(body)
    return web.Response(status=200)


async def containers_groups_name_or_id_patch(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, body) -> web.Response:
    """Update a container group.

    Update the number of container instances that run in a container group (corresponding IBM Containers command: &#x60;cf ic group update &lt;option&gt; &lt;group&gt;&#x60;).   Note: You can run only one update at a time.     The desired number is the number of container instances that you require. It must be within the current limits of Max and Min. To increase the number of desired container instances above the Max value, you must first execute an update on the Max value. Once this update is completed, you can increase the desired number of container instances. 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or unique ID of the container group that you want to update.
    :type name_or_id: str
    :param body: The container group parameter that you want to update.
    :type body: dict | bytes

    """
    body = ContainersGroupsNameOrIdPatchUpdatedInfo.from_dict(body)
    return web.Response(status=200)


async def containers_groups_name_or_id_unmaproute_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, body) -> web.Response:
    """Unmap a public route from a container group

    This endpoint unmaps a public route from a container group (corresponding IBM Containers command: &#x60;cf ic route unmap -n &lt;host&gt; -d &lt;domain&gt; &lt;group&gt;&#x60;). If no other public route is mapped to the container group, then the container group is no longer available from the internet.    When you unmap a route from a container group, the route is not deleted and can be mapped to other container groups. 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or unique ID (UUID) of the container group that you want to inspect.
    :type name_or_id: str
    :param body: The public route that is unmapped from the container group. A public route consists of the host name and domain.
    :type body: dict | bytes

    """
    body = Route.from_dict(body)
    return web.Response(status=200)


async def containers_groups_post(request: web.Request, x_auth_token, x_auth_project_id, body) -> web.Response:
    """Create and start a container group.

    This endpoint creates and starts a new container group in your space. A container group consists of two or more single containers that are all created from the same container image and as a consequence are configured in the same way. Container groups offer different options at no cost to make your app highly available, such as in-built load balancing, auto-recovery of unhealthy container instances, and auto-scaling of container instances based on CPU and memory usage.  To create a container group with IBM Containers, you must at least define a container group name and the image that the container group is based on. Required attributes:                 - Name: The container group name must start with a letter and then can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-).  - Image: You must include the full path to the image in your private Bluemix registry in the format:&#x60;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image&gt;&#x60;.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param body: Attributes that are required to create a container group in your space.
    :type body: dict | bytes

    """
    body = ContainersGroupsPostRequiredAttributes.from_dict(body)
    return web.Response(status=200)
