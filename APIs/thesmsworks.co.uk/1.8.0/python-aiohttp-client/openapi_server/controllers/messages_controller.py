from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancelled_message_response import CancelledMessageResponse
from openapi_server.models.deleted_message_response import DeletedMessageResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.message import Message
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.query import Query
from openapi_server.models.scheduled_message_response import ScheduledMessageResponse
from openapi_server.models.scheduled_messages_response import ScheduledMessagesResponse
from openapi_server.models.send_message_response import SendMessageResponse
from openapi_server import util


async def message_schedule_post(request: web.Request, sms_message) -> web.Response:
    """message_schedule_post

    Schedules an SMS message to be sent at the date-time you specify

    :param sms_message: Message properties
    :type sms_message: dict | bytes

    """
    sms_message = Message.from_dict(sms_message)
    return web.Response(status=200)


async def message_send_post(request: web.Request, sms_message) -> web.Response:
    """message_send_post

    Send an SMS Message

    :param sms_message: Message properties
    :type sms_message: dict | bytes

    """
    sms_message = Message.from_dict(sms_message)
    return web.Response(status=200)


async def messages_failed_post(request: web.Request, query) -> web.Response:
    """messages_failed_post

    Get failed messages matching your search criteria

    :param query: 
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def messages_inbox_post(request: web.Request, query) -> web.Response:
    """messages_inbox_post

    Get unread uncoming messages matching your search criteria

    :param query: 
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def messages_messageid_delete(request: web.Request, messageid) -> web.Response:
    """messages_messageid_delete

    Delete the message with the mathcing messageid

    :param messageid: The ID of the message you would like returned
    :type messageid: str

    """
    return web.Response(status=200)


async def messages_messageid_get(request: web.Request, messageid) -> web.Response:
    """messages_messageid_get

    Retrieve a logged message by the message ID

    :param messageid: The ID of the message you would like returned
    :type messageid: str

    """
    return web.Response(status=200)


async def messages_post(request: web.Request, query) -> web.Response:
    """messages_post

    Retrieve up to 1000 messages matching your search criteria

    :param query: 
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def messages_schedule_get(request: web.Request, ) -> web.Response:
    """messages_schedule_get

    Returns a list of messages scheduled from your account, comprising any messages scheduled in the last 3 months and any scheduled to send in the future


    """
    return web.Response(status=200)


async def messages_schedule_messageid_delete(request: web.Request, messageid) -> web.Response:
    """messages_schedule_messageid_delete

    Cancels a scheduled SMS message

    :param messageid: The ID of the message you would like returned
    :type messageid: str

    """
    return web.Response(status=200)


async def send_flash_message(request: web.Request, sms_message) -> web.Response:
    """send_flash_message

    Sends an SMS flash message, which appears on the recipients lock screen

    :param sms_message: Message properties
    :type sms_message: dict | bytes

    """
    sms_message = Message.from_dict(sms_message)
    return web.Response(status=200)
