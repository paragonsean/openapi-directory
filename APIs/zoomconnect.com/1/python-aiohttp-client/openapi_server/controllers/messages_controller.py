from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_analyse_message_request_message_and_recipient_number import WebServiceAnalyseMessageRequestMessageAndRecipientNumber
from openapi_server.models.web_service_analyse_message_request_message_only import WebServiceAnalyseMessageRequestMessageOnly
from openapi_server.models.web_service_analyse_message_response import WebServiceAnalyseMessageResponse
from openapi_server.models.web_service_message import WebServiceMessage
from openapi_server.models.web_service_messages import WebServiceMessages
from openapi_server import util


async def analyse(request: web.Request, body=None) -> web.Response:
    """analyse-

    Returns details for a single message

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageOnly.from_dict(body)
    return web.Response(status=200)


async def analyse_full(request: web.Request, body=None) -> web.Response:
    """analyse-full

    Returns full analysis of message

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageAndRecipientNumber.from_dict(body)
    return web.Response(status=200)


async def analyse_message_credit_cost(request: web.Request, body=None) -> web.Response:
    """analyse-message-credit-cost

    Returns the number of credit which would be required to send the request message to the requested recipient number

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageAndRecipientNumber.from_dict(body)
    return web.Response(status=200)


async def analyse_message_encoding(request: web.Request, body=None) -> web.Response:
    """analyse-message-encoding

    Returns the message encoding that would be required to send the requested message

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageOnly.from_dict(body)
    return web.Response(status=200)


async def analyse_message_length(request: web.Request, body=None) -> web.Response:
    """analyse-message-length

    Returns the number of characters the requested message consists of

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageOnly.from_dict(body)
    return web.Response(status=200)


async def analyse_number_of_messages(request: web.Request, body=None) -> web.Response:
    """analyse-number-of-messages

    Returns the number of SMS parts which would be sent when sending the requested message

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceAnalyseMessageRequestMessageOnly.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_messages_all_get(request: web.Request, page_size=None, page=None, type=None, status=None, from_date_time_sent=None, to_date_time_sent=None, from_date_time_received=None, to_date_time_received=None, from_number=None, to_number=None, message=None, campaign=None, data_field=None, deleted=None, read=None, replies_to_message_id=None) -> web.Response:
    """all

    Returns all messages

    :param page_size: number of elements to return at a time
    :type page_size: int
    :param page: page number
    :type page: int
    :param type: filter by message type
    :type type: str
    :param status: filter by message status
    :type status: str
    :param from_date_time_sent: date format: yyyyMMdd
    :type from_date_time_sent: str
    :param to_date_time_sent: date format: yyyyMMdd
    :type to_date_time_sent: str
    :param from_date_time_received: date format: yyyyMMdd
    :type from_date_time_received: str
    :param to_date_time_received: date format: yyyyMMdd
    :type to_date_time_received: str
    :param from_number: phone number the message was sent from
    :type from_number: str
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
    :param read: return only read / unread messages (inbox messages only)
    :type read: bool
    :param replies_to_message_id: return only inbox messages which are a reply to the message with the given message id
    :type replies_to_message_id: str

    """
    from_date_time_sent = util.deserialize_datetime(from_date_time_sent)
    to_date_time_sent = util.deserialize_datetime(to_date_time_sent)
    from_date_time_received = util.deserialize_datetime(from_date_time_received)
    to_date_time_received = util.deserialize_datetime(to_date_time_received)
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_delete(request: web.Request, message_id) -> web.Response:
    """delete

    Deletes a  message

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_get(request: web.Request, message_id) -> web.Response:
    """get

    Returns details for a single message

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_mark_read_post(request: web.Request, message_id) -> web.Response:
    """markRead

    Marks a  message as read

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_mark_read_put(request: web.Request, message_id) -> web.Response:
    """markRead

    Marks a  message as read

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_mark_unread_post(request: web.Request, message_id) -> web.Response:
    """markUnread

    Marks a  message as unread

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_messages_message_id_mark_unread_put(request: web.Request, message_id) -> web.Response:
    """markUnread

    Marks a  message as unread

    :param message_id: messageId
    :type message_id: str

    """
    return web.Response(status=200)
