from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_delete_positions_id import EndpointDeletePositionsID
from openapi_server.models.endpoint_patch_positions_id import EndpointPatchPositionsID
from openapi_server.models.endpoint_post_positions import EndpointPostPositions
from openapi_server import util


async def positions_iddelete(request: web.Request, id) -> web.Response:
    """positions_iddelete

    Remove an item from the OAuth&#39;ed end user&#39;s Curriculum Vitae.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def positions_idpatch(request: web.Request, id, category, organization, role, start_date, end_date=None, organization_size=None, position=None, summary=None, url=None) -> web.Response:
    """positions_idpatch

    Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by modifying an existing position.

    :param id: 
    :type id: int
    :param category: 
    :type category: str
    :param organization: 
    :type organization: str
    :param role: 
    :type role: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param organization_size: 
    :type organization_size: str
    :param position: 
    :type position: str
    :param summary: 
    :type summary: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def positions_post(request: web.Request, category, organization, role, start_date, end_date=None, organization_size=None, position=None, summary=None, url=None) -> web.Response:
    """positions_post

    Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by adding a position.

    :param category: 
    :type category: str
    :param organization: 
    :type organization: str
    :param role: 
    :type role: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param organization_size: 
    :type organization_size: str
    :param position: 
    :type position: str
    :param summary: 
    :type summary: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)
