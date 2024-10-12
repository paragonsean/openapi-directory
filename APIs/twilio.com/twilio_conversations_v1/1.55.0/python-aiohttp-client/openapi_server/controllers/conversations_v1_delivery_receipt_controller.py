from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_conversation_conversation_message_conversation_message_receipt import ConversationsV1ConversationConversationMessageConversationMessageReceipt
from openapi_server.models.conversations_v1_service_service_conversation_service_conversation_message_service_conversation_message_receipt import ConversationsV1ServiceServiceConversationServiceConversationMessageServiceConversationMessageReceipt
from openapi_server.models.list_conversation_message_receipt_response import ListConversationMessageReceiptResponse
from openapi_server.models.list_service_conversation_message_receipt_response import ListServiceConversationMessageReceiptResponse
from openapi_server import util


async def fetch_conversation_message_receipt(request: web.Request, conversation_sid, message_sid, sid) -> web.Response:
    """fetch_conversation_message_receipt

    Fetch the delivery and read receipts of the conversation message

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
    :type message_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_conversation_message_receipt(request: web.Request, chat_service_sid, conversation_sid, message_sid, sid) -> web.Response:
    """fetch_service_conversation_message_receipt

    Fetch the delivery and read receipts of the conversation message

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
    :type message_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_conversation_message_receipt(request: web.Request, conversation_sid, message_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conversation_message_receipt

    Retrieve a list of all delivery and read receipts of the conversation message

    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
    :type message_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_service_conversation_message_receipt(request: web.Request, chat_service_sid, conversation_sid, message_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_conversation_message_receipt

    Retrieve a list of all delivery and read receipts of the conversation message

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Message resource is associated with.
    :type chat_service_sid: str
    :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :type conversation_sid: str
    :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
    :type message_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
