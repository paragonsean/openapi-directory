from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_transfer_request import AcceptTransferRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient_transfer_details import RecipientTransferDetails
from openapi_server.models.recipient_transfer_details_list_result import RecipientTransferDetailsListResult
from openapi_server.models.validate_transfer_list_response import ValidateTransferListResponse
from openapi_server import util


async def recipient_transfers_accept(request: web.Request, transfer_name, parameters) -> web.Response:
    """Accepts the transfer with given transfer Id.

    

    :param transfer_name: Transfer Name.
    :type transfer_name: str
    :param parameters: Parameters supplied to accept the transfer.
    :type parameters: dict | bytes

    """
    parameters = AcceptTransferRequest.from_dict(parameters)
    return web.Response(status=200)


async def recipient_transfers_decline(request: web.Request, transfer_name) -> web.Response:
    """Declines the transfer with given transfer Id.

    

    :param transfer_name: Transfer Name.
    :type transfer_name: str

    """
    return web.Response(status=200)


async def recipient_transfers_get(request: web.Request, transfer_name) -> web.Response:
    """Gets the transfer with given transfer Id.

    

    :param transfer_name: Transfer Name.
    :type transfer_name: str

    """
    return web.Response(status=200)


async def recipient_transfers_list(request: web.Request, ) -> web.Response:
    """Lists the transfers received by caller.

    


    """
    return web.Response(status=200)


async def recipient_transfers_validate(request: web.Request, transfer_name, parameters) -> web.Response:
    """Validates if the products can be transferred in the context of the given transfer name.

    

    :param transfer_name: Transfer Name.
    :type transfer_name: str
    :param parameters: Parameters supplied to validate the transfer.
    :type parameters: dict | bytes

    """
    parameters = AcceptTransferRequest.from_dict(parameters)
    return web.Response(status=200)
