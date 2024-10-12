from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_estimate_fee_v2200_response import GetEstimateFeeV2200Response
from openapi_server import util


async def get_estimate_fee_v2(request: web.Request, blockchain, confirmation_target) -> web.Response:
    """Estimate transaction fee V2

    Returns an estimated transaction fee for a specific confirmation target. If you want your transaction to be included in the next block, then you give 1 as parameter. If it is not urgent, then you can wait a bit longer and get an estimation for the fifth next block.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param confirmation_target: Number of blocks in which the transaction should be confirmed
    :type confirmation_target: int

    """
    return web.Response(status=200)
