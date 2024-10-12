from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_error_dto import RestErrorDTO
from openapi_server.models.web_service_send_sms_request import WebServiceSendSmsRequest
from openapi_server.models.web_service_send_sms_requests import WebServiceSendSmsRequests
from openapi_server.models.web_service_send_sms_response import WebServiceSendSmsResponse
from openapi_server.models.web_service_send_sms_responses import WebServiceSendSmsResponses
from openapi_server import util


async def api_rest_v1_sms_send_bulk_get(request: web.Request, ) -> web.Response:
    """send-bulk

    Returns an example of the data to POST to send multiple messages in one transaction.


    """
    return web.Response(status=200)


async def api_rest_v1_sms_send_bulk_post(request: web.Request, body=None) -> web.Response:
    """send-bulk

    Send multiple messages in one transaction.

    :param body: requests
    :type body: dict | bytes

    """
    body = WebServiceSendSmsRequests.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_sms_send_get(request: web.Request, ) -> web.Response:
    """send

    Returns an example of the data to POST to send a single message.


    """
    return web.Response(status=200)


async def api_rest_v1_sms_send_post(request: web.Request, body=None) -> web.Response:
    """send

    Sends a single message. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; fields are required. All other fields are optional.

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceSendSmsRequest.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_sms_send_url_parameters_get(request: web.Request, recipient_number, message, date_to_send=None, campaign=None, data_field=None) -> web.Response:
    """send-url-parameters

    Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

    :param recipient_number: the phone number of the recipient to send to
    :type recipient_number: str
    :param message: the message to send
    :type message: str
    :param date_to_send: date format: yyyyMMddHHmm
    :type date_to_send: str
    :param campaign: optional campaign name
    :type campaign: str
    :param data_field: optional extra data
    :type data_field: str

    """
    date_to_send = util.deserialize_datetime(date_to_send)
    return web.Response(status=200)


async def api_rest_v1_sms_send_url_parameters_post(request: web.Request, recipient_number, message, date_to_send=None, campaign=None, data_field=None) -> web.Response:
    """send-url-parameters

    Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

    :param recipient_number: the phone number of the recipient to send to
    :type recipient_number: str
    :param message: the message to send
    :type message: str
    :param date_to_send: date format: yyyyMMddHHmm
    :type date_to_send: str
    :param campaign: optional campaign name
    :type campaign: str
    :param data_field: optional extra data
    :type data_field: str

    """
    date_to_send = util.deserialize_datetime(date_to_send)
    return web.Response(status=200)


async def api_rest_v1_sms_send_url_token_get(request: web.Request, token, recipient_number, message, date_to_send=None, campaign=None, data_field=None) -> web.Response:
    """send-url

    Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

    :param token: token
    :type token: str
    :param recipient_number: the phone number of the recipient to send to
    :type recipient_number: str
    :param message: the message to send
    :type message: str
    :param date_to_send: date format: yyyyMMddHHmm
    :type date_to_send: str
    :param campaign: optional campaign name
    :type campaign: str
    :param data_field: optional extra data
    :type data_field: str

    """
    date_to_send = util.deserialize_datetime(date_to_send)
    return web.Response(status=200)


async def api_rest_v1_sms_send_url_token_post(request: web.Request, token, recipient_number, message, date_to_send=None, campaign=None, data_field=None) -> web.Response:
    """send-url

    Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

    :param token: token
    :type token: str
    :param recipient_number: the phone number of the recipient to send to
    :type recipient_number: str
    :param message: the message to send
    :type message: str
    :param date_to_send: date format: yyyyMMddHHmm
    :type date_to_send: str
    :param campaign: optional campaign name
    :type campaign: str
    :param data_field: optional extra data
    :type data_field: str

    """
    date_to_send = util.deserialize_datetime(date_to_send)
    return web.Response(status=200)
