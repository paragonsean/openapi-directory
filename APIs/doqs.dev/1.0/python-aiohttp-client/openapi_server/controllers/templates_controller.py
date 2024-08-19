from typing import List, Dict
from aiohttp import web

from openapi_server.models.fill_template_request import FillTemplateRequest
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_ok_http_url import ResponseOkHttpUrl
from openapi_server.models.response_ok_list_apps_api_routes_templates_template import ResponseOkListAppsApiRoutesTemplatesTemplate
from openapi_server.models.response_ok_none_type import ResponseOkNoneType
from openapi_server.models.response_ok_template import ResponseOkTemplate
from openapi_server.models.update_template_request import UpdateTemplateRequest
from openapi_server import util


async def create(request: web.Request, file) -> web.Response:
    """Create

    

    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def delete_templates_id_delete(request: web.Request, id) -> web.Response:
    """Delete 

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def fill(request: web.Request, id, body) -> web.Response:
    """Fill

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FillTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def get(request: web.Request, id) -> web.Response:
    """Get Template

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_file_templates_id_file_get(request: web.Request, id) -> web.Response:
    """Get File

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def list(request: web.Request, limit=None, offset=None) -> web.Response:
    """List 

    

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def update(request: web.Request, id, body) -> web.Response:
    """Update

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTemplateRequest.from_dict(body)
    return web.Response(status=200)
