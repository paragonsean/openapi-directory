from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_template import WebServiceTemplate
from openapi_server.models.web_service_templates import WebServiceTemplates
from openapi_server import util


async def api_rest_v1_templates_all_get(request: web.Request, ) -> web.Response:
    """all

    Returns all templates


    """
    return web.Response(status=200)


async def api_rest_v1_templates_template_id_delete(request: web.Request, template_id) -> web.Response:
    """delete

    Deletes a  template

    :param template_id: templateId
    :type template_id: int

    """
    return web.Response(status=200)


async def api_rest_v1_templates_template_id_get(request: web.Request, template_id) -> web.Response:
    """get

    Returns details for a single template

    :param template_id: templateId
    :type template_id: int

    """
    return web.Response(status=200)
