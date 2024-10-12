from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_send_voice_message_response import WebServiceSendVoiceMessageResponse
from openapi_server.models.web_service_voice_message import WebServiceVoiceMessage
from openapi_server.models.web_service_voice_message_send_single_text_request import WebServiceVoiceMessageSendSingleTextRequest
from openapi_server.models.web_service_voice_messages import WebServiceVoiceMessages
from openapi_server import util


async def api_rest_v1_voice_all_get(request: web.Request, page_size=None, page=None, status=None, from_date_time_sent=None, to_date_time_sent=None, to_number=None, message=None, campaign=None, data_field=None, deleted=None) -> web.Response:
    """all

    Returns all voice messages

    :param page_size: number of elements to return at a time
    :type page_size: int
    :param page: page number
    :type page: int
    :param status: filter by message status
    :type status: str
    :param from_date_time_sent: date format: yyyyMMdd
    :type from_date_time_sent: str
    :param to_date_time_sent: date format: yyyyMMdd
    :type to_date_time_sent: str
    :param to_number: phone number the message was sent to
    :type to_number: str
    :param message: search matching message text
    :type message: str
    :param campaign: search by campaign
    :type campaign: str
    :param data_field: search by data field
    :type data_field: str
    :param deleted: return only deleted / not deleted messages
    :type deleted: bool

    """
    from_date_time_sent = util.deserialize_datetime(from_date_time_sent)
    to_date_time_sent = util.deserialize_datetime(to_date_time_sent)
    return web.Response(status=200)


async def api_rest_v1_voice_message_id_delete(request: web.Request, message_id) -> web.Response:
    """delete

    Deletes a  message

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_voice_message_id_get(request: web.Request, message_id) -> web.Response:
    """get

    Returns details for a single message

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def single_audio(request: web.Request, recipient_number, file, campaign=None, data_field=None, retry_count=None, retry_minimum_interval=None, retry_maximum_interval=None) -> web.Response:
    """single-audio

    Send a single audio voice message to one recipient. Note, Content-Type header must be set to multipart/form-data for this request.

    :param recipient_number: the phone number of the recipient to send to
    :type recipient_number: str
    :param file: audio file to play, supports MP3 or WAV format
    :type file: str
    :param campaign: optional campaign name
    :type campaign: str
    :param data_field: optional extra data
    :type data_field: str
    :param retry_count: optional number of times to retry unanswered call
    :type retry_count: int
    :param retry_minimum_interval: optional minimum interval in minutes between retry attempts
    :type retry_minimum_interval: int
    :param retry_maximum_interval: optional maximum interval in minutes between retry attempts
    :type retry_maximum_interval: int

    """
    return web.Response(status=200)


async def single_text(request: web.Request, body=None) -> web.Response:
    """single-text

    Send a single text voice message to one recipient

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceVoiceMessageSendSingleTextRequest.from_dict(body)
    return web.Response(status=200)
