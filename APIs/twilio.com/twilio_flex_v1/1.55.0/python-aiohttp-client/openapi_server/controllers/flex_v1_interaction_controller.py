from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_interaction import FlexV1Interaction
from openapi_server import util


async def create_interaction(request: web.Request, channel, routing, interaction_context_sid=None) -> web.Response:
    """create_interaction

    Create a new Interaction.

    :param channel: The Interaction&#39;s channel.
    :type channel: dict | bytes
    :param routing: The Interaction&#39;s routing logic.
    :type routing: dict | bytes
    :param interaction_context_sid: The Interaction context sid is used for adding a context lookup sid
    :type interaction_context_sid: str

    """
    channel = object.from_dict(channel)
    routing = object.from_dict(routing)
    return web.Response(status=200)


async def fetch_interaction(request: web.Request, sid) -> web.Response:
    """fetch_interaction

    

    :param sid: The SID of the Interaction resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)
