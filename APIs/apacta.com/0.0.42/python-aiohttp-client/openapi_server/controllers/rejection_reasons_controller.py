from typing import List, Dict
from aiohttp import web

from openapi_server.models.overview_rejection_reasons_get200_response import OverviewRejectionReasonsGet200Response
from openapi_server import util


async def overview_rejection_reasons_get(request: web.Request, ) -> web.Response:
    """Get a statistics data for rejection reasons

    


    """
    return web.Response(status=200)
