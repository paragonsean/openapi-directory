from typing import List, Dict
from aiohttp import web

from openapi_server.models.code_reference_request import CodeReferenceRequest
from openapi_server.models.delete_repository_reports_request import DeleteRepositoryReportsRequest
from openapi_server import util


async def v1_code_references_delete_reports_post(request: web.Request, body) -> web.Response:
    """v1_code_references_delete_reports_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteRepositoryReportsRequest.from_dict(body)
    return web.Response(status=200)


async def v1_code_references_post(request: web.Request, body) -> web.Response:
    """v1_code_references_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = CodeReferenceRequest.from_dict(body)
    return web.Response(status=200)
