from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_message import BatchMessage
from openapi_server.models.batch_message_response import BatchMessageResponse
from openapi_server.models.cancelled_message_response import CancelledMessageResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.message import Message
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.scheduled_batch_response import ScheduledBatchResponse
from openapi_server import util


async def batch_any_post(request: web.Request, messages) -> web.Response:
    """batch_any_post

    Sends a collection of unique SMS messages. Batches may contain up to 5000 messages at a time.

    :param messages: An array of messages
    :type messages: list | bytes

    """
    messages = [Message.from_dict(d) for d in messages]
    return web.Response(status=200)


async def batch_batchid_get(request: web.Request, batchid) -> web.Response:
    """batch_batchid_get

    Retrieve all messages in a batch with the given batch ID

    :param batchid: The ID of the batch you would like returned
    :type batchid: str

    """
    return web.Response(status=200)


async def batch_schedule_post(request: web.Request, sms_message) -> web.Response:
    """batch_schedule_post

    Schedules a batch of SMS messages to be sent at the date time you specify

    :param sms_message: Message properties
    :type sms_message: dict | bytes

    """
    sms_message = BatchMessage.from_dict(sms_message)
    return web.Response(status=200)


async def batch_send_post(request: web.Request, sms_message) -> web.Response:
    """batch_send_post

    Send a single SMS message to multiple recipients.  Batches may contain up to 5000 messages at a time.

    :param sms_message: Message properties
    :type sms_message: dict | bytes

    """
    sms_message = BatchMessage.from_dict(sms_message)
    return web.Response(status=200)


async def batches_schedule_batchid_delete(request: web.Request, batchid) -> web.Response:
    """batches_schedule_batchid_delete

    Cancels a scheduled SMS message

    :param batchid: The ID of the batch you would like returned
    :type batchid: str

    """
    return web.Response(status=200)
