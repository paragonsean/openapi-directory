from typing import List, Dict
from aiohttp import web

from openapi_server.models.downloadable_sample_repository_v1_save_post_request import DownloadableSampleRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def downloadable_sample_repository_v1_save_put(request: web.Request, sku, id, body=None) -> web.Response:
    """products/{sku}/downloadable-links/samples/{id}

    Update downloadable sample of the given product

    :param sku: 
    :type sku: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DownloadableSampleRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
