from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.get_reactions_response import GetReactionsResponse
from openapi_server.models.reaction_removal_response import ReactionRemovalResponse
from openapi_server.models.reaction_response import ReactionResponse
from openapi_server.models.send_reaction_request import SendReactionRequest
from openapi_server import util


async def delete_reaction_0(request: web.Request, id, type, user_id=None) -> web.Response:
    """Delete reaction

    Removes user reaction from the message  Sends events: - reaction.deleted  Required permissions: - DeleteReaction 

    :param id: 
    :type id: str
    :param type: 
    :type type: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_reactions_0(request: web.Request, id, limit=None, offset=None) -> web.Response:
    """Get reactions

    Returns list of reactions of specific message  Required permissions: - ReadChannel 

    :param id: 
    :type id: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def send_reaction_0(request: web.Request, id, body) -> web.Response:
    """Send reaction

    Sends reaction to specified message  Sends events: - reaction.new - reaction.updated  Required permissions: - CreateReaction - UseFrozenChannel 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendReactionRequest.from_dict(body)
    return web.Response(status=200)
