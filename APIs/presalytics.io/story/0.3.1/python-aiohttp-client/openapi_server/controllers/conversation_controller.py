from typing import List, Dict
from aiohttp import web

from openapi_server.models.message import Message
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server import util


async def story_id_messages_get(request: web.Request, id) -> web.Response:
    """Conversation: List Conversation Messages

    Get a list of messages that have been send in this story

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_messages_post(request: web.Request, id, body) -> web.Response:
    """Conversation: Send a Message

    Add a message to the Story&#39;s conversation

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: The message text
    :type body: str

    """
    return web.Response(status=200)
