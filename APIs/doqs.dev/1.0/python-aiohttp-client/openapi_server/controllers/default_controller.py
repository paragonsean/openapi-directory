from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_template_request import CreateOrUpdateTemplateRequest
from openapi_server.models.generate_pdf_payload import GeneratePDFPayload
from openapi_server.models.preview_model import PreviewModel
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_ok_designer_template import ResponseOkDesignerTemplate
from openapi_server.models.response_ok_list_fillr_entities_designer_template_designer_template import ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate
from openapi_server.models.response_ok_none_type import ResponseOkNoneType
from openapi_server.models.response_ok_preview_response import ResponseOkPreviewResponse
from openapi_server import util


async def create_template_designer_templates_post(request: web.Request, body) -> web.Response:
    """Create Template

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_designer_templates_id_delete(request: web.Request, id) -> web.Response:
    """Delete

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def generate_pdf_designer_templates_id_generate_post(request: web.Request, id, body) -> web.Response:
    """Generate Pdf

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GeneratePDFPayload.from_dict(body)
    return web.Response(status=200)


async def list_templates_designer_templates_get(request: web.Request, limit=None, offset=None) -> web.Response:
    """List Templates

    

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def list_templates_designer_templates_id_get(request: web.Request, id) -> web.Response:
    """List Templates

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def preview_designer_templates_preview_post(request: web.Request, body) -> web.Response:
    """Preview

    

    :param body: 
    :type body: dict | bytes

    """
    body = PreviewModel.from_dict(body)
    return web.Response(status=200)


async def update_template_designer_templates_id_put(request: web.Request, id, body) -> web.Response:
    """Update Template

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateTemplateRequest.from_dict(body)
    return web.Response(status=200)
