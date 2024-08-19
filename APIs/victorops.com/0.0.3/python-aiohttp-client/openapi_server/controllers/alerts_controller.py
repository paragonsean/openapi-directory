from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_alert_response import GetAlertResponse
from openapi_server import util


async def api_public_v1_alerts_uuid_get(request: web.Request, x_vo_api_id, x_vo_api_key, uuid) -> web.Response:
    """Retrieve alert details.

    Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param uuid: The VictorOps uuid of the alert
    :type uuid: str

    """
    return web.Response(status=200)
