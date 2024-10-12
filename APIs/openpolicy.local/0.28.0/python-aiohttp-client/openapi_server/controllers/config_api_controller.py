from typing import List, Dict
from aiohttp import web

from openapi_server.models.model200_single_result import Model200SingleResult
from openapi_server.models.model400 import Model400
from openapi_server import util


async def get_config(request: web.Request, pretty=None) -> web.Response:
    """Get configurations

    This API endpoint responds with active configuration (result response)  --- **Note** The &#x60;credentials&#x60; field in the &#x60;services&#x60; configuration and  The &#x60;private_key&#x60; and &#x60;key&#x60; fields in the &#x60;keys&#x60; configuration will be omitted from the API response  ---

    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)
