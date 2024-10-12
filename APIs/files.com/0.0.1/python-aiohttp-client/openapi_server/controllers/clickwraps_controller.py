from typing import List, Dict
from aiohttp import web

from openapi_server.models.clickwrap_entity import ClickwrapEntity
from openapi_server import util


async def delete_clickwraps_id(request: web.Request, id) -> web.Response:
    """Delete Clickwrap

    Delete Clickwrap

    :param id: Clickwrap ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_clickwraps(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List Clickwraps

    List Clickwraps

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_clickwraps_id(request: web.Request, id) -> web.Response:
    """Show Clickwrap

    Show Clickwrap

    :param id: Clickwrap ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_clickwraps_id(request: web.Request, id, body=None, name=None, use_with_bundles=None, use_with_inboxes=None, use_with_users=None) -> web.Response:
    """Update Clickwrap

    Update Clickwrap

    :param id: Clickwrap ID.
    :type id: int
    :param body: Body text of Clickwrap (supports Markdown formatting).
    :type body: str
    :param name: Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
    :type name: str
    :param use_with_bundles: Use this Clickwrap for Bundles?
    :type use_with_bundles: str
    :param use_with_inboxes: Use this Clickwrap for Inboxes?
    :type use_with_inboxes: str
    :param use_with_users: Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
    :type use_with_users: str

    """
    return web.Response(status=200)


async def post_clickwraps(request: web.Request, body=None, name=None, use_with_bundles=None, use_with_inboxes=None, use_with_users=None) -> web.Response:
    """Create Clickwrap

    Create Clickwrap

    :param body: Body text of Clickwrap (supports Markdown formatting).
    :type body: str
    :param name: Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.)
    :type name: str
    :param use_with_bundles: Use this Clickwrap for Bundles?
    :type use_with_bundles: str
    :param use_with_inboxes: Use this Clickwrap for Inboxes?
    :type use_with_inboxes: str
    :param use_with_users: Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password.
    :type use_with_users: str

    """
    return web.Response(status=200)
