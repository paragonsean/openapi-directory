from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_tax_class_repository_v1_save_post_request import TaxTaxClassRepositoryV1SavePostRequest
from openapi_server import util


async def tax_tax_class_repository_v1_save_put(request: web.Request, class_id, body=None) -> web.Response:
    """taxClasses/{classId}

    Create a Tax Class

    :param class_id: 
    :type class_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxClassRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
