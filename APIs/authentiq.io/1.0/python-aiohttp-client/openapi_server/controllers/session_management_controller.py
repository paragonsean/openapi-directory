from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def authorize_iframe(request: web.Request, client_id) -> web.Response:
    """Include a session iframe

    An OpenID Connect Session Management iframe to facilitate e.g. single sign-on or remote logouts.  The iframe implements the OIDC postMessage-based [change notification protocol](http://openid.net/specs/openid-connect-session-1_0.html#ChangeNotification) via which a client can receive notifications about session state changes. 

    :param client_id: Client identifier
    :type client_id: str

    """
    return web.Response(status=200)
