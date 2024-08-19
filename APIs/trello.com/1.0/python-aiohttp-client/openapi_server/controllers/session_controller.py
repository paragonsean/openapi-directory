from typing import List, Dict
from aiohttp import web

from openapi_server.models.sessions import Sessions
from openapi_server.models.sessions_status import SessionsStatus
from openapi_server import util


async def add_sessions(request: web.Request, key, token, body) -> web.Response:
    """addSessions()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Sessions\&quot; to be added.
    :type body: dict | bytes

    """
    body = Sessions.from_dict(body)
    return web.Response(status=200)


async def get_sessions_socket(request: web.Request, key, token) -> web.Response:
    """getSessionsSocket()

    This is the route for WebSocket requests.  See the socket API reference for a description of WebSocket usage.

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def update_sessions_by_id_session(request: web.Request, id_session, key, token, body) -> web.Response:
    """updateSessionsByIdSession()

    

    :param id_session: idSession
    :type id_session: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Sessions\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Sessions.from_dict(body)
    return web.Response(status=200)


async def update_sessions_status_by_id_session(request: web.Request, id_session, key, token, body) -> web.Response:
    """updateSessionsStatusByIdSession()

    

    :param id_session: idSession
    :type id_session: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Sessions Status\&quot; to be updated.
    :type body: dict | bytes

    """
    body = SessionsStatus.from_dict(body)
    return web.Response(status=200)
