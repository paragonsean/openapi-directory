from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_website_tracking_parameter import LiveWebsiteTrackingParameter
from openapi_server import util


async def v2_live_website_tracking_parameters_json_post(request: web.Request, person_id) -> web.Response:
    """Create an Live Website Tracking Parameter

    Creates a Live Website Tracking parameter to identify a person 

    :param person_id: The person to create the LiveWebsiteTrackingParameter for
    :type person_id: int

    """
    return web.Response(status=200)
