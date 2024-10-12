from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_registration_entity import BundleRegistrationEntity
from openapi_server import util


async def get_bundle_registrations(request: web.Request, user_id=None, cursor=None, per_page=None, bundle_id=None) -> web.Response:
    """List Bundle Registrations

    List Bundle Registrations

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param bundle_id: ID of the associated Bundle
    :type bundle_id: int

    """
    return web.Response(status=200)
