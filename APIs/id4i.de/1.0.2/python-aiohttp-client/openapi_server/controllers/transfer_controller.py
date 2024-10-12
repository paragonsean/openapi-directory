from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.transfer_receive_info import TransferReceiveInfo
from openapi_server.models.transfer_send_info import TransferSendInfo
from openapi_server import util


async def get_send_info(request: web.Request, id4n) -> web.Response:
    """Show transfer preparation information

    

    :param id4n: The ID4N to retrieve information about
    :type id4n: str

    """
    return web.Response(status=200)


async def prepare(request: web.Request, id4n, body) -> web.Response:
    """Prepare an object for transfer

    

    :param id4n: The ID4N to prepare for transfer
    :type id4n: str
    :param body: Transfer preparation status
    :type body: dict | bytes

    """
    body = TransferSendInfo.from_dict(body)
    return web.Response(status=200)


async def receive(request: web.Request, id4n, body) -> web.Response:
    """Transfer a GUID or collection, obtaining it (i.e. becoming the holder) and if allowed also taking ownership

    Taking ownership can be forbidden by a previous owner. See methods prepare and getInfo

    :param id4n: This ID4N identifies the object to take hold of
    :type id4n: str
    :param body: Required information to receive an id4n object
    :type body: dict | bytes

    """
    body = TransferReceiveInfo.from_dict(body)
    return web.Response(status=200)
