from typing import List, Dict
from aiohttp import web

from openapi_server.models.rpc_request import RpcRequest
from openapi_server.models.rpc_response import RpcResponse
from openapi_server import util


async def json_rpc(request: web.Request, body) -> web.Response:
    """Send a JSON-RPC call to a localhost neblio-Qt or nebliod node

    Call any Neblio RPC command from the Neblio API libraries. Useful for signing transactions with a local node and other functions. Will not work from a browser due to CORS restrictions. Requires a node to be running locally at 127.0.0.1

    :param body: 
    :type body: dict | bytes

    """
    body = RpcRequest.from_dict(body)
    return web.Response(status=200)
