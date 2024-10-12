from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.template_request import TemplateRequest
from openapi_server.models.template_response import TemplateResponse
from openapi_server.models.templates_response import TemplatesResponse
from openapi_server import util


async def templates_create(request: web.Request, account_id, body=None) -> web.Response:
    """Create template

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemplateRequest.from_dict(body)
    return web.Response(status=200)


async def templates_fetch(request: web.Request, account_id, template_id) -> web.Response:
    """Fetch template by ID

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param template_id: ID of template to return
    :type template_id: str

    """
    return web.Response(status=200)


async def templates_fetch_all(request: web.Request, account_id, offset=None, limit=None, name=None) -> web.Response:
    """Fetch templates

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param offset: Results to skip when paginating through a result set
    :type offset: int
    :param limit: Maximum number of results to return
    :type limit: int
    :param name: Filter by name or part of
    :type name: str

    """
    return web.Response(status=200)


async def templates_remove(request: web.Request, account_id, template_id) -> web.Response:
    """Deletes a template

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param template_id: Template id to delete
    :type template_id: str

    """
    return web.Response(status=200)


async def templates_update(request: web.Request, account_id, template_id) -> web.Response:
    """Updates a template

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param template_id: ID of template
    :type template_id: str

    """
    return web.Response(status=200)
