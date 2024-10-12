from typing import List, Dict
from aiohttp import web

from openapi_server.models.dialog_open_error_schema import DialogOpenErrorSchema
from openapi_server.models.dialog_open_schema import DialogOpenSchema
from openapi_server import util


async def dialog_open(request: web.Request, token, dialog, trigger_id) -> web.Response:
    """dialog_open

    Open a dialog with a user

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param dialog: The dialog definition. This must be a JSON-encoded string.
    :type dialog: str
    :param trigger_id: Exchange a trigger to post to the user.
    :type trigger_id: str

    """
    return web.Response(status=200)
