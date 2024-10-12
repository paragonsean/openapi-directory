from typing import List, Dict
from aiohttp import web

from openapi_server.models.downloadable_data_link_interface import DownloadableDataLinkInterface
from openapi_server.models.downloadable_link_repository_v1_save_post_request import DownloadableLinkRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def downloadable_link_repository_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """products/{sku}/downloadable-links

    List of links with associated samples

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)


async def downloadable_link_repository_v1_save_post(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/downloadable-links

    Update downloadable link of the given product (link type and its resources cannot be changed)

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = DownloadableLinkRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
