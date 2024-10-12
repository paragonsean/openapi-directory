from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_placement_group_request import CreatePlacementGroupRequest
from openapi_server.models.create_placement_group_response import CreatePlacementGroupResponse
from openapi_server.models.placement_group_response import PlacementGroupResponse
from openapi_server.models.placement_groups_response import PlacementGroupsResponse
from openapi_server.models.update_placement_group_request import UpdatePlacementGroupRequest
from openapi_server import util


async def placement_groups_get(request: web.Request, sort=None, name=None, label_selector=None, type=None) -> web.Response:
    """Get all PlacementGroups

    Returns all PlacementGroup objects.

    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str
    :param type: Can be used multiple times. The response will only contain PlacementGroups matching the type.
    :type type: str

    """
    return web.Response(status=200)


async def placement_groups_id_delete(request: web.Request, id) -> web.Response:
    """Delete a PlacementGroup

    Deletes a PlacementGroup.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def placement_groups_id_get(request: web.Request, id) -> web.Response:
    """Get a PlacementGroup

    Gets a specific PlacementGroup object.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def placement_groups_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a PlacementGroup

    Updates the PlacementGroup properties.  Note that when updating labels, the PlacementGroup’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the PlacementGroup object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the resource
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePlacementGroupRequest.from_dict(body)
    return web.Response(status=200)


async def placement_groups_post(request: web.Request, body=None) -> web.Response:
    """Create a PlacementGroup

    Creates a new PlacementGroup. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlacementGroupRequest.from_dict(body)
    return web.Response(status=200)
