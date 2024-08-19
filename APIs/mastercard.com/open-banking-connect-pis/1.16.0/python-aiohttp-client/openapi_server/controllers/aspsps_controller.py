from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_aspsps_ok_body import PostAspspsOKBody
from openapi_server.models.post_aspsps_params_body import PostAspspsParamsBody
from openapi_server import util


async def payments_aspsps_post(request: web.Request, body) -> web.Response:
    """Get list of ASPSPs

    Get the list of all active ASPSPs supported by the Open Banking Connect platform at this time with possibility to filter by id, name or country. This list is updated regularly as new ASPSPs are connected.

    :param body: Request Body
    :type body: dict | bytes

    """
    body = PostAspspsParamsBody.from_dict(body)
    return web.Response(status=200)
