from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server import util


async def api_key_delete_current(request: web.Request, ) -> web.Response:
    """Delete current API key.  (Requires current API connection to be using an API key.)

    Delete current API key.  (Requires current API connection to be using an API key.)


    """
    return web.Response(status=200)


async def api_key_find_current(request: web.Request, ) -> web.Response:
    """Show information about current API key.  (Requires current API connection to be using an API key.)

    Show information about current API key.  (Requires current API connection to be using an API key.)


    """
    return web.Response(status=200)


async def api_key_update_current(request: web.Request, expires_at=None, name=None, permission_set=None) -> web.Response:
    """Update current API key.  (Requires current API connection to be using an API key.)

    Update current API key.  (Requires current API connection to be using an API key.)

    :param expires_at: API Key expiration date
    :type expires_at: str
    :param name: Internal name for the API Key.  For your use.
    :type name: str
    :param permission_set: Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    :type permission_set: str

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)
