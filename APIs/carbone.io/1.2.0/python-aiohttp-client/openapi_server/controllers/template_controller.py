from typing import List, Dict
from aiohttp import web

from openapi_server.models.template_post200_response import TemplatePost200Response
from openapi_server.models.template_post_request import TemplatePostRequest
from openapi_server.models.template_post_request1 import TemplatePostRequest1
from openapi_server.models.template_template_id_delete200_response import TemplateTemplateIdDelete200Response
from openapi_server import util


async def template_post(request: web.Request, carbone_version, body) -> web.Response:
    """Upload a template.

    Documentation: https://carbone.io/api-reference.html#add-templates

    :param carbone_version: Carbone version
    :type carbone_version: int
    :param body: Template File to upload, supported formats: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file
    :type body: dict | bytes

    """
    body = TemplatePostRequest.from_dict(body)
    return web.Response(status=200)


async def template_template_id_delete(request: web.Request, template_id, carbone_version) -> web.Response:
    """Delete a template from a template ID

    Documentation: https://carbone.io/api-reference.html#delete-templates

    :param template_id: Unique identifier of the template
    :type template_id: str
    :param carbone_version: Carbone version
    :type carbone_version: int

    """
    return web.Response(status=200)


async def template_template_id_get(request: web.Request, template_id, carbone_version) -> web.Response:
    """Download a template from a template ID

    Documentation: https://carbone.io/api-reference.html#get-templates

    :param template_id: Unique identifier of the template
    :type template_id: str
    :param carbone_version: Carbone version
    :type carbone_version: int

    """
    return web.Response(status=200)
