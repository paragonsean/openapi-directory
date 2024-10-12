from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_messenger_account400_response import CreateMessengerAccount400Response
from openapi_server.models.create_messenger_account_request import CreateMessengerAccountRequest
from openapi_server.models.messenger_account_response import MessengerAccountResponse
from openapi_server.models.model401_response import Model401Response
from openapi_server.models.model403_response import Model403Response
from openapi_server.models.update_messenger_account200_response import UpdateMessengerAccount200Response
from openapi_server.models.update_messenger_account400_response import UpdateMessengerAccount400Response
from openapi_server.models.update_messenger_account_request import UpdateMessengerAccountRequest
from openapi_server import util


async def create_messenger_account(request: web.Request, body) -> web.Response:
    """Create a Messenger account

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateMessengerAccountRequest.from_dict(body)
    return web.Response(status=200)


async def delete_messenger_account(request: web.Request, external_id) -> web.Response:
    """Delete a Messenger account

    

    :param external_id: External id of the account you want to delete. In this case it is the Facebook Page ID.
    :type external_id: str

    """
    return web.Response(status=200)


async def get_messenger_account(request: web.Request, external_id) -> web.Response:
    """Retrieve a Messenger account

    

    :param external_id: External id of the account you want to retrieve. In this case it is the Facebook Page ID.
    :type external_id: str

    """
    return web.Response(status=200)


async def update_messenger_account(request: web.Request, external_id, body) -> web.Response:
    """Update a Messenger account

    

    :param external_id: External id of the account you want to update. In this case it is the Facebook Page ID.
    :type external_id: str
    :param body: Request body can contain any of the following
    :type body: dict | bytes

    """
    body = UpdateMessengerAccountRequest.from_dict(body)
    return web.Response(status=200)
