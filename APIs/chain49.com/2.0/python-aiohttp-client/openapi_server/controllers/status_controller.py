from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_blockchain200_response import GetBlockchain200Response
from openapi_server import util


async def get_available_blockchains(request: web.Request, ) -> web.Response:
    """List available blockchains

    Get an array of active blockchains


    """
    return web.Response(status=200)


async def get_blockchain(request: web.Request, blockchain) -> web.Response:
    """Blockchain Info Summary

    Get basic summary of info relating to the currently selected blockchain

    :param blockchain: Blockchain name
    :type blockchain: str

    """
    return web.Response(status=200)
