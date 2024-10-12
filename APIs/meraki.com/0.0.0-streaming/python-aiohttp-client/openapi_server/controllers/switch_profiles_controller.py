from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_organization_config_template_switch_profiles(request: web.Request, organization_id, config_template_id) -> web.Response:
    """List the switch profiles for your switch template configuration

    List the switch profiles for your switch template configuration

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)
