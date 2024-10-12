from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_conversation_id_offer_post_request import ConversationsConversationIdOfferPostRequest
from openapi_server.models.conversations_id_offer_post_request import ConversationsIdOfferPostRequest
from openapi_server import util


async def conversations_conversation_id_offer_post(request: web.Request, conversation_id, body=None) -> web.Response:
    """Make an offer to the other participant in the conversation

    Make an offer to the other participant in the conversation

    :param conversation_id: 
    :type conversation_id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ConversationsConversationIdOfferPostRequest.from_dict(body)
    return web.Response(status=200)


async def conversations_id_offer_post(request: web.Request, id, body=None) -> web.Response:
    """Make an offer to the other participant in the conversation

    Make an offer to the other participant in the conversation

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ConversationsIdOfferPostRequest.from_dict(body)
    return web.Response(status=200)
