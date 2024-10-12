from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest
from openapi_server import util


async def create_network_sm_bypass_activation_lock_attempt_1(request: web.Request, network_id, body) -> web.Response:
    """Bypass activation lock attempt

    Bypass activation lock attempt

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmBypassActivationLockAttemptRequest.from_dict(body)
    return web.Response(status=200)


async def get_network_sm_bypass_activation_lock_attempt_1(request: web.Request, network_id, attempt_id) -> web.Response:
    """Bypass activation lock attempt status

    Bypass activation lock attempt status

    :param network_id: 
    :type network_id: str
    :param attempt_id: 
    :type attempt_id: str

    """
    return web.Response(status=200)
