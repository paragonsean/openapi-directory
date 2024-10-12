from typing import List, Dict
from aiohttp import web

from openapi_server.models.collaborator import Collaborator
from openapi_server.models.collaborator_editable import CollaboratorEditable
from openapi_server import util


async def maps_id_collaborators_get(request: web.Request, id) -> web.Response:
    """List collaborators of a map

    List collaborators of a map.

    :param id: Map id
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_collaborators_user_id_delete(request: web.Request, id, user_id) -> web.Response:
    """Delete collaboration

    Delete collaboration.

    :param id: map id
    :type id: int
    :param user_id: user id
    :type user_id: int

    """
    return web.Response(status=200)


async def maps_id_collaborators_user_id_patch(request: web.Request, id, user_id, collaborator=None) -> web.Response:
    """Update collaborator

    Update collaborator. Wrap collaborator parameters in [collaborator]

    :param id: map id
    :type id: int
    :param user_id: user id
    :type user_id: int
    :param collaborator: collaborator attributes
    :type collaborator: dict | bytes

    """
    collaborator = CollaboratorEditable.from_dict(collaborator)
    return web.Response(status=200)
