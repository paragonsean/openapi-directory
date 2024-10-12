from typing import List, Dict
from aiohttp import web

from openapi_server.models.render_template_id_post200_response import RenderTemplateIdPost200Response
from openapi_server.models.render_template_id_post_request import RenderTemplateIdPostRequest
from openapi_server import util


async def render_render_id_get(request: web.Request, render_id, carbone_version) -> web.Response:
    """Retreive a generated document from a render ID.

    Documentation: https://carbone.io/api-reference.html#download-rendered-reports

    :param render_id: Unique identifier of the report
    :type render_id: str
    :param carbone_version: Carbone version
    :type carbone_version: int

    """
    return web.Response(status=200)


async def render_template_id_post(request: web.Request, template_id, carbone_version, body) -> web.Response:
    """Generate a document from a template ID, and a JSON data-set

    Documentation: https://carbone.io/api-reference.html#render-reports

    :param template_id: Unique identifier of the template
    :type template_id: str
    :param carbone_version: Carbone version
    :type carbone_version: int
    :param body: 
    :type body: dict | bytes

    """
    body = RenderTemplateIdPostRequest.from_dict(body)
    return web.Response(status=200)
