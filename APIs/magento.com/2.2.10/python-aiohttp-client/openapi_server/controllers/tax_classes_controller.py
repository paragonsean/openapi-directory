from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_tax_class_repository_v1_save_post_request import TaxTaxClassRepositoryV1SavePostRequest
from openapi_server import util


async def tax_tax_class_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """taxClasses

    Create a Tax Class

    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxClassRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
