from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.attach_volume_request import AttachVolumeRequest
from openapi_server.models.volumes_id_actions_change_protection_post_request import VolumesIdActionsChangeProtectionPostRequest
from openapi_server.models.volumes_id_actions_resize_post_request import VolumesIdActionsResizePostRequest
from openapi_server import util


async def volumes_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Volume

    Returns a specific Action for a Volume.

    :param id: ID of the Volume
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def volumes_id_actions_attach_post(request: web.Request, id, body=None) -> web.Response:
    """Attach Volume to a Server

    Attaches a Volume to a Server. Works only if the Server is in the same Location as the Volume.

    :param id: ID of the Volume
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AttachVolumeRequest.from_dict(body)
    return web.Response(status=200)


async def volumes_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Volume Protection

    Changes the protection configuration of a Volume.

    :param id: ID of the Volume
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = VolumesIdActionsChangeProtectionPostRequest.from_dict(body)
    return web.Response(status=200)


async def volumes_id_actions_detach_post(request: web.Request, id) -> web.Response:
    """Detach Volume

    Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a later time.

    :param id: ID of the Volume
    :type id: int

    """
    return web.Response(status=200)


async def volumes_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Volume

    Returns all Action objects for a Volume. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Volume
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def volumes_id_actions_resize_post(request: web.Request, id, body=None) -> web.Response:
    """Resize Volume

    Changes the size of a Volume. Note that downsizing a Volume is not possible.

    :param id: ID of the Volume
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = VolumesIdActionsResizePostRequest.from_dict(body)
    return web.Response(status=200)
