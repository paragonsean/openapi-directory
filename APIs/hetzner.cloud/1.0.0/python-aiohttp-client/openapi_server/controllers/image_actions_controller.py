from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.images_id_actions_change_protection_post_request import ImagesIdActionsChangeProtectionPostRequest
from openapi_server import util


async def images_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for an Image

    Returns a specific Action for an Image.

    :param id: ID of the Image
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def images_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Image Protection

    Changes the protection configuration of the Image. Can only be used on snapshots.

    :param id: ID of the Image
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ImagesIdActionsChangeProtectionPostRequest.from_dict(body)
    return web.Response(status=200)


async def images_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for an Image

    Returns all Action objects for an Image. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Image
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)
