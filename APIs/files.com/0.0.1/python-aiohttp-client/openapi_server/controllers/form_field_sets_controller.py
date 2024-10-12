from typing import List, Dict
from aiohttp import web

from openapi_server.models.form_field_set_entity import FormFieldSetEntity
from openapi_server.models.patch_form_field_sets import PatchFormFieldSets
from openapi_server.models.post_form_field_sets import PostFormFieldSets
from openapi_server import util


async def delete_form_field_sets_id(request: web.Request, id) -> web.Response:
    """Delete Form Field Set

    Delete Form Field Set

    :param id: Form Field Set ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_form_field_sets(request: web.Request, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Form Field Sets

    List Form Field Sets

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_form_field_sets_id(request: web.Request, id) -> web.Response:
    """Show Form Field Set

    Show Form Field Set

    :param id: Form Field Set ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_form_field_sets_id(request: web.Request, id, body) -> web.Response:
    """Update Form Field Set

    Update Form Field Set

    :param id: Form Field Set ID.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchFormFieldSets.from_dict(body)
    return web.Response(status=200)


async def post_form_field_sets(request: web.Request, body) -> web.Response:
    """Create Form Field Set

    Create Form Field Set

    :param body: 
    :type body: dict | bytes

    """
    body = PostFormFieldSets.from_dict(body)
    return web.Response(status=200)
