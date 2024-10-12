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


async def patch_transfer_instruments_id(request: web.Request, id, x_requested_verification_code=None, body=None) -> web.Response:
    """Update a transfer instrument

    Updates a transfer instrument.

    :param id: The unique identifier of the transfer instrument.
    :type id: str
    :param x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors associated with the transfer instrument. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferInstrumentInfo.from_dict(body)
    return web.Response(status=200)


async def post_transfer_instruments(request: web.Request, x_requested_verification_code=None, body=None) -> web.Response:
    """Create a transfer instrument

    Creates a transfer instrument.   A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the transfer instrument as required by payment industry regulations. We inform you of the verification results through webhooks or API responses.  When the transfer instrument passes the verification checks, you can start sending funds from the balance platform to the transfer instrument (such as payouts).

    :param x_requested_verification_code: Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferInstrumentInfo.from_dict(body)
    return web.Response(status=200)
