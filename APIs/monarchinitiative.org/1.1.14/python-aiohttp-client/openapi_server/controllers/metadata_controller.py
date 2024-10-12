from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_metadata_for_datasets(request: web.Request, ) -> web.Response:
    """Get metadata for all datasets from SciGraph

    


    """
    return web.Response(status=200)
