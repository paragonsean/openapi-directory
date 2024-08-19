from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_dataset(request: web.Request, dataset) -> web.Response:
    """Get metadata about a dataset.

    

    :param dataset: Name of dataset
    :type dataset: str

    """
    return web.Response(status=200)


async def get_datasets(request: web.Request, ) -> web.Response:
    """Get a list of all datasets.

    


    """
    return web.Response(status=200)
