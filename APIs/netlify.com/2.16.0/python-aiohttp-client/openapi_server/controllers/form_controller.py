from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.form import Form
from openapi_server import util


async def delete_site_form(request: web.Request, site_id, form_id) -> web.Response:
    """delete_site_form

    

    :param site_id: 
    :type site_id: str
    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)


async def list_site_forms(request: web.Request, site_id) -> web.Response:
    """list_site_forms

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)
