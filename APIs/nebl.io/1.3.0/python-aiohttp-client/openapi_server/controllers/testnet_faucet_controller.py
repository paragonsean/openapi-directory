from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_faucet_response import GetFaucetResponse
from openapi_server import util


async def testnet_get_faucet(request: web.Request, address, amount=None) -> web.Response:
    """Withdraws testnet NEBL to the specified address

    Withdraw testnet NEBL to your Neblio Testnet address. By default amount is 1500000000 or 15 NEBL and has a max of 50 NEBL. Only 2 withdrawals allowed per 24 hour period. 

    :param address: Your Neblio Testnet Address
    :type address: str
    :param amount: Amount of NEBL to withdrawal in satoshis
    :type amount: 

    """
    return web.Response(status=200)
