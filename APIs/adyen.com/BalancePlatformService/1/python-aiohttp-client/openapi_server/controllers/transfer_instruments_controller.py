from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.transfer_instrument import TransferInstrument
from openapi_server.models.transfer_instrument_info import TransferInstrumentInfo
from openapi_server import util


async def delete_transfer_instruments_id(request: web.Request, id) -> web.Response:
    """Delete a transfer instrument

    Deletes a transfer instrument.

    :param id: The unique identifier of the transfer instrument to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_transfer_instruments_id(request: web.Request, id) -> web.Response:
    """Get a transfer instrument

    Returns the details of a transfer instrument.

    :param id: The unique identifier of the transfer instrument.
    :type id: str

    """
    return web.Response(status=200)


async def patch_transfer_instruments_id(request: web.Request, id, body=None) -> web.Response:
    """Update a transfer instrument

    Updates a transfer instrument.

    :param id: The unique identifier of the transfer instrument.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferInstrumentInfo.from_dict(body)
    return web.Response(status=200)


async def post_transfer_instruments(request: web.Request, body=None) -> web.Response:
    """Create a transfer instrument

    Creates a transfer instrument.   A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the transfer instrument as required by payment industry regulations. We inform you of the verification results through webhooks or API responses.  When the transfer instrument passes the verification checks, you can start sending funds from the balance platform to the transfer instrument (such as payouts).

    :param body: 
    :type body: dict | bytes

    """
    body = TransferInstrumentInfo.from_dict(body)
    return web.Response(status=200)
