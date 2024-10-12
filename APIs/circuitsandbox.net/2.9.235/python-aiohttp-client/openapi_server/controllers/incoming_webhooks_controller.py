from typing import List, Dict
from aiohttp import web

from openapi_server.models.incoming_webhook import IncomingWebhook
from openapi_server import util


async def create_incoming_webhook(request: web.Request, conversation_id, name=None, user_id=None, description=None) -> web.Response:
    """Create a new webhook for existing conversation.

    Create a new webhook. Conversation must exist and creater has to be participant. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conversation_id: The id of the conversation.
    :type conversation_id: str
    :param name: The name of the webhook
    :type name: str
    :param user_id: The id of the user of the webhook
    :type user_id: str
    :param description: A short description of the webhook
    :type description: str

    """
    return web.Response(status=200)


async def delete_incoming_webhook(request: web.Request, webhook_id) -> web.Response:
    """Delete an existing webhook

    Delete a new webhook. Webhook must exist OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param webhook_id: The id of the webhook
    :type webhook_id: str

    """
    return web.Response(status=200)


async def get_incoming_webhook_by_user(request: web.Request, user_id, pagesize=None, searchpointer=None) -> web.Response:
    """Get all webhooks of a special user.

    Get all webhooks of a special user. OauthScopes: READ_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param user_id: The id of the user.
    :type user_id: str
    :param pagesize: Max number of hooks per request. Default is 25
    :type pagesize: 
    :param searchpointer: Start of search if consequtive call.
    :type searchpointer: str

    """
    return web.Response(status=200)


async def post_webhook_as_slack_message(request: web.Request, webhook_id, file_url=None, filename=None, markdown=None, subject=None, text=None) -> web.Response:
    """Post text item for conversation via webhook.

    Post text items to conversations via slack apps.

    :param webhook_id: The id of the webhook.
    :type webhook_id: str
    :param file_url: missing documentation
    :type file_url: str
    :param filename: missing documentation
    :type filename: str
    :param markdown: missing documentation
    :type markdown: bool
    :param subject: missing documentation
    :type subject: str
    :param text: The text which will occur in the conversation. May contain formats like *bold* or _italic_
    :type text: str

    """
    return web.Response(status=200)
