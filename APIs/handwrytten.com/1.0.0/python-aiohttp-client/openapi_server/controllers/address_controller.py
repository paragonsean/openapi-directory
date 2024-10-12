from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_recipient_address200_response import AddRecipientAddress200Response
from openapi_server.models.add_recipient_address_request import AddRecipientAddressRequest
from openapi_server.models.delete_recipient200_response import DeleteRecipient200Response
from openapi_server.models.delete_recipient_request import DeleteRecipientRequest
from openapi_server.models.recipient_address import RecipientAddress
from openapi_server.models.recipients_list_request import RecipientsListRequest
from openapi_server.models.update_recipient_request import UpdateRecipientRequest
from openapi_server import util


async def add_recipient_address(request: web.Request, body=None) -> web.Response:
    """add a new recipient address

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = AddRecipientAddressRequest.from_dict(body)
    return web.Response(status=200)


async def delete_recipient(request: web.Request, body) -> web.Response:
    """deletes an existing recipient address

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = DeleteRecipientRequest.from_dict(body)
    return web.Response(status=200)


async def recipients_list(request: web.Request, body) -> web.Response:
    """list the addresses in the user&#39;s account

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = RecipientsListRequest.from_dict(body)
    return web.Response(status=200)


async def update_recipient(request: web.Request, body) -> web.Response:
    """updates an existing new recipient address

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = UpdateRecipientRequest.from_dict(body)
    return web.Response(status=200)
