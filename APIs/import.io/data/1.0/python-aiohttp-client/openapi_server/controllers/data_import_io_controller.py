from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server import util


async def extractor_extractor_id_csv_latest_get(request: web.Request, extractor_id) -> web.Response:
    """Get the latest crawl run results as a csv

    

    :param extractor_id: the id of the extractor to start get the latest crawl run data
    :type extractor_id: str

    """
    return web.Response(status=200)


async def extractor_extractor_id_json_latest_get(request: web.Request, extractor_id) -> web.Response:
    """Get the latest crawl run results as json

    

    :param extractor_id: The id of the extractor to start get the latest crawl run data
    :type extractor_id: str

    """
    return web.Response(status=200)
