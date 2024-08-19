from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_public_v1_maintenancemode_start_post_request import ApiPublicV1MaintenancemodeStartPostRequest
from openapi_server.models.maintenance_mode_state import MaintenanceModeState
from openapi_server import util


async def api_public_v1_maintenancemode_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get an organization&#39;s current maintenance mode state

    

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_maintenancemode_maintenancemodeid_end_put(request: web.Request, x_vo_api_id, x_vo_api_key, maintenancemodeid) -> web.Response:
    """End maintenance mode for routing keys

    

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param maintenancemodeid: The id of the maintenance mode found in the active maintenance mode object
    :type maintenancemodeid: str

    """
    return web.Response(status=200)


async def api_public_v1_maintenancemode_start_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Start maintenance mode for routing keys

    

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: the definition of the maintenance mode you want to start
    :type body: dict | bytes

    """
    body = ApiPublicV1MaintenancemodeStartPostRequest.from_dict(body)
    return web.Response(status=200)
