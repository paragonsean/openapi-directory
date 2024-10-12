from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.subscription_definitions_response import SubscriptionDefinitionsResponse
from openapi_server import util


async def get_communication_preferences_v3_definitions_get_page(request: web.Request, ) -> web.Response:
    """Get subscription definitions

    Get a list of all subscription definitions for the portal


    """
    return web.Response(status=200)
