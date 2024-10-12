from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.successful_search1 import SuccessfulSearch1
from openapi_server import util


async def g_et_activity(request: web.Request, activity_id) -> web.Response:
    """Retrieve one activity by its id

    

    :param activity_id: 
    :type activity_id: str

    """
    return web.Response(status=200)
