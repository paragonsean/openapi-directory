from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_organization_config_template(request: web.Request, organization_id, config_template_id) -> web.Response:
    """Remove a configuration template

    Remove a configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_config_templates(request: web.Request, organization_id) -> web.Response:
    """List the configuration templates for this organization

    List the configuration templates for this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
