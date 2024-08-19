from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_holder_messaging_request import AccountHolderMessagingRequest
from openapi_server.models.account_holder_messaging_response_schema import AccountHolderMessagingResponseSchema
from openapi_server.models.errors_response import ErrorsResponse
from openapi_server import util


async def accountholdermessaging_post(request: web.Request, accountholder_messaging_request_schema=None) -> web.Response:
    """accountholdermessaging_post

    Allows issuers to display customized messages per token within the Apple Pay wallet, below the digitized image of the card. 

    :param accountholder_messaging_request_schema: Contains the details of the request message.
    :type accountholder_messaging_request_schema: dict | bytes

    """
    accountholder_messaging_request_schema = AccountHolderMessagingRequest.from_dict(accountholder_messaging_request_schema)
    return web.Response(status=200)
