from typing import List, Dict
from aiohttp import web

from openapi_server.models.note import Note
from openapi_server import util


async def workspace_slug_members_member_slug_notes_get(request: web.Request, workspace_slug, member_slug, page=None) -> web.Response:
    """Get the member&#39;s notes

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param page: 
    :type page: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_notes_id_put(request: web.Request, workspace_slug, member_slug, id, body=None) -> web.Response:
    """Update a note

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Note.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_member_slug_notes_post(request: web.Request, workspace_slug, member_slug, body=None) -> web.Response:
    """Create a note

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = Note.from_dict(body)
    return web.Response(status=200)
