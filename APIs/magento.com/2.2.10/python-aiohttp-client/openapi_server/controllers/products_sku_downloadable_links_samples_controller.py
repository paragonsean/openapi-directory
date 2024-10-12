from typing import List, Dict
from aiohttp import web

from openapi_server.models.downloadable_data_sample_interface import DownloadableDataSampleInterface
from openapi_server.models.downloadable_sample_repository_v1_save_post_request import DownloadableSampleRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def downloadable_sample_repository_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """products/{sku}/downloadable-links/samples

    List of samples for downloadable product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)


async def downloadable_sample_repository_v1_save_post(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/downloadable-links/samples

    Update downloadable sample of the given product

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = DownloadableSampleRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
