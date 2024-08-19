from typing import List, Dict
from aiohttp import web

from openapi_server.models.branding_conf import BrandingConf
from openapi_server.models.get_branding_conf200_response import GetBrandingConf200Response
from openapi_server.models.update_b_randing_conf200_response import UpdateBRandingConf200Response
from openapi_server import util


async def get_branding_conf(request: web.Request, ) -> web.Response:
    """Get branding configuration

    Get all web interface customization parameters


    """
    return web.Response(status=200)


async def reload_branding_conf(request: web.Request, ) -> web.Response:
    """Reload branding file

    Reload the configuration from file


    """
    return web.Response(status=200)


async def update_b_randing_conf(request: web.Request, body) -> web.Response:
    """Update web interface customization

    change color, logo, label etc.

    :param body: 
    :type body: dict | bytes

    """
    body = BrandingConf.from_dict(body)
    return web.Response(status=200)
