from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.manage_event import ManageEvent
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def story_id_events_get(request: web.Request, id) -> web.Response:
    """Events: List Events

    Get a list of Events available to users of this story

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_events_post(request: web.Request, id, body) -> web.Response:
    """Events: Manage Events

    Add a message to the Story&#39;s conversation

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: Collaborator user id and permission type
    :type body: dict | bytes

    """
    body = ManageEvent.from_dict(body)
    return web.Response(status=200)
